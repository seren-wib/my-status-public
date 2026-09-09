"""고아 로드맵 세기 — 아무도 안 가리키는 로드맵.

들어오는 참조로 치는 것: 위임 불릿 · `이 로드맵 밖`(경로·폴더·이름) · 섹션 참조 ·
항목 이름이 로드맵 이름과 붙는 것(front/js/links.js resolve와 같은 규칙) · 자격증 파일의 로드맵 경로.

**role-based가 고아인 것은 결함이 아니다** — 최상위 목표라 아무도 안 가리키는 게 정상이고,
참조를 받는다면 오히려 role→role·skill→role 불변식 위반을 의심할 것(docs/architecture.md).
참조를 바꾸는 작업(위임 접기·경로 이동) 뒤에 다시 돌린다.

    python tools/check_orphans.py
"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, 'tools')
from parse_roadmaps import norm_name, clean_title, ALIAS

DOMS = ['software','social','creative','academics','business','finance','health','language','meta']
docs = {}
for d in DOMS:
    for e in json.load(open(f'roadmaps/{d}/index.json', encoding='utf-8')):
        p = f'{d}/{e["path"]}'
        docs[p] = json.load(open(f'roadmaps/{d}/{e["path"]}.json', encoding='utf-8'))

name_index = {}
for p, doc in docs.items():
    for k in (norm_name(clean_title(doc.get('title') or '')), norm_name(p.split('/')[-1])):
        if k:
            name_index.setdefault(k, []).append(p)

def resolve_name(text, self_path):
    """links.js makeResolver와 같은 규칙 — 같은 분야 우선, 자기 자신 제외."""
    t = str(text).strip()
    if not t or '/' in t or len(t) > 40:
        return None
    n = norm_name(t)
    if not n:
        return None
    cands = (name_index.get(n) or name_index.get(ALIAS.get(n, '')) or
             (name_index.get(n[:-1]) if n.endswith('s') else None) or [])
    dom = self_path.split('/')[0] + '/'
    for c in cands:
        if c.startswith(dom) and c != self_path:
            return c
    for c in cands:
        if c != self_path:
            return c
    return None

inbound = {p: {} for p in docs}          # 대상 → {출처: [종류]}
def hit(target, src, kind):
    if target in inbound and target != src:
        inbound[target].setdefault(src, set()).add(kind)

def folder_hit(ref, src):
    """`.../Frameworks/` 같은 폴더 참조 → 그 폴더 아래 로드맵 전부."""
    pre = ref if ref.endswith('/') else ref + '/'
    n = 0
    for p in docs:
        if p.startswith(pre):
            hit(p, src, 'folder'); n += 1
    return n

def eat_ref(entry, src, kind):
    ref = (entry.get('ref') or '').strip()
    if ref.endswith('/'):
        if folder_hit(ref, src): return
        ref = ref.rstrip('/')
    if ref in docs:
        hit(ref, src, kind); return
    if ref and not ref.startswith('http'):
        if folder_hit(ref, src): return
    by_name = resolve_name(entry.get('label') or '', src)
    if by_name:
        hit(by_name, src, kind + '-name')

for src, doc in docs.items():
    for o in doc.get('outside') or []:
        eat_ref(o, src, 'outside')
    for part in doc.get('parts') or []:
        for sec in part.get('sections') or []:
            for r in sec.get('refs') or []:
                eat_ref(r, src, 'secref')
            groups = [sec.get('items') or []]
            for sub in sec.get('subs') or []:
                for r in sub.get('refs') or []:
                    eat_ref(r, src, 'secref')
                groups.append(sub.get('items') or [])
            for items in groups:
                for it in items:
                    if it.get('delegate'):
                        hit(it['delegate'], src, 'delegate')
                    else:
                        t = str(it.get('t') or '').split(' / ')[0]
                        by_name = resolve_name(t, src)
                        if by_name:
                            hit(by_name, src, 'item-name')

certs = 0
cidx = json.load(open('certifications/index.json', encoding='utf-8'))
for c in cidx:
    f = json.load(open(f'certifications/{c["domain"]}.json', encoding='utf-8'))
    for cat in f.get('categories') or []:
        for cert in cat.get('certs') or []:
            for p in cert.get('roadmaps') or []:
                if p in inbound:
                    inbound[p].setdefault(f'cert:{c["domain"]}', set()).add('cert'); certs += 1

orph = sorted(p for p, v in inbound.items() if not v)
print(f'로드맵 {len(docs)} · 자격증 링크 {certs} · 고아 {len(orph)}')
role = [p for p in orph if 'role-based' in p]
print(f'  그중 role-based(최상위라 정상) {len(role)}')
for p in orph:
    kind = 'role' if 'role-based' in p else 'skill/flat'
    print(f'  {p:60s} [{kind}] {docs[p].get("title")}')

# 참조가 1건뿐인 것도 같이 — 접힌 뒤 얇아진 것
thin = sorted((len(v), p) for p, v in inbound.items() if len(v) == 1 and 'role-based' not in p)
print(f'\n참조 1건뿐인 skill/flat 로드맵 {len(thin)}')
for _, p in thin[:25]:
    src = list(inbound[p])[0]
    print(f'  {p:60s} ← {src} {sorted(inbound[p][src])}')

print('\n=== role-based로 들어오는 참조의 출처 (불변식 점검) ===')
from collections import Counter
c = Counter()
detail = {}
for p, v in inbound.items():
    if 'role-based' not in p:
        continue
    for src, kinds in v.items():
        layer = ('cert' if src.startswith('cert:') else
                 'role→role' if 'role-based' in src else 'skill→role')
        c[layer] += 1
        detail.setdefault(layer, []).append(f'{src} → {p} {sorted(kinds)}')
for k, n in c.most_common():
    print(f'  {k}: {n}건')
    for line in detail[k][:4]:
        print('     ', line)
