# Google BigQuery `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to BigQuery

## 1. What is BigQuery?

### Overview of BigQuery / What is it?

- [ ] Serverless Cloud Data Warehouse / 띄워 둘 서버 없이 쓰는 분석 창고
- [ ] Columnar Analytical Store / 열 단위로 저장해 필요한 컬럼만 읽는 구조
- [ ] Separation of Storage and Compute / 저장과 연산을 따로 늘리는 구조
- [ ] Google Cloud Native Service / GCP 프로젝트에 바로 딸린 관리형 서비스

### Core Use Cases

- [ ] Large-scale Analytics and BI / 대용량 집계를 대시보드에 바로 연결하는 용도
- [ ] Log and Event Analytics / 로그·이벤트를 쌓아두고 바로 조회하는 용도
- [ ] Data Lake Query Engine / GCS에 있는 파일을 테이블처럼 조회하는 용도
- [ ] ML on Warehouse Data / 창고 안 데이터에 SQL로 모델을 적용하는 용도

### BigQuery vs Other Platforms

- [ ] BigQuery vs Snowflake / 컴퓨트 분리 방식을 Redshift까지 넣어 비교
- [ ] Serverless vs Provisioned Cluster Model / 서버 대기 없는 방식과 클러스터 예약 방식의 차이
- [ ] When to choose BigQuery? / 스캔량 과금이 유리해지는 워크로드 조건

## 2. Getting Started

### Access Methods

- [ ] Cloud Console / GCP 콘솔 안에서 쿼리 짜는 BigQuery Studio 화면 `추천`
- [ ] bq CLI / 터미널에서 쓰는 명령줄 도구
- [ ] Client Libraries / Python·Java 등 언어별로 붙이는 라이브러리
- [ ] BigQuery API / REST 호출로 직접 붙이는 방법

### Initial Configuration

- [ ] GCP Project Setup / 인스턴스 없이 프로젝트에 데이터셋부터 만드는 절차
- [ ] Sandbox and Free Tier Limits / 가입만으로 쓰는 무료 스캔량 한도
- [ ] Public Datasets / 구글이 미리 올려둔 공개 테이블 모음
- [ ] Location and Region Selection / 데이터셋을 만들 때 고정하는 저장 리전

---

# PART 2 · Architecture and Data Model

## 3. Architecture

- [ ] Dremel Query Engine / 쿼리를 트리로 나눠 병렬로 흩어 돌리는 엔진
- [ ] Colossus Distributed Storage / 컴퓨트와 분리된 구글 내부 분산 저장소
- [ ] Jupiter Network / 스토리지와 컴퓨트를 빠르게 잇는 데이터센터망
- [ ] Borg Compute Orchestration / 쿼리에 컴퓨트 자원을 배분하는 내부 스케줄러
- [ ] Slot / 쿼리가 나눠 쓰는 연산 단위
- [ ] Query Stages and Shuffle / 쿼리를 단계로 나누고 중간 결과를 재분배하는 과정

## 4. Resource Model

- [ ] Project, Dataset, Table Hierarchy / 프로젝트-데이터셋-테이블로 이어지는 계층
- [ ] Dataset Location and Constraints / 데이터셋에 고정되는 리전과 그로 인한 제약
- [ ] Table Naming and Qualification / 프로젝트.데이터셋.테이블로 이름을 완전히 쓰는 규칙
- [ ] Labels / 리소스에 붙여 비용·용도를 구분하는 태그
- [ ] Quotas and Limits / 프로젝트별로 걸리는 요청·스캔 한도
- [ ] INFORMATION_SCHEMA / 메타데이터를 SQL로 조회하는 시스템 뷰

## 5. Storage

- [ ] Capacitor Columnar Format / 구글 내부 열 지향 저장 포맷
- [ ] Logical vs Physical Storage Billing / 압축 전후 크기 중 무엇으로 과금할지 고르는 방식
- [ ] Active vs Long-term Storage / 90일 안 바뀐 테이블에 싸게 매기는 보관 등급
- [ ] Table Snapshots and Clones / 특정 시점을 읽기전용·쓰기가능으로 복제해두는 기능
- [ ] Time Travel Window / 최근 며칠간 과거 상태를 조회할 수 있는 기간
- [ ] Fail-safe Period / 타임트래블 지난 뒤 구글만 복구 가능한 유예 기간

## 6. GoogleSQL Specifics

### BigQuery-Specific Syntax

- [ ] Standard SQL vs Legacy SQL / 표준 문법과 구버전 BigQuery 문법의 차이
- [ ] Table Wildcards / _TABLE_SUFFIX로 여러 테이블을 한 번에 조회하는 표기
- [ ] Table Decorators and FOR SYSTEM_TIME AS OF / 과거 시점 테이블 상태를 지정해 조회하는 구문
- [ ] Scripting / DECLARE·SET·BEGIN END로 SQL에 절차를 넣는 기능
- [ ] Multi-statement Transactions / 여러 DML문을 하나의 원자 단위로 묶는 기능
- [ ] Parameterized Queries / 값을 자리표시자로 넘겨 재사용하는 쿼리 작성법

### Data Types

- [ ] BigQuery Types / STRUCT·ARRAY·JSON·GEOGRAPHY 같은 전용 타입
- [ ] Numeric Types / 정밀도가 다른 고정소수점 숫자 타입
- [ ] Timestamp vs Datetime Semantics / 시간대를 포함하는지로 갈리는 두 시간 타입

### Extended Functions

- [ ] Approximate Aggregation / 정확도를 조금 버리고 스캔을 줄이는 집계 함수
- [ ] Analytic Function Pitfalls at Scale / 대용량에서 윈도우 함수가 스캔·셔플을 키우는 함정
- [ ] Geospatial Functions / 위경도 데이터를 다루는 함수 모음 `선택`

## 7. Nested and Repeated Data

- [ ] STRUCT / 레거시 이름이 RECORD인 중첩 필드 타입
- [ ] ARRAY / REPEATED 모드로 한 컬럼에 값을 여러 개 담는 타입
- [ ] UNNEST and Correlated Join / 중첩 배열을 행으로 펼쳐 바깥 쿼리와 잇는 구문
- [ ] Denormalization over Star Schema / 조인 대신 중첩 필드로 미리 뭉쳐두는 설계
- [ ] JSON Type vs String Parsing / JSON을 타입으로 둘지 문자열로 파싱할지의 차이

## 8. Table Types

- [ ] Native Table / BigQuery 저장소 안에 데이터를 직접 담는 테이블
- [ ] External Table / GCS·Drive·Bigtable 데이터를 옮기지 않고 참조하는 테이블
- [ ] BigLake Table / 외부 데이터에 세밀한 접근 제어를 얹은 테이블
- [ ] Object Table / GCS 비정형 파일을 메타데이터로 참조하는 테이블 `선택`
- [ ] Views / 원본 테이블 접근권 없이 결과만 공개하는 인가된 뷰
- [ ] Materialized Views / 쿼리 결과를 미리 계산해두고 변경분만 갱신하는 뷰
- [ ] Search Index / 텍스트 검색을 빠르게 하려고 미리 만드는 색인 `선택`

---

# PART 3 · Data Ingestion and Pipelines

## 9. Data Loading

### Batch Ingestion

- [ ] Load Job / GCS 파일을 통째로 테이블에 적재하는 작업
- [ ] Supported Formats / CSV·JSON·Avro·Parquet·ORC 등 적재 가능 형식
- [ ] Schema Auto-detection / 파일 내용을 보고 컬럼 스키마를 자동 추론하는 기능
- [ ] Write Disposition / 적재할 때 기존 데이터를 지울지 이어붙일지 정하는 옵션
- [ ] Schema Evolution / 컬럼 추가·제약 완화로 스키마를 점진적으로 바꾸는 방법

### Managed Transfers

- [ ] Data Transfer Service / 외부 SaaS 데이터를 주기적으로 자동 적재하는 서비스
- [ ] Federated Query / Cloud SQL·Spanner를 옮기지 않고 조회하는 쿼리

## 10. Streaming and CDC

- [ ] Storage Write API / 스트리밍 삽입을 대체하는 고성능 쓰기 API `추천`
- [ ] Legacy streamingInsert / 행 단위로 바로 삽입하던 구버전 스트리밍 방식
- [ ] Streaming Buffer Behavior / 스트리밍으로 들어온 데이터가 잠시 머무는 버퍼 동작
- [ ] Exactly-once Semantics / 같은 레코드가 중복 적재되지 않도록 보장하는 방식
- [ ] Datastream / 원본 DB 변경분을 실시간으로 복제해오는 CDC 서비스
- [ ] Change Data Capture Tables / _CHANGE_TYPE 컬럼으로 삽입·수정·삭제를 구분하는 테이블

## 11. Transformation and Scheduling

- [ ] Scheduled Queries / 저장한 쿼리를 정해진 주기로 자동 실행하는 기능
- [ ] Stored Procedures and Table Functions / 절차를 저장해 재호출하거나 결과를 테이블로 반환하는 기능
- [ ] User-Defined Functions / SQL이나 JavaScript로 직접 만드는 함수
- [ ] Remote Functions / Cloud Run 코드를 SQL에서 호출하는 함수
- [ ] Dataform / SQL 변환 파이프라인을 버전 관리로 개발하는 도구 `추천`
- [ ] dbt on BigQuery / dbt로 BigQuery 위에서 SQL 변환을 관리하는 방식
- [ ] Dataflow / Apache Beam 파이프라인으로 변환 후 적재하는 연동

---

# PART 4 · Performance and Cost

## 12. Query Performance

### Data Layout

- [ ] Partitioned Tables / 시간·적재시각·정수 범위로 나눠 스캔을 줄이는 테이블
- [ ] Partition Pruning / 필터에 안 걸리는 파티션은 아예 안 읽게 막는 기능
- [ ] Clustered Tables / 지정한 컬럼 순서로 정렬해 읽을 블록을 줄이는 테이블
- [ ] Partitioning vs Clustering Choice / 날짜로 자를지 컬럼 정렬로 좁힐지 고르는 기준

### Execution Analysis

- [ ] Query Execution Plan / 쿼리가 단계별로 어떻게 실행됐는지 보여주는 계획
- [ ] Slot Utilization and Contention / 쿼리끼리 슬롯을 나눠 쓰며 생기는 경합 정도
- [ ] Data Skew and Shuffle Spill / 한쪽에 쏠린 데이터가 셔플 중 디스크로 넘치는 현상
- [ ] Join Strategies / 작은 테이블을 뿌리거나 해시로 맞춰 조인하는 방식

### Tuning Techniques

- [ ] Avoiding SELECT * / 필요한 컬럼만 골라 읽는 바이트를 줄이는 습관
- [ ] Filter Pushdown Awareness / 필터가 스캔 전에 걸리도록 쿼리를 짜는 감각
- [ ] Materialized View Rewrite / 쿼리를 자동으로 뷰 결과로 바꿔 스캔을 줄이는 최적화
- [ ] BI Engine Acceleration / 자주 쓰는 데이터를 메모리에 올려 대시보드를 가속하는 기능
- [ ] Query Result Cache / 동일한 쿼리 결과를 재사용해 스캔을 건너뛰는 캐시

## 13. Pricing and Cost Control

### Pricing Models `택 1`

- [ ] On-demand / 읽은 바이트 양만큼 매기는 기본 과금 방식 `추천`
- [ ] Capacity Pricing / 슬롯을 미리 예약해 정액으로 매기는 과금 방식

### Cost Management

- [ ] Reservations / 예약한 슬롯을 프로젝트에 배정하고 자동으로 늘리는 설정
- [ ] Dry Run / 실행 없이 읽을 바이트 양을 미리 계산하는 기능
- [ ] Custom Cost Controls / 쿼리당 과금 바이트 상한과 할당량을 거는 설정
- [ ] Storage Cost Optimization / 파티션에 만료 기간을 걸어 저장 비용을 줄이는 방법
- [ ] Cost Attribution / 라벨과 작업 기록으로 비용을 팀·용도별로 나누는 방법

---

# PART 5 · Operations and Extensions

## 14. Security and IAM

- [ ] IAM Roles / 미리 정의되거나 직접 만든 권한 묶음
- [ ] Resource-level Access / 데이터셋·테이블·컬럼 단위로 나눠 거는 접근 권한
- [ ] Column-level Security / 정책 태그로 특정 컬럼만 숨기거나 막는 보안
- [ ] Row-level Security / 조건에 맞는 행만 보이게 제한하는 보안
- [ ] Data Masking / 민감한 값을 조회 시 가리거나 바꿔 보여주는 기능
- [ ] Encryption / 고객이 직접 관리하는 키로 암호화하는 옵션
- [ ] VPC Service Controls / 네트워크 경계 밖으로 데이터가 못 나가게 막는 설정

## 15. Governance and Monitoring

- [ ] Dataplex / 데이터 자산을 검색·분류해두는 카탈로그
- [ ] Data Lineage / 데이터가 어느 테이블·작업을 거쳐왔는지 추적하는 기록
- [ ] Data Quality Checks / 정해진 규칙으로 데이터 이상을 자동 점검하는 기능
- [ ] Audit Logs / 누가 무엇을 조회·변경했는지 남는 로그
- [ ] Job Monitoring / 프로젝트 단위로 실행된 작업 이력을 조회하는 뷰
- [ ] Cloud Monitoring Metrics and Alerts / 슬롯 사용량 같은 지표를 보고 알림을 거는 기능
- [ ] Analytics Hub / 테이블을 복사 없이 다른 프로젝트와 공유하는 기능

## 16. Analytics Extensions

- [ ] BigQuery ML / CREATE MODEL 구문으로 SQL 안에서 모델을 학습하는 기능
- [ ] Model Types / 선형·부스티드 트리·K-means 등 지원 모델 종류
- [ ] Model Evaluation and Prediction / 학습한 모델 성능을 재고 새 데이터에 적용하는 절차
- [ ] Vertex AI Integration / BigQuery 데이터를 Vertex AI 모델과 바로 잇는 연동
- [ ] Vector Search and Embeddings / 임베딩을 저장해 유사도로 찾는 기능 `선택`
- [ ] BigQuery DataFrames / Pandas 문법으로 짜면 BigQuery 쿼리로 바뀌는 API
- [ ] Looker Studio Connection / BigQuery 데이터를 Looker Studio에 바로 연결하는 기능

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- 데이터 파이프라인 · 웨어하우스 모델링 `software/role-based/data-engineer.md`
- Snowflake `software/skill-based/Data-DB/snowflake.md`
- 데이터 분석 `software/role-based/data-analyst.md`
- 머신러닝 전반 `software/role-based/machine-learning.md`
- 스트리밍 수집 `software/skill-based/Data-DB/kafka.md`
