import { DOMAINS, getRoadmap, getLog, getStats, getProgress, postLog } from './api.js';
import { parseLog, applyRecord, annotate, isDelegated, splitItem, delegateLookup, secLabel,
         setWeights, itemName } from './merge.js';
import { esc, fmtPct, bar, weightFill, weightPct, doingBadge, pickBadge, loading, errorBox,
         cleanTitle } from './ui.js';
import { loadLinkIndex, makeResolver, makeItemResolver, outsideTargets, roadmapTitle,
         splitLabel } from './links.js';

// 이름 → 로드맵 경로 해석기. 렌더 트리 전체가 쓰므로 모듈 스코프에 둔다.
// 둘로 나뉜다 — `resolve`는 `이 로드맵 밖`·`참조` 줄용(거기 적혔다는 게 근거),
// `resolveItem`은 항목 카드용으로 **그 파일이 적어둔 대상만** 인정한다(links.js, 동명이인 방지)
let resolve = () => null;
let resolveItem = () => null;
// 위임 카드가 대상의 규모·진행률을 적으려고 쓰는 평면 인덱스 (stats.json의 roadmaps)
let roadmapStats = new Map();
// 지금 열려 있는 로드맵의 파싱 상태. 저장 뒤 다시 받지 않고 이걸 고쳐서 그 자리만 갱신한다
let current = null;

export async function renderDetail(container, domain, path, entry, progress) {
  container.innerHTML = loading;
  // stats는 위임 칸의 상태(대상 로드맵 진행률에서 파생)를 읽으려고 같이 받는다
  const [roadmap, logText, linkIndex, stats] = await Promise.all([
    getRoadmap(domain, path), getLog(domain, path), loadLinkIndex(), getStats()]);
  if (!roadmap) {
    container.innerHTML = errorBox(`roadmaps/${domain}/${path}.json을 불러오지 못했습니다.`);
    return;
  }
  resolve = makeResolver(linkIndex, `${domain}/${path}`);
  resolveItem = makeItemResolver(resolve, outsideTargets(roadmap, resolve),
                                 `${domain}/${path}`, roadmapTitle);
  roadmapStats = new Map(Object.entries((stats && stats.roadmaps) || {}));
  // 숙련도 눈금은 파이썬이 원본 — 받은 걸 심어야 카드 색과 stats.json 수치가 같아진다
  setWeights(stats && stats.weights);

  const log = parseLog(logText);
  const deleg = delegateLookup(stats);
  const stat = annotate(roadmap, log, deleg);
  current = { domain, path, roadmap, log, deleg };
  const bookmark = progress && progress[path];

  container.innerHTML = `
    <article class="detail">
      <header class="detail-head">
        <p class="breadcrumb"><a href="#/roadmaps/${domain}">${esc(domain)}</a> / ${esc(path)}</p>
        <h1>${esc(cleanTitle(roadmap.title))} ${roadmap.ai ? '<span class="badge ai">AI</span>' : ''}</h1>
        <div class="detail-progress">${progressHtml(stat)}</div>
        <div class="resume-box">${resumeLine(bookmark)}</div>
      </header>
      ${roadmap.parts.map(partHtml).join('')}
      ${outsideHtml(roadmap.outside, delegatedPaths(roadmap))}
    </article>`;
  wireEditors(container, domain, path, entry);
}

// 맨 위 진행 바 + 숫자 줄. 저장 뒤 이 조각만 다시 그리므로 함수로 뺐다
function progressHtml(stat) {
  return `${bar(stat.percent)}
    <span class="axis-nums">숙련 ${fmtPct(stat.percent)}
      · 구현 ${stat.done} / 이론 ${stat.theory}${stat.named ? ` / 맛봄 ${stat.named}` : ''} / 진행중 ${stat.doing} / 전체 ${stat.total}</span>`;
}

// 화면엔 **진행중 줄만** 낸다. progress의 섹션 요약(`secs`, 완료/이론완료/전체)은
// 다음 세션에 Claude가 어디를 이어갈지 고르는 용도라 사용자가 볼 물건이 아니다
// (2026-09-01). 파일 형식은 그대로다 — 안 그리기만 한다(docs/progress-format.md)
function resumeLine(bookmark) {
  if (!bookmark) return '';
  return (bookmark.doing || [])
    .map((d) => `<p class="resume doing-line">진행중: ${place(d)}</p>`).join('');
}

const place = (b) =>
  `${esc(b.sec)}${b.sub ? ` · ${esc(b.sub)}` : ''} — ${esc(b.item)} (${esc(b.at || '')})`;

function partHtml(part) {
  const head = part.no !== null && part.title !== null
    ? `<h2 class="part-title">PART ${part.no} · ${esc(part.title)}</h2>`
    : ''; // PART 없는 파일 21개
  return `${head}${part.sections.map(sectionHtml).join('')}`;
}

function sectionHtml(sec) {
  const label = `${sec.no}. ${sec.title}`;
  const body = `
    ${itemsHtml(sec.items, label, '')}
    ${(sec.subs || []).map((sub) => subHtml(sub, label)).join('')}`;
  const refs = refsHtml(sec.refs);
  const head = `<h3 class="sec-title">
    <span class="sec-name">${sec.no}. ${esc(sec.title)}</span>${secCount(sec.stat)}
  </h3>`;
  const inner = sec.choice ? choiceBox(sec.groupLv, sec.groupDoing, body) : body;
  return `<section class="sec" id="${esc(sec.anchor)}">
    ${head}${inner}${refs}
  </section>`;
}

// 섹션 진행률 — 분모는 annotate가 센 것(택 1 그룹은 1칸, 위임도 1칸)을 그대로 쓴다.
// 손댄 섹션만 눈에 띄게 하고, 0인 섹션은 회색 숫자로 남긴다
function secCount(st) {
  if (!st || !st.total) return '';
  const touched = st.touched;
  const extra = st.doing ? `진행중 ${st.doing}` : '';
  return `<span class="sec-count${touched ? ' has' : ''}">
    <b>${fmtPct((st.weight / st.total) * 100)}</b>
    <span class="sec-extra">${st.total}항목${extra ? ` · ${extra}` : ''}</span>
  </span>`;
}

function subHtml(sub, secLab) {
  const body = itemsHtml(sub.items, secLab, sub.title);
  const refs = refsHtml(sub.refs);
  const inner = sub.choice ? choiceBox(sub.groupLv, sub.groupDoing, body) : body;
  return `<div class="sub">
    <h4 class="sub-title">${esc(sub.title)}</h4>
    ${inner}${refs}
  </div>`;
}

const choiceBox = (lv, doing, inner) => `
  <div class="choice-box lv${lv || 0}${doing ? ' doing' : ''}">
    <span class="choice-label">택 1${doingBadge(doing)}</span>
    ${inner}
  </div>`;

function itemsHtml(items, secLab, subTitle) {
  if (!items || !items.length) return '';
  return `<div class="items">${items.map((it) => itemHtml(it, secLab, subTitle)).join('')}</div>`;
}

// 항목 하나 = 한 줄을 통째로 쓰는 카드. 윗줄에 이름, 아랫줄에 한국어 설명.
// 상태는 카드 색으로 드러내고, 미완 항목엔 마커를 붙이지 않는다
// (체크박스 나열이 눈을 피로하게 만들던 것을 없앤 것).
// data-* 는 카드 클릭 에디터가 로그 키(sec, sub, 이름)를 만들 때 쓴다 — 위임 카드엔 없다
function itemHtml(item, secLab, subTitle) {
  if (isDelegated(item)) return delegateHtml(item, secLab, subTitle);
  const tags = (item.tags || [])
    .map((t) => `<span class="tag t-${t === '추천' ? 'rec' : 'opt'}">${esc(t)}</span>`)
    .join('');
  const lv = item.lv || 0;
  const ev = item.log && item.log.ev ? ` title="${esc(item.log.ev)}"` : '';
  // 이름 부분으로만 링크를 판정한다 — 설명이 붙은 항목도 이름이 로드맵이면 이어져야 한다
  const { name, desc } = splitItem(item.t);
  const to = item.ref || resolveItem(name);
  const nameHtml = to
    ? `<a class="item-name item-link" href="#/roadmaps/${esc(to)}">${esc(name)}<span class="go">↗</span></a>`
    : `<span class="item-name">${esc(name)}</span>`;
  return `<div class="item lv${lv}${item.doing ? ' doing' : ''}${item.pick ? ' picked' : ''}"${weightFill(item.weight)}${ev}
      data-sec="${esc(secLab)}"${subTitle ? ` data-sub="${esc(subTitle)}"` : ''}
      data-item="${esc(itemName(item.t))}" data-lv="${lv}"${item.doing ? ' data-doing="1"' : ''}${item.pick ? ' data-pick="1"' : ''}>
    <div class="item-head">
      ${nameHtml}
      ${tags}
      ${pickBadge(item.pick)}
      ${doingBadge(item.doing)}
      ${weightPct(item.weight)}
    </div>
    ${desc ? `<p class="item-desc">${esc(desc)}</p>` : ''}
  </div>`;
}

// 위임 카드 — 다른 로드맵으로 뺀 **필수 부품** 한 칸. 분모 1칸이고 상태는 대상에서 파생하므로
// 색·마커는 자기 항목과 같이 가고, 대상의 규모와 진행률을 같이 적어 들어갈지 판단하게 한다.
// 채움은 **대상 로드맵의 숙련도** 그대로다(merge.js가 심어 준 item.weight) — 2026-09-01에
// 자체 환산표(완주 100 / 이론 75 / 학습%×0.75)를 버렸다. 눈금이 두 벌이면 같은 칸이
// 화면과 stats.json에서 다르게 보인다. "가득 = 전부 실증"은 그대로 성립한다
function delegateHtml(item, secLab, subTitle) {
  const lv = item.lv || 0;
  const to = item.delegate;
  const info = to ? roadmapStats.get(to) : null;
  // 택 1 전환 위임(2026-08-30)은 설명·추천 태그를 지니고 온다 — 자기 항목과 같은 표시
  const { name: plain, desc } = splitItem(item.t);
  const name = to
    ? `<a class="item-name item-link" href="#/roadmaps/${esc(to)}">${esc(plain)}<span class="go">↗</span></a>`
    : `<span class="item-name">${esc(plain)}</span>`;
  const tags = (item.tags || [])
    .map((t) => `<span class="tag t-${t === '추천' ? 'rec' : 'opt'}">${esc(t)}</span>`)
    .join('');
  const meta = [
    desc ? esc(desc) : (to ? esc(to) : '대상 미해결'),
    info ? `전체 ${info.total}항목` : '',
    info ? `숙련 ${fmtPct(info.percent)}` : '',
  ].filter(Boolean).join(' · ');
  return `<div class="item delegated lv${lv}${item.doing ? ' doing' : ''}${item.pick ? ' picked' : ''}"${
      weightFill(item.weight)}
      data-sec="${esc(secLab)}"${subTitle ? ` data-sub="${esc(subTitle)}"` : ''}
      data-item="${esc(plain)}" data-delegate="1"${item.pick ? ' data-pick="1"' : ''}>
    <div class="item-head">
      ${name}
      ${tags}
      <span class="tag t-ref">위임</span>
      ${pickBadge(item.pick)}
      ${doingBadge(item.doing)}
      ${weightPct(item.weight)}
    </div>
    <p class="item-desc deleg-meta">${meta}</p>
  </div>`;
}

// 본문 위임 카드로 이미 나간 대상들 — 바닥의 "이 로드맵 밖"에서 같은 줄을 또 보여주지 않는다
function delegatedPaths(roadmap) {
  const set = new Set();
  const eat = (items) => (items || []).forEach((it) => {
    if (isDelegated(it) && it.delegate) set.add(it.delegate);
  });
  for (const part of roadmap.parts || []) {
    for (const sec of part.sections || []) {
      eat(sec.items);
      (sec.subs || []).forEach((sub) => eat(sub.items));
    }
  }
  return set;
}

function refsHtml(refs) {
  if (!refs || !refs.length) return '';
  const li = refs.map((r) =>
    `<li>${refLink(r.ref, r.label)}${r.tag ? ` <span class="tag t-ref">${esc(r.tag)}</span>` : ''}</li>`).join('');
  return `<ul class="refs">${li}</ul>`;
}

function outsideHtml(outside, taken = new Set()) {
  if (!outside || !outside.length) return '';
  // 본문에 위임 카드로 나간 것은 뺀다. 경로가 안 적힌 줄은 이름으로 해석해 대조한다
  const rest = outside.filter((o) => {
    const ref = (o.ref || '').replace(/\/$/, '') || resolve(o.label);
    return !(ref && taken.has(ref));
  });
  if (!rest.length) return '';
  const li = rest.map((o) =>
    `<li>${refLink(o.ref, o.label)}${o.tag ? ` <span class="tag t-ref">${esc(o.tag)}</span>` : ''}</li>`).join('');
  return `<section class="sec outside">
    <h3 class="sec-title">이 로드맵 밖</h3>
    <ul class="refs">${li}</ul>
  </section>`;
}

// ── 카드 클릭 기록 에디터 ──────────────────────────────────────────────
// 카드를 클릭하면 아래에 lv 버튼 4개 + 진행중 체크 + ev 입력이 열린다.
// 저장 → POST /api/log → 서버가 append + build_stats 재생성 → 여기서 refetch·재렌더.
// 위임 카드는 data-item이 없어 안 열린다(위임 칸엔 로그 금지 — stat-model 규칙 8).

const LV_LABELS = { 1: '이름만', 2: '개념', 3: '이론', 4: '구현' };

function editorHtml(card) {
  const cur = +card.dataset.lv || 0;
  const inChoice = !!card.closest('.choice-box');
  const isDeleg = !!card.dataset.delegate;
  // 택 1 멤버에만 "주력" 토글 — 진행도와 무관한 선택 표식(pick 레코드)
  const pickBtn = inChoice
    ? `<button type="button" class="ed-pick">${card.dataset.pick ? '주력 해제' : '주력 지정'}</button>`
    : '';
  // 위임 카드엔 진행도 입력이 없다(위임 칸 로그 금지) — 택 1 안이면 주력 토글만
  if (isDeleg) {
    return `<div class="log-editor">
      <div class="ed-row">
        <span class="ed-note">진행도는 대상 로드맵에서 파생 — 여기선 기록 안 함</span>
        ${pickBtn}
        <button type="button" class="ed-cancel">취소</button>
      </div>
      <span class="ed-msg"></span>
    </div>`;
  }
  const btns = [1, 2, 3, 4].map((n) =>
    `<button type="button" data-lv="${n}" class="${n === cur ? 'on' : ''}">${n} ${LV_LABELS[n]}</button>`).join('');
  return `<div class="log-editor">
    <div class="ed-row">
      ${btns}
      <label class="ed-doing-label"><input type="checkbox" class="ed-doing"
        ${card.dataset.doing ? 'checked' : ''}> 진행중</label>
      ${pickBtn}
    </div>
    <div class="ed-row">
      <input class="ed-ev" placeholder="근거(ev) — 구현(4)은 필수">
      <button type="button" class="ed-save">저장</button>
      <button type="button" class="ed-cancel">취소</button>
    </div>
    <span class="ed-msg"></span>
  </div>`;
}

function wireEditors(container, domain, path, entry) {
  // 재렌더마다 innerHTML이 갈리므로 addEventListener 대신 onclick 할당(중복 방지)
  container.onclick = (e) => {
    if (e.target.closest('a, button, input, .log-editor')) return;
    const card = e.target.closest('.item[data-item]');
    if (!card) return;
    // 택 1 밖 위임 카드는 기록할 게 없다 — 진행도는 파생, 주력 선택도 그룹에서만 의미
    if (card.dataset.delegate && !card.closest('.choice-box')) return;
    const wasOpen = !!card.querySelector('.log-editor');
    container.querySelectorAll('.log-editor').forEach((el) => el.remove());
    if (wasOpen) return;   // 열린 카드를 다시 클릭 = 닫기
    card.insertAdjacentHTML('beforeend', editorHtml(card));
    card.querySelector('.log-editor').addEventListener('click', (ev) => {
      const b = ev.target.closest('button');
      if (b) onEditorButton(b, card, container, domain, path, entry);
    });
  };
}

// 저장 성공 → 페이지를 다시 받지 않고 바뀐 자리만 갈아끼운다.
// 예전엔 renderDetail을 다시 불렀는데, 그 첫 줄이 화면을 통째로 비워서
// 깜빡임·스크롤 튐·stats.json(180KB) 재요청이 매 저장마다 따라왔다.
// 서버가 응답에 실어 준 레코드(= 파일에 실제로 들어간 줄)를 그대로 얹는다 —
// `at`을 프론트가 따로 만들면 서버가 찍은 날짜와 어긋난다.
// 다시 그리는 건 그 섹션 하나뿐이라 sectionHtml을 그대로 재사용한다(표시 규칙은 한 군데).
function applySaved(container, card, records) {
  const secEl = card.closest('section.sec');
  if (!current || !secEl || !records || !records.length) return false;
  const sec = findSection(current.roadmap, card.dataset.sec);
  if (!sec) return false;

  records.forEach((r) => applyRecord(current.log, r));
  const stat = annotate(current.roadmap, current.log, current.deleg);
  const bar = container.querySelector('.detail-progress');
  if (bar) bar.innerHTML = progressHtml(stat);
  secEl.outerHTML = sectionHtml(sec);   // 높이가 그대로라 스크롤이 안 튄다
  return true;
}

const findSection = (roadmap, label) => (roadmap.parts || [])
  .flatMap((part) => part.sections || [])
  .find((sec) => secLabel(sec) === label) || null;

// 헤더의 "진행중/섹션 요약"은 data/progress에서 온다 — 서버가 방금 다시 만들었으니
// 새로 받아 얹는다. 카드 갱신을 막지 않도록 기다리지 않는다(2~3KB짜리 파일).
function refreshResume(container, domain, path) {
  const box = container.querySelector('.resume-box');
  if (!box) return;
  getProgress(domain).then((prog) => {
    if (box.isConnected) box.innerHTML = resumeLine(prog && prog[path]);
  });
}

async function onEditorButton(b, card, container, domain, path, entry) {
  const ed = card.querySelector('.log-editor');
  if (b.dataset.lv) {   // 수준 버튼 — 다시 누르면 해제(doing만 기록하는 경우)
    const was = b.classList.contains('on');
    ed.querySelectorAll('[data-lv]').forEach((x) => x.classList.remove('on'));
    if (!was) b.classList.add('on');
    return;
  }
  if (b.classList.contains('ed-cancel')) { ed.remove(); return; }
  if (b.classList.contains('ed-pick')) {   // 주력 토글 — 즉시 기록
    b.disabled = true;
    const rec = { sec: card.dataset.sec, item: card.dataset.item, pick: !card.dataset.pick };
    if (card.dataset.sub) rec.sub = card.dataset.sub;
    try {
      const res = await postLog(domain, path, [rec]);
      await settle(res, container, card, domain, path, entry);
    } catch (err) {
      ed.querySelector('.ed-msg').textContent = `실패: ${err.message}`;
      b.disabled = false;
    }
    return;
  }
  if (!b.classList.contains('ed-save')) return;

  const on = ed.querySelector('[data-lv].on');
  const lv = on ? +on.dataset.lv : null;
  const doing = ed.querySelector('.ed-doing').checked;
  const evTxt = ed.querySelector('.ed-ev').value.trim();
  const msg = ed.querySelector('.ed-msg');
  if (!lv && !doing) { msg.textContent = '수준을 고르거나 진행중을 켜야 저장됨'; return; }
  if (lv === 4 && !evTxt) { msg.textContent = '구현(4)은 근거(ev)가 필요함 — 뭘 만들었는지 한 줄'; return; }

  b.disabled = true;
  msg.textContent = '저장 중…';
  const rec = { sec: card.dataset.sec, item: card.dataset.item };
  if (card.dataset.sub) rec.sub = card.dataset.sub;
  if (lv) rec.lv = lv;
  if (doing) rec.doing = true;
  if (evTxt) rec.ev = evTxt;
  try {
    const res = await postLog(domain, path, [rec]);
    await settle(res, container, card, domain, path, entry);
  } catch (err) {
    msg.textContent = `실패: ${err.message}`;
    b.disabled = false;
  }
}

// 저장 뒤 화면 정리 — 제자리 갱신이 원칙이고, 실패하면(카드·섹션을 못 찾는 경우)
// 예전처럼 전체 재렌더로 물러선다. 어느 쪽이든 화면과 파일은 같은 상태가 된다.
async function settle(res, container, card, domain, path, entry) {
  if (applySaved(container, card, res && res.records)) {
    refreshResume(container, domain, path);
    return;
  }
  const prog = await getProgress(domain);
  await renderDetail(container, domain, path, entry, prog);
}

// 경로가 적혀 있으면 그걸로, 없으면 이름으로 로드맵을 찾아 링크한다.
// 한 라벨에 여럿이 묶인 경우("GitHub, GitLab, BitBucket")는 쪼개서 각각 건다
function refLink(ref, label) {
  if (ref && DOMAINS.some((d) => ref.startsWith(d.id + '/'))) {
    return `<a href="#/roadmaps/${esc(ref)}">${esc(label)}</a>`;
  }
  if (ref) return `${esc(label)} <span class="nums">${esc(ref)}</span>`;

  const parts = splitLabel(label).map((piece) => {
    const to = resolve(piece);
    return to ? `<a href="#/roadmaps/${esc(to)}">${esc(piece)}</a>` : esc(piece);
  });
  return parts.join(', ');
}
