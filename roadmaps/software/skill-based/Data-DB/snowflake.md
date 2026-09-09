# Snowflake `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Snowflake

## 1. What is Snowflake?

### Overview of Snowflake / What is it?

- [ ] Cloud Data Warehouse / 서버 없이 클라우드가 통째로 돌리는 창고형 DB
- [ ] SaaS / 패치·튜닝 없이 계정만 만들면 되는 서비스
- [ ] Separation of Storage and Compute / 데이터는 한 곳에 두고 계산기만 따로 켜는 구조
- [ ] Multi-cloud Deployment / AWS·Azure·GCP 중 계정 리전을 고르는 일

### Core Use Cases

- [ ] Analytics and BI Backend / 대시보드 쿼리를 받아주는 뒷단
- [ ] Data Lake / 외부 파일을 옮기지 않고 그대로 읽는 용도
- [ ] Data Sharing and Marketplace / 복사 없이 남의 계정에 데이터를 공개하는 장터
- [ ] Data Application Backend / 앱이 직접 찔러 쓰는 데이터 뒷단

### Snowflake vs Other Platforms

- [ ] Snowflake vs BigQuery / BigQuery·Redshift와 웨어하우스 제어 방식으로 갈리는 차이
- [ ] Snowflake vs On-premises Data Warehouse / 하드웨어를 직접 사서 안 돌리는 차이
- [ ] When to choose Snowflake? / 계산 부하가 들쭉날쭉할 때 고르는 이유

## 2. Getting Started

### Access Methods

- [ ] Snowsight Web UI / 웨어하우스를 고르고 쿼리하는 웹 콘솔 `추천`
- [ ] SnowSQL CLI / 터미널에서 웨어하우스에 붙어 쿼리하는 도구
- [ ] Drivers and Connectors / JDBC·ODBC·Python으로 외부 앱을 붙이는 길
- [ ] Snowflake REST API / HTTP 호출로 SQL을 실행하는 방법

### Account Basics

- [ ] Account Identifier / 리전과 클라우드까지 박힌 계정 주소
- [ ] Editions / 보안·기능 수준별로 나뉜 요금 등급
- [ ] Trial Account Setup / 카드 없이 30일 써보는 계정
- [ ] Session Context / 쿼리 전에 역할·웨어하우스·DB·스키마부터 고르는 일

---

# PART 2 · Architecture

## 3. Multi-Cluster Shared Data Architecture

- [ ] Three Layers / 저장·계산·관리를 따로 쪼갠 세 겹
- [ ] Cloud Services Layer / 메타데이터·최적화·보안을 맡는 관리 계층
- [ ] Query Lifecycle / 쿼리가 파싱부터 결과까지 거치는 단계
- [ ] Result Cache / 같은 쿼리를 웨어하우스 없이 되돌려주는 캐시
- [ ] Metadata Cache / 통계만으로 웨어하우스 없이 답하는 캐시
- [ ] Warehouse Local Disk Cache / 켜진 웨어하우스가 읽은 조각을 남겨두는 캐시

## 4. Virtual Warehouses

### Sizing and Scaling

- [ ] Warehouse Sizes / XS부터 6XL까지 고르는 컴퓨팅 크기
- [ ] Scale Up vs Scale Out / 크기를 키울지 클러스터를 늘릴지의 선택
- [ ] Multi-cluster Warehouse / 접속이 몰릴 때 클러스터를 더 켜는 설정
- [ ] Scaling Policy / 클러스터를 빨리 늘릴지 아껴 늘릴지 정하는 정책

### Operational Configuration

- [ ] Auto-suspend and Auto-resume / 안 쓰면 꺼지고 쿼리 오면 켜지는 설정
- [ ] Warehouse per Workload Pattern / 작업별로 웨어하우스를 따로 두는 방식
- [ ] Query Queuing and Concurrency / 웨어하우스가 다 차면 쿼리가 줄 서는 일
- [ ] Statement Timeout Parameters / 오래 도는 쿼리를 강제로 끊는 시간 설정

## 5. Storage and Micro-partitions

- [ ] Micro-partition Structure / 데이터를 자동으로 잘게 쪼개 저장하는 단위
- [ ] Columnar Storage / 열 단위로 저장해 압축률을 높이는 방식
- [ ] Partition Metadata / 조각마다 최소·최대값을 미리 적어두는 통계
- [ ] Partition Pruning / 조건에 안 맞는 조각을 아예 안 읽는 최적화
- [ ] Clustering Depth / 값이 얼마나 여러 조각에 흩어졌는지 나타내는 지표
- [ ] Immutable Files / 수정 대신 새 조각을 통째로 쓰는 방식

## 6. Object Model

### Object Hierarchy

- [ ] Account, Database, Schema, Table / 계정 아래로 담기는 대상이 좁아지는 계층
- [ ] Fully Qualified Names / DB.스키마.테이블로 정확히 짚는 이름
- [ ] Table Types / 타임트래블·페일세이프 보관 기간이 다른 테이블 종류
- [ ] Views / 정의만 감추는 뷰와 결과를 미리 저장해두는 뷰

### Time Travel

- [ ] Time Travel / 과거 시점 데이터를 그대로 되돌려 보는 기능
- [ ] Data Retention Period / 타임트래블로 되돌릴 수 있는 보관 일수
- [ ] UNDROP / 지운 객체를 보관 기간 안에 되살리는 명령
- [ ] Fail-safe / 타임트래블이 끝난 뒤 스노우플레이크만 복구 가능한 기간
- [ ] Zero-copy Cloning / 조각을 복사 안 하고 포인터만 떠서 만드는 사본

---

# PART 3 · Data Ingestion and Transformation

## 7. Data Loading

### Stage

- [ ] Stage Types / 파일을 어디에 임시로 두는지에 따른 종류
- [ ] PUT and GET Commands / 로컬 파일을 스테이지에 올리고 내리는 명령
- [ ] External Stage / 클라우드 버킷을 자격 증명 없이 붙이는 저장 위치

### COPY INTO

- [ ] File Format Objects / CSV·JSON·Parquet·Avro 읽는 규칙을 저장한 객체
- [ ] COPY Options / 에러 무시·원본 삭제 같은 적재 규칙 옵션
- [ ] Load Metadata and Idempotency / 같은 파일을 두 번 넣어도 중복 안 되는 이유
- [ ] File Sizing Best Practice / 적재 파일을 100~250MB로 쪼개는 요령
- [ ] Load Validation / 실제로 넣기 전에 오류만 미리 확인하는 기능

### Unloading

- [ ] COPY INTO location / 테이블 데이터를 파일로 다시 뽑아내는 명령

## 8. Continuous Ingestion

- [ ] Snowpipe / 새 파일이 오면 자동으로 끌어와 적재하는 서비스
- [ ] Cloud Event Notification Setup / 버킷에 파일이 생겼다고 알려주는 연결
- [ ] Snowpipe Streaming / 파일 없이 행 단위로 바로 밀어 넣는 방식
- [ ] Pipe Monitoring / 파이프가 언제 뭘 얼마나 넣었는지 보는 기록
- [ ] Batch vs Streaming Cost Tradeoff / 모아 넣을지 바로 넣을지의 비용 저울질

## 9. Semi-Structured Data

- [ ] VARIANT, OBJECT, ARRAY Types / 스키마 없이 반정형 데이터를 담는 타입
- [ ] Path Notation and Casting / 콜론으로 중첩값을 짚어 타입을 바꾸는 문법
- [ ] FLATTEN / LATERAL FLATTEN으로 중첩 배열을 행으로 풀어 펼치는 함수
- [ ] Schema Detection / 파일만 보고 컬럼 구조를 추측하는 기능
- [ ] Schema Evolution on Load / 적재 중 새 컬럼이 생기면 자동으로 늘리는 기능
- [ ] Iceberg Tables and External Tables / 외부 파일을 소유권 없이 테이블처럼 읽는 방식

## 10. Transformation Pipelines

- [ ] Streams / 테이블에 생긴 변경분만 골라내는 객체
- [ ] Stream Types / 변경 전체를 볼지 추가분만 볼지 나뉜 종류
- [ ] Tasks / 정해진 시각이나 조건에 SQL을 돌리는 스케줄러
- [ ] Task Graph / 태스크끼리 순서를 물리는 의존 그래프
- [ ] Dynamic Tables / 원본이 바뀌면 알아서 갱신되는 결과 테이블 `추천`
- [ ] Incremental vs Full Refresh / 바뀐 만큼만 갱신할지 통째로 다시 만들지의 선택

---

# PART 4 · Performance and Cost

## 11. Query Performance

### Query Profiling

- [ ] Query Profile / 쿼리가 어느 단계에서 오래 걸렸는지 보는 그림
- [ ] Common Bottlenecks / 메모리 넘침·조인 폭발·대기로 느려지는 원인
- [ ] Pruning Efficiency / 전체 조각 중 실제로 읽은 비율

### Optimization Techniques

- [ ] Clustering Keys / 조각을 값 기준으로 정렬해 두는 열 지정
- [ ] Automatic Clustering Service / 흐트러진 조각을 알아서 다시 정렬하는 서비스
- [ ] Search Optimization Service / 점 조회를 빠르게 하려고 만드는 별도 색인
- [ ] Query Acceleration Service / 튀는 쿼리에 서버리스 자원을 더 붙이는 서비스
- [ ] Materialized View Tradeoffs / 결과를 미리 저장해두는 대신 드는 유지 비용
- [ ] Caching Strategy / 결과·메타데이터·디스크 캐시를 골라 쓰는 전략

## 12. Cost Management

### Pricing Model

- [ ] Credit Consumption Model / 웨어하우스를 켜 둔 시간만큼 깎이는 단위
- [ ] Compute vs Storage vs Cloud Services Cost / 셋으로 나뉘어 따로 매겨지는 요금
- [ ] Serverless Feature Cost / 웨어하우스 없이 쓰는 기능에 따로 붙는 요금

### Cost Control

- [ ] Resource Monitors / 크레딧 한도를 넘으면 웨어하우스를 멈추는 감시
- [ ] Budgets / 계정 전체 지출에 미리 상한을 거는 기능
- [ ] Usage Views / 어느 웨어하우스가 얼마나 켜졌는지 보는 기록
- [ ] Cost Attribution / 태그를 붙여 비용을 팀·프로젝트별로 가르는 방법
- [ ] Warehouse Right-sizing / 필요보다 큰 웨어하우스를 줄여 켜는 조정

---

# PART 5 · Governance and Operations

## 13. Access Control

- [ ] Role-Based Access Control / 사람 대신 역할에 권한을 몰아주는 방식
- [ ] System Roles / 계정 전체·객체·보안을 나눠 맡는 기본 역할
- [ ] Privileges and Grants / 역할에 뭘 할 수 있는지 부여하는 단위
- [ ] Ownership and Future Grants / 나중에 생길 객체까지 미리 권한을 걸어두는 규칙
- [ ] Discretionary Access Control Model / 객체 소유자가 권한을 넘겨줄 수 있는 방식
- [ ] Secondary Roles / 주 역할 말고 추가로 켜서 합쳐 쓰는 역할

## 14. Security and Governance

### Security

- [ ] Authentication / SSO·키 쌍·2차 인증 중 고르는 로그인 방식
- [ ] Network Policies / 접속 가능한 IP·경로를 좁히는 규칙
- [ ] Encryption / 스노우플레이크와 고객 키를 함께 써 암호화하는 방식

### Data Governance

- [ ] Object Tagging / 객체에 분류용 이름표를 붙이는 기능
- [ ] Masking Policies / 보는 사람 역할에 따라 값을 가려 보여주는 규칙
- [ ] Row Access Policies / 역할마다 볼 수 있는 행을 걸러주는 규칙
- [ ] Data Classification / 민감 정보 담긴 컬럼을 자동으로 찾아 표시하는 기능
- [ ] Access History and Lineage / 누가 언제 뭘 읽었고 어디서 왔는지 추적

## 15. Data Sharing

- [ ] Secure Data Sharing / 복사 없이 다른 계정에 조각을 그대로 보여주는 방식
- [ ] Reader Accounts / 계정 없는 상대에게 대신 만들어주는 접속
- [ ] Snowflake Marketplace / 계정 간 공유 데이터를 사고파는 장터
- [ ] Data Clean Rooms / 원본은 안 보여주고 집계만 맞대는 공간 `선택`
- [ ] Database Replication / 다른 리전·클라우드로 데이터를 복제해두는 기능

## 16. Developer Ecosystem

- [ ] Snowpark / SQL 대신 코드로 웨어하우스에 계산을 미는 API
- [ ] User-Defined Functions / SQL·Python·Java로 직접 짜 넣는 함수
- [ ] Stored Procedures / 여러 SQL문을 절차형으로 묶어 저장하는 단위
- [ ] External Functions / 계정 밖 API를 SQL에서 호출하는 함수
- [ ] Snowflake CLI and Git Integration / 명령줄과 저장소에서 객체를 배포하는 방법
- [ ] dbt on Snowflake / dbt가 웨어하우스에 SQL 변환을 미는 연동 `추천`
- [ ] Cortex AI Functions / 데이터를 안 옮기고 SQL 안에서 LLM을 부르는 기능 `선택`

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- 데이터 파이프라인 · 웨어하우스 모델링 `software/role-based/data-engineer.md`
- BigQuery `software/skill-based/Data-DB/bigquery.md`
- 데이터 분석 `software/role-based/data-analyst.md`
- BI 리포팅 `software/skill-based/Data-DB/power-bi.md`
- 클라우드 인프라 `software/skill-based/Infra-DevOps/aws.md`
