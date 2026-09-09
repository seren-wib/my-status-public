# Datadog `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Datadog

## 1. What is Datadog?

### Overview of Datadog / What is it?

- [ ] SaaS Observability Platform / 관측 데이터를 밖의 회사 저장소에 맡기는 방식
- [ ] Agent-based Collection / 호스트마다 수집기를 심어 신호를 올려 보내는 구조
- [ ] Metrics, Traces, Logs / 수치·요청 경로·원문으로 갈리는 세 신호
- [ ] Host and Ingest Based Pricing Model / 호스트 수와 보낸 양으로 요금이 갈리는 셈법

### Product Components

- [ ] Infrastructure Monitoring / 호스트와 컨테이너의 자원 상태를 모으는 제품
- [ ] APM and Distributed Tracing / 요청 하나가 서비스를 건너간 경로를 잇는 제품
- [ ] Log Management / 흩어진 로그 원문을 모아 검색 대상으로 만드는 제품
- [ ] RUM and Synthetic Monitoring / 실제 방문자와 가짜 방문자로 화면을 재는 제품
- [ ] Database Monitoring / 느린 질의와 실행 계획까지 들여다보는 제품
- [ ] Cloud Security and SIEM / 설정 위반과 보안 로그를 규칙으로 거르는 제품

### Adoption Decision

- [ ] Tradeoff Against a Self-hosted Stack / 직접 굴리는 스택과 견주는 운영 부담의 갈림
- [ ] Understanding Cost Structure, Host, Ingested Span, Indexed Log / 청구서가 불어나는 세 단위

## 2. Datadog Agent

### Installation `택 1`

- [ ] Host Package / 리눅스·윈도우에 패키지로 깔아 데몬으로 두는 방식 `추천`
- [ ] Docker Agent / 컨테이너 하나로 띄워 호스트 소켓을 물리는 방식
- [ ] Kubernetes, Helm, Operator / 클러스터마다 데몬셋으로 퍼뜨리는 설치 방식
- [ ] Serverless Extension, Lambda / 상주 호스트가 없는 함수에서 신호를 빼내는 방식

### Configuration

- [ ] datadog.yaml / API 키와 사이트, 기능 스위치를 담는 주 설정 파일
- [ ] conf.d and Integration Config / 감시 대상별 설정 파일을 두는 디렉터리 규칙
- [ ] Agent Commands, status, check, flare / 수집기 상태 확인과 진단 묶음 생성 명령
- [ ] DogStatsD / 앱이 UDP로 던진 지표를 받는 수집기 안의 창구
- [ ] Trace Agent / 계측 라이브러리가 보낸 스팬을 받아 넘기는 부분
- [ ] Process Agent and Live Processes / 호스트에서 도는 프로세스 목록을 올리는 부분

### Autodiscovery

- [ ] Container Labels and Pod Annotations / 컨테이너에 붙인 표식으로 점검 설정을 지정하는 방법
- [ ] Config Templates / 이미지 이름별로 미리 정해 둔 점검 설정 틀
- [ ] Ad Identifiers / 어떤 컨테이너에 어떤 설정을 붙일지 짝짓는 식별자

## 3. Tagging

- [ ] Tag Key:Value Structure / 신호마다 붙는 키와 값 한 쌍의 형식
- [ ] Reserved Tags, host, env, service, version / 플랫폼이 뜻을 미리 정해 둔 예약 태그
- [ ] Unified Service Tagging / 세 태그를 신호마다 똑같이 박아 화면을 잇는 규칙
- [ ] Host Tags vs Metric Tags / 호스트에 붙는 태그와 지표에 붙는 태그의 갈림
- [ ] Tag Cardinality Management / 태그 값 가짓수로 과금 단위가 불어나는 것을 막는 기준
- [ ] Scope / 화면과 질의가 볼 대상을 태그로 좁히는 범위

---

# PART 2 · Data Collection

## 4. Metrics

### Metric Types

- [ ] Count and Rate / 발생 횟수와 초당 값으로 나눠 보내는 형
- [ ] Gauge / 그 순간의 값 하나만 남기는 형
- [ ] Histogram and Distribution / 호스트마다 접을지 전역 백분위를 낼지 갈림
- [ ] Set / 서로 다른 값의 가짓수만 세는 형

### Collection Paths

- [ ] Built-in Integrations / 미들웨어별 점검을 미리 만들어 둔 카탈로그
- [ ] Custom Agent Check and Python Check / 수집기 안에서 돌 점검을 직접 짜는 경로
- [ ] DogStatsD Client / 앱 코드에서 지표를 직접 던지는 라이브러리
- [ ] Metrics API / 수집기 없이 HTTP로 지표를 밀어 넣는 경로
- [ ] OpenTelemetry Ingest / 중립 규격으로 계측한 신호를 받아 주는 입구

### Management

- [ ] Metrics Explorer / 저장된 지표를 태그로 갈라 훑어보는 화면
- [ ] Metric Summary / 지표별 태그 수와 전송 상태를 모아 보는 목록
- [ ] Custom Metric Cost / 태그 조합 하나가 과금 단위 하나가 되는 셈법
- [ ] Metrics without Limits / 저장은 다 하고 질의용 태그만 골라 요금을 줄이는 기능
- [ ] Rollup and Historical Metrics / 오래된 값을 굵은 간격으로 접어 두는 보존 방식

## 5. Log Management

### Collection

- [ ] Agent Log Collection, logs_enabled / 수집기의 로그 수집을 여는 스위치
- [ ] File Tailing and Container Log / 파일 끝과 컨테이너 표준출력에서 줄을 읽는 경로
- [ ] Forwarder, Lambda, HTTP Intake / 수집기가 없는 곳에서 로그를 대신 밀어 주는 통로

### Processing

- [ ] Log Pipeline / 들어온 로그를 순서대로 손보는 처리 사슬
- [ ] Grok Parser / 한 줄 문자열에서 속성을 뽑아내는 패턴 규칙
- [ ] Remapper, Date, Status, Attribute / 제각각인 필드를 표준 자리로 옮기는 처리
- [ ] Processing Rules, Multi-line, Exclude / 보내기 전에 수집기에서 줄을 묶고 거르는 규칙
- [ ] Standard Attributes and Facet / 자주 쓰는 필드를 검색·집계 축으로 세우는 방법

### Cost Control

- [ ] Index and Retention / 검색 대상으로 남길 로그와 보관 기간을 정하는 칸
- [ ] Exclusion Filter and Sampling / 색인에 넣지 않고 흘려보낼 비율을 정하는 조건
- [ ] Archive and Rehydration / 값싼 저장소에 부어 두고 필요할 때만 되살리는 흐름
- [ ] Logging without Limits / 다 받아 두고 색인만 골라 요금을 가르는 사고방식

## 6. APM

### Instrumentation

- [ ] Auto Instrumentation and Tracing Library / 코드 수정 없이 스팬이 생기게 하는 방식
- [ ] Single Step Instrumentation / 수집기 설치만으로 앱 계측까지 끼워 넣는 방식
- [ ] Custom Span and Manual Instrumentation / 자동으로 안 잡히는 구간을 직접 열어 재는 방법
- [ ] Trace Propagation Headers / 서비스 사이에서 추적 id를 넘겨 경로를 잇는 헤더

### Analysis

- [ ] Service Catalog and Service Map / 서비스 목록과 호출 관계를 그림으로 보는 화면
- [ ] Trace Explorer and Flame Graph / 요청 하나의 구간별 시간을 층으로 보는 화면
- [ ] Span Tags and Generate Metrics from Spans / 스팬 속성을 골라 상시 지표로 굳히는 방법
- [ ] Ingestion Sampling and Retention Filter / 보낼 스팬 비율과 남길 스팬 조건을 나누는 층
- [ ] Error Tracking / 같은 원인의 오류를 한 건으로 묶는 기능
- [ ] Continuous Profiler / 운영 중인 프로세스의 자원 소모 지점을 짚는 기능
- [ ] Data Streams Monitoring / 큐를 건너간 메시지의 지연을 잇는 기능 `선택`

## 7. Frontend and Synthetic Monitoring

### RUM

- [ ] Browser SDK and Mobile SDK / 방문자 기기에서 화면 신호를 보내는 계측 코드
- [ ] Session, View, Action / 방문자 행동을 방문·화면·조작 단위로 쪼갠 모델
- [ ] Core Web Vitals / 로딩·반응·흔들림으로 체감 속도를 재는 지표 묶음
- [ ] Session Replay / 방문자가 본 화면을 그대로 되감아 보는 기능
- [ ] RUM-Trace Linking / 느린 화면에서 그 요청의 서버 구간으로 넘어가는 연결

### Synthetic Monitoring

- [ ] API Test, HTTP, SSL, DNS / 밖에서 주기로 찔러 응답과 인증서를 재는 점검
- [ ] Browser Test and Recorder / 클릭 순서를 녹화해 화면 시나리오로 돌리는 점검
- [ ] Multistep API Test / 앞 응답 값을 다음 요청에 넘겨 흐름을 재는 점검
- [ ] Private Location / 사내망 안에서 점검을 돌리는 자체 실행 지점
- [ ] CI/CD Pipeline Integration / 배포 단계에서 점검 결과로 통과를 가르는 연결

---

# PART 3 · Querying and Alerting

## 8. Query / Dashboard

### Queries

- [ ] Metric Query Structure, from, avg by, rollup / 대상·묶음·간격 세 칸으로 짜인 질의 형식
- [ ] Space Aggregation vs Time Aggregation / 여러 호스트를 접는 것과 시간을 접는 것의 갈림
- [ ] Functions, Arithmetic, Rank, Timeshift / 결과에 계산·순위·시차를 덧씌우는 변환
- [ ] Formula & Function Editor / 여러 질의를 식 하나로 묶어 비율을 내는 편집기

### Dashboard

- [ ] Timeboard vs Screenboard / 시간축을 맞춘 판과 자유 배치 판의 갈림
- [ ] Widget, Timeseries, Query Value, Toplist, Heatmap, Table / 같은 질의를 어떤 그림으로 낼지 고르는 조각
- [ ] Template Variable / 태그 값을 골라 판 전체를 한 번에 좁히는 변수
- [ ] Powerpack / 위젯 묶음을 여러 판에 옮겨 쓰는 단위
- [ ] Notebook / 그래프와 설명을 섞어 조사 과정을 남기는 문서
- [ ] Sharing and Public URL / 계정 없는 사람에게 판을 보이는 공개 방법

## 9. Monitors

### Types

- [ ] Metric Monitor / 지표 값이 기준을 넘는지 보는 감시
- [ ] Log and APM Monitor / 로그 건수나 서비스 오류율을 조건으로 삼는 감시
- [ ] Anomaly, Outlier, Forecast Monitor / 평소 패턴·무리 이탈·추세로 기준을 대신하는 감시
- [ ] Composite Monitor / 여러 감시 결과를 논리식으로 묶은 감시
- [ ] Watchdog / 기준을 안 세워도 이상 구간을 집어내는 기능

### Configuration

- [ ] Threshold, Warning, Critical / 경고와 위험을 나누는 두 단계 기준값
- [ ] Evaluation Window and Delay / 얼마 구간을 볼지와 늦게 오는 값을 기다릴 시간
- [ ] No Data and Auto Resolve / 값이 끊겼을 때와 회복했을 때의 처리 규칙
- [ ] Notification Message, @-mention, Template Variables / 알림 문구에 대상과 태그 값을 끼우는 방법
- [ ] Multi Alert, group by / 태그 묶음마다 알림을 따로 띄우는 설정

### Operations

- [ ] Downtime and Scheduled Mute / 배포·점검 시간에 알림을 미리 막는 예약
- [ ] Monitor Tags / 감시 항목을 팀·서비스별로 골라내는 표식
- [ ] Incident Management / 장애 하나를 선언하고 대응 기록을 모으는 기능 `선택`
- [ ] On-Call / 당번과 호출 단계를 정해 알림을 사람에게 붙이는 기능 `선택`

## 10. SLO

- [ ] SLI Definition, Metric-based, Monitor-based / 좋은 요청의 비율을 무엇으로 셀지 정하는 기준
- [ ] Error Budget / 목표 미달을 허용해 두는 실패 몫
- [ ] Time Slice SLO / 시간을 조각내 나쁜 구간의 비율로 세는 방식
- [ ] SLO Alert and Burn Rate / 남은 몫을 태우는 속도로 미리 알리는 감시

---

# PART 4 · Operations

## 11. Infrastructure / Cloud

- [ ] Host Map and Container Map / 호스트와 컨테이너를 한 칸씩 색으로 늘어놓는 화면
- [ ] Cloud Integration, AWS, GCP, Azure / 계정 권한을 붙여 관리형 서비스 지표를 끌어오는 연결
- [ ] Kubernetes Orchestrator Explorer / 클러스터 오브젝트 상태를 목록으로 훑는 화면
- [ ] Network Performance Monitoring / 서비스 사이 통신량과 재전송을 보는 제품 `선택`
- [ ] Database Monitoring / 질의별 대기 시간을 DB 안에서 캐 오는 연동 `선택`
- [ ] Cloud Cost Management / 청구 데이터를 태그별로 갈라 보는 제품 `선택`

## 12. Configuration as Code

- [ ] API Key and Application Key / 조직 인증과 사용자 권한을 나눠 쥐는 두 열쇠
- [ ] Datadog API / 대시보드와 감시를 밖에서 만들고 고치는 창구
- [ ] Terraform Datadog Provider / 감시와 판을 코드로 선언해 맞춰 두는 도구
- [ ] Dashboard JSON Export and Import / 화면에서 만든 판을 파일로 빼고 되넣는 방법
- [ ] Monitor as Code / 감시 정의를 저장소에 두고 리뷰를 거치는 운영 방식
- [ ] CI Visibility / 빌드와 테스트 실패를 관측 대상으로 올리는 제품 `선택`

## 13. Organization Operations

- [ ] Team, Role, Permission / 사람을 묶고 볼 수 있는 범위를 가르는 단위
- [ ] SSO and SAML / 사내 계정으로 로그인을 넘기는 연동 `별도`
- [ ] Sensitive Data Scanner / 로그와 스팬에 섞인 개인정보를 규칙으로 가리는 기능
- [ ] Audit Trail / 누가 설정을 바꿨는지 남기는 기록
- [ ] Usage Attribution / 태그별로 사용량을 갈라 청구를 팀에 붙이는 기능
- [ ] Data Retention Policy / 신호별로 얼마나 남길지 정하는 조직 규칙

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Kubernetes `software/skill-based/Infra-DevOps/kubernetes.md`
- 오픈소스 관측 스택 `software/skill-based/Infra-DevOps/prometheus.md`, `grafana.md`
- 계측 표준 `software/skill-based/Infra-DevOps/opentelemetry.md`
- 에러 추적 `software/skill-based/Infra-DevOps/sentry.md`
- 설정 코드화 `software/skill-based/Infra-DevOps/terraform.md`
