"""프론트 개발 서버 — 저장소 루트 정적 서빙 + /api/works 리스팅 + /api/log 기록 쓰기.

실행: python tools/serve.py [port] [--open]   (기본 8000)
더블클릭으로 띄우려면 저장소 루트의 `run.bat`(윈도우) / `run.command`(맥)
"""
import contextlib
import datetime
import io as _io
import json
import os
import sys
import threading
import time
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 재생성은 같은 프로세스 안에서 돈다 — 예전엔 POST마다 파이썬을 새로 띄웠고,
# 그때마다 로드맵 json 357개를 다시 파싱했다. import해 두면 build_stats의 파싱 캐시가
# 살아 있어 두 번째 저장부터는 바뀐 로그 파일만 다시 읽는다.
# build_stats는 상대경로로 읽고 쓰므로 cwd가 저장소 루트여야 한다.
# Handler는 directory=ROOT를 명시하니 chdir이 정적 서빙에 영향을 주지 않는다.
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import build_stats   # noqa: E402

# /api/log 쓰기 직렬화 — ThreadingHTTPServer라 동시 POST가 가능해서 잠근다
WRITE_LOCK = threading.Lock()

# 콘솔 코드페이지가 한글을 못 받으면 print 한 줄에 서버가 죽는다(윈도우 기본 cp949/cp1252).
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except (AttributeError, OSError):
    pass


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.send_response(302)
            self.send_header('Location', '/front/index.html')
            self.end_headers()
            return
        if self.path == '/api/works':
            base = os.path.join(ROOT, 'works')
            out = []
            for dirpath, _dirs, files in os.walk(base):
                for name in files:
                    if name == '.gitkeep':
                        continue
                    full = os.path.join(dirpath, name)
                    st = os.stat(full)
                    out.append({
                        'path': os.path.relpath(full, base).replace(os.sep, '/'),
                        'size': st.st_size,
                        'mtime': int(st.st_mtime),
                    })
            out.sort(key=lambda w: -w['mtime'])
            body = json.dumps(out, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def _json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        """POST /api/log — 프론트 기록 입력. body:
        {"path": "<분야>/<로드맵 경로>", "records": [{sec, sub?, item, lv?, doing?, ev?, at?}]}

        키가 로드맵에 실재하는지는 여기서 대조하지 않는다 — append 후 build_stats.main()이
        로드맵에 없는 키에서 1을 내며 목록을 찍는다(기존 검증기 재사용, 원본은 하나 원칙).
        실패하면 방금 붙인 만큼 파일을 되돌리고 400을 준다.
        성공하면 progress·stats 재생성까지 끝난 상태다. 응답에 기록된 레코드를 그대로 실어
        보내므로(`records`) 프론트는 다시 받지 않고 화면만 그 자리에서 갱신하면 된다.
        """
        if self.path != '/api/log':
            self._json(404, {'error': 'unknown endpoint'})
            return
        try:
            n = int(self.headers.get('Content-Length') or 0)
            req = json.loads(self.rfile.read(n).decode('utf-8'))
            path = req['path']
            records = req['records']
            assert isinstance(records, list) and records
        except Exception:
            self._json(400, {'error': 'body는 {"path": ..., "records": [...]}'})
            return

        # 경로는 로드맵 json 실재로 검증 — 상대경로 탈출도 여기서 같이 막힌다
        if os.sep in path.replace('/', '') or not os.path.isfile(
                os.path.join(ROOT, 'roadmaps', *path.split('/')) + '.json'):
            self._json(400, {'error': f'로드맵이 없음: {path}'})
            return

        today = datetime.date.today().isoformat()
        lines, records_out = [], []
        for r in records:
            lv, doing = r.get('lv'), r.get('doing')
            # pick = 택 1 주력 표식(집계 무관, 화면 전용) — pick만 있는 줄도 유효
            if lv is None and not doing and 'pick' not in r:
                self._json(400, {'error': 'lv·doing·pick 중 하나는 있어야 함'})
                return
            if lv is not None and lv not in (1, 2, 3, 4):
                self._json(400, {'error': f'lv는 1~4: {lv}'})
                return
            # 실증(lv:4)은 근거 없는 자기신고를 막는다 — docs/stat-model.md 규칙 7의 최소 방어선
            if lv == 4 and not (r.get('ev') or '').strip():
                self._json(400, {'error': 'lv:4는 ev(실증 근거)가 필요함'})
                return
            if not r.get('sec') or not r.get('item'):
                self._json(400, {'error': 'sec·item은 필수'})
                return
            out = {'at': r.get('at') or today, 'sec': r['sec']}
            if r.get('sub'):
                out['sub'] = r['sub']
            out['item'] = r['item']
            if lv is not None:
                out['lv'] = lv
            if doing:
                out['doing'] = True
            if 'pick' in r:
                out['pick'] = bool(r['pick'])
            if (r.get('ev') or '').strip():
                out['ev'] = r['ev'].strip()
            lines.append(json.dumps(out, ensure_ascii=False))
            records_out.append(out)

        log_path = os.path.join(ROOT, 'data', 'log', *path.split('/')) + '.jsonl'
        t0 = time.perf_counter()
        with WRITE_LOCK:
            before = os.path.getsize(log_path) if os.path.isfile(log_path) else 0
            with open(log_path, 'a', encoding='utf-8', newline='\n') as f:
                # 빈 틀 파일이 개행 없이 "{}"로 끝나 있으면 줄을 갈라준다
                if before and open(log_path, 'rb').read()[-1:] != b'\n':
                    f.write('\n')
                f.write('\n'.join(lines) + '\n')
            t1 = time.perf_counter()
            # build_stats.main()은 로드맵에 없는 키를 만나면 **아무것도 쓰기 전에** 1을 낸다.
            # 그 목록은 stderr로 나가므로 받아서 400의 detail에 그대로 싣는다(기존 동작 유지).
            # redirect는 프로세스 전역이라 이 수십 ms 사이의 GET 접근 로그 한 줄이
            # 같이 삼켜질 수 있다 — 로그 한 줄일 뿐이라 그대로 둔다.
            err = _io.StringIO()
            with contextlib.redirect_stdout(_io.StringIO()), contextlib.redirect_stderr(err):
                rc = build_stats.main()
            t2 = time.perf_counter()
            if rc != 0:
                with open(log_path, 'r+b') as f:   # 롤백 — 붙이기 전 크기로 자른다
                    f.truncate(before)
                self._json(400, {'error': '로드맵에 없는 키', 'detail': err.getvalue().strip()})
                return
        # 접근 로그와 같은 stderr로 — stdout은 콘솔이 아닐 때 버퍼링돼 늦게 나온다
        print(f'[log] +{len(lines)}줄 append {(t1 - t0) * 1000:.0f}ms · '
              f'rebuild {(t2 - t1) * 1000:.0f}ms · {path}', file=sys.stderr)
        self._json(200, {'ok': True, 'written': len(lines), 'records': records_out})


if __name__ == '__main__':
    nums = [a for a in sys.argv[1:] if not a.startswith('-')]
    port = int(nums[0]) if nums else 8000
    url = f'http://localhost:{port}/'
    try:
        # 브라우저가 여러 연결을 동시에 열므로 단일 스레드면 요청이 줄을 선다
        srv = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    except OSError as e:
        print(f'[에러] {port} 포트를 쓸 수 없습니다: {e}')
        print(f'이미 켜져 있다면 브라우저에서 {url} 를 열면 됩니다.')
        print('다른 포트로 띄우려면: python tools/serve.py 8001 --open')
        sys.exit(1)
    print(f'serving {ROOT}')
    print(url)
    print('종료하려면 이 창을 닫거나 Ctrl+C')
    if '--open' in sys.argv:
        webbrowser.open(url)   # bind가 끝난 뒤라 바로 열어도 안전
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('\n종료')
