"""로드맵 md → json 변환기.

roadmaps/<분야>/**/*.md 를 읽어 같은 폴더에 .json 을 생성하고
분야마다 roadmaps/<분야>/index.json 을 만든다. md가 있는 분야만 처리.
스키마는 docs 참고. stdlib만 사용.
"""
import io
import json
import os
import re
import sys

# 윈도우 콘솔은 cp949/cp1252라 한글 print 한 줄에 도구가 죽는다 (serve.py와 같은 함정)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = 'roadmaps'
TAGS = ('추천', '선택', '별도', '위임')
DELEGATE = '위임'   # 다른 로드맵으로 넘김. `별도`는 뜻이 다름 — 별도 제품·요금제·라이선스(항목 줄 13개)
REF_RE = re.compile(r'^$')   # main()에서 분야 목록으로 다시 채움
CURDIR = ''                  # 현재 파싱 중인 파일의 roadmaps/ 기준 디렉터리


def domains():
    """md 파일이 하나라도 있는 분야 폴더."""
    out = []
    for d in sorted(os.listdir(ROOT)):
        if os.path.isdir(os.path.join(ROOT, d)) and any(
                f.endswith('.md') for _, _, fs in os.walk(os.path.join(ROOT, d)) for f in fs):
            out.append(d)
    return out


def resolve(ref):
    """참조 문자열 → roadmaps/ 기준 경로. 분야 프리픽스가 없으면 같은 폴더로 해석."""
    if REF_RE.match(ref):
        return ref
    if '/' not in ref and ref.endswith('.md') and CURDIR:
        return f'{CURDIR}/{ref}'
    return None


def anchor(no, title):
    s = f"{no}-{title.lower()}"
    s = re.sub(r'[^0-9a-z가-힣 -]', '', s)
    return re.sub(r'\s+', '-', s.strip())


def strip_ext(ref):
    return ref[:-3] if ref.endswith('.md') else ref


def strip_meta(text, consumed):
    """태그·참조로 소비된 백틱만 걷어내고, 남은 백틱은 이름의 일부로 보고 부호만 벗긴다.

    `- [ ] \\`!\\`` · `- [ ] Connect using \\`psql\\`` 처럼 항목 이름 자체가 백틱인 경우가 있어
    무조건 걷어내면 't'가 빈 문자열이 되거나 이름이 뭉개진다 (openclaw·claude-code·postgresql-dba).
    """
    for m in consumed:
        text = re.sub(r'\s*`' + re.escape(m) + r'`', '', text, count=1)
    return re.sub(r'`([^`]+)`', r'\1', text).strip()


def strip_heading(raw):
    """헤딩에서 태그(`택 1`·`추천`·`선택`·`별도`·`위임`)만 걷어낸다. 나머지 백틱은 제목의 일부."""
    consumed = [m for m in re.findall(r'`([^`]+)`', raw) if m == '택 1' or m in TAGS]
    return strip_meta(raw, consumed)


def parse_item(text):
    """`- [ ]` 뒤 텍스트 → 항목 dict."""
    item = {}
    tags, ref, inline_choice = [], None, False
    consumed = []
    for m in re.findall(r'`([^`]+)`', text):
        if m == '택 1':
            inline_choice = True
            consumed.append(m)
        elif m in TAGS:
            tags.append(m)
            consumed.append(m)
        elif resolve(m):
            ref = strip_ext(resolve(m))
            consumed.append(m)
    item['t'] = strip_meta(text, consumed)
    if tags:
        item['tags'] = tags
    if ref:
        item['ref'] = ref
    if inline_choice:
        item['choice_inline'] = True
    return item


def parse_ref_bullet(line):
    """체크박스 아닌 참조 불릿 → {label, ref?, tag?} 또는 None.

    두 형태가 있다.
    - `# 이 로드맵 밖`의 목록: `- 라벨 `경로.md`` → ref를 가짐
    - 본문 섹션의 위임 표시: `- Delivery `위임`` → 보통 경로가 없고 태그만 있음.
      경로가 없다고 버리면 섹션↔skill 결합이 json에서 통째로 사라진다(위임 220건).

    **경로와 태그는 공존한다** (2026-08-27). 이름으로 대상을 못 찾는 참조가 26건 있어
    md에서 경로를 못 박을 수 있어야 한다: `- Observation Basics `social/.../observation.md` `위임``
    """
    m = re.match(r'- (.+)', line)
    if not m or line.startswith('- [ ]'):
        return None
    body = m.group(1)
    toks = re.findall(r'`([^`]+)`', body)
    refs = [resolve(r) for r in toks if resolve(r)]
    tags = [t for t in toks if t in TAGS]
    if not refs and not tags:
        return None
    consumed = [t for t in toks if resolve(t) or t in TAGS]
    out = {'label': strip_meta(body, consumed)}
    if refs:
        out['ref'] = strip_ext(refs[0])
    if tags:
        # 위임이 섞여 있으면 그게 대표 태그다(위임 판정이 tag == '위임'이라서).
        # 같이 붙은 `추천` 등은 tags로 보존한다 — 택 1 위임 옵션이 추천 칩을 잃지 않게 (2026-08-30)
        out['tag'] = DELEGATE if DELEGATE in tags else tags[0]
        extra = [t for t in tags if t != out['tag']]
        if extra:
            out['tags'] = extra
    return out


# ── 이름 → 로드맵 해석 (front/js/links.js와 같은 규칙을 파이썬으로) ──────────

ALIAS = {'postgresql': 'postgresqldba', 'postgres': 'postgresqldba',
         'git': 'gitgithub', 'github': 'gitgithub', 'golang': 'go'}


def clean_title(t):
    return re.sub(r'\s*AI 생성$', '', str(t))


def norm_name(s):
    """대소문자·공백·점·하이픈·괄호 부연·and를 무시한 비교 키. `+`·`#`은 언어를 가르므로 남긴다."""
    s = str(s).lower()
    s = re.sub(r'\(.*?\)', '', s).replace('&', ' and ')
    s = re.sub(r'\broadmaps?\b', '', s)
    s = re.sub(r'\band\b', '', s)
    return re.sub(r'[^a-z0-9+#]', '', s)


def resolve_delegate(label, doc, self_path, name_index):
    """위임 대상 경로. 순서가 중요하다 — 파일이 스스로 적어둔 경로가 이름 추측을 이긴다.

    1) 불릿에 경로가 적혀 있으면 그것 (호출측에서 이미 처리)
    2) 같은 파일 `이 로드맵 밖`의 경로 파일명과 대조 — 164건이 여기서 붙는다.
       `mediator`의 `Listening`이 전역 색인으로는 language/english/listening으로 잘못 가는데
       파일 자신은 social/skill-based/Relating/listening.md 라고 적어두었다
    3) 전역 이름 색인 (같은 분야 우선 — listening·reading·writing 등 이름 충돌 7건)
    """
    key = norm_name(label)
    if not key:
        return None
    for o in doc['outside']:
        ref = (o.get('ref') or '').rstrip('/')
        if ref and norm_name(ref.split('/')[-1]) == key:
            return ref
    cands = (name_index.get(key) or name_index.get(ALIAS.get(key, '')) or
             (name_index.get(key[:-1]) if key.endswith('s') else None) or [])
    dom = self_path.split('/')[0] + '/'
    for c in cands:
        if c.startswith(dom) and c != self_path:
            return c
    for c in cands:
        if c != self_path:
            return c
    return None


def english_label(o, titles):
    """`이 로드맵 밖` 라벨을 대상 로드맵의 영어 제목으로. md는 안 건드린다(한글 라벨 1558개).

    폴더 참조(`.../Frameworks/`)는 폴더명, 로드맵 아닌 외부 링크(roadmap.sh)는 적힌 라벨 그대로.
    """
    ref = o.get('ref') or ''
    if not ref:
        return o['label']
    path = ref.rstrip('/')
    if path in titles:
        return clean_title(titles[path])
    tail = path.split('/')[-1]
    if ref.endswith('/'):
        return tail                       # 폴더 참조 → 폴더명
    return tail.replace('-', ' ').title()  # 로드맵 아닌 외부 링크(roadmap.sh/.../projects)


def parse_file(path):
    global CURDIR
    CURDIR = os.path.relpath(os.path.dirname(path), ROOT).replace(os.sep, '/')
    lines = io.open(path, encoding='utf-8').read().splitlines()
    doc = {'title': None, 'ai': False, 'source': None, 'parts': [], 'outside': []}
    part = section = sub = None
    in_outside = False

    for ln in lines:
        if ln.startswith('# 이 로드맵 밖'):
            in_outside = True
            continue
        if in_outside:
            b = parse_ref_bullet(ln)
            if b:
                doc['outside'].append(b)
            elif ln.startswith('- '):  # 외부 링크(roadmap.sh 등)
                m = re.match(r'- (.+?) `([^`]+)`', ln)
                if m:
                    doc['outside'].append({'label': m.group(1).strip(), 'ref': m.group(2)})
            continue

        m = re.match(r'# PART (\d+) · (.+)', ln)
        if m:
            part = {'no': int(m.group(1)), 'title': m.group(2).strip(), 'sections': []}
            doc['parts'].append(part)
            section = sub = None
            continue

        if ln.startswith('# ') and doc['title'] is None:
            doc['title'] = strip_heading(ln[2:])
            doc['ai'] = 'AI 생성' in ln
            continue

        if ln.startswith('> ') and doc['ai'] and doc['source'] is None and section is None:
            doc['source'] = ln[2:].strip()
            continue

        m = re.match(r'## (\d+)\. (.+)', ln)
        if m:
            no, raw = int(m.group(1)), m.group(2)
            title = strip_heading(raw)
            section = {'no': no, 'title': title, 'anchor': anchor(no, title),
                       'subs': [], 'items': []}
            if '`택 1`' in raw:
                section['choice'] = True
            if part is None:  # PART 없는 파일
                part = {'no': None, 'title': None, 'sections': []}
                doc['parts'].append(part)
            part['sections'].append(section)
            sub = None
            continue

        m = re.match(r'#{3,4} (.+)', ln)   # #### 3곳(postgresql-dba·ux-design)은 ###와 동급 처리
        if m:
            raw = m.group(1)
            sub = {'title': strip_heading(raw), 'items': []}
            if '`택 1`' in raw:
                sub['choice'] = True
            section['subs'].append(sub)
            continue

        m = re.match(r'- \[ \] (.+)', ln)
        if m:
            (sub['items'] if sub else section['items']).append(parse_item(m.group(1)))
            continue

        if section is not None:  # 본문의 비체크박스 참조 불릿
            b = parse_ref_bullet(ln)
            if b and b.get('tag') == DELEGATE:
                # 위임은 학습 목록 안에 있다 — 220건 전부 `##` 섹션 안이고 부록 위치는 0건.
                # 40건은 목록 맨 앞(선수 지식)이라 refs로 빼면 그 위치가 소실된다.
                # 대상 경로는 main()의 2패스에서 채운다(파일 끝의 `이 로드맵 밖`을 봐야 하므로).
                item = {'t': b['label'], 'delegate': b.get('ref')}
                if b.get('tags'):
                    item['tags'] = b['tags']
                (sub['items'] if sub else section['items']).append(item)
            elif b:
                (sub if sub else section).setdefault('refs', []).append(b)

    return doc


def counts(doc):
    secs = sum(len(p['sections']) for p in doc['parts'])
    real = lambda its: sum(1 for it in its if 'delegate' not in it)   # 위임은 학습 항목이 아님
    items = sum(real(s['items']) + sum(real(u['items']) for u in s['subs'])
                for p in doc['parts'] for s in p['sections'])
    return secs, items


def iter_items(doc):
    for part in doc['parts']:
        for sec in part['sections']:
            for it in sec['items']:
                yield it
            for sub in sec['subs']:
                for it in sub['items']:
                    yield it


def main():
    global REF_RE
    doms = domains()
    REF_RE = re.compile(r'^(?:' + '|'.join(map(re.escape, doms)) + r')/')

    # 1패스: 전부 파싱만. 위임 대상과 `이 로드맵 밖` 라벨은 다른 파일의 제목을 알아야 정해진다
    docs = []
    for dom in doms:
        base = os.path.join(ROOT, dom)
        for root, _, fs in os.walk(base):
            for f in sorted(fs):
                if f.endswith('.md'):
                    src = os.path.join(root, f)
                    rel = os.path.relpath(src, base).replace(os.sep, '/')[:-3]
                    docs.append((dom, rel, src[:-3] + '.json', parse_file(src)))

    titles = {f'{dom}/{rel}': doc['title'] for dom, rel, _, doc in docs}
    name_index = {}
    for dom, rel, _, doc in docs:
        for k in (norm_name(clean_title(doc['title'] or '')), norm_name(rel.split('/')[-1])):
            if k:
                name_index.setdefault(k, []).append(f'{dom}/{rel}')

    # 2패스: 위임 대상 해석 + 라벨 영어화 + 쓰기
    index = {d: [] for d in doms}
    deleg = resolved = 0
    dangling = []
    for dom, rel, out, doc in docs:
        path = f'{dom}/{rel}'
        seen, kept = set(), []
        for o in doc['outside']:
            o['label'] = english_label(o, titles)
            key = (o['label'], o.get('ref'))
            if key in seen:      # 폴더 참조 둘이 같은 폴더를 가리키면 영어화 후 같은 줄이 된다
                continue
            seen.add(key)
            kept.append(o)
        doc['outside'] = kept
        for it in iter_items(doc):
            if 'delegate' not in it:
                continue
            deleg += 1
            if not it['delegate']:
                it['delegate'] = resolve_delegate(it['t'], doc, path, name_index)
            if it['delegate']:
                resolved += 1
            else:
                dangling.append((path, it['t']))
        io.open(out, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
        secs, items = counts(doc)
        index[dom].append({'path': rel, 'title': doc['title'], 'ai': doc['ai'],
                           'parts': len(doc['parts']), 'sections': secs, 'items': items})

    grand = 0
    for dom in doms:
        index[dom].sort(key=lambda r: r['path'])
        io.open(os.path.join(ROOT, dom, 'index.json'), 'w', encoding='utf-8', newline='\n').write(
            json.dumps(index[dom], ensure_ascii=False, indent=2) + '\n')
        n = sum(r['items'] for r in index[dom])
        grand += n
        print(f"{dom}: 로드맵 {len(index[dom])}개 · 항목 {n}개")
    print(f"합계 항목 {grand}개")
    print(f"위임 {deleg}개 · 대상 연결 {resolved}개 · 미해결 {len(dangling)}개")
    for path, label in dangling:
        print(f"  대상을 못 찾음: {path} — {label}", file=sys.stderr)


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    sys.exit(main())
