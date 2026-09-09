"""로그 → 스탯 수치 계산.

아래 AXES(축·스킬 → 로드맵 매핑) + 로드맵 json(분모) + data/log/**.jsonl(완료)을 읽어
data/stats.json 을 생성한다. 생성물은 손으로 고치지 말 것 — 재실행하면 덮어씀.
매핑을 바꾸려면 AXES를 고칠 것. 규칙·사유는 docs/stat-model.md. stdlib만 사용.
"""
import io
import json
import os
import sys

# 윈도우 콘솔은 cp949/cp1252라 한글 print 한 줄에 도구가 죽는다 (serve.py와 같은 함정)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOMAINS = ['software', 'social', 'creative', 'academics', 'business', 'finance', 'health', 'language', 'meta']   # 로드맵 내용이 있는 분야만

AXES = [
    {'id': 'KNOWLEDGE', 'label': '지식', 'measures': '아는 것의 축적', 'kind': 'gauge', 'sources': ['checkbox'],
     'skills': [
         {'id': 'History', 'label': '역사·시대', 'roadmaps': ['academics/history']},
         {'id': 'Human', 'label': '심리·사회', 'roadmaps': ['academics/psychology']},
         {'id': 'Economy', 'label': '경제·금융', 'roadmaps': ['academics/economics', 'finance'], 'exclude': ['finance/personal-finance']},
         {'id': 'Formal', 'label': '수리 — 수·논리로 사고', 'roadmaps': ['academics/math']},
         {'id': 'Technical', 'label': 'CS 이론', 'roadmaps': ['software/skill-based/CS-Theory'], 'exclude': ['software/skill-based/CS-Theory/code-review']},
         {'id': 'Linguistic', 'label': '외국어', 'roadmaps': ['language/english', 'language/japanese']},
     ]},
    {'id': 'CRAFT', 'label': '제작', 'measures': '만들어내는 것', 'kind': 'gauge', 'sources': ['checkbox', 'works'],
     'skills': [
         {'id': 'Engineering', 'label': '코드로 만듦', 'roadmaps': ['software/role-based', 'software/skill-based/Languages', 'software/skill-based/Frameworks', 'software/skill-based/AI', 'software/skill-based/Data-DB', 'software/skill-based/Blockchain', 'software/skill-based/Game-Dev']},
         {'id': 'Interfacing', 'label': '도구·시스템을 다룸', 'roadmaps': ['software/skill-based/Infra-DevOps', 'software/skill-based/Build-Tools']},
         {'id': 'Diagnosis', 'label': '고장난 걸 고침', 'roadmaps': ['software/skill-based/Testing', 'software/skill-based/CS-Theory/code-review']},
         {'id': 'Composition', 'label': '글로 만듦 (작법)', 'roadmaps': ['creative/skill-based/Writing', 'creative/role-based/fiction']},
         {'id': 'Visual', 'label': '이미지로 만듦', 'roadmaps': ['creative/skill-based/Drawing', 'creative/role-based/illustration', 'creative/role-based/comics', 'software/skill-based/Design']},
         {'id': 'Sonic', 'label': '소리·영상으로 만듦', 'roadmaps': ['creative/skill-based/Sound', 'creative/skill-based/Video', 'creative/role-based/song', 'creative/role-based/video-production']},
         # 설득 알맹이는 social 본체(체크조건 필터), business엔 검증·판매 프로세스만 남음 → Rhetoric 아닌 CRAFT
         {'id': 'Venture', 'label': '사업 — 팔리는 구조를 만듦', 'roadmaps': ['business'], 'exclude': ['business/skill-based/Operations/hiring-team']},
     ]},
    {'id': 'CHARACTER', 'label': '성격', 'measures': '자기조절·의지·회복탄력성', 'kind': 'gauge', 'sources': ['behavior'],
     'skills': [
         {'id': 'Volition', 'label': '의지력·일관성', 'roadmaps': ['meta/habits'], 'metrics': ['스트릭']},
         {'id': 'Composure', 'label': '압박·실패를 견딤', 'roadmaps': [], 'metrics': ['행동 로그']},
         {'id': 'Temporal', 'label': '시간·자원 배분', 'roadmaps': ['meta/time-management', 'finance/personal-finance']},
         {'id': 'Focus', 'label': '주의 지속', 'roadmaps': [], 'metrics': ['행동 로그']},
     ]},
    {'id': 'SOCIAL', 'label': '사회성', 'measures': '대인 영향력·관계', 'kind': 'gauge', 'sources': ['checkbox', 'behavior'],
     'skills': [
         # social은 role-based(목표 축) + skill-based(부품) 2층. 둘 다 셈 — software의 role/skill 중복 허용과 동일
         {'id': 'Rhetoric', 'label': '말로 사람을 움직임', 'roadmaps': [
             'social/skill-based/Influence', 'social/skill-based/GroupInfluence',
             'social/skill-based/Manipulation', 'social/skill-based/Coercion',
             'social/skill-based/Deception', 'social/skill-based/Speaking',
             'social/skill-based/Conflict',
             # role 층은 2026-08-26 인물상(archetype) 15개로 재편 — 각 archetype은 한 스킬에만 귀속
             'social/role-based/demagogue', 'social/role-based/orator',
             'social/role-based/cult-leader', 'social/role-based/negotiator',
             'social/role-based/mediator', 'social/role-based/operative',
             'social/role-based/con-artist', 'social/role-based/coercer',
             'social/role-based/manipulator']},
         {'id': 'Empathy', 'label': '정서 공명 — 상대의 상태를 느낌', 'roadmaps': [
             'social/skill-based/Relating', 'social/role-based/connector']},
         {'id': 'Insight', 'label': '간파 — 상대의 의도·이해관계를 읽음', 'roadmaps': [
             'social/skill-based/Reading', 'social/role-based/interrogator']},
         {'id': 'Presence', 'label': '존재감 — 내가 읽히는 방식을 다룸', 'roadmaps': [
             'social/skill-based/Presence', 'social/skill-based/Seduction',
             'social/role-based/public-figure', 'social/role-based/seducer']},
         {'id': 'Authority', 'label': '사람을 움직이고 책임짐', 'roadmaps': [
             'social/skill-based/Leading', 'social/role-based/leader',
             'social/role-based/political-operator',
             'business/skill-based/Operations/hiring-team']},
     ]},
    {'id': 'PHYSIQUE', 'label': '신체', 'measures': '몸', 'kind': 'gauge', 'sources': ['measurement'],
     'skills': [
         # 실측 백분위 = 스킬 숙련도. 원천은 data/log/physique.jsonl(종목별 최신값), 귀속·표준표는 docs/stat-model.md
         {'id': 'Strength', 'label': '최대 근력', 'roadmaps': [], 'metrics': ['squat·bench·deadlift 1RM — Strength Level 백분위']},
         {'id': 'Endurance', 'label': '심폐지구력', 'roadmaps': [], 'metrics': ['cooper(12분 달리기)→VO2max — ACSM 백분위']},
         {'id': 'Stamina', 'label': '근지구력', 'roadmaps': [], 'metrics': ['pushup — ACSM 백분위', 'plank']},
         {'id': 'Mobility', 'label': '유연성·가동범위', 'roadmaps': [], 'metrics': ['sit-and-reach — ACSM 백분위']},
         {'id': 'Recovery', 'label': '회복·수면 질', 'roadmaps': [], 'metrics': ['수면시간', 'HRV']},   # 표준표 미선정 — 보류
     ]},
    {'id': 'INVENTORY', 'label': '소유', 'measures': '돈·증명·작업물·경력', 'kind': 'panel', 'sources': ['manual'],
     'skills': [
     ]},
]

UNMAPPED = ['health', 'meta/learning']   # 사유는 docs/stat-model.md

# 숙련도 가중치 — lv별 기여분. 실증%·학습%가 "칸을 몇 개 끝냈나"를 세는 것과 달리
# 숙련도%는 **얼마나 깊이 아나**를 재므로 lv:1·2도 센다(2026-09-01, docs/stat-model.md 규칙 7).
# 곡선이 볼록한 이유: 이름만 스무 개가 개념 하나와 같아야 하고, 3→4 간격이 제일 커야
# 실증이 목표로 남는다. 이 dict가 **유일한 원본**이다 — stats.json의 `weights`로 실려 나가
# 프론트(front/js/merge.js)가 카드 색칠에 같은 값을 쓴다. 여기만 고치면 화면까지 따라온다.
WEIGHTS = {1: 0.05, 2: 0.2, 3: 0.6, 4: 1.0}


def load(p):
    return json.load(io.open(p, encoding='utf-8'))


# 파일 기준 캐시 — 같은 프로세스가 여러 번 재생성할 때(serve.py의 /api/log)만 의미가 있다.
# 기록 한 줄을 저장하면 바뀌는 건 로그 파일 하나인데, 로드맵 json 357개를 다시 파싱해
# 슬롯 목록을 다시 조립하고 로그 348개를 다시 열던 것을 없앤다.
# 키에 mtime·크기가 들어가므로 parse_roadmaps.py가 json을 다시 쓰거나 로그가 append되면
# 저절로 무효화된다. CLI 1회 실행은 같은 파일을 두 번 안 보므로 동작·출력이 그대로다.
# **캐시된 값은 읽기 전용으로 다뤄야 한다** — 아무도 고치지 않는 전제로 나눠 쓴다.
_CACHE = {}


def by_file(kind, p, make):
    """`make(p)`의 결과를 파일 판본(mtime·크기)째로 들고 있는다. 파일이 바뀌면 다시 만든다.

    `kind`는 같은 파일에서 뽑은 다른 산출물을 가르는 이름(슬롯 목록 vs 로그 상태).
    (kind, 경로)당 한 칸만 둔다 — 서버가 오래 떠 있어도 캐시가 계속 부풀지 않게.
    """
    key = (kind, os.path.abspath(p))
    st = os.stat(p) if os.path.isfile(p) else None
    stamp = (st.st_mtime_ns, st.st_size) if st else None
    hit = _CACHE.get(key)
    if hit is None or hit[0] != stamp:
        hit = _CACHE[key] = (stamp, make(p))
    return hit[1]


def under(path, entry):
    return path == entry or path.startswith(entry + '/')


def item_name(t):
    """항목 텍스트 → 진행도 키에 쓸 이름 (첫 ` / ` 앞부분).

    항목 문법이 `English Name / 한국어 설명`이라 텍스트 전체를 키로 쓰면 설명을
    다듬을 때마다 기존 기록이 허공을 가리킴. 이름만 잡으면 전 로드맵 23985개가
    충돌 0으로 유니크함(2026-08-26 실측). 새 항목을 쓸 때 같은 섹션 안에서
    이름이 겹치지 않게 할 것 — 겹치면 두 항목이 한 키로 뭉친다.
    """
    return t.split(' / ', 1)[0]


def roadmap_sections(doc):
    """로드맵 json → [(섹션 라벨, 일반 슬롯 목록, 택1 그룹 목록)].

    슬롯은 두 종류다.
      ('item', (섹션, 서브섹션, 이름)) — 로그로 상태가 정해지는 자기 항목
      ('deleg', 대상 로드맵 경로)      — 위임 칸. 상태는 대상 로드맵에서 파생한다

    헤딩 `택 1` 그룹은 분모 1 — 안에서 하나만 하면 로드맵 요구는 끝이므로
    항목 수만큼 세면 100%에 닿을 수 없는 분모가 됨. 인라인 택1은 일반 항목.
    섹션 단위로 쪼개 두는 건 progress의 `secs` 요약을 같은 계산에서 뽑기 위함
    (2026-08-27. 선형 커서 제거 — docs/progress-format.md).
    """
    out = []
    for part in doc['parts']:
        for sec in part['sections']:
            key = f"{sec['no']}. {sec['title']}"

            # 항목 슬롯 키에 서브섹션이 들어간다 — 같은 섹션 안에서 항목명이 겹치는 경우가
            # 60건 있고 (redis `Usecases`가 Strings·Lists·Sets 아래 하나씩) 서브섹션을 빼면
            # 서로 다른 항목이 한 키로 뭉쳐 하나만 해도 전부 완료로 잡힌다. 섹션 직속은 sub=None.
            # 위임 슬롯은 로그 키가 없다 — 같은 대상을 두 불릿이 가리키면(aspnet-core의
            # `Git`·`GitHub, GitLab, BitBucket`) 두 칸으로 센다. 불릿 하나가 한 칸이다.
            def slots(its, sub=None, _key=key):
                return [('deleg', it['delegate']) if 'delegate' in it
                        else ('item', (_key, sub, item_name(it['t'])))
                        for it in its]

            plain, groups = [], []
            if sec.get('choice'):
                groups.append(slots(sec['items'])
                              + [s for sub in sec['subs']
                                 for s in slots(sub['items'], sub['title'])])
            else:
                plain += slots(sec['items'])
                for sub in sec['subs']:
                    ss = slots(sub['items'], sub['title'])
                    (groups.append(ss) if sub.get('choice') else plain.extend(ss))

            ingroup = {s for g in groups for s in g}
            seen, uniq = set(), []
            for s in plain:
                if s in ingroup:       # 같은 이름이 그룹 안팎에 다 있으면 그룹 쪽
                    continue
                if s[0] == 'item':     # 항목 키는 유일해야 한다(현재 충돌 0). 위임 칸은 중복 허용
                    if s in seen:
                        continue
                    seen.add(s)
                uniq.append(s)
            out.append((key, uniq, groups))
    return out


def own_only(plain, groups):
    """위임 칸을 뺀 (일반, 그룹). 1패스는 자기 항목만으로 진행률을 낸다."""
    keep = lambda ss: [s for s in ss if s[0] == 'item']
    return keep(plain), [g for g in map(keep, groups) if g]


def item_keys(secs):
    """로그가 붙을 수 있는 키 전체 — 오타 난 로그 줄을 잡는 데 쓴다."""
    return {v for _, plain, groups in secs
            for kind, v in plain + [s for g in groups for s in g] if kind == 'item'}


def deleg_state(t):
    """대상 로드맵의 **자기 항목** 집계 → 위임 칸 (상태, 진행중 여부). 미기록이면 None.

    상태 3은 "기록 있음(부분 진행)"이지 진행중이 아니다(2026-08-29 분리) —
    진행중은 **대상에 doing:true 레코드가 실제로 있을 때만** 참이다.
    옛 규칙은 부분 진행을 통째로 진행중으로 세어, 위임 대상이 조금이라도 진행되면
    상위 로드맵마다 진행중 배지가 박혔다.
    대상의 위임 칸은 보지 않는다 — social skill끼리 순환 참조가 가능해서
    재귀로 파생시키면 무한루프가 난다. 그래서 2패스 고정(docs/stat-model.md 규칙 8).
    """
    if not t['total'] or not t['touched']:
        return None
    if t['done'] == t['total']:
        state = 1
    elif t['done'] + t['theory'] == t['total']:
        state = 2
    else:
        state = 3
    return state, t['doing'] > 0


def tally(plain, groups, state, deleg, dmast=None):
    """(완료, 이론완료, 진행중, 기록있음, 분모, 가중합).

    lv:4 완료 · lv:3 이론완료 · `doing` 플래그 진행중(수준과 직교 — lv:3+doing이
    "이론 끝, 구현 진행중"). lv:1(이름만)·lv:2(개념)는 완료·이론 어느 쪽도 아니지만
    '기록있음'에는 든다 — 위임 파생과 progress 표시가 미기록과 가르는 데 쓴다.
    %에는 안 들어간다(docs/stat-model.md 규칙 7).

    가중합은 숙련도%의 분자 — 칸마다 `WEIGHTS[lv]`를 더한다. **위임 칸은 lv 환산을 쓰지 않고
    대상 로드맵의 숙련도 비율(`dmast`)을 그대로 받는다.** 상태 3(부분 진행)이 lv 없음이라
    0으로 떨어지던 구멍이 여기서 막힌다 — 대상을 절반 아는 칸은 절반으로 센다.
    """
    def rec(slot):
        kind, v = slot
        if kind == 'item':
            return state.get(v)
        d = deleg.get(v)   # 위임 칸: (파생 상태, 진행중)을 의사 레코드로 환산
        if d is None:
            return None
        st, doing = d
        out = {1: {'lv': 4}, 2: {'lv': 3}, 3: {}}[st]   # 3 = 기록 있음(부분 진행), lv 없음
        return dict(out, doing=True) if doing else out

    def lv(slot):
        r = rec(slot)
        return r.get('lv', 0) if r else 0

    def wt(slot):
        if slot[0] == 'deleg':
            return (dmast or {}).get(slot[1], 0.0)
        return WEIGHTS.get(lv(slot), 0.0)

    done = sum(1 for s in plain if lv(s) == 4)
    theory = sum(1 for s in plain if lv(s) == 3)
    doing = sum(1 for s in plain if (rec(s) or {}).get('doing'))
    touched = sum(1 for s in plain if rec(s))
    weight = sum(wt(s) for s in plain)
    for g in groups:   # 그룹 = 분모 1. 가장 높은 lv 하나로 대표, doing은 독립 전파
        lvs = [lv(s) for s in g]
        if 4 in lvs:
            done += 1
        elif 3 in lvs:
            theory += 1
        if any((rec(s) or {}).get('doing') for s in g):
            doing += 1
        if any(rec(s) for s in g):
            touched += 1
        weight += max(wt(s) for s in g)   # 대표 하나 — 분모가 1칸이니 분자도 1칸분
    return done, theory, doing, touched, len(plain) + len(groups), weight


def read_log(path):
    """jsonl → {(sec, sub, 항목 이름): 시점이 가장 늦은 레코드}. `lv`도 `doing`도 없는 줄은 무시.

    레코드는 `lv`(도달 수준 1~4) + `doing`(진행중 플래그, 수준과 직교) 2필드다
    (2026-08-29 전환 — 구 단일 `s`는 "이론완료 후 구현 진행중"과
    "이름만 앎 vs 안 함"을 표현하지 못했다. docs/progress-format.md).
    `sub`는 서브섹션(`###`) 제목. 섹션 직속 항목이면 없거나 null.
    `item`은 이름만 적는 게 규칙이지만, 옛 기록이 설명까지 담고 있어도
    `item_name`으로 잘라 같은 키로 붙는다. 레코드 통째로 두는 건 `at`이
    progress의 `doing`에 필요해서다.

    승자는 **파일 순서가 아니라 `at`**이다(2026-08-29 개정). 같은 날이면 파일 순서로
    가른다 — 하루에 lv:1→lv:3→lv:4를 잇달아 쓰는 게 정상 흐름이라서다. 파일 순서만 보던
    옛 규칙은 옛 날짜를 백필로 덧붙이면 최신 판정을 조용히 덮어썼다.
    화면 쪽 `front/js/merge.js`의 `parseLog`가 같은 규칙이다 — 한쪽만 고치지 말 것.
    """
    return by_file('log', path, _read_log)


def _read_log(path):
    state = {}
    if not os.path.isfile(path):
        return state
    for ln in io.open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        r = json.loads(ln)
        if 'lv' in r or 'doing' in r:
            k = (r['sec'], r.get('sub'), item_name(r['item']))
            prev = state.get(k)
            if prev is None or (r.get('at') or '') >= (prev.get('at') or ''):
                state[k] = r
    return state


def collect():
    """({roadmap 경로: 집계}, {분야: progress}, 알 수 없는 키 목록).

    **2패스다.** 1패스는 로드맵마다 자기 항목만으로 진행률을 낸다. 2패스는 위임 칸
    296개에 대상 로드맵의 1패스 결과를 얹어 분모 1칸씩으로 센다(2026-08-27).
    위임을 분모에서 빼던 옛 방식은 "leverage를 다 해도 coercer가 안 움직인다"는
    구멍이 있었다 — 로드맵이 파일로 뺀 부품은 선택 사항이 아니라 필수 부품이다.

    progress는 로그에서 다시 만든다 — 원천은 언제나 log, progress는 캐시다.
    기록이 하나도 없는 로드맵은 담지 않는다(빈 틀 348개를 매 세션 읽던 낭비 제거).
    """
    parsed, unknown = {}, []
    for dom in DOMAINS:
        for row in load(f'roadmaps/{dom}/index.json'):
            path = f"{dom}/{row['path']}"
            # 슬롯 목록만 캐시하고 원본 json은 들고 있지 않는다 — 뽑고 나면 쓸 데가 없다
            secs = by_file('secs', f"roadmaps/{dom}/{row['path']}.json",
                           lambda q: roadmap_sections(load(q)))
            state = read_log(f"data/log/{path}.jsonl")
            known = item_keys(secs)
            for k in state:
                if k not in known:
                    unknown.append((path, k))
            parsed[path] = (dom, row['path'], secs, state)

    own = {}   # 1패스 — 자기 항목만
    for path, (_, _, secs, state) in parsed.items():
        d = th = dg = tc = t = 0
        w = 0.0
        for _, plain, groups in secs:
            a, b, c, e, n, g = tally(*own_only(plain, groups), state, {})
            d, th, dg, tc, t, w = d + a, th + b, dg + c, tc + e, t + n, w + g
        own[path] = {'total': t, 'done': d, 'theory': th, 'doing': dg, 'touched': tc,
                     'weight': w}
    deleg = {path: deleg_state(t) for path, t in own.items()}
    # 위임 칸이 받아갈 숙련도 비율. 상태 파생과 같은 이유로 **자기 항목 집계에서만** 낸다
    # — 대상의 위임 칸까지 보면 순환 참조로 무한루프(규칙 8, 2패스 고정)
    dmast = {path: (t['weight'] / t['total'] if t['total'] else 0.0)
             for path, t in own.items()}

    out, prog = {}, {dom: {} for dom in DOMAINS}
    for path, (dom, rel, secs, state) in parsed.items():   # 2패스 — 위임 칸 포함
        total = done = theory = doing = 0
        weight = 0.0
        summary, doing_items = {}, []
        for label, plain, groups in secs:
            d, th, dg, tc, t, g = tally(plain, groups, state, deleg, dmast)
            done, theory, doing, total = done + d, theory + th, doing + dg, total + t
            weight += g
            if tc:   # 손댄 섹션만 — 없는 섹션은 미진행 (lv:1·2만 있어도 손댄 것)
                summary[label] = f'{d}/{th}/{t}'
        # `doing`은 "이어서 하기" 북마크라 로그가 있는 자기 항목만 싣는다.
        # 진행중인 위임 칸은 대상 로드맵 쪽 progress에 이미 실려 있다
        for (sec, sub, item), r in state.items():
            if r.get('doing'):
                e = {'sec': sec, 'item': item, 'at': r.get('at')}
                if sub:
                    e = {'sec': sec, 'sub': sub, 'item': item, 'at': r.get('at')}
                doing_items.append(e)

        d = deleg[path]
        out[path] = {'total': total, 'done': done, 'theory': theory, 'doing': doing,
                     'weight': weight,
                     # 위임 칸이 받아갈 숙련도 — **자기 항목만**(dmast). 이 로드맵 자신의
                     # `percent`는 자기 위임 칸까지 포함한 2패스 값이라 서로 다르다.
                     # 위임은 delegate_state와 같은 이유로 1패스 값을 쓴다(재귀 금지, 규칙 8)
                     'delegate_mastery': round(dmast[path] * 100, 2),
                     # 이 로드맵을 위임한 칸이 갖는 상태·진행중. 프론트가 같은 값을 써야
                     # 두 분모·두 상태가 어긋나지 않는다 (front/js/merge.js)
                     'delegate_state': d[0] if d else None,
                     'delegate_doing': bool(d and d[1])}
        if summary or doing_items:
            prog[dom][rel] = {'doing': sorted(doing_items, key=lambda e: e['at'] or ''),
                              'secs': summary}
    return out, prog, unknown


def write_progress(prog):
    """data/progress/<분야>-progress.json 재생성. 커서 없음 — 섹션별 요약 + 진행중 목록."""
    for dom, body in prog.items():
        io.open(f'data/progress/{dom}-progress.json', 'w', encoding='utf-8', newline='\n').write(
            json.dumps(body, ensure_ascii=False, indent=2) + '\n')


def pct(done, total):
    return round(done * 100 / total, 2) if total else None


def flat(t):
    """로드맵 집계 → stats.json에 실을 모양.

    원시 가중합(`weight`)은 빼고 `percent`(숙련도)로만 내보낸다 — 프론트가 분자와 %를
    둘 다 들고 있으면 어느 쪽이 원본인지 흐려지고, 재계산할 이유도 생긴다.
    """
    return {'total': t['total'], 'done': t['done'], 'theory': t['theory'],
            'doing': t['doing'],
            'delegate_state': t['delegate_state'], 'delegate_doing': t['delegate_doing'],
            'delegate_mastery': t['delegate_mastery'],
            'percent': pct(t['weight'], t['total'])}


def main():
    rm, prog, unknown = collect()
    if unknown:
        for path, k in unknown:
            print(f'로그가 없는 항목을 가리킴: {path} {k}', file=sys.stderr)
        return 1

    axes = []
    for ax in AXES:
        skills, sk_weights = [], []
        for sk in ax['skills']:
            hit = [p for p in rm
                   if any(under(p, e) for e in sk['roadmaps'])
                   and not any(under(p, e) for e in sk.get('exclude', []))]
            tot = sum(rm[p]['total'] for p in hit)
            done = sum(rm[p]['done'] for p in hit)
            theory = sum(rm[p]['theory'] for p in hit)
            weight = sum(rm[p]['weight'] for p in hit)
            sk_weights.append(weight)
            skills.append({
                'id': sk['id'], 'label': sk['label'],
                # percent = **숙련도 하나뿐**. lv별 가중합/분모 (docs/stat-model.md 규칙 7).
                # 실증%·학습%는 2026-09-01에 폐기 — 칸의 수준은 카드가 lv로 보여주므로
                # 퍼센트를 셋으로 쪼갤 이유가 없었다. 완료·이론 개수는 그대로 남는다
                'percent': pct(weight, tot),
                'done': done, 'theory': theory, 'total': tot,
                'doing': sum(rm[p]['doing'] for p in hit),
                'roadmaps': [dict(path=p, **flat(rm[p])) for p in sorted(hit)],
            })
        tot = sum(s['total'] for s in skills)
        done = sum(s['done'] for s in skills)
        theory = sum(s['theory'] for s in skills)
        weight = sum(sk_weights)
        axes.append({'id': ax['id'], 'label': ax['label'], 'measures': ax['measures'],
                     'kind': ax['kind'], 'sources': ax['sources'],
                     'percent': pct(weight, tot),
                     'done': done, 'theory': theory, 'total': tot,
                     'skills': skills})

    # 로드맵별 진행률 평면 인덱스 — 축 매핑과 무관하게 348개 전부.
    # UNMAPPED(health·meta/learning)도 여기엔 들어간다(프론트 카드 표시용).
    # `weights`는 숙련도 눈금의 원본을 화면까지 내보내는 통로다 — 프론트가 이걸 읽어
    # 카드를 칠하므로 WEIGHTS만 고치면 수치와 색이 같이 움직인다(front/js/merge.js)
    out = {'version': 1, 'weights': WEIGHTS, 'axes': axes,
           'roadmaps': {p: flat(rm[p]) for p in sorted(rm)}}
    io.open('data/stats.json', 'w', encoding='utf-8', newline='\n').write(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    write_progress(prog)
    for a in axes:
        print(f"{a['id']:10} 숙련 {a['percent']}%  "
              f"구현 {a['done']}(이론 {a['theory']})/{a['total']}")
    return 0


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    sys.exit(main())
