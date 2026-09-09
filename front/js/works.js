import { getWorks } from './api.js';
import { esc, loading } from './ui.js';

export async function renderWorks(view) {
  view.innerHTML = loading;
  const works = await getWorks();

  if (works === null) {
    view.innerHTML = `<div class="works"><h1>작업물</h1>
      <p class="error">/api/works 응답이 없습니다 — python tools/serve.py로 실행해야 목록이 보입니다.</p></div>`;
    return;
  }
  if (works.length === 0) {
    view.innerHTML = `<div class="works"><h1>작업물</h1>
      <p class="hint">works/ 아래 로드맵 경로 폴더에 파일을 넣으면 여기에 표시됩니다.</p></div>`;
    return;
  }

  // 분야(경로 첫 마디)별 그룹핑
  const groups = new Map();
  for (const w of works) {
    const domain = w.path.split('/')[0];
    if (!groups.has(domain)) groups.set(domain, []);
    groups.get(domain).push(w);
  }

  const fmtSize = (n) => (n >= 1048576 ? `${(n / 1048576).toFixed(1)}MB`
    : n >= 1024 ? `${(n / 1024).toFixed(1)}KB` : `${n}B`);
  const fmtDate = (t) => new Date(t * 1000).toISOString().slice(0, 10);

  const sections = [...groups].map(([domain, files]) => `
    <details class="works-domain" open>
      <summary>${esc(domain)} <span class="nums">${files.length}</span></summary>
      <ul class="works-list">
        ${files.map((w) => `
          <li>
            <a href="/works/${encodeURI(w.path)}" target="_blank">${esc(w.path)}</a>
            <span class="nums">${fmtSize(w.size)} · ${fmtDate(w.mtime)}</span>
          </li>`).join('')}
      </ul>
    </details>`).join('');

  view.innerHTML = `<div class="works"><h1>작업물 <span class="nums">${works.length}개</span></h1>${sections}</div>`;
}
