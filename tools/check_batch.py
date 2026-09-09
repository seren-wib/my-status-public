# -*- coding: utf-8 -*-
"""배치 검증기 — git HEAD와 워킹트리의 로드맵 md를 대조한다.

설명 채우기 배치는 `- [ ]` 줄만 고쳐야 한다. 그런데 항목 줄은 전부 바뀌므로
diff로는 "항목이 섹션을 넘어갔는지"를 못 본다 — 헤딩은 그대로이기 때문이다.
실제로 2026-08-26 배치 2에서 에이전트 하나가 항목 5개를 옆 섹션으로 밀었다가
스스로 되돌린 일이 있었다. 그걸 기계로 잡으려고 만든 도구다.

`check_items.py`는 결과물의 문법을 보고, 이 도구는 **원본 대비 무엇이 움직였는지**를 본다.

검사:
  1. 줄 수 불변
  2. 항목(`- [ ]`) 수 불변
  3. 항목이 아닌 줄(헤딩·참조·구분선) 완전 동일
  4. (섹션, 서브섹션, 항목 이름) 집합 불변 — 항목이 섹션을 넘어갔는지, 이름이 바뀌었는지
     이름 변경은 배치에서 허용된 예외이므로 **위반이 아니라 목록으로 보고**한다

사용법:
    python tools/check_batch.py              # 워킹트리에서 바뀐 로드맵 md 전부
    python tools/check_batch.py <파일 경로>…  # 지정한 것만
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import re
import subprocess

ITEM = re.compile(r'^- \[[ x]\] (.*)$')
HEAD_RE = re.compile(r'^(#{1,4}) +(.*)$')


def git_show(path):
    r = subprocess.run(['git', 'show', 'HEAD:' + path],
                       capture_output=True)
    if r.returncode:
        return None
    return r.stdout.decode('utf-8')


def changed_files():
    r = subprocess.run(['git', 'diff', '--name-only', '--', 'roadmaps'],
                       capture_output=True, text=True, encoding='utf-8')
    return [p for p in r.stdout.split('\n') if p.endswith('.md')]


def item_name(body):
    """항목 이름 = 첫 ` / ` 앞. 줄 끝 백틱 태그는 떼고 본다."""
    body = re.sub(r'(\s*`[^`]+`)+\s*$', '', body).strip()
    return body.split(' / ', 1)[0].strip()


def index(text):
    """md 텍스트 → {(섹션, 서브섹션, 이름)}, 항목 아닌 줄 목록, 줄 수, 항목 수."""
    sec = sub = None
    keys, other, n = [], [], 0
    for ln in text.split('\n'):
        m = ITEM.match(ln)
        if m:
            n += 1
            keys.append((sec, sub, item_name(m.group(1))))
            continue
        other.append(ln)
        h = HEAD_RE.match(ln)
        if h:
            level, title = len(h.group(1)), h.group(2).strip()
            if level <= 2:
                sec, sub = title, None
            else:
                sub = title
    return keys, other, text.count('\n'), n


def check(path):
    old = git_show(path)
    if old is None:
        print('  ?? HEAD에 없는 파일 — 새로 만든 것')
        return 0
    new = open(path, encoding='utf-8').read()
    ok, ov, oln, on = index(old)
    nk, nv, nln, nn = index(new)

    bad = 0
    if oln != nln:
        print('  !! 줄 수 %d → %d' % (oln, nln)); bad += 1
    if on != nn:
        print('  !! 항목 수 %d → %d' % (on, nn)); bad += 1
    if ov != nv:
        print('  !! 항목이 아닌 줄이 바뀜 (헤딩·참조·구분선)'); bad += 1
        for a, b in zip(ov, nv):
            if a != b:
                print('       - %s\n       + %s' % (a, b))
                break

    # 순서까지 봐야 섹션 이동을 잡는다 — 집합만 보면 자리바꿈이 안 걸린다
    if len(ok) == len(nk):
        moved = [(i, a, b) for i, (a, b) in enumerate(zip(ok, nk)) if a != b]
        renamed = [(a, b) for _, a, b in moved if a[0] == b[0] and a[1] == b[1]]
        relocated = [(a, b) for _, a, b in moved if a[0] != b[0] or a[1] != b[1]]
        if relocated:
            print('  !! 항목이 섹션을 넘어감 — %d건' % len(relocated)); bad += 1
            for a, b in relocated[:10]:
                print('       %s → %s  (%s)' % (a[0], b[0], a[2]))
        if renamed:
            print('  ·· 이름 변경 %d건 (배치에서 허용된 예외)' % len(renamed))
            for a, b in renamed[:10]:
                print('       %s → %s' % (a[2], b[2]))
    if not bad:
        print('  통과')
    return bad


def main():
    paths = sys.argv[1:] or changed_files()
    if not paths:
        print('바뀐 로드맵 md가 없다')
        return 0
    total = 0
    for p in paths:
        print(p)
        total += check(p)
    print('\n파일 %d개 · 위반 %d건' % (len(paths), total))
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
