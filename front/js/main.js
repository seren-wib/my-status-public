import { renderProfile } from './profile.js';
import { renderRoadmaps } from './roadmaps.js';
import { renderWorks } from './works.js';

const view = document.getElementById('view');

function route() {
  const hash = location.hash.slice(1) || '/profile';
  const parts = hash.split('/').filter(Boolean).map(decodeURIComponent);
  const tab = parts[0] || 'profile';

  document.querySelectorAll('.topbar nav a').forEach((a) =>
    a.classList.toggle('active', a.dataset.tab === tab));

  if (tab === 'roadmaps') {
    renderRoadmaps(view, parts[1] || null, parts.slice(2).join('/'));
  } else if (tab === 'works') {
    renderWorks(view);
  } else {
    renderProfile(view, parts[1] || 'stats');
  }
}

addEventListener('hashchange', route);
route();
