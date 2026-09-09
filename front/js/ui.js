// 공용 렌더 헬퍼 — 전부 html 문자열 반환. 텍스트는 반드시 esc()를 거친다.

export const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

// 0~100 값. null → '—'. 소수는 의미 있는 자리까지만.
export function fmtPct(v) {
  if (v === null || v === undefined) return '—';
  if (v === 0) return '0%';
  const r = Math.round(v * 100) / 100;
  return `${r}%`;
}

// 진행 바 — 층 하나, 숙련도%만. 2026-09-01에 이중 바(학습/실증)를 접었다:
// 퍼센트가 하나뿐이라 겹칠 층이 없다. 칸별 수준은 카드 lv 색이 대신 보여준다
export function bar(percent) {
  if (percent === null || percent === undefined) {
    return '<div class="bar bar-empty"><span>측정 데이터 없음</span></div>';
  }
  // 0이 아닌 극소값은 최소 0.5%로 보여 바가 살아있음을 표시
  const v = Math.max(0, Math.min(100, percent || 0));
  return `<div class="bar"><div class="bar-done" style="width:${v > 0 ? Math.max(v, 0.5) : 0}%"></div></div>`;
}

// 수준 표시는 마커가 아니라 카드 색칠이다 — **숙련도 기여분(0~1)만큼** 가로로 채운다
// (--fill은 CSS ::before가 읽는다). 2026-09-01에 lv/4 등간격에서 가중치로 바꿨다 —
// 색 길이와 숙련도% 수치가 같은 값을 보게 하려는 것. 눈금 원본은 build_stats.py의 WEIGHTS.
// doing은 수준과 직교라 오른쪽 배지로 따로 알린다
export const weightFill = (w) => (w > 0 ? ` style="--fill:${round2(w * 100)}%"` : '');

const round2 = (v) => Math.round(v * 100) / 100;

// 카드에 적는 기여분 표시 — 색 길이를 숫자로 한 번 더 말해준다
export const weightPct = (w) =>
  (w > 0 ? `<span class="item-pct">${round2(w * 100)}%</span>` : '');

export const doingBadge = (doing) => (doing ? '<span class="doing-badge">진행중</span>' : '');

// 택 1 그룹에서 고른 "내 주력" 표식 — 진행도와 직교(pick 레코드, 화면 전용)
export const pickBadge = (pick) => (pick ? '<span class="pick-badge">주력</span>' : '');

// 카드 배경을 숙련도만큼 왼쪽부터 채운다. 0%면 칠하지 않는다.
export function fillStyle(percent) {
  const d = Math.max(0, Math.min(100, percent || 0));
  return d ? ` style="--done:${d}%"` : '';
}

// 5축 오각형 레이더. axes = [{label, percent}] — percent는 숙련도(0~100 또는 null)
export function radar(axes, size = 300) {
  const cx = size / 2, cy = size / 2 + 6, r = size * 0.33;
  const n = axes.length;
  const pt = (i, ratio) => {
    const a = -Math.PI / 2 + (i * 2 * Math.PI) / n;
    return [cx + Math.cos(a) * r * ratio, cy + Math.sin(a) * r * ratio];
  };
  const poly = (ratios) => ratios.map((v, i) => pt(i, v).join(',')).join(' ');

  const rings = [0.25, 0.5, 0.75, 1].map((g) =>
    `<polygon class="radar-ring" points="${poly(axes.map(() => g))}"/>`).join('');
  const spokes = axes.map((_, i) =>
    `<line class="radar-spoke" x1="${cx}" y1="${cy}" x2="${pt(i, 1)[0]}" y2="${pt(i, 1)[1]}"/>`).join('');

  // 값이 0이어도 형태가 보이도록 최소 반경을 준다 (표시용, 수치는 라벨에 그대로)
  const ratio = (v) => 0.04 + (Math.max(0, v || 0) / 100) * 0.96;
  const donePoly = poly(axes.map((a) => ratio(a.percent)));

  const labels = axes.map((a, i) => {
    const [x, y] = pt(i, 1.22);
    const anchor = Math.abs(x - cx) < 4 ? 'middle' : x > cx ? 'start' : 'end';
    return `<text class="radar-label" x="${x}" y="${y}" text-anchor="${anchor}">${esc(a.label)}</text>
            <text class="radar-value" x="${x}" y="${y + 13}" text-anchor="${anchor}">${fmtPct(a.percent)}</text>`;
  }).join('');

  return `<svg class="radar" viewBox="0 0 ${size} ${size + 10}" width="${size}" height="${size + 10}">
    ${rings}${spokes}
    <polygon class="radar-done" points="${donePoly}"/>
    ${labels}
  </svg>`;
}

// 제목 끝 "AI 생성" 접미사는 AI 배지와 중복이라 표시에서만 제거
export const cleanTitle = (t) => String(t).replace(/\s*AI 생성$/, '');

export const loading = '<p class="hint">불러오는 중…</p>';

export const errorBox = (msg) => `<p class="error">${esc(msg)}</p>`;
