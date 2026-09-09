# 프로젝트 구조

> 2026-08-26 갱신 · 아홉 분야 전부 완성(meta 포함) · 수준 축 PART 전면 해체 반영

---

```
my-status/
├── CLAUDE.md                    프로젝트 지침 (AI가 매 세션 읽음)
├── docs/
│   ├── architecture.md          이 문서
│   ├── certification-format.md  자격증 파일 양식·격자 (2026-08-26)
│   ├── AI-GENERATED.md          AI 작성분 전체(`AI 생성` 태그 실측 261파일) — 신규 94 ·
│   │                            social archetype 15 · 원본 증축분 + 만들지 않기로 한 기술 목록
│   ├── stat-model.md            스탯 산출 규칙 (환산·실증·폐기 결정)
│   └── progress-format.md       진행도 기록 형식 (progress·log)
├── roadmaps/                    배우는 것 전부 (체크박스로 쪼개지는 기술)
│   ├── software/                소프트웨어 — 로드맵 181개 · 18623항목
│   │   ├── index.json           전 로드맵 목록 (파서 생성)
│   │   │                        · 각 로드맵은 md + json 병존 (json은 파서 산출물, 손대지 말 것)
│   │   ├── role-based/          직군 로드맵 29개 · 3255항목 (2026-08-26 성취 밴드 250항목 milestones/로 이주)
│   │   └── skill-based/         기술 로드맵 152개 · 15368항목
│   │       ├── AI/ 15           Blockchain/ 5      Build-Tools/ 6
│   │       ├── CS-Theory/ 9     Data-DB/ 21        Design/ 4
│   │       ├── Frameworks/ 33   Game-Dev/ 3        Infra-DevOps/ 27
│   │       └── Languages/ 17    Testing/ 12
│   ├── finance/                 재정 — 평면 4 카테고리 · 로드맵 12개 · 188항목 (2026-08-26, 축적형이라 role 없음)
│   │   ├── investing/ 5         foundations etf stocks trading portfolio
│   │   │                        · 항목은 "내 돈으로 계산·조회"형. 한국 환경(ISA·국내상장 해외ETF) 기준
│   │   ├── accounting/ 2        bookkeeping(사업자 장부) financial-statements(재무제표 읽기)
│   │   ├── tax/ 2               income-tax(연말정산·종소세) business-tax(부가세·원천징수)
│   │   └── personal-finance/ 3  budgeting pension insurance
│   ├── business/                사업 — role/skill 2층 · 로드맵 18개 · 336항목 (2026-08-25, 실행형)
│   │   ├── role-based/          목표 3개 — freelancer(수주가 이어짐) solopreneur(혼자 만들어 팖)
│   │   │                        founder(굴러가는 회사). 병렬 — 선행관계 없음, 겹침은 공유 skill
│   │   └── skill-based/         부품 15개 · 4 카테고리
│   │       ├── Validation/ 3    customer-research market-testing pricing
│   │       ├── Marketing/ 5     positioning copywriting content-marketing paid-acquisition growth-analytics
│   │       ├── Sales/ 3         sales-process client-management partnerships
│   │       └── Operations/ 4    legal operations hiring-team fundraising
│   │                            · hiring-team·fundraising은 founder 전용 부품
│   ├── creative/                창작 — social과 같은 role/skill 2층 · 로드맵 25개 · 474항목 (2026-08-25)
│   │   ├── role-based/          완성물 5개 — illustration comics fiction song video-production
│   │   │                        · 완성물 흐름(기획→제작→공개)만 담고 기법은 skill에 `위임`
│   │   └── skill-based/         부품 20개 · 4 카테고리
│   │       ├── Drawing/ 5       sketching perspective figure light-and-color composition
│   │       ├── Writing/ 6       story-structure character dialogue-scene prose-style revision
│   │       │                    interactive-narrative(분기·게임 시나리오)
│   │       ├── Sound/ 5         music-fundamentals composing arrangement mixing sound-design(효과음)
│   │       └── Video/ 4         shooting editing color-grading motion-graphics
│   ├── social/                  인간 기술 — role/skill 2층 · 로드맵 65개 · 1967항목 (2026-08-26 archetype 재편)
│   │   ├── role-based/          **인물상 15개** — 공정 단계를 밟으면 그 인물상의 정점에 도달
│   │   │                        대중: demagogue(선동가) orator(연설가) cult-leader(컬트 지도자)
│   │   │                        제도: political-operator(정치인) leader(지도자) connector(연결자)
│   │   │                        테이블: negotiator(협상가) mediator(중재자) interrogator(심문관)
│   │   │                        대인: manipulator(조종자) seducer(유혹자) public-figure(명사)
│   │   │                        기만·강압: con-artist(사기꾼) operative(첩보원) coercer(강압자)
│   │   │                        · 각 파일 2행 인용문에 **정점 좌표** 명시(측정용 눈금)
│   │   │                        · PART = **공정 축**(그 인물상이 일하는 순서). 깊이는 각 단계 안의 층
│   │   │                        · **수준은 PART가 아니다** — 구 `PART 6 · 정점`은 2026-08-26 용해됨
│   │   └── skill-based/         부품 50개 · 12 카테고리
│   │       ├── Reading/ 8       observation nonverbal inference lie-detection
│   │       │                    elicitation group-reading traces cold-reading
│   │       ├── Influence/ 4     Manipulation/ 7      GroupInfluence/ 4
│   │       ├── Relating/ 5      Speaking/ 3          Leading/ 3
│   │       └── Presence/ 4      Conflict/ 3   Deception/ 3   Seduction/ 3   Coercion/ 3
│   ├── language/                외국어 — 평면 카테고리 · 로드맵 13개 · 813항목 (2026-08-26)
│   │   │                        · 기능별 파일 × 수준별 PART(영 CEFR A1→C2 · 일 JLPT N5→N1+이후) 격자.
│   │   │                          0부터 현지인 수준까지, 어휘·한자는 급수 덱 단위 항목(개별 나열 금지)
│   │   ├── english/ 6           foundations grammar reading listening speaking writing
│   │   └── japanese/ 7          foundations kanji grammar reading listening speaking writing
│   ├── health/                  건강 — 평면 카테고리 · 로드맵 7개 · 82항목 (2026-08-26, 실행형)
│   │   │                        · 로드맵=지식(UNMAPPED). 몸은 data/log/physique.jsonl 실측 → PHYSIQUE
│   │   ├── fitness/ 4           strength-training cardio-running program-design mobility
│   │   ├── nutrition/ 2         nutrition-basics meal-planning
│   │   └── sleep/ 1             sleep-hygiene
│   ├── meta/                    메타 스킬 — 평면 3 카테고리 · 로드맵 10개 · 194항목 (2026-08-26, 마지막 분야)
│   │   │                        · 항목은 "개념 이름 + 내 데이터 수치"형. 이론 층은 academics/psychology 본체
│   │   ├── learning/ 4          memory-retention deliberate-practice reading-notes metacognition
│   │   │                        · 스탯 무매핑(의도) — 사유는 docs/stat-model.md
│   │   ├── time-management/ 3   planning prioritization focus  → CHARACTER.Temporal
│   │   └── habits/ 3            habit-formation habit-breaking tracking-recovery  → CHARACTER.Volition
│   └── academics/               학문·교양 — 평면 카테고리 · 로드맵 17개 · 1034항목 (2026-08-25)
│       ├── math/ 4              linear-algebra calculus statistics discrete-math
│       ├── psychology/ 4        cognitive social-psychology personality developmental
│       │                        · 이론 층 (실전 기법은 social/ 몫). 복종·세뇌·다크 트라이어드 등
│       │                          비도덕 영역의 학술 연구 포함 (사용자 지정 커버리지)
│       ├── economics/ 3         microeconomics macroeconomics behavioral-economics
│       └── history/ 6           시대별 디렉터리 — ancient(~476) medieval(476~1453)
│                                early-modern(1453~1789) modern(1789~1945) contemporary(1945~)
│                                korea(한국사). 각 폴더 첫 파일은 overview, 주제 파일은 추후 추가
├── certifications/              **딸 수 있는 것** — 자격증 지도. 진행률 없음(INVENTORY 동류)
│   │                            2026-08-26 · 7분야 65개. 국내·해외 구분 없이 실음
│   ├── index.json               분야 목록 (파서 생성)
│   └── <분야>.md / .json        software 27 · finance 12 · language 9 · creative 6 · business 5 ·
│                                health 4 · academics 2. social·meta는 딸 게 없어 파일 없음
│                                · 양식·격자는 docs/certification-format.md, 변환은 tools/parse_certs.py
│                                · 로드맵과 `로드맵` 경로(prefix)로 붙고, 취득 여부는 inventory의 id로 붙음
├── milestones/                  **이루는 것** — 로드맵이 아니라 성취 기록. 진행률·분모 없음
│   └── software.md              2026-08-26 role 22개의 `PART · 정상의 영역` 밴드를 해체해 이주.
│                                파서는 roadmaps/ 만 훑으므로 stats에 안 잡힘.
│                                형식 통합은 검토 후 **안 함**(2026-08-26) — 자격증은 외부 판정(합격증)이라
│                                고정 키가 서고, 마일스톤은 자기 판정 서술문이라 스키마가 안 겹침.
│                                json 변환은 프론트가 마일스톤 화면을 요구할 때
├── data/
│   ├── progress/                섹션 요약 캐시 — <분야>-progress.json, 손댄 로드맵만 등장.
│   │                            build_stats.py가 로그에서 재생성 — 손으로 고치지 말 것 (2026-08-27 커서 제거)
│   ├── log/<분야>/              학습 이력(원천) — 로드맵당 jsonl 1개, 9분야 348개
│   ├── stats.json               축·스킬 % (생성물 — tools/build_stats.py)
│   └── inventory.json           소유 목록 — 재정·증명·작업물·경력 (수기 갱신)
├── works/                       작업물 — roadmaps/ 미러, 로드맵당 폴더 1개 (실습 산출물형 실증)
└── tools/
    ├── parse_roadmaps.py        md → json 변환기 (stdlib). md 수정 시 재실행
    ├── parse_certs.py           자격증 md → json (stdlib). 키 누락·id 중복·죽은 로드맵 경로를 잡아냄
    └── build_stats.py           축·스킬 매핑(AXES) + 로그 → data/stats.json
```

**합계 348 로드맵 · 23711항목 · 진행률 분모 23135슬롯** (2026-08-28 기준 — 파서 출력이 원본,
분야별 수치는 `python tools/parse_roadmaps.py` 재실행으로 확인. 항목/분모 구분은 `CLAUDE.md` "핵심 숫자").

**아홉 분야 전부 내용이 있고 구축 단계는 끝났다** (2026-08-27 위임 정리 캠페인 종료).
세션 운영 규약은 `CLAUDE.md`, 구축 이력은 `docs/build-log.md`.

---

## 구조를 가르는 기준

**체크박스로 배울 수 있으면 기술(`roadmaps/`), 측정하는 거면 능력치.**

화술·설득은 배울 수 있는 항목으로 쪼개지므로 로드맵(`social/`).
매력·관계·체력 수치는 체크박스로 안 쪼개지므로 스탯. RPG로 치면 스탯 STR ↔ 스킬 검술의 관계.
신체도 같은 논리로 갈라짐 — 운동 프로그램 익히기는 `health/`(로드맵), 몸무게·기록은 측정값(PHYSIQUE).
스탯은 로드맵 진행률에서 산출되는 식으로 두 레이어가 연결됨 — 산출 규칙은 `docs/stat-model.md`.

**두 축의 차이 (software·social 공통).**
`role-based/` 는 "무엇이 되고 싶은가" (backend, 조종). 여러 기술을 얕게 훑음.
`skill-based/` 는 "무엇을 익히는가" (redis, dark-patterns). 한 기술을 깊게 팜.
같은 기술이 양쪽에 중복 등장함 — 진행도를 로드맵 파일과 분리해야 하는 직접적인 이유.
social이 2026-08-25에 이 이분법을 채택함(그전엔 로드맵별 theory/practice 폴더).
다른 분야에 강요하지는 않음 — md 양식만 통일하면 파서는 문제없음.

**이름은 영어, 설명은 한국어 (2026-08-26 확정).** 화면에 뜨는 모든 **이름**은 영어로 쓴다 —
로드맵 H1 · PART 제목 · 섹션(`##`) · 서브섹션(`###`) · **항목 이름**. 폴더·카테고리가 전부 영어라
이름만 한국어면 섞여 보인다. 고유명사는 원래 표기대로(`iOS`·`DevSecOps`·`PostgreSQL DBA`).

**항목 문법은 `영어 개념명 / 한국어 설명`.** 설명은 한국어 그대로 두는 게 원칙 —
`Dependence Asymmetry / 누가 더 아쉬운가가 힘의 기울기`. 짧은 개념은 이름만 써도 된다(`Table Design`).
한국어 문장이 본체인 항목은 앞에 영어 이름을 붙이고 문장을 설명으로 남긴다(정보 손실 금지).
백틱 태그(`택 1`·`추천`·`선택`·`위임`·`별도`)는 파서가 읽는 표시자라 **한국어 그대로** 둔다.

## 위임(`위임`) — 깊은 기술은 참조로, 얕은 기술은 항목으로

> 2026-08-27 확정. 판별은 기계적이다 — **대상이 자기 로드맵 파일을 갖고 있으면 깊은 것.**

- **깊은 것**(java·leverage류)은 그 파일로 넘기고, 이 로드맵에는 **참조 한 줄**만 둔다.
  같은 내용을 항목으로 다시 쓰지 않는다
- **얕은 것**(bcrypt류)은 이 로드맵의 항목으로 쓴다
- 문법은 `` - 이름 `위임` `` — 체크박스가 아닌 불릿. 이름으로 대상을 못 찾으면
  경로를 못 박는다: `` - Observation Basics `social/skill-based/Reading/observation.md` `위임` ``
- **위임은 학습 목록 안에 있다.** 216건 전부 `##` 섹션 안이고 부록 위치는 0건 —
  40건은 목록 맨 앞(선수 지식), 나머지는 맨 끝(본체가 저 파일). 파서가 `items` 배열 **제자리에**
  `{"t": 이름, "delegate": 경로}`로 넣으므로 순서가 보존된다
- 대상 해석 순서는 **① 불릿에 적힌 경로 → ② 같은 파일 `이 로드맵 밖`의 경로 파일명 대조 →
  ③ 전역 이름 색인(같은 분야 우선)**. ②가 ③보다 앞서는 이유: `mediator`의 `Listening`이
  전역 색인으로는 `language/english/listening`으로 잘못 갔는데 파일 자신은
  `social/skill-based/Relating/listening.md`라고 적어두었다
- 이름이 `별도`였던 것을 2026-08-27에 `위임`으로 바꿨다. "따로·부가"로 읽혀 **선택 사항처럼 보였는데
  실제 뜻은 정반대**(중요해서 파일까지 뺀 필수 부품)였다
- **위임 칸은 분모 1칸이다** (2026-08-27). 필수 부품이니 진행률에서 빼면 안 된다.
  상태는 대상 로드맵 진행률에서 파생하고 위임 칸엔 로그를 쓰지 않는다 —
  파생 규칙·재귀 금지 사유는 `docs/stat-model.md` 규칙 8

**`별도`는 뜻이 다르다 — 섞지 말 것.** 항목 줄(`- [ ]`)에 붙은 `별도` 13개는
**별도 제품·요금제·라이선스**를 뜻한다(`` Data Plus / 상위 요금제 `별도` `` · `` Console / 제조사 라이선스 `별도` ``).
위임이 아니므로 분모에서 빼지 않는다.

2026-08-26 일괄 전환: 제목 56 · 헤딩 1940 · 항목명 약 1580. **잔여 0**, 항목 수 23985 불변,
유니크 키 23985 충돌 0. **항목 이름은 진행 기록의 키**(`(sec, sub, 항목 이름)`)라 바꿀 때는
기록이 걸린 항목인지 먼저 확인할 것 — 당시엔 `Languages/c`의 6건뿐이었고 전부 영어라 무사했다.

**키에는 이름만 들어간다 — 슬래시 뒤 설명은 마음대로 고쳐도 된다** (2026-08-26 개정).
설명을 다듬는 일이 앞으로 계속 있으므로 키에서 뺐다. 대신 **같은 섹션(+서브섹션) 안에서
이름이 겹치면 두 항목이 한 키로 뭉친다** — 항목을 쓸 때 이름을 구분되게 지을 것.
규칙 원본은 `docs/progress-format.md`, 구현은 `build_stats.py` `item_name` / `merge.js` `itemName`.

**분야별 구조 분기 기준 (2026-08-25 확정).** 목표가 여러 부품을 조합하는 분야는 role/skill 2층
(software·social·creative), 지식·실력 축적 분야는 평평한 카테고리(academics·language·health·meta·finance).
business는 2026-08-25 role/skill 2층으로 확정(실행형 — 사용자가 "언젠가 팔 생각"을 확인, 조합형 분기 적용).
빈 분야의 내부 폴더는 미리 파지 않고 작성 시점에 확정 —
social이 구조를 먼저 확정했다가 갈아엎은 전례가 근거.

**본체 판정 기준 (2026-08-25, business 작성 때 확정).** 한 주제가 여러 분야에 걸치면
**항목의 체크 조건**으로 본체를 가름 — 읽고 설명하면 `academics`, 계산·장부면 `finance`,
팔아보고 만들어봐야면 `business`, 사람이 움직여야면 `social`. 같은 주제(예: 가격)도 층이 다르면
각자 자기 분야에 있는 게 정상이고 중복이 아님. 이 필터로 business엔 이론 항목 반입 금지 —
들어오려 하면 본체 분야로 보내고 참조만 남김.

**creative role 경계 (2026-08-25).** role은 완성물 단위만 — 스타일·용도 갈래(실사/만화체, 곡/효과음,
소설/게임 시나리오)는 role을 나누지 않고 skill층에서 가름. game-assets role은 안 만듦:
완성물은 게임이고 게임의 자리는 `software/skill-based/Game-Dev` — creative에 세우면 같은 목표의 이중 등록.
sound-design·interactive-narrative는 role 참조 없이 skill로만 존재(skill층은 원래 독립).

**천장 설계 — 목적지는 실무 진입이 아니라 그 분야의 탑** (2026-08-26 실측 후 확정).
전 분야 천장을 실측한 결과 최고가 미들 하단(software)·관찰자(social)였음 — 측정 원본은
메모리 `roadmap-ceiling-measurement`. 원인은 형식이 아니라 **지식 유형 결핍**이었음
(`Trade-off` 0회 · `Little's Law` 0 · `Linearizability` 0 · social의 반복·보정 루프 0).

- **형식은 개념 명명을 유지한다.** 개념 명명으로 최상위 표현이 가능하다는 증거가 저장소에 이미 있음
  (`mysql.md` `Durability Settings / innodb_flush_log_at_trx_commit, sync_binlog` ·
  `kafka.md` `Unclean Leader Election`). 성취형("오픈소스 머지")은 검증 불가·중복이라 폐기 방향
- **실행형 문장은 천장을 1회 실행에 고정한다** — 실행형 3분야(creative·health·finance)가
  천장 최하위 3분야와 정확히 일치. 예외는 `japanese/kanji.md`(개념 이름 + 외부 검증 수치 결합)
- **social은 role을 인물상으로 재편해 천장을 세웠다**(2026-08-26). 아래 별도 절 참조
- software·business는 role이 이미 인물상 문법이라 구조 변경 불필요 — **깊이 증축이 남은 과제**

**social role = 인물상(archetype) (2026-08-26 재편).**
재편 전 social만 role 문법이 달랐음 — software는 `backend`·`devops`(직업), business는
`founder`·`freelancer`(인물상)인데 social만 `persuasion`·`manipulation`(능력명).
능력 이름은 정점이 정의되지 않아 항목이 개론에서 멈추는 구조적 원인이었음.

- **role = 한 사람이 될 수 있는 상.** 각 파일은 2행 인용문에 **정점 좌표**를 명시(예: 선동가 = 괴벨스·맥카시,
  협상가 = 크리스 보스·키신저, 조종자 = Hare PCL-R·Stark 강압적 통제).
  **좌표는 측정용 눈금이지 목표가 아님** — PHYSIQUE가 Strength Level 백분위를 눈금으로 쓰는 것과 같은 용법
- **정점에서 역산해 항목을 뽑는다.** 이 방식으로 기존 결핍이 자동 충족됨 —
  집단 규모(cult-leader) · 제도 권력(political-operator) · 다자 중개(mediator) ·
  예측 보정(interrogator의 Brier score·보정 곡선 — 구 `insight.md`가 "탐지 정확도 54%"라 자백하고도
  정확도를 올릴 층이 없던 문제 해소)
- **정점이 없으면 role이 아니라 skill이다.** `relationship`이 이 기준으로 폐기됨 —
  본문이 전부 `Approach 위임`·`Listening 위임`이라 skill층 색인에 불과했고, 고유 내용은
  `Relating/bonding.md`·`networking.md`가 이미 보유. `persuasion`도 전 archetype의 공통 부품이라
  skill층 `Influence/`가 본체
- skill 층 50파일은 불변 — 부품이라 archetype이 바뀌어도 재사용. role→skill 단방향 불변식 유지
- **윤리선**: 체크 조건이 실제 사람을 피해자로 요구하는 항목 금지. 항목은 개념 이해 단위이며
  다크 계열(조종자·사기꾼·강압자 등)은 학술·법의학·범죄학 문헌 층위로 구성하고 법적 경계 항목을 포함

**PART 축 규칙 — 수준은 PART가 아니다 (2026-08-26 확정. 같은 실수를 두 번 했으므로 명문화).**

- **한 파일의 PART 축은 하나뿐이다.** social role은 공정 축(표적→결속→의존→현실 통제→운용),
  business role도 공정 축(검증→첫 매출→팀→자금→스케일). 여기에 수준 축(`정점`·`정상의 영역`)을
  마지막 PART로 덧붙이면 **축이 섞인다** — PART 5까지 밟아온 문법으로 마지막 PART를 읽을 수 없고,
  공정에 N+1단계가 없으므로 그 칸은 무엇을 넣어도 범주 오류가 된다
- **그 결과가 필러다.** 실제로 그 칸이 입문 교과서 목차(orator의 에토스·파토스·로고스),
  옆 분야로의 화제 전환(coercer의 국가 제재론), 전 파일 복제 보일러플레이트(`Mechanism Teaching` 13/15파일)로
  채워졌다. 필러는 게으름이 아니라 **축 오류의 필연**
- **깊이는 별관이 아니라 각 단계의 위층에 둔다.** 정점급 개념은 자기 공정 단계 섹션 끝에 앉힌다
  (`Nash Bargaining`→가치 창출, 인질 협상→고부담, Schelling 억지→위협 설계)
- **수준 축이 정말 필요하면 격자로 분리한다** — `language/`가 선례: 기능은 파일 축, 수준은 PART 축.
  축 하나당 차원 하나
- **성취는 학습 체크리스트에 안 섞는다.** '배우는 것'(지식 명사구·체크박스·진행률)과
  '이루는 것'(성취 서술문)을 같은 섹션에 두면 난이도 절벽이 생기고 그 항목이 안 끝나 섹션이 안 닫힌다.
  성취는 `milestones/`(진행률 없음, INVENTORY 동류). software 밴드 250항목이 이 규칙으로 이주됨.
  단 body 자체가 실행 마일스톤 문법인 분야(business)는 절벽이 없어 공정 단계로 용해함

**참조 불변식 (social에서 확정, 다층 분야 공통).**
`role→skill`만 허용. `role→role` 금지(role이 role을 요구하면 "백엔드 되려면 프론트 먼저"가 됨),
`skill→role` 백링크도 금지(한 skill을 여러 role이 공유하므로 특정 role 지목은 틀린 정보).
`skill→skill`은 허용. 결과적으로 참조 그래프는 단방향 DAG.
role끼리 겹치는 건 참조가 아니라 **공유 skill**로 표현됨.

---

## social 내부 구분 — 설득·조종·선동·리더십

윤리 규정이 아니라 분류 기준. 메커니즘이 달라서 파일을 나눔:

| | 설득 | 조종 | 선동 |
|---|---|---|---|
| 대상 | 개인~소집단 | 개인 | 집단 |
| 판단력 | 통과 | 우회 | 정체성을 침 |
| 의도 공개 시 | 유효 | 붕괴 | 유효 |
| 경로 | 대화·문서 | 관계 | 매체 |

- 고유 영역: `manipulation/` 정보통제·인지부하·관계착취·다크패턴 / `propaganda/` 집단역학·매체전략·군중심리
- 겹치는 기법(프레이밍·사회적 증거 등)은 `persuasion/` 본체, 나머지 둘이 참조 (중복 체크 → 분모 오염 방지)
- `propaganda/` 는 `academics/history/`(1839~1991, 선전선동사 포함)도 참조
- 리더십은 별개 — 일회성 영향력이 아니라 지속 관계 + 책임 (Authority 정의 그대로)
- 위 넷은 전부 **출력**. 입력은 `relationship/`(정서 공명 → Empathy)과 `insight/`(의도 추론 → Insight)로 나뉨.
  같은 "읽기"지만 재료가 다름 — 정서 공명과 의도 추론은 한쪽만 높은 프로필이 실재함

---

## 분야 간 중복

분야가 늘면서 같은 주제가 여러 분야에 걸침. 전부 정상이며, 기존 설계(진행도 분리 + 섹션 앵커 ref)로 해결:

- 회계 — `finance/accounting/` 이 본체, business 로드맵에서는 참조
- 학습·습관·주의 — 이론은 `academics/psychology/cognitive`, **내 데이터로 재는 운용**은 `meta/` (2026-08-26)
- blockchain — `software/` 에 이미 있음, finance(투자) 관점이 생기면 참조
- **수학 — software에 얕게 존재함 (2026-08-22 실측).** `role-based/machine-learning.md` §2에
  선형대수 5·미적분 3·확률 4·통계 4항목, `ai-data-scientist.md` 에 통계 섹션. 이산수학은 체크박스 1개가 전부.
  전용 로드맵이 아니라 남의 파일 섹션에 얹힌 수준 → `academics/math/` 에 제대로 만들고 중복은 설계로 해결.
  npm(전용 파일 없이 nodejs.md 섹션에 존재)과 동일한 케이스

참조(ref) 기준 경로는 `roadmaps/` 기준으로 확정 (2026-08-23, 1151곳 `software/` 프리픽스 일괄 승격).
json 내 ref는 확장자 없음 — md가 나중에 없어져도 키가 안 낡게.

---

## 죽은 기술 — 무엇을 표시하고 무엇을 안 하나 (2026-08-27)

로드맵은 **"이걸 배우면 지금 쓸 수 있다"를 암묵 전제**한다. 그 전제가 깨진 기술을 중립적으로 적어두면
항목 하나하나가 맞는 설명이어도 **시제가 틀린 것을 배우게 된다.** 게다가 다 체크하면 스탯이 오르므로
저장소가 죽은 기술 학습에 보상까지 준다.

**표시하는 것 — 사실이 바뀐 것.** 파일을 지우지 않고 **첫 섹션에 상태 항목을 넣는다**(분모 +2~3):

| 등급 | 뜻 | 선례 |
|---|---|---|
| Sunset | 유지보수 종료가 **공식 발표**됨 | `adobe-xd`(Maintenance Mode Status·Figma Migration Path) · `web3js`(Sunset Status·Migration Path·Why Still Read It) |
| 전제 변경 | 살아 있지만 배우는 사람이 부딪히는 조건이 바뀜 | `travis-ci`(Migration Trend Toward GitHub Actions·When to still use) · `heroku`(Eco·Basic 요금제 등급) |
| 흡수·개명 | 후속 프로젝트에 합쳐짐 | `remix`(Relationship with React Router 7) |
| 제거된 모드 | 제품은 살아 있고 그 안의 방식이 빠짐 | `kafka`의 `ZooKeeper Mode`(4.0에서 빠진 옛 방식) — **이름은 그대로 두고 설명만 고친다**(로그 키 보존) |

**표시하지 않는 것 — "밀렸다·유행이 지났다".** `sketch`·`mobx`·`redux`·`jenkins`처럼 점유율이 줄었을 뿐
공식적으로 살아 있는 것은 건드리지 않는다. 손대기 시작하면 판정이 취향이 되고 저장소가 **유행 추적기**가 된다.
경계는 **발표된 사실이 있느냐** 하나다.

**항목을 지우지 않는 이유**: 남아 있는 저장소를 읽을 일이 실제로 있고, 이미 배운 사람의 로그 키가 깨진다.
`Why Still Read It` 같은 항목으로 **남은 쓸모의 자리**를 명시하는 쪽이 정확하다.

---

## 만들지 않기로 한 분야 (재조사 방지)

- **요리·생활기술** — 우선순위 낮음
- **법·세무** — 별도 분야로 안 뺌. 세무는 `finance/tax/`, 사업 법무 실무는 `business/skill-based/Operations/legal`(2026-08-25).
  법학 이론·판례 읽기는 영구 배제 — 창업자는 변호사한테 뭘 물을지 알면 됨
- **콘텐츠 사업·유튜브 운영** — 당장 아님. 하게 되면 `business/role-based/` role 후보. 영상 편집 자체는 `creative/skill-based/Video/`

**business에 만들지 않기로 한 것 (2026-08-25, 격자 닫음. 흡수처 명시):**
- 경제·경영 이론 → `academics/economics/` 본체 (business는 실행 항목만)
- 회계·세무·재무제표 → `finance/` 본체, legal·operations에서 참조만
- 대면 설득·협상·네트워킹 → `social/skill-based/` 본체, sales-process가 참조
- 제품 만들기 자체 → `software/`·`creative/` 소관. business는 "뭘 만들지 검증"까지만.
  freelancer의 팔 기술 본체도 본인 분야 로드맵
- 브랜드 디자인 실물 → `creative/`·`software/skill-based/Design/` 참조
- 주식·부동산 투자 → `finance/investing/` — "파는 것"이 아니라 "굴리는 것"

**자격증 파일 격자 (2026-08-26, 작성과 함께 확정. 상세는 `docs/certification-format.md`).**
- **자격증은 로드맵이 아니다.** 진행률이 없고(합격/미합격), 공부 진도는 로드맵이 이미 셈.
  체크박스로 두면 같은 공부가 분모에 두 번 들어감 → `roadmaps/` 밖에 두고 파서·`build_stats.py`가 안 훑음
- **딸 수 있는 것**(`certifications/`)과 **딴 것**(`inventory.json`)은 **`id`로 붙음.** 이름 문자열 대조 금지
- 싣는 기준: 국가기술·국가전문·국가공인 민간자격·공인 어학시험·글로벌 벤더 공식 인증.
  **국내·해외 구분 없음**(2026-08-26 사용자 지시). 비공인 민간자격은 배제 — 공인 여부가 유일한 잣대
- **자격증 하나는 파일 하나에만.** 분야를 걸치면 `로드맵` 경로로 붙음(사회조사분석사 = business 본체,
  로드맵에 academics 2개). 프론트가 경로 역인덱스를 돌리면 양쪽에서 뜸
- 안 싣는 것: 비용(응시료는 매년 바뀜 — 공식 사이트가 원본) · 사양 종목 · 시험이지 자격이 아닌 것(TOPCIT) ·
  학위 자체가 요건의 전부인 것. 단 전공만 맞으면 되는 것(임상심리사·건강운동관리사)은 조건을 적어 실음
- social·meta는 **딸 자격증이 없음** — 빈 파일 안 만듦(재조사 방지)

**meta에 만들지 않기로 한 것 (2026-08-26, 격자 닫음. 마지막 분야라 여기서 전체 격자가 닫힘):**
- 학습·기억·주의·강화의 **이론** → `academics/psychology/cognitive` 본체.
  판별법은 finance/economics와 동일 — 체크 조건에 **"내 덱·내 기록·내 지표"가 붙으면 meta**,
  실험과 이론만 읽으면 academics (`Spacing and Testing Effect`는 이미 cognitive에 있음)
- 동기·성격 이론 → `academics/psychology/personality` · 수면 위생 → `health/sleep` ·
  어휘 덱 실물 → `language/` · 운동 루틴 내용 → `health/fitness`
- 생산성 앱 카탈로그 — 도구는 `택 1` 한 그룹으로 끝. 앱 이름을 항목으로 늘리지 않음
- **속독(speed reading) 영구 배제** — 안구운동 연구로 반증됨(이해도를 깎지 않는 배속은 없음).
  파동이론·관상과 같은 잣대. `reading-notes`의 `Inspectional Read`가 정당한 대체물
- 마음챙김·명상 프로그램 — 별도 분야로 안 뺌. 필요해지면 `health/`에 파일 추가
- 목표 설정 이론(OKR·SMART) 자체 — `planning`의 `Goal to Project` 한 항목으로 흡수,
  프레임워크 비교는 안 함

**finance에 만들지 않기로 한 것 (2026-08-26, 격자 닫음):**
- 부동산 투자 — 사용자 계획 없음. 하게 되면 `investing/`에 파일 추가
- 코인 — 재개 계획 없음. 차트 기법은 `investing/trading`이 자산 불문으로 커버.
  코인 고유(지갑·수탁·토크노믹스)는 재개 시 추가
- 파동이론(엘리엇) — 반증 불가능·유사과학, 영구 배제 (social의 관상·필적학과 같은 잣대).
  trading에 "TA의 한계 확인" 항목으로만 존재
- 금융 자격증(CFA·AFPK 등) 준비 — 자격증은 INVENTORY 소관
- 경제 원리·시장 이론 → `academics/economics/` 본체. 판별법: 항목에 "내"가 붙으면 finance, 안 붙으면 economics
- 학술 재무(CAPM·포트폴리오 이론) — investing 항목의 이론 배경(s:2 층)으로 흡수.
  학문으로 깊게 필요해지면 그때 economics에 파일 추가

---

## 파서 예외 (md 실물의 특이 케이스 — 파서·검사 도구를 고칠 때 필수)

- PART 구분이 없는 파일 21개. 분량이 적어 대단원을 안 나눈 원본들 → PART를 필수로 두면 안 됨
- `###` 서브섹션이 없는 파일 5개 (`full-stack` `code-review` `leetcode` `zustand` `kubernetes`).
  항목이 `##` 섹션 바로 아래 붙음 → 서브섹션을 필수로 두면 안 됨
- `skill-based/CS-Theory/code-review.md` 는 원본 pdf 다운로드가 안 돼서 프린터로 출력해 변환한 거라
  항목이 키워드가 아니라 마침표 붙은 문장임. 다른 파일은 전부 명사구
- `####` 4단 헤딩 3개 존재(postgresql-dba 2 · ux-design 1). 파서는 `###`와 동급으로 취급
- `택 1` 364개 중 356개는 헤딩(`##`/`###`)에 붙음 → 그 헤딩 아래 항목 전체가 한 그룹.
  나머지 8개는 항목 안에 `/`로 선택지를 나열한 자기완결형. 파서는 `choice` 플래그만 기록,
  분모는 `build_stats.py`가 그룹당 1로 계산 — `docs/stat-model.md` 규칙 5
