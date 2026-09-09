# my-status (공개용 사본)

> 이 저장소는 비공개로 운영 중인 원본의 **공개용 사본**입니다.
> 개인 학습 기록·진행도·개인 정보는 전부 걷어냈고, 구조와 도구만 남겼습니다.

## 뭐 하는 프로젝트인가

RPG 게임의 **캐릭터 상태창**을 나 자신에게 붙이는 프로젝트입니다.
지식·기술·체력 같은 능력치가 있고, 그 능력치는 로드맵을 하나씩 배우면서 오릅니다.

- 9개 분야(software·social·creative·academics·business·finance·health·language·meta)에
  로드맵 md 파일이 격자로 깔려 있습니다. 한 줄이 학습 항목 하나입니다.
- 항목을 배우면 `data/log/<로드맵>.jsonl`에 한 줄을 남깁니다.
  수준은 4단계 — 1 이름만 안다 · 2 개념 · 3 이론 · 4 구현해서 실증.
- `tools/build_stats.py`가 로그를 읽어 진행도(`data/progress/`)와 스탯(`data/stats.json`)을 **다시 생성**합니다.
  손으로 고치는 파일은 로그뿐입니다.
- `front/`는 그 결과를 상태창처럼 보여주는 바닐라 정적 페이지입니다.
  `run.bat`(윈도우) / `run.command`(맥)을 실행하면 로컬 서버가 뜹니다. 화면에서 카드를 눌러 기록을 남길 수도 있습니다.

## 들어 있는 것
- `roadmaps/` — 로드맵 261개. 전부 AI로 작성한 것이고 파일 첫 줄에 `` `AI 생성` `` 태그가 있습니다
- `certifications/` · `milestones/` — 자격증 목록과 성취(로드맵과 달리 분모에 안 들어감)
- `tools/` — md → json 파서, 스탯 빌더, 정합성 검사기. 표준 라이브러리만 씁니다
- `front/` — 정적 프론트 + `tools/serve.py` 로컬 서버
- `docs/` — 폴더 구조, 스탯 모델, 기록 형식, 자격증 양식

## 들어 있지 않은 것
- **roadmap.sh 원본에서 온 로드맵 87개.**
  [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)의 라이선스가
  저장소 밖 재배포를 금지하므로 제외했습니다. 이 프로젝트의 격자 구조 자체는 roadmap.sh에서 영감을 받았습니다.
- 학습 기록 — `data/log/*.jsonl`은 전부 빈 틀 `{}`이고, 진행도는 전 분야 0%입니다
- 개인 정보, 그리고 원본을 만들면서 남긴 작업 일지

docs에 적힌 로드맵 수·항목 수가 실제와 다른 것은 위 제외 때문입니다.
