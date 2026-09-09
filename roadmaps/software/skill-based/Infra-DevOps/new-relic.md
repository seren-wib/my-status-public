# New Relic `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to New Relic

## 1. What is New Relic?

### Overview of New Relic / What is it?

- [ ] All-in-one Observability Platform / 신호별 도구를 나누지 않고 한 계정에 모은 형태
- [ ] NRDB / 모든 신호를 한 데이터베이스에 이벤트로 쌓는 저장소
- [ ] Ingest and User Based Pricing / 들어온 용량과 사용자 수로 값이 매겨지는 방식
- [ ] Full-Stack Observability Orientation / 앱부터 브라우저까지 같은 질의로 잇는 지향

### Data Types

- [ ] Event / 시각과 속성을 묶은 한 줄짜리 기록 단위
- [ ] Metric / 시간 구간마다 값을 미리 접어 둔 수치 형태
- [ ] Log / 본문 문자열에 속성을 붙여 넣은 기록
- [ ] Trace and Span / 요청 하나와 그 안 구간을 잇는 기록 형태
- [ ] MELT Model / 네 신호를 저장 형태로 나눈 분류

### Entity Model

- [ ] Entity and Entity GUID / 감시 대상 하나에 붙는 고유 식별자
- [ ] Entity Type / 대상을 앱·호스트·브라우저 갈래로 나눈 분류
- [ ] Entity Tag / 엔티티에 키와 값을 붙여 골라내는 표식
- [ ] Workload / 여러 엔티티를 관심 묶음 하나로 만든 단위
- [ ] Relationship and Service Map / 호출 관계를 이어 그린 시스템 지도

## 2. Getting Started

### Account Structure

- [ ] Organization and Account / 조직 아래 계정을 나눠 데이터를 가르는 층
- [ ] License Key and Ingest Key / 데이터를 밀어 넣을 때 쓰는 인증 문자열
- [ ] User Key / 질의와 설정 변경을 부를 때 쓰는 열쇠
- [ ] Sub-account Separation Strategy / 팀·환경별로 계정을 쪼개 놓는 기준

### Data Ingestion `택 1`

- [ ] Guided Install / 환경을 훑어 붙일 에이전트를 골라 주는 설치 `추천`
- [ ] Individual Agent Installation / 대상마다 에이전트를 따로 골라 넣는 방식
- [ ] Telemetry API / 에이전트 없이 HTTP로 직접 밀어 넣는 창구
- [ ] OpenTelemetry Exporter / 표준 형식으로 만든 신호를 받아 주는 경로

### UI Structure

- [ ] All Entities / 계정 안 모든 대상을 한 목록으로 훑는 화면
- [ ] APM & Services / 서비스 단위 지표를 모아 둔 진입 화면
- [ ] Query Your Data / NRQL을 직접 적어 되묻는 질의 화면
- [ ] Dashboards / 질의 결과 차트를 모아 붙인 화면

## 3. Agents / Integrations

### APM Agent

- [ ] Per-Language Agents / 언어 런타임마다 따로 만들어진 계측 라이브러리
- [ ] newrelic.yml / 앱 이름과 키를 파일이나 환경변수로 주는 설정
- [ ] Auto Instrumentation Scope / 코드를 안 고쳐도 잡히는 라이브러리 범위
- [ ] Enabling Distributed Tracing / 서비스를 건너가는 요청 추적을 켜는 설정

### Infrastructure

- [ ] Infrastructure Agent / 호스트 자원과 프로세스를 올려 보내는 데몬
- [ ] On-host Integration / 같은 호스트의 미들웨어 지표를 받아 오는 확장
- [ ] Flex Integration / 명령 출력이나 JSON을 설정만으로 지표로 만드는 방식
- [ ] Kubernetes Integration / 클러스터 오브젝트를 엔티티로 올리는 통합

### Cloud

- [ ] AWS, Azure, GCP Integration / 클라우드 계정을 붙여 관리형 자원을 받는 방식
- [ ] Metric Streams vs Polling / 밀어 받을지 주기로 물어볼지 가르는 선택

---

# PART 2 · NRQL

## 4. NRQL Basics

- [ ] SELECT and FROM / 이벤트 타입을 대상으로 지목하는 질의 뼈대
- [ ] WHERE, Operators, LIKE, RLIKE, IN / 속성 값으로 이벤트를 걸러 내는 조건절
- [ ] SINCE, UNTIL, Relative Time / 질의가 볼 시간 구간을 잘라 주는 절
- [ ] FACET / 속성 값별로 결과를 갈라 세는 절
- [ ] LIMIT and ORDER BY / 결과 줄 수와 정렬 순서를 정하는 절
- [ ] TIMESERIES / 결과를 시간 칸으로 나눠 그리게 하는 절
- [ ] COMPARE WITH / 같은 질의를 과거 구간과 겹쳐 보는 절

## 5. NRQL Functions

- [ ] Aggregators / 여러 이벤트를 값 하나로 접는 함수 묶음
- [ ] Percentile / 느린 쪽 꼬리를 순위 값으로 보는 함수
- [ ] uniqueCount / 서로 다른 값의 개수와 목록을 뽑는 함수
- [ ] rate / 누적 값을 시간당 변화량으로 바꾸는 함수
- [ ] filter / 한 질의 안에서 집계마다 조건을 다르게 주는 함수
- [ ] apdex / 만족 기준 시간을 인자로 주고 점수를 내는 함수
- [ ] funnel / 정해진 단계를 차례로 밟은 비율을 세는 함수
- [ ] Subquery / 집계 결과를 다시 질의 대상으로 넣는 구문
- [ ] Lookup Table / 올려 둔 표를 질의에 끌어다 붙이는 방법

## 6. NRQL in Practice

- [ ] Timeslice Metric vs Dimensional Metric / 옛 이름 기반 지표와 속성 기반 지표의 갈림
- [ ] Metric Query Syntax / 접힌 지표에서 최소·최대 같은 칸을 꺼내는 문법
- [ ] Sending Custom Events / 내 이벤트 타입을 만들어 밀어 넣는 방법
- [ ] Adding Custom Attributes / 에이전트가 붙인 속성 옆에 내 값을 더하는 방법
- [ ] Data Retention and Drop Rule / 타입별 보관 기간과 버릴 것을 정하는 설정
- [ ] Query Limit / 한 질의가 훑는 이벤트 수에 걸린 상한

---

# PART 3 · Usage by Product

## 7. APM

- [ ] Transaction and Transaction Trace / 요청 한 건 단위와 느린 건만 남긴 상세 기록
- [ ] Apdex Score / 응답 시간을 만족·불만족으로 나눠 매긴 점수
- [ ] Web vs Non-web Transaction / 요청형과 백그라운드 작업형을 가르는 분류
- [ ] Database and External Service Breakdown / 응답 시간을 DB와 외부 호출 몫으로 쪼갠 내역
- [ ] Error Inbox and Error Group / 같은 원인 오류를 묶어 담당과 상태를 다는 곳
- [ ] Distributed Tracing UI / 서비스를 건너간 스팬을 폭포 그림으로 보는 화면
- [ ] Code-level Metrics / 지표를 소스 함수와 줄 단위까지 내려 붙이는 기능
- [ ] Change Tracking and Deployment Marker / 배포 시점을 차트에 찍어 전후를 가르는 표식
- [ ] Continuous Profiling / 실행 중 CPU를 함수별로 상시 표집하는 기능 `선택`

## 8. Browser / Mobile / Synthetic

- [ ] Browser Agent / 스크립트를 직접 넣을지 앱이 심게 할지 가르는 설치
- [ ] Page View and SPA Monitoring / 화면 전환을 새 로드와 경로 변경으로 나눠 세는 방식
- [ ] Core Web Vitals / 체감 로딩·반응·흔들림을 재는 세 지표
- [ ] Session Trace and Session Replay / 방문자 한 명의 행동 순서를 되짚는 기록
- [ ] JS Error Tracking / 브라우저 예외를 원본 소스 위치로 되돌리는 기능
- [ ] Mobile Agent and Crash Analysis / 앱 강제 종료를 스택별로 묶어 세는 기능
- [ ] Synthetic Monitor / 밖에서 주기로 찔러 응답을 확인하는 감시
- [ ] Private Minion / 사내망 안에서 그 감시를 돌리는 실행기

## 9. Logs

- [ ] Log Forwarder / 파일과 스트림의 로그를 골라 올려 보내는 경로
- [ ] Parsing Rule / 본문 문자열을 속성 칸으로 쪼개는 규칙
- [ ] Logs in Context / 로그를 같은 요청의 트레이스에 붙이는 방법
- [ ] Log Patterns / 비슷한 본문을 같은 틀로 묶어 세는 기능
- [ ] Drop Filter / 저장 전에 특정 로그를 버리게 하는 조건
- [ ] Live Tail / 들어오는 로그를 실시간으로 흘려 보는 화면

## 10. Infrastructure / Kubernetes

- [ ] Host Overview and Processes / 호스트 자원과 프로세스별 점유를 함께 보는 화면
- [ ] Kubernetes Cluster Explorer / 노드와 파드 상태를 계층 그림으로 훑는 화면
- [ ] Container Metrics / 컨테이너 단위 사용량과 제한 대비 비율
- [ ] Auto-Discovery / 새로 뜬 대상을 조건에 맞춰 자동으로 붙이는 기능
- [ ] Network Monitoring / 장비 인터페이스와 흐름 데이터를 받는 감시 `선택`

---

# PART 4 · Alerting and Automation

## 11. Alerts

### Conditions

- [ ] NRQL Alert Condition / 질의 결과 값에 임계를 걸어 만드는 조건
- [ ] Static vs Baseline Threshold / 고정값과 학습된 정상 범위를 가르는 선택
- [ ] Threshold Duration and Aggregation Window / 값을 모으는 창과 어긋남이 이어질 시간
- [ ] Signal Loss and Gap Filling / 데이터가 끊긴 구간의 빈 칸을 다루는 설정
- [ ] Anomaly Detection / 과거 패턴에서 벗어난 값을 골라내는 방식

### Grouping and Routing

- [ ] Alert Policy / 조건 여러 개를 한 묶음으로 관리하는 단위
- [ ] Incident Preference / 조건과 대상별로 사건을 몇 개로 쪼갤지 정하는 설정
- [ ] Workflow / 사건을 골라 내용을 채워 내보내는 단계
- [ ] Destination / 알림이 실제로 도착할 바깥 창구 등록
- [ ] Muting Rule / 정해진 시간과 대상의 알림을 잠재우는 규칙

### Operations

- [ ] Issue and Incident Lifecycle / 사건이 열리고 확인되고 닫히는 상태 흐름
- [ ] Alert Coverage Gap / 알림이 걸려 있지 않은 대상을 찾는 점검
- [ ] Alert Quality Review / 울린 알림 중 헛것의 비율을 되짚는 검토

## 12. Service Level Management

- [ ] SLI Definition / 좋은 요청과 전체 요청을 질의로 정하는 방법
- [ ] SLO Target and Error Budget / 목표 비율과 남은 실패 허용치
- [ ] SLM Dashboard / 여러 서비스의 목표 달성률을 모아 둔 화면
- [ ] Budget Burn Review / 허용치가 닳는 속도를 주기로 되짚는 검토

## 13. Dashboards

- [ ] Dashboard, Page, Widget / 화면과 페이지와 차트로 이어지는 구성 층
- [ ] Chart Type / 질의 결과 모양에 맞는 차트를 고르는 기준
- [ ] Template Variable / 값 하나로 화면 전체 질의를 갈아 끼우는 변수
- [ ] Facet Linking and Drill Down / 차트 조각을 눌러 좁힌 질의로 넘어가는 이동
- [ ] Dashboard JSON / 화면 정의를 코드로 내보내고 되돌리는 형식
- [ ] Sharing and Public Link / 계정 밖 사람에게 화면을 여는 방법

---

# PART 5 · Operations

## 14. NerdGraph / Automation

- [ ] NerdGraph GraphQL API / 계정 설정과 질의를 한 창구에서 부르는 API
- [ ] Terraform New Relic Provider / 조건과 화면을 선언 파일로 관리하는 도구
- [ ] Alerts as Code / 알림 설정을 저장소에 두고 리뷰하는 방식
- [ ] Entity Tag Automation / 배포 정보로 태그를 자동으로 붙이는 방법
- [ ] CI/CD Integration and Deployment Marker / 파이프라인 끝에서 배포 사실을 밀어 넣는 연동

## 15. Account and Cost Operations

- [ ] User Type / 쓸 수 있는 기능 폭으로 갈리는 사용자 등급
- [ ] Group and Role Based Access / 묶은 사용자에게 권한을 얹는 구조
- [ ] Ingest Cost Structure / 들어온 용량으로 값이 매겨지는 셈법
- [ ] Data Plus / 보관 기간과 기능을 늘린 상위 요금제 `별도`
- [ ] Drop Rule and Sampling / 안 볼 데이터를 미리 줄여 비용을 깎는 수단
- [ ] Usage Dashboard / 어디서 용량이 많이 들어오는지 뜯어보는 화면

## 16. Extensions `선택`

- [ ] New Relic CLI / 터미널에서 계정과 설정을 다루는 명령 도구
- [ ] Custom Nerdpack and Nerdlet / 직접 만든 화면을 플랫폼에 얹는 앱 단위
- [ ] Instant Observability Quickstart / 미리 만들어 둔 화면과 알림 꾸러미
- [ ] Pixie and eBPF Auto-telemetry / 코드를 안 고치고 커널에서 신호를 뜨는 방식

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Kubernetes `software/skill-based/Infra-DevOps/kubernetes.md`
- 오픈소스 관측 스택 `software/skill-based/Infra-DevOps/prometheus.md`, `grafana.md`
- 계측 표준 `software/skill-based/Infra-DevOps/opentelemetry.md`
- SaaS 관측 대안 `software/skill-based/Infra-DevOps/datadog.md`
- 에러 추적 `software/skill-based/Infra-DevOps/sentry.md`
