# my-status (public)

RPG 상태창처럼 내 학습을 추적하는 저장소의 **공개용 사본**입니다.
원본은 비공개이며, 이 사본은 개인 기록·개인 정보를 전부 걷어낸 상태입니다.

## 들어 있는 것
- `roadmaps/` — 로드맵 261개 (전부 AI로 작성한 것. 파일 첫 줄에 `` `AI 생성` `` 태그)
- `certifications/` · `milestones/` — 자격증·성취 목록
- `tools/` — md → json 파서, 스탯 빌더, 정합성 검사기 (stdlib만 사용)
- `front/` — 바닐라 정적 프론트. `run.bat`(윈도우) / `run.command`(맥) 실행
- `docs/` — 구조·스탯 모델·기록 형식

## 들어 있지 않은 것
- **roadmap.sh 원본에서 온 로드맵 87개.** [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)의
  라이선스가 저장소 밖으로의 재배포를 금지하므로 제외했습니다. 이 프로젝트의 격자 구조는 roadmap.sh에서 영감을 받았습니다.
- 학습 기록(`data/log/*.jsonl`은 전부 빈 틀 `{}`), 진행도, 개인 정보

로드맵 수·항목 수가 docs에 적힌 숫자와 다른 것은 위 제외 때문입니다.
