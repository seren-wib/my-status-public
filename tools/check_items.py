# -*- coding: utf-8 -*-
"""로드맵 항목 문법 검사기.

`tools/parse_roadmaps.py`가 만든 json을 읽어 항목 문법(`English Name / 한국어 설명`)의
위반과 경고를 뱉는다. 설명 채우기 배치를 돌릴 때마다 실행할 것 —
23985항목을 눈으로 볼 수는 없다.

**위반**은 데이터가 깨지는 것이라 반드시 고친다. **경고**는 문체 문제라 눈으로 판단한다.
규칙의 근거는 docs/architecture.md(항목 문법)와 docs/progress-format.md(진행도 키).

사용법:
    python tools/check_items.py             # 전 분야
    python tools/check_items.py software    # 한 분야
    python tools/check_items.py software/skill-based/Data-DB/sqlite   # 한 로드맵
    python tools/check_items.py --warn 5    # 특정 경고 번호만 자세히
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import io
import json
import os
import re
import collections

DOMAINS = ['software', 'social', 'creative', 'academics', 'business',
           'finance', 'health', 'language', 'meta']

TAGS = ('추천', '선택', '별도')
CHOICE = '택 1'
HANGUL = re.compile('[가-힣]')
# 설명이 서술문으로 끝나는지 — 항목은 "배울 것"이라 명사구로 끝내는 게 규칙
# `묶음`·`모음`·`도구 모음`은 명사다 — 명사형 어미 `음`을 통째로 잡으면 오탐이 난다
SENTENCE_END = re.compile(r'(했음|었음|됐음|됨|다)$')
# 실행형 1회 문장 — 천장을 1회 실행에 고정한다 (메모리 roadmap-ceiling-measurement)
ONE_SHOT = re.compile(r'(해보기|하기|한 번|한 장|한 곡|해보자)$')

MAX_DESC = 30      # 넘으면 두 가지를 말하고 있을 확률이 높다
MIN_DESC = 12      # 이하면 내용이 빈 것


def split_item(t):
    """항목 텍스트 → (이름, 설명). 진행도 키와 같은 규칙(첫 ` / ` 앞이 이름)."""
    return t.split(' / ', 1) if ' / ' in t else (t, '')


def walk(domains):
    """(로드맵 경로, 섹션 라벨, 서브섹션, 항목 dict) 를 흘려보낸다."""
    for dom in domains:
        idx = 'roadmaps/%s/index.json' % dom
        if not os.path.isfile(idx):
            continue
        for row in json.load(io.open(idx, encoding='utf-8')):
            path = '%s/%s' % (dom, row['path'])
            doc = json.load(io.open('roadmaps/%s/%s.json' % (dom, row['path']), encoding='utf-8'))
            for part in doc['parts']:
                for sec in part['sections']:
                    label = '%s. %s' % (sec['no'], sec['title'])
                    for it in sec['items']:
                        yield path, label, None, it
                    for sub in sec['subs']:
                        for it in sub['items']:
                            yield path, label, sub['title'], it


def check_md_tags(domains, only=None):
    """설명 안쪽에 백틱 태그가 든 항목을 찾는다 — md 원본을 읽는다.

    파서는 줄 어디에 있든 백틱 태그를 걷어낸다. 그래서 설명 한가운데에
    `선택` 같은 걸 백틱으로 감싸 쓰면 그 단어가 설명에서 통째로 사라진다.
    사라진 뒤의 json만 봐서는 알 수 없으므로 여기서만 md를 본다.

    이름 뒤·구분자 앞에 붙은 태그(`- [ ] Styling Approach `택 1` / …`)는 걸러낸다 —
    파서가 이름·설명·플래그를 다 살려내므로 표기 불일치일 뿐 손실이 아니다.
    """
    bad = []
    tag_re = re.compile(r'`([^`]+)`')
    tail_re = re.compile(r'(\s*`[^`]+`)+\s*$')
    for dom in domains:
        idx = 'roadmaps/%s/index.json' % dom
        if not os.path.isfile(idx):
            continue
        for row in json.load(io.open(idx, encoding='utf-8')):
            path = '%s/%s' % (dom, row['path'])
            if only and not (path == only or path.startswith(only + '/')):
                continue
            for raw in io.open('roadmaps/%s/%s.md' % (dom, row['path']), encoding='utf-8'):
                ln = raw.rstrip()
                if not ln.startswith('- [ ] '):
                    continue
                head = tail_re.sub('', ln)          # 줄 끝 태그 뭉치를 떼고
                if ' / ' not in head:
                    continue                        # 설명이 없으면 잃을 것도 없다
                desc = head.split(' / ', 1)[1]      # 설명 안쪽만 본다
                for m in tag_re.finditer(desc):
                    if m.group(1) in TAGS or m.group(1) == CHOICE:
                        bad.append((path, ln))
                        break
    return bad


def check(domains, only=None):
    violations = collections.defaultdict(list)   # 번호 → [(경로, 설명)]
    warnings = collections.defaultdict(list)
    seen_key = set()
    desc_owner = collections.defaultdict(set)    # 설명 문구 → {로드맵}
    total = 0

    for path, label, sub, it in walk(domains):
        if only and not (path == only or path.startswith(only + '/')):
            continue
        total += 1
        t = it['t']
        name, desc = split_item(t)
        where = '%s § %s%s' % (path, label, ' · ' + sub if sub else '')

        # 1. 슬래시 2개 이상 — 이름이 잘못 잘린다
        if t.count(' / ') >= 2:
            violations[1].append((where, t))

        # 2. 같은 (sec, sub) 안 이름 중복 — 진행도 키가 뭉친다
        key = (path, label, sub, name)
        if key in seen_key:
            violations[2].append((where, t))
        seen_key.add(key)

        # 3번(줄 끝이 아닌 백틱 태그)은 md를 봐야 잡힌다 — check_md_tags()가 맡는다.
        # 파서가 백틱을 이미 걷어낸 json으로는 원리상 검출이 불가능하다.

        if not desc:
            continue

        # 4. 파일을 넘어 같은 문구가 반복 — 보일러플레이트
        #    단 같은 이름(공유 제품)이면 설명이 같은 게 정상이다 —
        #    `SQLite`가 backend·ios에 다 있으면 설명이 갈리는 쪽이 오히려 이상하다.
        #    진짜 게으른 복붙은 **다른 이름에 같은 설명**이 붙는 것이므로 이름까지 같이 본다
        desc_owner[desc].add((path, name))
        # 5. 얄팍
        if len(desc) <= MIN_DESC:
            warnings[5].append((where, t))
        # 6. 실행형 1회 문장
        if ONE_SHOT.search(desc):
            warnings[6].append((where, t))
        # 7. 대시로 절을 이어붙인 압축 문체
        if '—' in desc or ' - ' in desc:
            warnings[7].append((where, t))
        # 8. 서술문 종결
        if HANGUL.search(desc) and SENTENCE_END.search(desc):
            warnings[8].append((where, t))
        # 9. 너무 김
        if len(desc) > MAX_DESC:
            warnings[9].append((where, t))

    for desc, owners in desc_owner.items():
        names = {n for _, n in owners}
        if len(owners) >= 2 and len(names) >= 2:      # 이름이 다른데 설명이 같다
            warnings[4].append((' · '.join(sorted(p for p, _ in owners)),
                                '%s  ← %s' % (desc, ' / '.join(sorted(names)))))

    return total, violations, warnings


LABELS = {
    1: '슬래시 2개 이상 — 이름이 잘못 잘린다',
    2: '같은 섹션 안 이름 중복 — 진행도 키가 뭉친다',
    3: '설명 안에 백틱 태그 — 파서가 그 단어를 지워 버린다',
    4: '이름이 다른데 설명이 같음 — 게으른 복붙',
    5: '설명 %d자 이하 — 얄팍' % MIN_DESC,
    6: '실행형 1회 문장 — 천장을 1회 실행에 고정',
    7: '대시로 절을 이어붙임 — 압축 문체',
    8: '서술문 종결 — 명사구로 끝낼 것',
    9: '설명 %d자 초과 — 두 가지를 말하고 있을 수 있음' % MAX_DESC,
}


def report(total, violations, warnings, detail=None):
    nv = sum(len(v) for v in violations.values())
    nw = sum(len(v) for v in warnings.values())
    print('항목 %d개 검사 — 위반 %d · 경고 %d' % (total, nv, nw))

    print('\n[위반]')
    if not nv:
        print('  없음')
    for n in sorted(violations):
        print('  %d. %s — %d건' % (n, LABELS[n], len(violations[n])))
        for where, t in violations[n][:20]:
            print('       %s\n         %s' % (where, t))
        if len(violations[n]) > 20:
            print('       … 외 %d건' % (len(violations[n]) - 20))

    print('\n[경고]')
    if not nw:
        print('  없음')
    for n in sorted(warnings):
        print('  %d. %s — %d건' % (n, LABELS[n], len(warnings[n])))
    if detail and detail in warnings:
        print('\n[경고 %d 상세] %s' % (detail, LABELS[detail]))
        for where, t in warnings[detail]:
            print('  %s\n    %s' % (where, t))

    return 1 if nv else 0


def main():
    argv = sys.argv[1:]
    detail = None
    if '--warn' in argv:
        i = argv.index('--warn')
        detail = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]   # 값까지 걷어내야 분야명으로 안 먹힌다
    args = [a for a in argv if not a.startswith('--')]

    target = args[0] if args else None
    if target and target.split('/')[0] not in DOMAINS:
        print('알 수 없는 분야: %s' % target)
        return 2
    domains = [target.split('/')[0]] if target else DOMAINS
    only = target if target and '/' in target else None

    total, violations, warnings = check(domains, only)
    for path, ln in check_md_tags(domains, only):
        violations[3].append((path, ln))
    return report(total, violations, warnings, detail)


if __name__ == '__main__':
    sys.exit(main())
