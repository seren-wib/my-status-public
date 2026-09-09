# Grafana `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Grafana

## 1. What is Grafana?

### Overview of Grafana / What is it?

- [ ] Visualization and Dashboarding Platform / 남의 저장소에 든 값을 화면으로 만드는 층
- [ ] Datasource-agnostic Query Layer / 저장소를 가리지 않고 같은 판으로 묻는 구조
- [ ] Alerting Hub / 서로 다른 소스의 경보를 한 곳에서 판정하는 자리
- [ ] OSS vs Enterprise vs Grafana Cloud / 자체 설치판과 구독판을 가르는 기능 차이

### Core Use Cases

- [ ] Infrastructure Dashboard / 서버·컨테이너 상태를 한 판에 모으는 용도
- [ ] Application and Business KPI Dashboard / 매출·가입 수치를 같은 판에 얹는 용도
- [ ] Incident Review and Postmortem / 장애 시각으로 되돌려 원인을 훑는 용도

### Grafana Stack `선택`

- [ ] Loki / 본문 대신 라벨만 색인하는 로그 저장소
- [ ] Tempo / 트레이스 ID로 스팬을 되찾는 저장소
- [ ] Mimir / 지표를 길게 보관하도록 늘린 저장소
- [ ] Pyroscope / 프로파일을 시계열로 쌓아 보는 저장소
- [ ] Alloy / 여러 신호를 한 에이전트로 모아 보내는 수집기

## 2. Getting Started

### Installation `택 1`

- Docker / 이미지로 띄우고 설정을 볼륨에 두는 설치 `software/skill-based/Infra-DevOps/docker.md` `추천` `위임`
- [ ] Package and Binary / 호스트 서비스로 등록해 올리는 설치
- [ ] Helm Chart / 쿠버네티스에 값 파일로 얹는 설치
- [ ] Grafana Cloud / 서버를 안 두고 계정만으로 쓰는 호스팅판

### Initial Configuration

- [ ] grafana.ini and Environment Variables / 서버 설정을 파일과 환경변수로 나눠 주는 자리
- [ ] Admin Account and Anonymous Access / 첫 관리자와 로그인 없는 열람을 정하는 설정
- [ ] Plugin Installation, grafana-cli / 명령줄로 확장을 내려받아 붙이는 방법

### UI Structure

- [ ] Dashboard, Panel, Row / 판·그림 한 칸·접히는 묶음의 층위
- [ ] Explore / 판에 저장하지 않고 즉석으로 캐묻는 화면

## 3. Data Sources

### Connection

- [ ] Datasource Registration, URL, Auth / 주소와 인증 정보로 저장소를 붙이는 등록
- [ ] Default Datasource / 새 패널이 자동으로 고르는 소스 지정
- [ ] Provisioning YAML / 소스 연결을 화면 없이 파일로 심는 방법

### Major Data Sources

- [ ] Prometheus / 시계열 질의를 빌더로 짜 주는 소스 연결
- [ ] Loki / 로그 줄을 라벨로 좁혀 보는 소스 연결
- [ ] Elasticsearch / 색인 문서를 집계해 계열로 받는 소스 연결
- [ ] SQL, MySQL, PostgreSQL / 결과 표를 시계열 모양으로 바꿔 받는 소스 연결
- [ ] InfluxDB / Flux나 InfluxQL 편집기를 쓰는 소스 연결
- [ ] CloudWatch / AWS 지표를 계정 권한으로 끌어오는 소스 연결
- [ ] TestData / 소스 없이 가짜 계열을 만들어 주는 연습용 소스

### Multiple Sources

- [ ] Mixed Datasource / 한 패널 안에 서로 다른 소스의 질의를 섞는 설정
- [ ] Datasource Variable / 운영과 개발 소스를 골라 갈아 끼우는 값 자리

---

# PART 2 · Panels and Dashboards

## 4. Query Editor

- [ ] Builder vs Code Mode / 폼으로 짤지 원문으로 짤지 가르는 편집 방식
- [ ] Query Options, Min Interval, Max Data Points, Relative Time / 화면 폭에 맞춰 해상도와 구간을 정하는 설정
- [ ] Multiple Queries, Ref ID / 한 패널의 여러 질의를 A·B로 가르는 이름표
- [ ] Query Inspector and Panel JSON / 실제로 나간 요청과 받은 값을 들여다보는 창
- [ ] Expressions, Math, Reduce, Resample / 받아 온 결과끼리 다시 계산해 새 계열을 만드는 자리
- [ ] Interval Variables, $__interval, $__rate_interval / 조회 폭에서 자동으로 계산되는 간격 값
- [ ] SQL Macros, $__timeFilter, $__timeGroup / 시간 조건과 구간 묶기를 SQL에 끼우는 치환자

## 5. Panel Types

### Time Series

- [ ] Time Series / 값이 시간을 따라 오르내린 자취를 보는 패널
- [ ] Bar Chart / 시간이 아닌 항목끼리 크기를 견주는 패널
- [ ] Histogram / 값이 어느 구간에 얼마나 몰렸는지 보는 패널
- [ ] Heatmap / 분포가 시간에 따라 어디로 몰리는지 보는 패널

### Single Value

- [ ] Stat / 지금 값 하나와 그 흐름을 크게 띄우는 패널
- [ ] Gauge / 값이 임계선까지 얼마나 남았는지 보는 패널
- [ ] Bar Gauge / 여러 대상의 현재 값을 나란히 줄 세우는 패널

### Tables and Lists

- [ ] Table / 계열을 행과 열로 펼쳐 값을 직접 읽는 패널
- [ ] Logs / 원문 줄을 시간순으로 훑어 내려가는 패널
- [ ] Traces / 요청 하나가 서비스를 거친 구간을 보는 패널

### Others

- [ ] Pie Chart / 전체에서 각 몫이 차지하는 비율을 보는 패널
- [ ] State Timeline and Status History / 상태가 언제 바뀌어 얼마나 머물렀는지 보는 패널
- [ ] Geomap / 좌표가 붙은 값을 지도 위에 얹는 패널
- [ ] Node Graph / 서비스 사이 호출 관계를 점과 선으로 보는 패널
- [ ] Text and Markdown / 판에 설명과 링크를 적어 두는 패널

## 6. Panel Options

### Visual Representation

- [ ] Unit and Decimals / 바이트·초 같은 단위와 자릿수를 붙이는 설정
- [ ] Standard Options, Min, Max, Color Scheme / 축 범위와 색 배정을 패널 전체에 주는 설정
- [ ] Thresholds / 값이 넘으면 색이 갈리는 경계선
- [ ] Value Mappings / 코드값을 사람이 읽을 말로 바꾸는 대응표
- [ ] Legend and Tooltip / 계열 이름과 커서 아래 값을 보이는 방식
- [ ] Axis and Log Scale / 값 차이가 클 때 축을 로그로 눕히는 설정

### Field Override

- [ ] Override Rules / 특정 계열에만 다른 표시 설정을 덮는 규칙
- [ ] Matcher, by Name, by Regex, by Type / 덮어쓸 계열을 이름·정규식·형으로 고르는 조건

### Transformations

- [ ] Reduce and Filter by Name / 계열을 한 값으로 접거나 이름으로 걸러내는 전이
- [ ] Join by Field and Merge / 다른 질의 결과를 같은 열 기준으로 붙이는 전이
- [ ] Organize Fields, Rename, Reorder / 열 이름과 순서를 화면용으로 다듬는 전이
- [ ] Group By and Add Field from Calculation / 열 값으로 묶어 접고 계산 열을 더하는 전이
- [ ] Config from Query Results / 질의 결과 값을 임계선·단위 설정으로 쓰는 전이

## 7. Dashboard Composition

### Variables

- [ ] Query Variable / 소스에 물어 얻은 목록으로 선택지를 채우는 변수
- [ ] Custom, Constant, Interval Variable / 손으로 적은 목록·고정값·시간 폭 선택지
- [ ] Textbox Variable / 보는 사람이 값을 직접 적어 넣는 변수
- [ ] Ad-hoc Filters / 판 전체 질의에 조건을 즉석으로 얹는 변수
- [ ] Multi-value and Include All / 여러 값을 한꺼번에 고르게 여는 설정
- [ ] Chained Variable / 앞 선택에 따라 뒤 목록이 좁아지는 연결
- [ ] Variable Syntax, $var, ${var:regex} / 변수를 질의에 끼울 때 형식을 고르는 표기

### Layout

- [ ] Row and Repeat by Variable / 변수 값마다 묶음 줄을 통째로 찍어내는 배치
- [ ] Panel Repeat / 변수 값마다 같은 패널을 늘어놓는 배치
- [ ] Data Links and Panel Links / 값을 눌러 다른 판이나 로그로 넘어가는 연결
- [ ] Dashboard Links / 관련된 다른 판을 판 위쪽에 걸어 두는 목록

### Time

- [ ] Time Range and Time Picker / 판 전체 질의가 따르는 조회 구간 선택
- [ ] Time Shift and Comparison / 지난주 같은 시각과 겹쳐 보는 구간 이동
- [ ] Auto Refresh Interval / 화면이 스스로 다시 물어보는 주기

### Sharing

- [ ] Snapshot / 값을 그대로 굳혀 소스 없이 보이는 사본
- [ ] Public Dashboard / 로그인 없는 사람에게 여는 읽기 전용 주소
- [ ] Embed and iframe / 패널 하나를 다른 웹 페이지에 끼워 넣는 방법
- [ ] Export and Import JSON / 판을 파일로 내보내 다른 서버에 옮기는 방법
- [ ] Library Panel / 여러 판이 패널 한 벌을 공유해 같이 고치는 방식

---

# PART 3 · Alerting

## 8. Grafana Alerting

### Rules

- [ ] Alert Rule, Query, Condition / 질의 결과가 어떤 상태면 경보인지 정하는 규칙
- [ ] Reduce and Threshold Expression / 계열을 한 값으로 접어 경계와 견주는 단계
- [ ] Pending Period and Evaluation Group / 조건이 얼마나 이어져야 울릴지 정하는 대기
- [ ] No Data and Error Handling / 값이 안 오거나 질의가 깨질 때 취할 상태
- [ ] Grafana Managed vs Datasource Managed Rule / 판정을 여기서 할지 소스에 맡길지 가르는 갈림

### Routing

- [ ] Notification Policy Tree / 라벨을 따라 내려가며 받을 쪽을 고르는 트리
- [ ] Label Matching / 경보에 붙은 라벨로 경로를 가르는 조건
- [ ] Contact Point, Slack, Email, Webhook, PagerDuty / 알림이 실제로 나가는 도착지 설정
- [ ] Notification Template / 알림 문구에 값과 라벨을 끼워 짜는 틀
- [ ] Mute Timing and Silence / 정해진 시간대나 조건에 알림을 눌러 두는 방법

### Operations

- [ ] Alert Grouping / 비슷한 경보를 한 알림으로 묶어 보내는 방식
- [ ] Alert State History / 경보가 언제 켜지고 꺼졌는지 되짚는 기록
- [ ] Alert Rule Version Control / 규칙이 언제 누구 손에 바뀌었는지 남는 이력

---

# PART 4 · Operations

## 9. Provisioning as Code

- [ ] Datasource Provisioning / 소스 연결을 배포에 실어 서버에 심는 방법
- [ ] Dashboard Provisioning and File Provider / 폴더의 판 파일을 서버가 읽어 올리는 방식
- [ ] Alerting Provisioning / 경보 규칙과 경로를 파일로 배포하는 방법
- [ ] Dashboard JSON Model, schemaVersion, uid / 판 하나를 통째로 적은 문서 구조
- [ ] Grafonnet and Jsonnet / 판 JSON을 손으로 안 적고 찍어내는 언어
- [ ] Terraform Grafana Provider / 판·소스·권한을 인프라 코드로 잡는 방법
- [ ] Git-Based Dashboard Version Control / 판 변경을 리뷰 거쳐 반영하는 절차

## 10. Access Control

- [ ] Organization, Team, User / 판과 소스를 나눠 갖는 소속 단위
- [ ] Roles, Viewer, Editor, Admin / 보기·고치기·설정을 가르는 기본 역할
- [ ] Folder and Dashboard Permissions / 폴더에 준 권한이 안쪽 판으로 내려가는 규칙
- [ ] Fine-grained RBAC / 기능 단위까지 쪼개 주는 권한 방식 `선택`
- [ ] Service Account and API Token / 사람 아닌 프로그램에 주는 접근 자격

### Authentication `택 1`

- [ ] Built-in Login / 계정과 비밀번호를 자체 저장소에 두는 방식 `추천`
- [ ] OAuth and OIDC / 외부 신원 제공자에게 로그인을 넘기는 방식
- [ ] LDAP / 사내 디렉터리 계정과 그룹을 그대로 쓰는 방식
- [ ] SAML / 기업 SSO와 인증 주장을 주고받는 방식 `별도`

## 11. Plugins

- [ ] Panel Plugin / 기본에 없는 그림 종류를 더하는 확장
- [ ] Datasource Plugin / 지원 안 하는 저장소를 붙이게 하는 확장
- [ ] App Plugin / 판과 페이지를 묶어 한 화면으로 내는 확장
- [ ] Plugin Catalog and Signature / 서명으로 출처를 확인하고 설치하는 목록
- [ ] Custom Plugin Development Basics / 확장을 직접 만들 때의 구성과 규약

## 12. Operations and Performance

- [ ] Backend Database, SQLite, MySQL, PostgreSQL / 판·계정·설정을 담아 두는 자체 저장소
- [ ] High Availability Setup / 서버를 여러 대로 두고 경보 판정을 나누는 구성
- [ ] Dashboard Performance / 판 하나가 소스에 던지는 질의 수를 줄이는 방법
- [ ] Query Caching / 같은 질의 결과를 잠시 재사용해 소스를 아끼는 기능 `선택`
- [ ] Image Renderer / 패널을 그림 파일로 굽는 별도 구성 요소
- [ ] Backup and Migration / 자체 저장소를 옮겨 판을 이전하는 절차
- [ ] Grafana HTTP API / 판·소스·사용자를 프로그램으로 다루는 창구

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- 메트릭 수집·PromQL `software/skill-based/Infra-DevOps/prometheus.md`
- 계측 표준 `software/skill-based/Infra-DevOps/opentelemetry.md`
- SaaS 관측 대안 `software/skill-based/Infra-DevOps/datadog.md`, `new-relic.md`
- 로그 검색 백엔드 `software/skill-based/Data-DB/elasticsearch.md`
- 설정 코드화 `software/skill-based/Infra-DevOps/terraform.md`
