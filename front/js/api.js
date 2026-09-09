// 데이터 fetch + 캐시. 전부 저장소 루트 기준 절대경로로 요청한다.

// 라벨은 로드맵 제목·폴더명과 같은 언어(영어)로 통일한다.
export const DOMAINS = [
  { id: 'software',  label: 'Software' },
  { id: 'social',    label: 'Social' },
  { id: 'creative',  label: 'Creative' },
  { id: 'academics', label: 'Academics' },
  { id: 'business',  label: 'Business' },
  { id: 'finance',   label: 'Finance' },
  { id: 'health',    label: 'Health' },
  { id: 'language',  label: 'Language' },
  { id: 'meta',      label: 'Meta' },
];

export const domainLabel = (id) => (DOMAINS.find((d) => d.id === id) || { label: id }).label;

const cache = new Map();

async function cached(url, parse) {
  if (cache.has(url)) return cache.get(url);
  const p = fetch(url).then((r) => (r.ok ? parse(r) : null)).catch(() => null);
  cache.set(url, p);
  return p;
}

// 404·파싱 실패는 null — 호출측이 빈 상태로 처리한다.
export const fetchJson = (url) => cached(url, (r) => r.json());
export const fetchText = (url) => cached(url, (r) => r.text());

export const getStats = () => fetchJson('/data/stats.json');
export const getInventory = () => fetchJson('/data/inventory.json');
export const getCertIndex = () => fetchJson('/certifications/index.json');
export const getCertDomain = (domain) => fetchJson(`/certifications/${domain}.json`);
export const getDomainIndex = (domain) => fetchJson(`/roadmaps/${domain}/index.json`);
export const getProgress = (domain) => fetchJson(`/data/progress/${domain}-progress.json`);
export const getRoadmap = (domain, path) => fetchJson(`/roadmaps/${domain}/${path}.json`);
export const getLog = (domain, path) => fetchText(`/data/log/${domain}/${path}.jsonl`);
export const getWorks = () => fetchJson('/api/works');

// 기록 쓰기 — 서버가 jsonl append + build_stats 재생성까지 마친다.
// 성공하면 파생물 캐시(log·stats·progress)를 지워 다음 렌더가 새로 읽게 한다.
export async function postLog(domain, path, records) {
  const r = await fetch('/api/log', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ path: `${domain}/${path}`, records }),
  });
  const body = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(body.error || `HTTP ${r.status}`);
  cache.delete(`/data/log/${domain}/${path}.jsonl`);
  cache.delete('/data/stats.json');
  cache.delete(`/data/progress/${domain}-progress.json`);
  return body;
}
