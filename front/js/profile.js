import { getStats, getInventory, getCertIndex, getCertDomain, getDomainIndex,
         DOMAINS, domainLabel } from './api.js';
import { esc, fmtPct, bar, radar, cleanTitle, loading, errorBox } from './ui.js';

const TABS = [
  { id: 'stats', label: '스탯' },
  { id: 'skills', label: '기술 습득치' },
  { id: 'inventory', label: '인벤토리' },
];

export async function renderProfile(view, tab = 'stats') {
  if (!TABS.some((t) => t.id === tab)) tab = 'stats';
  view.innerHTML = `
    <div class="subtabs">
      ${TABS.map((t) => `<a class="${t.id === tab ? 'active' : ''}" href="#/profile/${t.id}">${t.label}</a>`).join('')}
    </div>
    <div id="profile-body">${loading}</div>`;
  const body = view.querySelector('#profile-body');

  if (tab === 'stats') return statsView(body);
  if (tab === 'skills') return skillsView(body);
  return inventoryView(body);
}

/* ── 스탯: 오각형 레이더 + 축 게이지 드릴다운 ───────────── */
async function statsView(body) {
  const stats = await getStats();
  if (!stats) {
    body.innerHTML = errorBox('data/stats.json을 불러오지 못했습니다. python tools/serve.py로 실행했는지 확인하세요.');
    return;
  }
  const gauges = stats.axes.filter((a) => a.kind === 'gauge');
  body.innerHTML = `
    <div class="stats-layout">
      <section class="panel radar-panel">
        ${radar(gauges.map((a) => ({ label: a.label, percent: a.percent })), 330)}
        <p class="radar-legend">
          <span class="key key-done"></span> 숙련도 (수준별 가중)
        </p>
      </section>
      <section class="panel">
        ${gauges.map(axisCard).join('')}
      </section>
    </div>`;
}

function axisCard(axis) {
  const noData = axis.percent === null || axis.total === 0;
  return `
  <details class="axis">
    <summary>
      <span class="axis-name">${esc(axis.label)}</span>
      <span class="axis-id">${esc(axis.id)}</span>
      <span class="axis-measures">${esc(axis.measures)}</span>
      <span class="axis-nums">${noData ? '' :
        `숙련 ${fmtPct(axis.percent)} · 구현 ${axis.done} / 이론 ${axis.theory} / 전체 ${axis.total}`}</span>
      ${bar(axis.percent)}
    </summary>
    <div class="skills">
      ${(axis.skills || []).map(skillRow).join('') || '<p class="hint">스킬 없음</p>'}
    </div>
  </details>`;
}

function skillRow(skill) {
  const noData = skill.percent === null || skill.total === 0;
  // 행 전체가 클릭 대상 — 경로만 파랗게 칠하면 목록이 링크 벽이 된다
  const roadmaps = (skill.roadmaps || []).map((r) => `
    <li><a class="row-link" href="#/roadmaps/${esc(r.path)}">
        <span class="row-name">${esc(r.path)}</span>
        <span class="nums">${r.done}/${r.theory}/${r.total}${r.doing ? ` · 진행중 ${r.doing}` : ''}</span>
      </a></li>`).join('');
  return `
  <details class="skill">
    <summary>
      <span class="skill-name">${esc(skill.label)}</span>
      <span class="axis-id">${esc(skill.id)}</span>
      <span class="axis-nums">${noData ? '측정 데이터 없음' :
        `숙련 ${fmtPct(skill.percent)} · 구현 ${skill.done} / 이론 ${skill.theory} / 전체 ${skill.total}`}</span>
      ${bar(skill.percent)}
    </summary>
    ${roadmaps ? `<ul class="skill-roadmaps">${roadmaps}</ul>` : '<p class="hint">연결된 로드맵 없음</p>'}
  </details>`;
}

/* ── 기술 습득치: 로드맵 348개 습득률 ──────────────────── */
async function skillsView(body) {
  const [stats, ...indexes] = await Promise.all([getStats(), ...DOMAINS.map((d) => getDomainIndex(d.id))]);
  if (!stats || !stats.roadmaps) {
    body.innerHTML = errorBox('stats.json에 roadmaps 인덱스가 없습니다. python tools/build_stats.py를 재실행하세요.');
    return;
  }
  // 경로 대신 로드맵 제목으로 보여주기 위한 맵
  const titles = new Map();
  indexes.forEach((idx, i) => (idx || []).forEach((e) =>
    titles.set(`${DOMAINS[i].id}/${e.path}`, cleanTitle(e.title))));
  const rows = Object.entries(stats.roadmaps).map(([path, r]) => ({ path, ...r }));
  const sum = (k) => rows.reduce((a, b) => a + b[k], 0);
  // weight(가중합)은 stats.json에 안 실린다 — percent×total로 되살려 합친다
  const grand = { total: sum('total'), done: sum('done'), theory: sum('theory'),
                  weight: rows.reduce((a, b) => a + ((b.percent || 0) * b.total) / 100, 0) };

  const groups = new Map(DOMAINS.map((d) => [d.id, []]));
  for (const r of rows) {
    const dom = r.path.split('/')[0];
    if (groups.has(dom)) groups.get(dom).push(r);
  }

  const sections = [...groups].map(([dom, list]) => {
    const t = list.reduce((a, b) => a + b.total, 0);
    const d = list.reduce((a, b) => a + b.done, 0);
    const th = list.reduce((a, b) => a + b.theory, 0);
    // 분야 숙련도 = Σ가중합 / Σ분모. 가중합은 stats.json에 안 실리므로 percent×total로 되살린다
    const w = list.reduce((a, b) => a + ((b.percent || 0) * b.total) / 100, 0);
    // 습득한 것이 위로 오도록 정렬
    list.sort((a, b) => (b.percent || 0) - (a.percent || 0) || a.path.localeCompare(b.path));
    return `
      <details class="tech-domain" ${d || th ? 'open' : ''}>
        <summary>
          <span class="tech-domain-name">${esc(domainLabel(dom))}</span>
          <span class="nums">로드맵 ${list.length}개 · 구현 ${d} / 이론 ${th} / 전체 ${t}</span>
          <span class="tech-pct">${fmtPct(t ? (w * 100) / t : null)}</span>
          ${bar(t ? (w * 100) / t : 0)}
        </summary>
        <ul class="tech-list">
          ${list.map((r) => `
            <li class="tech-row">
              <a class="row-link tech-row-link" href="#/roadmaps/${esc(r.path)}">
                <span class="row-name">${esc(titles.get(r.path) || r.path)}</span>
                <span class="nums">${esc(r.path.split('/').slice(1, -1).join('/'))} · 구현 ${r.done}/${r.total}</span>
                <span class="tech-pct">${fmtPct(r.percent)}</span>
                ${bar(r.percent)}
              </a>
            </li>`).join('')}
        </ul>
      </details>`;
  }).join('');

  body.innerHTML = `
    <section class="panel">
      <div class="tech-grand">
        <h2>전체 습득치</h2>
        <span class="tech-grand-pct">${fmtPct((grand.weight * 100) / grand.total)}</span>
        <span class="nums">구현 ${grand.done} / 이론 ${grand.theory} / 전체 ${grand.total}항목 · 로드맵 ${rows.length}개</span>
        ${bar((grand.weight * 100) / grand.total)}
      </div>
      ${sections}
    </section>`;
}

/* ── 인벤토리: 재정·자격증·학위·경력·작업물 ─────────────── */
async function inventoryView(body) {
  const [inv, certIdx] = await Promise.all([getInventory(), getCertIndex()]);
  if (!inv) {
    body.innerHTML = errorBox('data/inventory.json을 불러오지 못했습니다.');
    return;
  }
  const certDomains = (certIdx || []).map((c) => c.domain);
  const certFiles = await Promise.all(certDomains.map(getCertDomain));
  const ownedIds = new Set((inv.certifications || []).map((c) => c.id));

  const fin = inv.finance || {};
  const finRow = (label, m) => `
    <div class="inv-metric">
      <span class="inv-metric-label">${label}</span>
      <span class="inv-metric-value">${m && m.value !== null && m.value !== undefined
        ? `${esc(m.value)} ${esc(m.unit || '')}` : '—'}</span>
    </div>`;

  const list = (arr, fmt, empty) =>
    arr && arr.length ? `<ul>${arr.map(fmt).join('')}</ul>` : `<p class="hint">${empty}</p>`;

  const totalCerts = (certIdx || []).reduce((a, c) => a + c.count, 0);

  body.innerHTML = `
    <div class="inv-layout">
      <section class="panel">
        <div class="inv-group">
          <h2>재정</h2>
          ${finRow('순자산', fin.net_worth)}
          ${finRow('저축률', fin.savings_rate)}
          ${finRow('버틸 개월', fin.runway_months)}
        </div>
        <div class="inv-group">
          <h2>학위</h2>
          ${list(inv.degrees, (d) => `<li>${esc(d.school)} ${esc(d.major)} <span class="nums">${esc(d.level)} · ${esc(d.at)}</span></li>`, '비어 있음')}
        </div>
        <div class="inv-group">
          <h2>경력</h2>
          ${list(inv.career, (c) => `<li>${esc(c.org)} ${esc(c.title)} <span class="nums">${esc(c.from)}~${esc(c.to || '')}</span></li>`, '비어 있음')}
        </div>
        <div class="inv-group">
          <h2>작업물</h2>
          ${list(inv.works, (w) => `<li>${esc(w.name)} <span class="nums">${esc(w.at)}</span></li>`, '비어 있음 — 작업물 탭에서 실물 확인')}
        </div>
      </section>
      <section class="panel">
        <h2 class="cert-head">자격증 <span class="nums">보유 ${ownedIds.size} · 딸 수 있는 것 ${totalCerts}개</span></h2>
        ${certFiles.map((f, i) => certDomainBlock(certDomains[i], f, ownedIds)).join('')}
      </section>
    </div>`;
}

function certDomainBlock(domain, file, ownedIds) {
  if (!file) return `<p class="hint">${esc(domain)} 자격증 목록을 불러오지 못했습니다.</p>`;
  const cats = (file.categories || []).map((cat) => `
    <h3 class="cert-cat">${esc(cat.title)}</h3>
    <div class="cert-cards">
      ${cat.certs.map((c) => certCard(c, ownedIds)).join('')}
    </div>`).join('');
  return `
    <details class="cert-domain">
      <summary>
        <span class="cert-domain-name">${esc(domainLabel(domain))}</span>
        <span class="nums">${file.count}개</span>
      </summary>
      ${cats}
    </details>`;
}

function certCard(c, ownedIds) {
  const owned = ownedIds.has(c.id); // 이름이 아니라 id로 대조
  const links = (c.roadmaps || []).map((p) =>
    `<a class="cert-link" href="#/roadmaps/${esc(p)}">${esc(p.split('/').slice(1).join('/') || p)}</a>`).join('');
  return `
    <div class="cert-card ${owned ? 'owned' : ''}">
      <div class="cert-name">${esc(c.name)} ${owned ? '<span class="badge owned">보유</span>' : ''}</div>
      <div class="cert-meta">${esc(c.issuer || '')}${c.region ? ` · ${esc(c.region)}` : ''}</div>
      ${c.exam ? `<div class="cert-line"><b>시험</b> ${esc(c.exam)}</div>` : ''}
      ${c.eligibility ? `<div class="cert-line"><b>응시</b> ${esc(c.eligibility)}</div>` : ''}
      ${c.renewal ? `<div class="cert-line"><b>갱신</b> ${esc(c.renewal)}</div>` : ''}
      ${c.note ? `<div class="cert-note">${esc(c.note)}</div>` : ''}
      ${links ? `<div class="cert-links">${links}</div>` : ''}
    </div>`;
}
