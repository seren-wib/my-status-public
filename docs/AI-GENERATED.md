# AI 생성 로드맵 목록

> **`AI 생성` 태그 실측 261파일 (2026-08-28 기준).** roadmap.sh 원본이 아니라 AI가 작성한 로드맵 —
> 각 파일 첫 줄에 `` `AI 생성` `` 태그가 붙어 있음. **원본은 태그다** — 이 문서는 경위 기록이고,
> 정확한 목록이 필요하면 태그를 grep할 것
> 괄호 안 숫자는 그 파일의 `- [ ]` 항목 수

## software 신규 집필 (2026-08-22) · 94개 파일 / 9849 학습항목

기존 로드맵 87개가 참조는 하지만 개별 로드맵이 없던 기술들.
`qa.md`는 있는데 테스트 도구가 없고, `postgresql-dba.md`는 있는데 MySQL이 없는 식으로
**카테고리가 통째로 비어 있어서** 채운 것.

본문에서 `qa.md` 처럼 파일명만 적은 것은 `roadmaps/software/` 아래 기존 로드맵을 가리킴.

---

## social role 인물상 재편 (2026-08-26)

**15개 archetype 파일 전부 AI 작성 · 1263항목.** 구 role 14개(persuasion·manipulation·insight 등
능력명)를 폐기하고 인물상으로 재편 — 사유·원칙은 `docs/architecture.md`.

demagogue(선동가 88) · orator(연설가 85) · cult-leader(컬트 지도자 88) ·
political-operator(정치인 80) · leader(지도자 79) · connector(연결자 81) ·
negotiator(협상가 88) · mediator(중재자 88) · interrogator(심문관 87) ·
manipulator(조종자 73 — 파일럿) · seducer(유혹자 87) · public-figure(명사 76) ·
con-artist(사기꾼 89) · operative(첩보원 87) · coercer(강압자 87)

**집필 후 검토에서 잡은 것 (2026-08-26).** 6개 조 병렬 집필의 부작용 —
집필 지시에 "예측·적응·전수 축"을 공통으로 넣은 결과 `Mechanism Teaching`이 13/15 파일에,
`Outcome Forecasting` 8·`Calibration Record` 5·`Failure Mode Catalog` 4에 복제됨(≈35항목).
전부 archetype 고유 항목으로 교체(예: leader→`Succession Planning`, orator→`Speechwriting for Others`,
connector→`Tie Decay Forecast`). 보정 축이 인물상의 본체인 곳만 유지(interrogator·demagogue·manipulator).
같은 이름 다른 개념도 분화(`Escalation Ladder` → coercer는 Kahn 확전, manipulator는 `Compliance Escalation`,
mediator는 `Conflict Escalation Stages`). 남은 중복 25건은 `Two-Level Games`(Putnam)·
`Mere Exposure Effect`(Zajonc)처럼 여러 인물상이 실제로 공유하는 정전 개념이라 유지.
**교훈**: 병렬 집필 프롬프트에 공통 축을 지시하면 그 축이 그대로 보일러플레이트가 됨 —
축은 지시하되 "그 인물상 고유의 것으로 쓸 것"을 함께 박아야 함

폐기: coercion · conflict · deception · insight · leadership · manipulation · negotiation ·
networking · persuasion · propaganda · relationship · seduction · self-presentation · speaking
(내용은 승계 archetype 또는 기존 skill 파일이 보유 — 손실 0 확인 후 삭제)

## 원본 파일에 AI가 증축한 부분 (2026-08-26)

**현재 `roadmaps/` 잔존 0.** 밴드는 2026-08-26 전량 해체됨. 아래는 그 경위 기록.

- 최초 증축 46파일 +521항목 → **social 14파일 +153항목**은 archetype 재편으로 흡수·폐기(같은 날),
  나머지 **32파일 +368항목**도 같은 날 해체됨. 사유는 아래
- **해체 사유 — 축 혼합.** role 파일의 PART 축은 공정(또는 커리큘럼) 하나인데 밴드가 수준 축이라
  마지막 PART에 다른 축을 용접한 꼴이었음. 공정에 N+1단계가 없으니 그 칸이 필러로 채워짐.
  실측 판정도 "진단서로는 유효, 치료제로는 무효"였음(전체 1.3%·skill 152파일엔 0개·경로 없이 도착점만)
- **처리 방식이 두 갈래로 갈림** — 근거는 body와 밴드의 문법이 같은가:
  - `business/role-based/` 3파일 +37 → **용해.** body 자체가 실행 마일스톤 문법이라
    (`First Paid Contract`·`Ten Paying Customers`) 공정 단계에 넣어도 절벽이 없음.
    판정 불가 1건씩(`Market Reference` 류) 삭제, 나머지는 해당 단계로 이동
  - `software/role-based/` 22파일 +250 → **`milestones/software.md`로 이주.**
    body는 지식 명사구(`Circuit Breaker`)인데 밴드는 성취 서술문이라 섞으면 난이도 절벽이 생기고
    섹션이 안 닫혀 진행이 막힘. 성취는 '배우는 것'이 아니라 '이루는 것'이라 진행률 분모에서 뺌.
    186항목 이주 + 공통 50줄을 7줄로 통합(판정 기준 명시) · 14항목 삭제(판정 불가·body 재탕)
  - 나머지 role 7파일은 애초에 밴드가 없었음(증축 중단 상태였음) — 이제 29파일 전부 균일
- **남은 과제는 그대로**: 천장을 다시 세우려면 밴드가 아니라 **개념 명명으로 body를 깊게** 해야 함
  (`kafka.md`의 `Unclean Leader Election`·`japanese/kanji.md`의 급수 덱+정답률 방식이 저장소 내 선례)
- 규칙 명문화: `docs/architecture.md` "PART 축 규칙 — 수준은 PART가 아니다"

---

## 신규 폴더

### roadmaps/software/skill-based/Testing — 12개 / 1257항목

`qa.md` 역할 로드맵은 있었으나 도구 로드맵이 전무했음

playwright(115) · cypress(106) · jest(107) · vitest(100) · selenium(107) · puppeteer(104)
junit(105) · phpunit(98) · pytest(107) · rspec(104) · appium(104) · detox(100)

### roadmaps/software/skill-based/Build-Tools — 6개 / 652항목

maven(123) · gradle(126) · vite(112) · webpack(116) · esbuild(66) · cmake(109)

### roadmaps/software/skill-based/Blockchain — 5개 / 489항목

`blockchain.md` 역할 로드맵은 있었으나 언어·도구 로드맵이 전무했음

solidity(129) · hardhat(101) · foundry(106) · web3js(73) · ethersjs(80)

### roadmaps/software/skill-based/Design — 4개 / 313항목

`product-design.md` · `ux-design.md` 는 있었으나 도구 로드맵이 전무했음

figma(109) · sketch(76) · adobe-xd(70) · balsamiq(58)

### roadmaps/software/skill-based/Game-Dev — 3개 / 368항목

`game-developer.md` 역할 로드맵은 있었으나 엔진 로드맵이 전무했음

unity(130) · unreal-engine(129) · godot(109)

---

## 기존 폴더에 추가

### roadmaps/software/skill-based/Infra-DevOps — 20개 / 2121항목

**CI/CD** — GitHub Actions만 `git-github.md` 섹션으로 있었고 나머지 전무
circleci(101) · jenkins(109) · gitlab-ci(100) · teamcity(106) · argocd(102) · travis-ci(63)

**관측·모니터링** — 카테고리 전무
prometheus(129) · grafana(128) · datadog(124) · new-relic(124) · opentelemetry(126) · sentry(106)

**클라우드** — `aws.md` 만 있었음
azure(126) · gcp(123) · vercel(81) · digitalocean(77) · heroku(80)

**웹 서버** — 카테고리 전무
nginx(116) · apache-httpd(118) · caddy(82)

### roadmaps/software/skill-based/Frameworks — 20개 / 1936항목

**웹 프레임워크** — 13개가 있었으나 아래가 빠져 있었음
flask(103) · fastapi(98) · express(104) · nestjs(100) · astro(106)
remix(121) · symfony(124) · quarkus(122) · ktor(100)

**CSS·UI** — `css.md` 는 있었으나 프레임워크 로드맵 전무
tailwind(100) · sass(93) · shadcn-ui(72) · material-ui(86) · chakra-ui(81)

**ORM·상태 관리** — 카테고리 전무
prisma(103) · typeorm(98) · sequelize(105) · redux(94) · zustand(55) · mobx(71)

### roadmaps/software/skill-based/Data-DB — 16개 / 1847항목

**DB 제품** — postgresql-dba · mongodb · redis · elasticsearch 4개만 있었음
mysql(128) · sqlite(80) · mariadb(95) · cassandra(107) · oracle(130) · ms-sql(126)
couchdb(99) · neo4j(117) · snowflake(117) · bigquery(122)

**메시지 브로커·데이터 파이프라인** — 카테고리 전무
kafka(128) · spark(126) · rabbitmq(120) · airflow(128) · dbt(101) · databricks(123)

### roadmaps/software/skill-based/AI — 8개 / 866항목

`machine-learning.md` · `ai-engineer.md` 는 있었으나 프레임워크·벡터DB 로드맵이 전무

**ML·AI 프레임워크**
tensorflow(129) · pytorch(126) · langchain(129) · llamaindex(129)

**벡터 DB**
pinecone(93) · chroma(74) · weaviate(92) · qdrant(94)

---

## 만들지 않은 것

전수조사에서 세분화 없는 제품이 624개 나왔으나 절반 이상은 **학습 로드맵 대상이 아님.**
"설치 → 기본 사용법" 세 줄로 끝나는 라이브러리라 개별 로드맵을 만들면 오히려 지저분해짐.
재조사를 막기 위해 기록해둠.

```
Axios  ruff  black  mypy  Bogus  Serde  Zap  ejs  clap  YARD  Winston  Morgan
CanCanCan  Scrutor  AutoMapper  Zombie.js  Kaminari  Pagy  NSubstitute  Moq
Formik  FormKit  Vuelidate  react-query  pyright  staticcheck  Ktlint  Detekt
Serilog  NLog  Logback  SLF4J  Zerolog  등
```

에디터(VS Code · Vim · Emacs)도 등장 빈도는 높지만 학습 로드맵 대상이 아니라 제외함.
