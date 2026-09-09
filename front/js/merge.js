// 로드맵 json + log jsonl 병합과 진행률 계산 — 순수 함수만 (DOM 무관).
//
// 레코드 2필드 (2026-08-29 전환, docs/progress-format.md):
//   lv: 도달 수준 1 이름만 / 2 개념 / 3 이론 / 4 구현(실증). 0 = 기록 없음
//   doing: 진행중 플래그 — 수준과 직교(lv:3+doing = "이론 끝, 구현 진행중")
// 퍼센트는 **숙련도 하나**다 — lv별 가중치(WEIGHTS)의 합/분모. lv:1·2도 그만큼 든다.
// 실증%·학습%는 2026-09-01 폐기(칸의 수준은 카드 lv 색으로 이미 보인다, stat-model 규칙 7).
// 키는 (sec, sub, 항목 이름) 3종. sec은 로그 쪽 형식 "N. 제목"으로 합성해 매칭한다.

export const LV_NONE = 0;

// 숙련도 가중치 — **원본은 tools/build_stats.py의 WEIGHTS**다. stats.json의 `weights`로
// 실려 오는 걸 setWeights로 받아 쓴다. 여기 기본값을 박아두면 파이썬 수치와 화면 색이
// 조용히 갈라지므로 박지 않는다. 못 받았을 때만 옛 눈금(lv/4)으로 물러선다.
let WEIGHTS = null;
export const setWeights = (w) => { WEIGHTS = w || null; };

// lv → 0~1 기여분. 카드 색칠 폭이자 숙련도%의 분자 한 칸.
export const lvWeight = (lv) => {
  if (!lv) return 0;
  return WEIGHTS ? (WEIGHTS[lv] || 0) : lv / 4;
};

// 항목 문법은 `English Name / 한국어 설명`. 설명은 언제든 다듬으므로 키에서 뺀다
// (전 로드맵 23985개가 이름만으로 충돌 0 — tools/build_stats.py item_name과 같은 규칙)
export const itemName = (t) => String(t).split(' / ')[0];

// 화면 표시용 분리 — 꼬리에 한글이 있을 때만 설명으로 본다.
// 안 그러면 `vim / nvim`·`Mobile Apps / Android, iOS`가 잘못 쪼개진다
const HANGUL = /[가-힣]/;
export function splitItem(t) {
  const text = String(t);
  const i = text.indexOf(' / ');
  if (i < 0) return { name: text, desc: '' };
  const desc = text.slice(i + 3);
  return HANGUL.test(desc) ? { name: text.slice(0, i), desc } : { name: text, desc: '' };
}

export const logKey = (sec, sub, item) => [sec, sub || '', itemName(item)].join('\u0000');

export const secLabel = (sec) => `${sec.no}. ${sec.title}`;

// jsonl 텍스트 → { recs: 진행 레코드 Map, picks: 선택 레코드 Map } (키별 시점이 가장 늦은 것).
// recs 규칙은 build_stats.py의 read_log와 같아야 한다 — 한쪽만 고치면 화면과 수치가 어긋난다.
// picks(`pick` 필드)는 택 1 그룹의 "내 주력" 표식 — 수치 집계와 무관, 화면 전용(2026-08-30).
export function parseLog(text) {
  const log = { recs: new Map(), picks: new Map() };
  if (!text) return log;
  for (const raw of text.split('\n')) {
    const line = raw.trim();
    if (!line) continue;
    let o;
    try { o = JSON.parse(line); } catch { continue; }
    applyRecord(log, o);
  }
  return log;
}

// 레코드 한 줄을 파싱 결과에 얹는다. 방금 저장한 줄을 화면에 반영할 때도 이걸 쓴다
// (front/js/detail.js) — 다시 읽었을 때와 같은 그림이 나와야 하므로 승자 규칙은 하나다.
// 늦은 `at`이 이긴다. 같은 날이면 나중에 얹은 것(파일 순서로는 나중 줄)이 이긴다 —
// 옛 날짜를 백필로 덧붙여도 최신 판정을 덮어쓰지 않게 하려는 것(2026-08-29).
export function applyRecord(log, o) {
  if (!o || o.sec === undefined || o.item === undefined) return;
  const k = logKey(o.sec, o.sub, o.item);
  const put = (map) => {
    const prev = map.get(k);
    if (!prev || (o.at || '') >= (prev.at || '')) map.set(k, o);
  };
  if (o.lv !== undefined || o.doing !== undefined) put(log.recs);
  if (o.pick !== undefined) put(log.picks);
}

// 위임 항목(`delegate` 보유)은 다른 로드맵으로 뺀 **필수 부품**이다. 선택 사항이 아니라
// 중요해서 파일까지 뺀 것이므로 **분모 1칸**으로 센다(2026-08-27).
// 항목 줄의 `별도` 태그는 뜻이 다르다(별도 제품·요금제·라이선스) — 그건 자기 항목이다.
export const isDelegated = (item) => 'delegate' in item;

// 위임 칸의 상태는 대상 로드맵 진행률에서 파생한다. 규칙은 여기서 다시 계산하지 않고
// tools/build_stats.py가 낸 stats.json의 roadmaps[대상].delegate_state를 그대로 읽는다 —
// 두 군데서 계산하면 파이썬 분모와 화면 분모가 조용히 어긋난다(CLAUDE.md 연동 규칙).
// 파생 상태(1 완료/2 이론완료/3 부분 진행)를 lv 눈금으로 환산해 자기 항목과 같은 스킨을 입힌다.
// 진행중(doing)은 상태와 별개로 **대상에 doing 레코드가 있을 때만** 얹는다(2026-08-29 분리)
// — 환산표는 build_stats.py tally()의 rec()과 같아야 한다.
// 숙련도는 lv 환산을 거치지 않고 **대상의 `delegate_mastery`를 그대로** 쓴다 —
// 상태 3(부분 진행)이 lv 없음이라 0으로 떨어지던 자리를 대상의 실제 깊이로 채운다.
// 대상의 `percent`(자기 위임 칸까지 포함한 2패스 값)가 아니라 자기 항목만 센 값이다 —
// build_stats.py tally()가 쓰는 `dmast`와 같은 수여야 화면과 수치가 안 갈라진다.
export const delegateLookup = (stats) => {
  const out = new Map();
  const cast = { 1: 4, 2: 3, 3: 0 };
  for (const [path, v] of Object.entries((stats && stats.roadmaps) || {})) {
    if (v.delegate_state) {
      out.set(path, { lv: cast[v.delegate_state], doing: !!v.delegate_doing,
                      mastery: (v.delegate_mastery || 0) / 100 });
    }
  }
  return out;
};

// roadmap 객체의 각 item에 lv·doing을 심고(choice 그룹엔 groupLv·groupDoing),
// 분모 규칙(일반 항목 + 택1 그룹당 1)대로 집계를 돌려준다.
// 섹션마다 같은 규칙으로 sec.stat도 심는다 — 어느 파트를 하다 말았는지 보여야
// 골라 들어갈 수 있다(커서를 없앤 뒤로 화면이 위치를 대신한다, 2026-08-27).
export function annotate(roadmap, log, deleg = new Map()) {
  const map = log.recs || log;          // parseLog 결과 또는 순수 Map(테스트용)
  const picks = log.picks || new Map();
  let total = 0;
  const count = { 4: 0, 3: 0, 2: 0, 1: 0 };
  let doingN = 0;
  let weight = 0;   // 숙련도%의 분자 — lv:1·2도 가중치만큼 든다
  let cur = null; // 지금 세고 있는 섹션의 누적기

  const tally = (lv, doing, touched, wt) => {
    total += 1;
    if (lv) count[lv] += 1;
    if (doing) doingN += 1;
    weight += wt;
    if (!cur) return;
    cur.total += 1;
    if (lv === 4) cur.done += 1;
    else if (lv === 3) cur.theory += 1;
    if (doing) cur.doing += 1;
    if (touched) cur.touched += 1;
    cur.weight += wt;
  };

  for (const part of roadmap.parts || []) {
    for (const sec of part.sections || []) {
      const label = secLabel(sec);
      cur = { total: 0, done: 0, theory: 0, doing: 0, touched: 0, weight: 0 };
      sec.stat = cur;
      const sectionGroup = []; // sec.choice: 직속+모든 sub 항목이 한 그룹
      const mark = (item, sub) => {
        const rec = isDelegated(item)
          ? deleg.get(item.delegate) || null
          : map.get(logKey(label, sub, item.t)) || null;
        item.lv = (rec && rec.lv) || LV_NONE;
        item.doing = !!(rec && rec.doing);
        // 카드 색칠 폭 = 숙련도 기여분. 위임 칸은 lv이 아니라 대상의 숙련도를 그대로 받는다
        item.weight = isDelegated(item)
          ? ((rec && rec.mastery) || 0)
          : lvWeight(item.lv);
        // 부분 진행 위임 칸은 lv:0·doing:false여도 기록 있음 — 미기록과 갈라야 한다
        item.touched = !!rec;
        item.log = isDelegated(item) ? null : rec;
        // 선택(pick)은 위임 여부와 무관하게 키로 찾는다 — 위임 칸 로그 금지의 유일한 예외
        item.pickRec = picks.get(logKey(label, sub, item.t)) || null;
        item.pick = false;   // 그룹 단위 승자 선정 후 켠다
        return item;
      };
      // 택 1 그룹에서 pick:true 중 가장 늦은 하나만 유효 — 다른 옵션을 고르면 자연 교체
      const crownPick = (members) => {
        let best = null;
        for (const m of members) {
          if (m.pickRec && m.pickRec.pick === true &&
              (!best || (m.pickRec.at || '') >= (best.pickRec.at || ''))) best = m;
        }
        if (best) best.pick = true;
      };
      // 그룹 = 분모 1. 가장 높은 lv 하나로 대표, doing·touched는 독립 전파.
      // 가중합도 대표 하나만 — 분모가 1칸이니 분자도 1칸분(build_stats.py tally와 같은 규칙)
      const groupTally = (members) =>
        tally(Math.max(0, ...members.map((m) => m.lv)),
              members.some((m) => m.doing), members.some((m) => m.touched),
              Math.max(0, ...members.map((m) => m.weight)));

      for (const item of sec.items || []) {
        const it = mark(item, undefined);
        if (sec.choice) sectionGroup.push(it);
        else tally(it.lv, it.doing, it.touched, it.weight);
      }
      for (const sub of sec.subs || []) {
        const subGroup = [];
        for (const item of sub.items || []) {
          const it = mark(item, sub.title);
          if (sec.choice) sectionGroup.push(it);
          else if (sub.choice) subGroup.push(it);
          else tally(it.lv, it.doing, it.touched, it.weight);
        }
        if (!sec.choice && sub.choice) {
          sub.groupLv = Math.max(0, ...subGroup.map((m) => m.lv));
          sub.groupDoing = subGroup.some((m) => m.doing);
          groupTally(subGroup);
          crownPick(subGroup);
        }
      }
      if (sec.choice) {
        sec.groupLv = Math.max(0, ...sectionGroup.map((m) => m.lv));
        sec.groupDoing = sectionGroup.some((m) => m.doing);
        groupTally(sectionGroup);
        crownPick(sectionGroup);
      }
      cur = null;
    }
  }

  const pct = (n) => (total ? (n / total) * 100 : null);
  return {
    total,
    done: count[4],
    theory: count[3],
    named: count[1] + count[2],             // lv:1·2 — %엔 안 들지만 미기록과는 다르다
    doing: doingN,
    percent: pct(weight),                   // 숙련도% — 화면에 나가는 유일한 퍼센트
  };
}
