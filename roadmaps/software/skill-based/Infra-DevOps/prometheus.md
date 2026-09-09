# Prometheus `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Prometheus

## 1. What is Prometheus?

### Overview of Prometheus / What is it?

- [ ] Time Series Database / 같은 계열에 시각과 값을 이어 붙이는 저장 구조
- [ ] Pull-based Metrics Collection / 서버가 대상에 직접 붙어 긁어오는 수집 방향
- [ ] Dimensional Data Model and Labels / 라벨 조합으로 계열을 가르는 데이터 모델
- [ ] CNCF Graduated Project / 재단이 졸업 등급을 매긴 오픈소스 위치

### Core Use Cases

- [ ] Infrastructure Monitoring / 장비 자원 사용량을 계열로 쌓아 두는 용도
- [ ] Application Metrics and SLO / 서비스 목표 수치를 코드에서 내보내는 용도
- [ ] Kubernetes Monitoring / 사라지고 생기는 파드를 계속 찾아 재는 용도
- [ ] Alerting / 질의 결과가 조건에 걸릴 때 사람을 부르는 용도

### What Prometheus Is Not

- [ ] Not a Log Store / 원문 한 줄이 아니라 수치만 담는 한계
- [ ] Not a Tracing System / 요청 하나의 경로를 못 따라가는 한계

### Components

- [ ] Prometheus Server / 긁기와 저장과 질의를 한 프로세스에 담은 본체
- [ ] Exporters / 남의 소프트웨어 상태를 수치로 바꿔 내주는 프로세스
- [ ] Pushgateway / 짧게 살다 죽는 작업이 값을 맡겨 두는 중간 자리
- [ ] Alertmanager / 발화한 알림을 묶고 보낼 곳을 정하는 프로세스
- [ ] Client Libraries / 앱이 스스로 값을 내주게 만드는 언어별 구현

## 2. Getting Started

### Installation `택 1`

- [ ] Docker and Docker Compose / 설정 파일과 함께 컨테이너로 띄우는 방법 `추천`
- [ ] Binary Download / 단일 실행 파일을 내려받아 직접 띄우는 방법
- [ ] kube-prometheus-stack (Helm) / 서버와 규칙을 한 차트로 함께 올리는 방법

### First Run

- [ ] prometheus.yml Basic Structure / global과 scrape_configs로 나뉜 설정 뼈대
- [ ] Expression Browser / 내장 화면에서 질의를 쳐 계열을 확인하는 자리
- [ ] Targets / 발견된 대상의 마지막 긁기 성패를 보는 화면
- [ ] Runtime Flags and Reload / 기동 인자와 설정 재적용을 가르는 경계

## 3. Data Model

### Time Series Structure

- [ ] Metric Name / 무엇을 잰 값인지 가리키는 계열 이름
- [ ] Label Set / 계열에 붙은 키와 값 쌍의 묶음
- [ ] Sample / 시각 하나와 값 하나로 이뤄진 관측 한 점
- [ ] Time Series Identity / 이름과 라벨 조합이 계열을 가르는 규칙

### Metric Types

- [ ] Counter / 되돌아가지 않고 늘기만 하는 누적 수
- [ ] Gauge / 오르내리는 현재 값을 그대로 담는 형식
- [ ] Histogram / 값을 구간별 누적 수로 담아 분포를 재는 형식
- [ ] Summary / 대상이 미리 계산한 분위수를 그대로 내주는 형식
- [ ] Native Histogram / 구간을 자동으로 잡아 저장을 줄인 새 형식

### Naming Conventions

- [ ] Metric Naming Conventions / 접미사로 단위와 누적 여부를 드러내는 규약
- [ ] Base Units / 초와 바이트처럼 배수 없는 단위로 통일하는 규칙
- [ ] Label Cardinality Caution / 라벨 값 가짓수가 계열 수를 곱해 버리는 지점

---

# PART 2 · Data Collection

## 4. Scraping

### Scrape Behavior

- [ ] Pull Model / 대상이 보내지 않고 서버가 가져오는 방향
- [ ] /metrics Endpoint / 현재 값을 한 번에 텍스트로 내주는 경로
- [ ] Exposition Format and OpenMetrics / 한 줄에 계열과 값을 적는 텍스트 표기
- [ ] scrape_interval and scrape_timeout / 긁는 주기와 포기 시점을 정하는 설정
- [ ] Staleness Handling / 대상이 사라진 뒤 계열을 끊어 표시하는 처리

### scrape_config

- [ ] Job, Target, Instance / 설정 묶음과 주소와 개체로 이어지는 이름 층
- [ ] metrics_path and scheme / 긁어갈 경로와 http·https 선택
- [ ] honor_labels and honor_timestamps / 대상이 준 라벨과 시각을 그대로 둘지 정하는 설정
- [ ] Basic Auth and TLS Config / 긁는 쪽이 대상에 자신을 증명하는 설정
- [ ] sample_limit and label_limit / 한 대상이 밀어 넣을 계열 수의 상한

### Pushgateway `선택`

- [ ] Batch Job Metrics / 긁힐 때까지 살지 않는 작업의 값을 남기는 방법
- [ ] When Not to Use It / 상시 프로세스에 쓰면 옛 값이 고이는 이유

## 5. Service Discovery

- [ ] Static Config / 대상 주소를 설정 파일에 직접 적는 방식
- [ ] File-based SD / 바깥이 쓴 목록 파일을 다시 읽어 대상을 갱신하는 방식
- [ ] Kubernetes SD / API 서버에 물어 파드와 서비스를 대상으로 삼는 방식
- [ ] Cloud SD / 클라우드 인스턴스 목록을 조회해 대상을 채우는 방식
- [ ] Consul SD / 서비스 등록소에 올라온 항목을 대상으로 끌어오는 방식
- [ ] DNS SD / SRV와 A 레코드 조회로 대상 주소를 얻는 방식

## 6. Relabeling

- [ ] relabel_configs vs metric_relabel_configs / 긁기 전 대상과 긁은 뒤 계열을 가르는 자리
- [ ] __meta_ Meta Labels / 발견 단계에서만 붙었다 사라지는 임시 라벨
- [ ] Actions / 라벨을 바꾸거나 대상을 걸러 내는 동작 종류
- [ ] Target Filtering / 발견된 대상 중 실제로 긁을 것만 남기는 방법
- [ ] Dropping High-Cardinality Series / 라벨 값이 많은 계열을 저장 전에 버리는 방법

## 7. Exporters / Instrumentation

### Infrastructure Exporters

- [ ] node_exporter / 커널이 내주는 장비 자원 수치를 노출하는 프로세스
- [ ] cAdvisor / 컨테이너별 자원 사용량을 계열로 내주는 프로세스
- [ ] kube-state-metrics / 클러스터 객체의 선언 상태를 계열로 바꾸는 프로세스
- [ ] blackbox_exporter / 바깥에서 찔러 본 응답 성패를 계열로 내주는 프로세스
- [ ] snmp_exporter / 네트워크 장비 OID를 긁어 계열로 옮기는 프로세스

### Middleware Exporters

- [ ] mysqld_exporter and postgres_exporter / DB 상태 조회 결과를 계열로 내주는 프로세스
- [ ] redis_exporter / INFO 출력에서 메모리와 연결 수를 뽑는 프로세스
- [ ] JMX Exporter / 자바 MBean 값을 계열 이름으로 옮기는 규칙

### Direct Instrumentation

- [ ] Client Libraries / 계열 등록과 값 갱신을 코드에 심는 언어별 라이브러리
- [ ] Custom Metrics Design / 무엇을 세고 라벨을 어디까지 나눌지 정하는 설계
- [ ] RED Method / 요청 수와 오류 수와 지연으로 서비스를 보는 관점
- [ ] USE Method / 사용률과 포화와 오류로 자원을 보는 관점

---

# PART 3 · PromQL

## 8. PromQL Basics

### Selector

- [ ] Instant Vector Selector / 시각 하나에서 계열마다 값 한 점을 고르는 표현
- [ ] Range Vector Selector / 계열마다 지난 구간의 점 여럿을 묶는 표현
- [ ] Label Matchers / 라벨 값의 일치와 정규식으로 계열을 고르는 조건
- [ ] Offset Modifier and @ Modifier / 질의 기준 시각을 과거로 옮기는 지정

### Operators

- [ ] Arithmetic Operators / 짝지은 계열끼리 값을 더하고 나누는 연산
- [ ] Comparison Operators / 조건에 안 맞는 계열을 걸러 내는 비교 연산
- [ ] Logical Set Operators / 두 질의 결과를 계열 집합으로 합치고 빼는 연산
- [ ] Vector Matching / 양쪽 계열을 어떤 라벨로 짝지을지 정하는 규칙
- [ ] Many-to-one Matching / 한쪽 계열 하나에 여럿을 붙이는 짝짓기

## 9. PromQL Functions

- [ ] Rate Functions / 누적 수를 초당 증가량으로 바꾸는 함수
- [ ] Counter Handling / 재시작으로 0이 된 구간을 이어 붙이는 처리
- [ ] Aggregation Operators / 여러 계열을 하나로 접어 값을 모으는 연산
- [ ] Aggregation Modifiers / 접을 때 남기거나 버릴 라벨을 고르는 지정
- [ ] Histogram Quantile / 버킷 누적 수에서 분위수를 되짚어 추정하는 함수
- [ ] Over-time Functions / 구간 안의 점들을 계열별로 접는 함수
- [ ] Prediction / 기울기를 이어 앞으로의 값을 내다보는 함수
- [ ] Label Manipulation / 질의 결과의 라벨을 새로 만들거나 잇는 함수

## 10. Query Practice

- [ ] Subquery / 질의 결과를 다시 구간 벡터로 만들어 감싸는 문법
- [ ] Recording Rules / 무거운 질의를 미리 계산해 새 계열로 저장하는 규칙
- [ ] Rule Group and Evaluation Interval / 규칙을 순서대로 돌리는 묶음과 주기
- [ ] Diagnosing Expensive Query Patterns / 훑는 계열 수가 많아 느려진 질의를 찾는 방법
- [ ] Writing SLI Queries / 성공 비율과 지연 목표를 질의 한 줄로 적는 방법
- [ ] Error Budget Burn Rate / 남은 실패 허용치를 깎아 먹는 속도

---

# PART 4 · Alerting

## 11. Alerting Rules

- [ ] alert, expr, for / 이름과 조건과 유지 시간으로 이뤄진 규칙 세 줄
- [ ] Pending vs Firing / 조건이 유지 시간을 채워야 발화로 넘어가는 단계
- [ ] Labels and Annotations / 묶음 기준이 되는 라벨과 사람이 읽을 문구
- [ ] Go Template / 알림 문구에 값과 라벨을 끼워 넣는 문법
- [ ] Severity Design / 깨울 것과 아침에 볼 것을 가르는 등급 설계
- [ ] Multi-Window Multi-Burn-Rate Alert / 긴 창과 짧은 창을 겹쳐 오탐을 줄이는 구성

## 12. Alertmanager

### Routing

- [ ] Route Tree / 라벨 조건을 따라 내려가며 받는 곳을 정하는 트리
- [ ] Grouping / 같은 라벨의 알림을 한 통으로 묶어 보내는 설정
- [ ] repeat_interval / 해소되지 않은 알림을 다시 보내는 간격

### Inhibition

- [ ] Inhibition Rules / 상위 장애가 뜨면 하위 알림을 덮어 두는 규칙
- [ ] Silences / 정해진 기간 동안 특정 라벨의 알림을 막는 조치
- [ ] Mute Time Intervals / 요일과 시간대로 알림을 접어 두는 일정

### Receivers

- [ ] Receiver Types / 알림을 실어 보낼 바깥 통로의 종류
- [ ] Notification Templates / 통로마다 제목과 본문을 다시 짜는 틀
- [ ] High Availability Mode / 여러 대가 서로 알려 중복 발송을 막는 구성

---

# PART 5 · Operations and Scaling

## 13. Storage / TSDB

- [ ] TSDB Structure / 최근 값을 메모리에 두고 기록으로 지키는 구조
- [ ] Block Compaction / 두 시간짜리 조각을 큰 블록으로 합치는 작업
- [ ] Retention / 오래되거나 넘친 블록을 지우는 보존 한계
- [ ] Cardinality Diagnosis / 계열 수를 부풀린 라벨과 이름을 찾는 화면
- [ ] Remote Write and Remote Read / 바깥 저장소로 계열을 흘려보내고 되읽는 경로

## 14. Long-term Storage and Scaling `택 1`

- [ ] Federation / 상위 서버가 하위 서버의 접힌 계열만 긁어 오는 방식
- [ ] Thanos / 사이드카로 블록을 객체 저장소에 올려 잇는 방식 `추천`
- [ ] Cortex and Mimir / 쓰기와 질의를 나눠 맡는 다중 테넌트 구현
- [ ] VictoriaMetrics / 한 덩어리로 돌며 저장을 줄인 호환 구현

### Long-term Storage Concepts

- [ ] Object Storage Backend / 블록을 S3 같은 통에 얹어 보존을 늘리는 방식
- [ ] Downsampling / 오래된 구간을 성긴 간격으로 줄여 두는 처리
- [ ] Global Query View / 여러 서버의 계열을 한 질의로 합쳐 보는 층

## 15. Operations

### Performance

- [ ] Sizing / 계열 수와 보존 기간으로 자원을 어림하는 계산
- [ ] Scrape Load Distribution / 대상을 해시로 나눠 여러 대가 맡는 분할

### Reliability

- [ ] Prometheus HA Pair / 같은 대상을 둘이 나란히 긁어 공백을 없애는 구성
- [ ] Snapshot API and Backup / 블록을 잠깐 굳혀 복사해 두는 경로
- [ ] Self-Monitoring / 긁기 지연과 규칙 실패를 자기 계열로 보는 방법

### Security

- [ ] Web Config / 서버가 내주는 화면과 API에 자물쇠를 거는 설정

## 16. Kubernetes Integration

- [ ] Prometheus Operator / 설정 파일 대신 CRD로 서버를 굴리는 컨트롤러
- [ ] ServiceMonitor and PodMonitor / 긁을 대상을 클러스터 객체로 선언하는 리소스
- [ ] PrometheusRule CRD / 기록과 알림 규칙을 클러스터 객체로 두는 리소스
- [ ] Prometheus Adapter / 질의 결과를 오토스케일러가 읽게 넘기는 다리

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Kubernetes `software/skill-based/Infra-DevOps/kubernetes.md`
- 대시보드 시각화 `software/skill-based/Infra-DevOps/grafana.md`
- 계측 표준 `software/skill-based/Infra-DevOps/opentelemetry.md`
- SaaS 관측 대안 `software/skill-based/Infra-DevOps/datadog.md`, `new-relic.md`
- 확장 설계 `software/skill-based/CS-Theory/system-design.md`
