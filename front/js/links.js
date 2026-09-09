// 이름 → 로드맵 경로 해석. 로드맵 md는 "PostgreSQL" 처럼 이름만 적고 경로를 안 쓰는
// 참조가 많아서(220곳), 전 분야 index.json으로 이름 색인을 만들어 링크를 붙인다.
import { DOMAINS, getDomainIndex } from './api.js';
import { cleanTitle } from './ui.js';

// 대소문자·공백·점·하이픈·괄호 부연·and를 무시한 비교 키.
// `+`와 `#`은 언어 이름을 가르므로 남긴다 (C / C++ / C#)
export function normName(s) {
  return String(s)
    .toLowerCase()
    .replace(/\(.*?\)/g, '')
    .replace(/&/g, ' and ')
    .replace(/\broadmaps?\b/g, '')
    .replace(/\band\b/g, '')
    .replace(/[^a-z0-9+#]/g, '');
}

// 표기가 다른 것들 — 값은 경로가 아니라 색인 키라, 로드맵이 사라지면 조용히 안 붙는다
const ALIAS = {
  postgresql: 'postgresqldba',
  postgres: 'postgresqldba',
  git: 'gitgithub',
  github: 'gitgithub',
  golang: 'go',
};

let indexPromise = null;
// 경로 → 로드맵 제목. 이름 색인을 만들면서 같이 채운다 — 항목 카드 해석기가
// "항목 이름이 대상 제목과 정확히 같은가"를 물을 때 쓴다
const titles = new Map();
export const roadmapTitle = (path) => titles.get(path) || '';

export function loadLinkIndex() {
  if (indexPromise) return indexPromise;
  indexPromise = Promise.all(DOMAINS.map((d) => getDomainIndex(d.id))).then((idxs) => {
    // 키 하나에 후보를 전부 모은다 — 이름 충돌 7건(listening·reading·writing·speaking·
    // grammar·foundations·overview)은 여기서 고르지 않고 resolve가 분야로 가른다
    const map = new Map();
    idxs.forEach((idx, i) => (idx || []).forEach((e) => {
      const path = `${DOMAINS[i].id}/${e.path}`;
      titles.set(path, cleanTitle(e.title));
      const keys = [normName(cleanTitle(e.title)), normName(e.path.split('/').pop())];
      for (const k of keys) {
        if (!k) continue;
        const list = map.get(k) || map.set(k, []).get(k);
        if (!list.includes(path)) list.push(path);
      }
    }));
    return map;
  });
  return indexPromise;
}

// 링크를 걸 만한 이름인지 — "이름 / 설명"형 항목과 긴 문장은 제외
const LINKABLE = /^[^/]{1,40}$/;

// 후보 중 하나를 고른다 — **같은 분야 우선**(tools/parse_roadmaps.py의 resolve_delegate와 같은 규칙).
// social의 `Listening`이 language/english/listening으로 새던 것을 막는다
function pick(cands, selfPath) {
  const dom = selfPath.split('/')[0] + '/';
  return cands.find((c) => c.startsWith(dom) && c !== selfPath)
    || cands.find((c) => c !== selfPath)   // 자기 자신은 링크하지 않음
    || null;
}

export function makeResolver(map, selfPath) {
  return function resolve(text) {
    if (!text || !LINKABLE.test(text.trim())) return null;
    const n = normName(text);
    if (!n) return null;
    const cands = map.get(n)
      || (ALIAS[n] && map.get(ALIAS[n]))
      || (n.endsWith('s') && map.get(n.slice(0, -1)))
      || null;
    return cands ? pick(cands, selfPath) : null;
  };
}

// 이 로드맵이 `이 로드맵 밖`에 실제로 적어둔 대상들. 경로가 적힌 줄은 그대로,
// 이름만 적힌 줄(220곳)은 이름 색인으로 풀어서 넣는다. 한 줄에 여럿이 묶인 라벨도 쪼갠다
export function outsideTargets(roadmap, resolve) {
  const out = new Set();
  for (const o of (roadmap && roadmap.outside) || []) {
    const ref = (o.ref || '').replace(/\/$/, '');
    if (ref) { out.add(ref); continue; }
    for (const piece of splitLabel(o.label || '')) {
      const to = resolve(piece);
      if (to) out.add(to);
    }
  }
  return out;
}

// 이름이 같아도 **다른 물건**인 자리. 아래 규칙을 통과하는데도 뜻이 다른 것들이라 손으로 끊는다.
// 키는 `<로드맵 경로>\0<정규화한 항목 이름>`. 2026-09-01에 후보 230건을 전수로 판정해 얻은 목록
const NOT_A_LINK = new Set([
  // C의 Unity는 임베디드용 테스트 프레임워크다 — 옆에 CMocka·Check가 나란히 있다
  'software/skill-based/Languages/c\u0000unity',
  // ReAct(Reason + Act)는 추론-행동 반복 패턴이지 React 프레임워크가 아니다
  'software/skill-based/AI/ai-agents\u0000react',
  // pytorch의 Backend는 NCCL·Gloo 통신 방식 설정이지 백엔드 개발자 로드맵이 아니다
  'software/skill-based/AI/pytorch\u0000backend',
  // mongodb의 JavaScript는 BSON 데이터 타입이다 — 이웃이 Symbol·Date·Int64
  'software/skill-based/Data-DB/mongodb\u0000javascript',
]);

// 반대로 **분야를 넘지만 진짜 그 로드맵**인 자리. 같은 전수 판정에서 나왔다 —
// 아래 규칙이 같은 분야만 인정하는데, 이것들은 그 벽을 넘어야 맞다
const ALSO_LINK = new Set([
  'software/role-based/ux-design\u0000behavioraleconomics',
  'software/role-based/machine-learning\u0000discretemathematics',
  'social/role-based/public-figure\u0000positioning',
  'software/role-based/bi-analyst\u0000operations',
  'software/role-based/devrel\u0000editing',
  'academics/psychology/cognitive\u0000deliberatepractice',
  'software/role-based/engineering-manager\u0000people',
  'academics/economics/behavioral-economics\u0000cognitiveload',
  'academics/psychology/cognitive\u0000cognitiveload',
  'software/role-based/bi-analyst\u0000networking',
  'software/role-based/devrel\u0000networking',
]);

// 항목 이름이 대상 로드맵을 그대로 부르는가 — 제목·파일명·별칭·복수형까지 본다.
// `MS SQL`↔`Microsoft SQL Server`(파일명 ms-sql) · `Git`↔`Git and GitHub`(ALIAS) ·
// `Code Reviews`↔`code-review`(복수형)가 여기서 붙는다
function namesTarget(text, to, titleOf) {
  const n = normName(text);
  const keys = new Set([normName(titleOf(to) || ''), normName(to.split('/').pop())]);
  for (const k of [n, ALIAS[n], n.endsWith('s') ? n.slice(0, -1) : '']) {
    if (k && keys.has(k)) return true;
  }
  return false;
}

// **항목 카드 전용 해석기 — 이름이 같다는 것만으로는 안 건다.** 근거가 있어야 한다 (2026-09-01):
//   ① 그 파일이 `이 로드맵 밖`에 그 대상을 적어뒀다
//   ② **같은 분야**이면서 항목 이름이 대상 로드맵을 그대로 부른다(`namesTarget`)
//   ③ 위 두 목록에 손으로 적어둔 예외
//
// 전에는 이름만 맞으면 걸었고, 같은 이름을 다른 뜻으로 쓰는 항목이 수두룩했다 —
// `Unity`는 이 저장소에 셋이고(C 테스트 프레임워크 · 치알디니 7번째 원칙 · 게임엔진),
// 앞의 둘이 게임엔진으로 끌려갔다. `Composition`(React children ↔ 그림 구도) ·
// `Character`(Rust 문자 타입 ↔ 등장인물) · `Traces`(분산추적 ↔ 사람 흔적 읽기) ·
// `Networking`(소켓 ↔ 인맥) 등 230건 중 184건이 근거 없는 링크였다.
//
// 후보 230건은 2026-09-01에 **전수 판정**했다(SAME 195 · DIFF 35). 규칙 ①②가 184건을 맞게 걸고
// 오탐 4 · 누락 11이 남아 그 15건을 위 두 목록에 적었다. 새 로드맵이 생겨 또 충돌하면 한 줄 추가.
//
// `이 로드맵 밖`·`참조` 줄 자체는 이 제한을 안 받는다 — 거기 적혀 있다는 게 이미 근거다.
export function makeItemResolver(resolve, allowed, selfPath, titleOf) {
  const dom = selfPath.split('/')[0] + '/';
  return (text) => {
    const to = resolve(text);
    if (!to) return null;
    const key = `${selfPath}\u0000${normName(text)}`;
    if (NOT_A_LINK.has(key)) return null;
    if (ALSO_LINK.has(key) || allowed.has(to)) return to;
    return to.startsWith(dom) && namesTarget(text, to, titleOf) ? to : null;
  };
}

// "GitHub, GitLab, BitBucket" 처럼 한 라벨에 여러 개가 묶인 경우가 있어 쉼표로 쪼갠다
export const splitLabel = (label) =>
  String(label).split(',').map((s) => s.trim()).filter(Boolean);
