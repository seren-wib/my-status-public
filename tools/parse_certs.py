# -*- coding: utf-8 -*-
"""자격증 md -> json 변환기.

certifications/<분야>.md 를 읽어 같은 폴더에 .json 을 생성하고
certifications/index.json 을 만든다. 양식은 docs/certification-format.md.

로드맵 파서(parse_roadmaps.py)와 별개다 — 자격증은 체크박스가 아니라 카드 목록이고
진행률 분모에 들어가지 않는다.
"""
import io
import json
import os
import re
import sys
# 윈도우 콘솔은 cp949/cp1252라 한글 print 한 줄에 도구가 죽는다 (serve.py와 같은 함정)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = 'certifications'
ROADMAP_ROOT = 'roadmaps'

KEYS = {
    '발급': 'issuer',
    '지역': 'region',
    '조건': 'eligibility',
    '시험': 'exam',
    '갱신': 'renewal',
    '로드맵': 'roadmaps',
    '비고': 'note',
}
REQUIRED = ['issuer', 'region', 'eligibility', 'exam', 'renewal', 'roadmaps']

H2 = re.compile(r'^##\s+(.+?)\s*$')
H3 = re.compile(r'^###\s+(.+?)\s+`([a-z0-9-]+)`\s*$')
KV = re.compile(r'^-\s+([가-힣]+)\s*:\s*(.+?)\s*$')
BACKTICK = re.compile(r'`([^`]+)`')


def strip_ext(p):
    return p[:-3] if p.endswith('.md') else p


def parse(path, domain, errors):
    title = None
    categories = []
    cat = None
    cert = None

    def close():
        if cert is None:
            return
        missing = [k for k in REQUIRED if not cert.get(k)]
        if missing:
            errors.append('%s: %s 에 키 누락 %s' % (domain, cert['id'], ','.join(missing)))
        cat['certs'].append(cert)

    for no, raw in enumerate(io.open(path, encoding='utf-8'), 1):
        line = raw.rstrip('\n')
        if line.startswith('# '):
            title = line[2:].strip()
            continue
        m = H3.match(line)
        if m:
            close()
            if cat is None:
                errors.append('%s:%d: 분류(##) 없이 자격증이 나옴' % (domain, no))
                cat = {'title': None, 'certs': []}
                categories.append(cat)
            cert = {'id': m.group(2), 'name': m.group(1).strip(), 'roadmaps': [], 'note': None}
            continue
        m = H2.match(line)
        if m:
            close()
            cert = None
            cat = {'title': m.group(1).strip(), 'certs': []}
            categories.append(cat)
            continue
        m = KV.match(line)
        if m and cert is not None:
            key = KEYS.get(m.group(1))
            if key is None:
                errors.append('%s:%d: 모르는 키 %s' % (domain, no, m.group(1)))
                continue
            val = m.group(2).strip()
            if key == 'roadmaps':
                cert['roadmaps'] = [strip_ext(x) for x in BACKTICK.findall(val)]
                if not cert['roadmaps']:
                    errors.append('%s:%d: 로드맵 경로가 백틱으로 안 싸임' % (domain, no))
            else:
                cert[key] = val
    close()
    categories = [c for c in categories if c['certs']]
    return {'domain': domain, 'title': title,
            'count': sum(len(c['certs']) for c in categories),
            'categories': categories}


def check_paths(doc, errors):
    """로드맵 경로가 실제 파일 또는 폴더인지 확인 (prefix 매칭이므로 둘 다 허용)."""
    for cat in doc['categories']:
        for cert in cat['certs']:
            for r in cert['roadmaps']:
                base = os.path.join(ROADMAP_ROOT, r)
                if not (os.path.isdir(base) or os.path.exists(base + '.md')):
                    errors.append('%s: %s 의 로드맵 경로 없음 — %s' % (doc['domain'], cert['id'], r))


def main():
    errors = []
    seen = {}
    index = []
    for name in sorted(os.listdir(ROOT)):
        if not name.endswith('.md'):
            continue
        domain = name[:-3]
        doc = parse(os.path.join(ROOT, name), domain, errors)
        check_paths(doc, errors)
        for cat in doc['categories']:
            for cert in cat['certs']:
                if cert['id'] in seen:
                    errors.append('id 중복 %s — %s, %s' % (cert['id'], seen[cert['id']], domain))
                seen[cert['id']] = domain
        out = os.path.join(ROOT, domain + '.json')
        with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write('\n')
        index.append({'domain': domain, 'title': doc['title'], 'count': doc['count']})
        print('%s: 자격증 %d개 · 분류 %d개' % (domain, doc['count'], len(doc['categories'])))

    with io.open(os.path.join(ROOT, 'index.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('합계 %d개 (분야 %d)' % (sum(i['count'] for i in index), len(index)))

    if errors:
        print('\n오류 %d건:' % len(errors))
        for e in errors:
            print(' -', e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
