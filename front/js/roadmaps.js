import { DOMAINS, domainLabel, getDomainIndex, getProgress, getStats } from './api.js';
import { renderDetail } from './detail.js';
import { esc, fmtPct, fillStyle, loading, errorBox, cleanTitle } from './ui.js';

// 진행중 판정: progress에 doing이 있거나 손댄 섹션(secs)이 있으면 시작한 것
export function inProgress(progress, path) {
  const p = progress && progress[path];
  if (!p) return false;
  return (p.doing && p.doing.length > 0) || (p.secs && Object.keys(p.secs).length > 0);
}

const withSide = (domain, treeInner, inner) => `
  <div class="rm-layout">
    <aside class="rm-side">${sideDomains(domain, treeInner)}</aside>
    <section class="rm-main" id="rm-main">${inner}</section>
  </div>`;

export async function renderRoadmaps(view, domain, rest) {
  if (!domain) {
    view.innerHTML = withSide(null, '', '<p class="hint">좌측에서 분야를 선택하세요.</p>');
    return;
  }
  view.innerHTML = withSide(domain, '', loading);

  const [index, progress, stats] = await Promise.all([
    getDomainIndex(domain), getProgress(domain), getStats()]);
  if (!index) {
    view.querySelector('#rm-main').innerHTML =
      errorBox(`roadmaps/${domain}/index.json을 불러오지 못했습니다.`);
    return;
  }
  const rmStats = (stats && stats.roadmaps) || {};
  const entry = index.find((e) => e.path === rest);

  if (entry) {
    // 상세는 전폭 — 항목 카드가 좁아지지 않도록 사이드바를 두지 않는다
    view.innerHTML = '<section class="rm-full" id="rm-main"></section>';
    await renderDetail(view.querySelector('#rm-main'), domain, rest, entry, progress);
  } else {
    view.innerHTML = withSide(domain, treeHtml(domain, index, rest),
      folderView(domain, index, progress, rest, rmStats));
  }
}

function sideDomains(active, treeInner = '') {
  return DOMAINS.map((d) => `
    <div class="side-domain ${d.id === active ? 'active' : ''}">
      <a class="side-domain-link" href="#/roadmaps/${d.id}">${esc(d.label)}</a>
      ${d.id === active ? treeInner : ''}
    </div>`).join('');
}

// index.json 경로에서 폴더 트리 파생 — 분야별 특례 없음
function buildTree(index) {
  const root = { children: new Map(), count: index.length };
  for (const e of index) {
    const dirs = e.path.split('/').slice(0, -1);
    let node = root;
    for (const d of dirs) {
      if (!node.children.has(d)) node.children.set(d, { children: new Map(), count: 0 });
      node = node.children.get(d);
      node.count += 1;
    }
  }
  return root;
}

function treeHtml(domain, index, rest) {
  const render = (node, prefix) => {
    const parts = [];
    for (const [name, child] of [...node.children].sort((a, b) => a[0].localeCompare(b[0]))) {
      const path = prefix ? `${prefix}/${name}` : name;
      const open = rest === path || rest.startsWith(path + '/');
      parts.push(`
        <details class="tree-folder" ${open ? 'open' : ''}>
          <summary class="${rest === path ? 'current' : ''}">
            <a href="#/roadmaps/${domain}/${esc(path)}">${esc(name)}</a>
            <span class="nums">${child.count}</span>
          </summary>
          ${render(child, path)}
        </details>`);
    }
    return parts.join('');
  };
  return `<div class="tree">${render(buildTree(index), '')}</div>`;
}

// 현재 폴더(rest) 아래 전체 로드맵을 하위 폴더별 그룹으로 나열
function folderView(domain, index, progress, rest, rmStats) {
  const under = rest
    ? index.filter((e) => e.path.startsWith(rest + '/'))
    : index;
  if (rest && under.length === 0) {
    return errorBox(`'${rest}' 아래에 로드맵이 없습니다.`);
  }

  const groups = new Map();
  for (const e of under) {
    const dir = e.path.split('/').slice(0, -1).join('/');
    if (!groups.has(dir)) groups.set(dir, []);
    groups.get(dir).push(e);
  }

  const sections = [...groups]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([dir, entries]) => `
      <h2 class="group-title">${esc(dir || domainLabel(domain))}</h2>
      <div class="cards">${entries.map((e) => card(domain, progress, e, rmStats)).join('')}</div>`)
    .join('');

  // 이 폴더 전체 숙련도 — 가중합은 stats.json에 안 실리므로 percent×total로 되살려 합친다
  const at = (e, k) => (rmStats[`${domain}/${e.path}`] || {})[k] || 0;
  const tot = under.reduce((a, e) => a + at(e, 'total'), 0);
  const done = under.reduce((a, e) => a + at(e, 'done'), 0);
  const w = under.reduce((a, e) => a + (at(e, 'percent') * at(e, 'total')) / 100, 0);

  return `
    <div class="folder-head">
      <h1>${esc(domainLabel(domain))}${rest ? ` / ${esc(rest)}` : ''}</h1>
      <span class="nums">로드맵 ${under.length}개 · 구현 ${done} / 전체 ${tot}항목</span>
      <span class="folder-pct">${fmtPct(tot ? (w * 100) / tot : null)}</span>
    </div>
    ${sections}`;
}

function card(domain, progress, e, rmStats) {
  const doing = inProgress(progress, e.path);
  const st = rmStats[`${domain}/${e.path}`];
  const pct = st ? st.percent : null;
  return `
    <a class="card ${doing ? 'doing' : ''}"
       href="#/roadmaps/${domain}/${esc(e.path)}"${fillStyle(pct)}>
      <span class="card-title">${esc(cleanTitle(e.title))}</span>
      <span class="card-side">
        <span class="card-pct ${pct ? 'has' : ''}">${st ? fmtPct(pct) : ''}</span>
        <span class="card-meta">${st ? `${st.done}/${st.total}` : `섹션 ${e.sections}`}</span>
      </span>
      <span class="card-badges">
        ${e.ai ? '<span class="badge ai">AI</span>' : ''}
        ${doing ? '<span class="badge doing">진행중</span>' : ''}
      </span>
    </a>`;
}
