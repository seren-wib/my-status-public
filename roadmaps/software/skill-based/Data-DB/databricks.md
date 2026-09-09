# Databricks `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Databricks

## 1. What is Databricks?

### Overview of Databricks / What is it?

- [ ] Lakehouse Platform / 파일 스토리지에 창고 기능을 얹은 구조
- [ ] Managed Spark / 클러스터 운영을 대신 맡아주는 방식
- [ ] Data Lake + Warehouse Unification / 저장과 정형 조회를 한 계층으로 합친 구조
- [ ] Control Plane and Data Plane / 관리 기능과 실제 데이터 처리를 분리한 구조

### Core Use Cases

- [ ] Large-scale ETL / 대용량 데이터를 정제·적재하는 배치 작업
- [ ] SQL Analytics and BI / 쿼리와 대시보드로 데이터를 들여다보는 용도
- [ ] ML / 모델 학습부터 서빙까지 한 플랫폼에서 잇는 용도
- [ ] Streaming Pipeline / 실시간 데이터를 끊김 없이 흘려 처리하는 방식

### Comparison

- [ ] Lakehouse vs Data Warehouse vs Data Lake / 구조화 강제·비용·유연성이 갈리는 지점
- [ ] Databricks vs Snowflake / 클러스터를 직접 굴리는지 완전관리형인지의 차이
- [ ] Databricks vs Self-managed Spark / 클러스터 구축·운영 부담을 넘기는지의 차이
- [ ] Cloud Provider Differences / AWS·Azure·GCP마다 배포 방식이 달라지는 부분

## 2. Workspace Basics

- [ ] Account / 계정 아래 여러 워크스페이스를 두는 계층 구조
- [ ] Workspace UI Structure / 노트북·클러스터·데이터를 한 화면에서 오가는 구조
- [ ] Git Folder and Repos / 노트북을 깃 저장소와 동기화하는 폴더
- [ ] DBFS vs Volume / 레거시 마운트 저장소와 카탈로그 관리 저장소의 차이
- [ ] Databricks CLI / 터미널에서 워크스페이스를 조작하는 도구
- [ ] Personal Access Token and OAuth / API 인증에 쓰는 두 가지 방식

## 3. Compute

### Cluster Types

- [ ] All-purpose Cluster / 탐색 작업용으로 계속 켜 둔 채 쓰는 클러스터
- [ ] Job Cluster / 잡 시작할 때 떴다 끝나면 바로 꺼지는 클러스터 `추천`
- [ ] SQL Warehouse / SQL 쿼리 실행에 맞춰 최적화된 컴퓨트
- [ ] Serverless Compute / 클러스터 크기를 안 골라도 바로 뜨는 컴퓨트

### Configuration

- [ ] Databricks Runtime / DBR·ML Runtime·Photon 중 고르는 실행 버전
- [ ] Node Type / Driver 한 대와 Worker 여러 대의 역할 차이
- [ ] Autoscaling / 부하에 따라 워커 수를 자동으로 늘리고 줄이는 기능
- [ ] Spot and Preemptible Instance / 값싼 대신 언제든 회수될 수 있는 인스턴스
- [ ] Auto Termination / 일정 시간 idle이면 클러스터를 자동으로 끄는 설정
- [ ] Cluster Policy / 만들 수 있는 클러스터 종류·크기를 제한하는 규칙
- [ ] Access Mode / Single User·Shared 중 접근 범위를 고르는 설정
- [ ] Init Script / 클러스터 뜰 때 라이브러리를 자동 설치하는 스크립트

---

# PART 2 · Data Layer

## 4. Delta Lake

### Basics

- [ ] Parquet + Transaction Log / 파일 포맷에 변경 이력을 더한 구조
- [ ] _delta_log / 테이블 변경 내역을 커밋 단위로 쌓아두는 폴더
- [ ] ACID Transaction / 파일 위에서도 원자성·일관성을 보장하는 트랜잭션
- [ ] Schema Enforcement and Evolution / 어긋난 쓰기를 막을지 받아들일지 정하는 기능

### Operators

- [ ] MERGE INTO / 있으면 갱신 없으면 삽입을 한 문장으로 처리하는 명령
- [ ] UPDATE and DELETE / 조건에 맞는 행만 골라 고치거나 지우는 명령
- [ ] Time Travel / VERSION AS OF로 과거 버전 데이터를 조회하는 기능
- [ ] RESTORE / 특정 버전으로 테이블 상태를 되돌리는 명령
- [ ] Change Data Feed / 행 단위 변경 내역을 구독해 읽는 기능

### Optimization

- [ ] OPTIMIZE / 작은 파일들을 큰 파일로 합쳐 읽기 속도를 높이는 명령
- [ ] Z-Ordering / 여러 컬럼 순으로 정렬해 스캔 범위를 줄이는 기법
- [ ] Liquid Clustering / 파티션 없이 클러스터링 키를 자동으로 다시 잡는 방식
- [ ] VACUUM / 보관 기간 지난 지워진 파일을 실제로 삭제하는 명령
- [ ] Deletion Vector / 파일을 다시 안 쓰고 지워진 행만 표시하는 방식
- [ ] Partitioning Criteria / 폴더로 나눌 컬럼을 골라 스캔 범위를 줄이는 기준

## 5. Unity Catalog

- [ ] Catalog, Schema, Table 3-Level Namespace / 카탈로그·스키마·테이블로 이어지는 3단 체계
- [ ] Metastore / 카탈로그 전체의 메타데이터를 관리하는 저장소
- [ ] Managed vs External Table / 파일 삭제까지 맡기는지 위치만 등록하는지의 차이
- [ ] External Location and Storage Credential / 외부 저장 경로와 인증 정보를 등록하는 객체
- [ ] Volume / 정형 테이블 밖의 파일을 카탈로그로 관리하는 객체
- [ ] Privilege Model / GRANT문으로 객체별 권한을 내려주는 체계
- [ ] Lineage Tracking / 데이터가 거쳐온 테이블·잡을 자동으로 추적하는 기능
- [ ] Delta Sharing / 복제 없이 다른 조직과 테이블을 공유하는 프로토콜
- [ ] Hive Metastore Migration / 옛 메타스토어에서 Unity Catalog로 옮기는 작업

## 6. Data Ingestion

- [ ] Medallion Architecture / Bronze·Silver·Gold로 점점 정제해 가는 설계
- [ ] Auto Loader / cloudFiles로 새로 들어온 파일만 골라 자동으로 읽는 기능
- [ ] Schema Inference / 들어온 파일에서 스키마를 읽고 바뀌면 반영하는 옵션
- [ ] COPY INTO / 이미 처리한 파일은 건너뛰고 멱등하게 적재하는 명령
- [ ] Batch File Load / Parquet·CSV·JSON 등을 한 번에 통째로 읽는 방식
- [ ] Lakehouse Federation / JDBC로 외부 DB를 복제 없이 그대로 조회하는 기능
- [ ] Kafka and Event Hub / 메시지 큐에서 스트림 데이터를 그대로 받아오는 소스
- [ ] Partner Connect / 외부 도구를 워크스페이스에 미리 연결해 두는 갤러리 `선택`

---

# PART 3 · Development

## 7. Development Environment

- [ ] Notebook / Cell 단위로 실행하며 Magic Command로 언어를 바꾸는 문서
- [ ] Multi-language Mixing / %python·%sql 등으로 한 노트북에서 언어를 섞어 쓰는 방법
- [ ] Widget / 노트북 실행 시 값을 입력받는 파라미터 UI
- [ ] dbutils / fs·secrets·notebook 등 노트북 안에서 쓰는 유틸리티 모음
- [ ] %run vs dbutils.notebook.run / 변수 공유 여부로 갈리는 노트북 호출 방식
- [ ] Databricks Connect / 로컬 IDE 코드를 원격 클러스터로 보내 실행하는 도구
- [ ] Asset Bundles (DAB) / 노트북·잡·인프라 설정을 코드로 묶어 배포하는 도구

## 8. Spark on Databricks

- [ ] PySpark DataFrame API / 노트북에서 파이썬으로 스파크 코드를 짜는 인터페이스
- [ ] Spark SQL / 노트북·SQL 에디터에서 그대로 쓰는 SQL 인터페이스
- [ ] Photon Engine / 코드는 그대로 두고 실행 엔진만 바꿔 속도를 올리는 옵션
- [ ] Adaptive Query Execution / 실행 중 통계를 보고 쿼리 계획을 다시 짜는 옵션
- [ ] Spark UI and Query Profile / 잡 실행 과정을 화면으로 들여다보는 도구
- [ ] Data Skew / 쏠린 데이터를 작은 테이블에 복제해 우회하는 튜닝
- [ ] Structured Streaming on Delta / Delta 테이블을 소스·싱크로 바로 쓰는 스트리밍 방식

## 9. SQL and BI

- [ ] SQL Editor / 워크스페이스 안에서 SQL을 바로 짜고 실행하는 화면
- [ ] Query History and Query Profile / 지난 쿼리 기록과 단계별 소요 시간을 보는 화면
- [ ] Dashboard / 쿼리 결과를 카드로 모아 시각화하는 화면
- [ ] Alert / 쿼리 결과가 조건을 넘으면 알려주는 기능
- [ ] Materialized View and Streaming Table / 결과를 미리 계산해 저장해 두는 테이블
- [ ] BI Tool Integration / Power BI·Tableau 등 외부 BI 툴이 붙는 연결
- [ ] SQL Warehouse Sizing / Serverless와 Pro 중 비용을 놓고 고르는 크기

## 10. Workflows

- [ ] Job / 여러 Task를 묶어 실행 순서를 정하는 단위
- [ ] Task Type / Notebook·Python Wheel·JAR 등 실행할 작업의 형식
- [ ] Task Dependency / 앞 Task 성공 여부로 다음 실행을 가르는 조건
- [ ] Trigger / 정해진 시각이나 파일 도착을 실행 신호로 쓰는 설정
- [ ] Retry and Timeout / 실패하거나 오래 걸리면 재시도·중단하는 설정
- [ ] Job Parameter / 실행할 때마다 값을 바꿔 넣는 잡 변수
- [ ] Notification / 잡 성공·실패를 이메일·웹훅으로 알리는 설정
- [ ] External Orchestrator Integration / 외부 도구에서 API로 잡을 실행시키는 연동

---

# PART 4 · Pipelines and ML

## 11. Delta Live Tables

- [ ] Declarative Pipeline Concept / 실행 순서 대신 원하는 결과만 선언하는 방식
- [ ] Streaming Table vs Materialized View / 증분 처리인지 전체 재계산인지의 차이
- [ ] Expectations / 행 단위 품질 규칙을 걸어 어긋나면 걸러내는 기능
- [ ] Pipeline Mode / Triggered와 Continuous 중 계속 돌릴지 정하는 모드
- [ ] Development vs Production Mode / 클러스터를 재사용할지 매번 새로 띄울지의 차이
- [ ] Choosing Between DLT and Workflows / 선언형 파이프라인과 범용 오케스트레이션 중 고르는 기준

## 12. Machine Learning `선택`

- [ ] MLflow Tracking / 실험과 실행 단위로 모델 학습 결과를 기록하는 도구
- [ ] Model Registry / Unity Catalog 안에서 모델 버전을 관리하는 저장소
- [ ] Feature Store / 학습·서빙에서 같은 피처를 공유해 쓰는 저장소
- [ ] AutoML / 데이터만 넣으면 여러 모델을 자동으로 시도해보는 기능
- [ ] Model Serving Endpoint / 등록한 모델을 API로 바로 호출하게 띄우는 엔드포인트
- [ ] Vector Search / 임베딩 유사도 검색으로 RAG에 쓰는 인덱스
- [ ] Mosaic AI / Foundation Model API로 모델을 서빙·파인튜닝하는 브랜드

---

# PART 5 · Operations

## 13. Governance and Security

- [ ] Identity / User·Group·Service Principal 단위로 권한을 매핑하는 개념
- [ ] SCIM Provisioning / 외부 ID 공급자와 사용자·그룹을 자동으로 동기화하는 기능
- [ ] Secret Scope / 비밀번호·토큰을 코드에 안 박고 안전하게 보관하는 공간
- [ ] Row Filter and Column Mask / 같은 테이블도 사용자별로 다르게 보여주는 기능
- [ ] Audit Log / 누가 언제 무엇을 했는지 남기는 감사 기록
- [ ] Network Security / Private Link·IP 허용 목록으로 접근 경로를 좁히는 설정

## 14. Cost Management

- [ ] DBU Billing Model / 컴퓨트 사용량을 DBU 단위로 환산해 과금하는 방식
- [ ] Compute Type Price Differences / 클러스터 종류마다 DBU 단가가 갈리는 부분
- [ ] Tag / 리소스에 라벨을 붙여 비용을 팀·프로젝트별로 나누는 방법
- [ ] System Table / billing·access 등 사용 내역을 SQL로 조회하는 시스템 테이블
- [ ] Budget and Alert / 예산을 정해두고 넘으면 알려주는 기능
- [ ] Cost Saving Patterns / Job Cluster·Auto Termination·Spot 등으로 비용을 줄이는 조합

## 15. CI/CD and Operations

- [ ] Git Integration / 노트북·코드를 깃 저장소와 연동해 버전 관리하는 기능
- [ ] Asset Bundles Deployment / 번들로 정의한 리소스를 환경별로 배포하는 절차
- [ ] Terraform Provider / Terraform으로 워크스페이스 리소스를 코드로 관리하는 도구
- [ ] REST API and SDK / 워크스페이스 기능을 코드로 호출하는 인터페이스
- [ ] Environment Separation / dev·staging·prod로 워크스페이스를 나누는 방식
- [ ] Testing / pytest·nutter로 노트북·잡 코드를 테스트하는 방법
- [ ] Lakehouse Monitoring / 테이블 데이터 품질과 드리프트를 자동으로 감시하는 기능

---

# 이 로드맵 밖

- 데이터 파이프라인 전반 `software/role-based/data-engineer.md`
- Spark 엔진 자체 `software/skill-based/Data-DB/spark.md`
- 변환 레이어 `software/skill-based/Data-DB/dbt.md`
- 경쟁 웨어하우스 `software/skill-based/Data-DB/snowflake.md`, `bigquery.md`
- 모델 운영 `software/role-based/mlops.md`
- 클라우드 인프라 `software/skill-based/Infra-DevOps/aws.md`, `terraform.md`
