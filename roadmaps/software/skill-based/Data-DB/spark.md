# Apache Spark `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Spark

## 1. What is Apache Spark?

### Overview of Spark / What is it?

- [ ] Distributed Data Processing Engine / 여러 노드에 데이터를 쪼개 병렬로 처리하는 엔진
- [ ] In-Memory Computation / 중간 결과를 디스크 대신 메모리에 두는 방식
- [ ] Unified Batch and Streaming / 배치와 스트림을 같은 API로 처리하는 방식
- [ ] Lazy Evaluation and DAG Execution / 연산을 계획으로 쌓았다가 요청 시 몰아 실행

### Core Use Cases

- [ ] Large-scale ETL / 한 대에 안 들어가는 규모의 추출·변환·적재
- [ ] Stream Processing / 끊임없이 들어오는 데이터를 즉시 처리
- [ ] Machine Learning Pipeline / 전처리부터 학습까지 분산 노드에서 처리

### Spark vs Other Systems

- [ ] Spark vs Hadoop MapReduce / 단계마다 디스크를 안 거치고 메모리로 이어 처리
- [ ] Spark vs Single-node Pandas / 한 대에 못 담는 크기를 여러 대로 쪼개는 차이
- [ ] When to choose Spark? / 데이터가 메모리·한 대 용량을 넘을 때 고르는 기준

## 2. Getting Started

### Runtime Environment `택 1`

- [ ] Local Mode / 드라이버와 executor를 한 프로세스로 흉내내는 모드 `추천`
- [ ] Docker Image / 클러스터 구성 없이 컨테이너 하나로 실행
- [ ] Managed Platform (Databricks, EMR, Dataproc) / 클러스터 관리를 대신 맡기는 서비스

### API Languages `택 1`

- [ ] PySpark / Python으로 JVM 위 Spark를 호출하는 API `추천`
- [ ] Scala API / JVM 네이티브라 오버헤드가 없는 API
- [ ] Spark SQL only / 코드 없이 SQL만으로 쿼리를 짜는 방식

### First Run

- [ ] SparkSession / 클러스터 연결과 설정을 쥔 진입점
- [ ] pyspark / spark-shell과 함께 드라이버에 붙어 즉석 질의하는 셸
- [ ] spark-submit / 작성한 잡을 클러스터에 제출하는 명령

## 3. RDD Fundamentals

- [ ] Resilient Distributed Dataset / 노드에 흩어져 저장되는 불변 분산 컬렉션
- [ ] Partition / 데이터를 나눠 각 노드에 배정하는 단위
- [ ] Lineage / 파티션이 유실됐을 때 재계산할 연산 계보
- [ ] Transformations vs Actions / 계획만 쌓는 연산과 실행을 트리거하는 연산
- [ ] Narrow vs Wide Dependency / 셔플 없이 되는 의존과 재분배가 필요한 의존
- [ ] Transformations / map·filter·flatMap·reduceByKey로 계획만 쌓는 연산
- [ ] Actions / collect·count·take·saveAsTextFile로 계획을 실행시키는 연산
- [ ] Why Not to Use RDDs Directly / Catalyst 최적화를 못 받는 저수준이라는 단점

---

# PART 2 · Structured API

## 4. DataFrame and Dataset

### Concepts

- [ ] DataFrame vs Dataset vs RDD / 스키마와 최적화 여부로 갈리는 세 계층
- [ ] Schema / StructType으로 컬럼 이름과 타입을 미리 선언하는 구조
- [ ] Row and Column / 스키마 없는 레코드와 이름 붙은 표현식

### Basic Operations

- [ ] Projection and Filtering / select·filter·where로 컬럼을 고르고 행을 거름
- [ ] Column Expression / col·lit·expr로 참조·상수·SQL을 표현식으로 만드는 법
- [ ] Adding and Renaming / withColumn·withColumnRenamed·drop으로 컬럼 조작

### Aggregations and Joins

- [ ] Aggregations / groupBy·agg·count·sum·avg로 키별 집계를 셔플 뒤 계산
- [ ] Joins / inner·left·right·full·semi·anti로 갈리는 조인 방식
- [ ] Set Operations / union·intersect·except로 하는 집합 연산
- [ ] Pivot and Unpivot / 행 값을 컬럼으로 펼치거나 다시 접는 변환

### Data Cleaning

- [ ] Null Handling / na.fill·na.drop·coalesce로 결측값을 채우거나 제거
- [ ] Date and Timestamp Functions / 날짜·시각을 파싱하고 연산하는 함수들
- [ ] String Functions / regexp_extract·split·concat 같은 문자열 처리 함수
- [ ] Complex Types / array·map·struct와 이를 펼치는 explode

## 5. Spark SQL

- [ ] SQL vs DataFrame API / 같은 실행 계획으로 컴파일되는 두 표현 방식
- [ ] Temp View and Global Temp View / 세션 범위와 클러스터 범위로 갈리는 뷰
- [ ] Catalog / Database·Table 메타데이터를 관리하는 이름공간
- [ ] Managed vs External Table / 데이터 파일까지 책임지는지로 갈리는 테이블
- [ ] Window Functions / rank·row_number·lag·lead로 파티션 내 순서를 매김
- [ ] Hive Metastore Integration / 기존 Hive 테이블 메타데이터를 그대로 사용

## 6. UDF and Advanced Functions

- [ ] Built-in Function First Principle / UDF보다 최적화되는 내장 함수 우선 원칙
- [ ] Python UDF / 행마다 JVM과 Python을 오가며 드는 직렬화 비용
- [ ] Pandas UDF / Arrow로 배치 단위로 묶어 처리하는 벡터화 UDF
- [ ] Higher-Order Functions / transform·filter·aggregate로 배열 안에서 반복

## 7. Data Sources

### File Formats

- [ ] Parquet / 컬럼 단위로 저장해 필요한 컬럼만 읽는 포맷 `추천`
- [ ] ORC and Avro / 컬럼형 대안과 스키마 내장 행 기반 포맷
- [ ] CSV and JSON / 스키마 추론 비용이 크고 파싱이 느린 텍스트 포맷

### Reading and Writing

- [ ] DataFrameReader and DataFrameWriter / 소스·싱크를 오가는 읽기·쓰기 진입점
- [ ] Save Mode / append·overwrite·error·ignore로 갈리는 충돌 처리
- [ ] Partitioned Write / partitionBy로 컬럼 값에 따라 디렉터리를 나눠 씀
- [ ] Bucketing / 조인 키로 미리 셔플해 저장해 두는 방식
- [ ] Schema Inference vs Explicit Schema / 파일을 읽어 추측할지 직접 줄지

### External Integrations

- [ ] JDBC Source / 필터를 DB 쪽에서 미리 걸러오는 predicate pushdown
- [ ] Object Storage / S3·GCS·ADLS 같은 원격 저장소를 소스로 사용
- [ ] Kafka Source and Sink / 토픽을 스트림 입력이나 출력으로 연결

---

# PART 3 · Execution Model and Performance

## 8. Execution Model

### Cluster Components

- [ ] Driver / 실행 계획을 짜고 태스크를 분배하는 프로세스
- [ ] Executor / 태스크를 실제로 실행하는 워커 프로세스
- [ ] Cluster Manager / executor에 자원을 배정하는 관리자

### Units of Execution

- [ ] Job, Stage, Task / 액션 하나가 셔플 경계로 쪼개지는 실행 단위
- [ ] DAG Scheduler / 스테이지 간 의존을 그래프로 짜는 스케줄러
- [ ] Stage Boundary / 셔플이 일어나는 지점에서 갈리는 경계

### Query Optimization

- [ ] Catalyst Optimizer / 쿼리를 분석해 실행 계획을 최적화하는 엔진
- [ ] Logical and Physical Plan / 무엇을 할지와 어떻게 할지로 나뉜 단계
- [ ] Tungsten / 바이트코드를 생성해 연산을 합치는 whole-stage codegen
- [ ] Reading Plans / explain으로 최적화된 실행 계획을 확인하는 법

## 9. Shuffle and Partitioning

- [ ] Shuffle Trigger Conditions / 파티션 간 데이터 재분배가 일어나는 조건
- [ ] repartition vs coalesce / 셔플을 동반하는지로 갈리는 파티션 조정
- [ ] Partition Count Tuning / spark.sql.shuffle.partitions로 정하는 파티션 수
- [ ] Data Skew / 특정 키에 데이터가 몰려 태스크가 오래 걸리는 문제
- [ ] Salting / 몰린 키를 임의 값으로 쪼개 분산시키는 기법
- [ ] Broadcast Join / 작은 쪽을 통째로 복제해 셔플을 없애는 조인
- [ ] Sort-Merge Join vs Hash Join / 정렬 후 병합할지 해시로 맞출지 갈림
- [ ] Adaptive Query Execution (AQE) / 런타임 통계로 실행 계획을 다시 짬

## 10. Caching and Memory

- [ ] cache vs persist / 저장 위치를 고정할지 고를 수 있는지의 차이
- [ ] Storage Level / MEMORY_ONLY·MEMORY_AND_DISK 중 캐시 위치 지정
- [ ] unpersist / 더는 안 쓰는 캐시를 명시적으로 비우는 관리
- [ ] Unified Memory Model / Execution·Storage 영역이 경계를 나누는 구조
- [ ] Executor Sizing / spark.executor.memory·cores로 정하는 자원 배정
- [ ] Spill to Disk / 메모리가 부족해 중간 데이터를 디스크로 내보냄
- [ ] Diagnosing OOM Causes / 메모리 부족으로 executor가 죽는 원인 진단

## 11. Performance Tuning

- [ ] Predicate and Projection Pushdown / 필터·컬럼 선택을 읽기 단계로 미는 최적화
- [ ] Small File Problem / 작은 파일이 많아 태스크 오버헤드가 커지는 문제
- [ ] File Compaction / 작은 파일들을 큰 파일로 합쳐 정리하는 작업
- [ ] Serialization / Kryo로 기본보다 빠르고 작게 직렬화
- [ ] Dynamic Allocation / 부하에 맞춰 executor 수를 늘리고 줄이는 기능

---

# PART 4 · Streaming and Ecosystem

## 12. Structured Streaming

### Model

- [ ] Unbounded Table Model / 스트림을 끝없이 늘어나는 테이블로 보는 모델
- [ ] Micro-batch vs Continuous Processing / 짧은 배치로 쪼갤지 지속 처리할지
- [ ] Trigger / processingTime·once·availableNow로 배치 주기를 지정

### Time and State

- [ ] Event Time vs Processing Time / 데이터가 발생한 시각과 처리된 시각의 차이
- [ ] Windowing / Tumbling·Sliding·Session으로 이벤트 시간을 구간 묶기
- [ ] Watermark / 늦게 도착한 데이터를 얼마나 기다릴지 정하는 기준
- [ ] Stream-Stream Join / 두 스트림을 상태 유지하며 시간 내에 엮는 조인

### Output and Reliability

- [ ] Output Mode / append·update·complete로 결과를 내보내는 방식
- [ ] Checkpointing / 진행 상태와 오프셋을 저장해 재시작을 대비하는 기능
- [ ] Exactly-once / 재시도해도 안 겹치는 idempotent sink로 보장
- [ ] foreachBatch / 마이크로배치 결과를 배치 API로 넘겨 처리

## 13. Lakehouse Table Format

- [ ] Delta Lake / Parquet 위에 트랜잭션 로그를 얹은 테이블 포맷 `추천`
- [ ] Apache Iceberg / 스냅샷 기반으로 스키마·파티션 변경을 관리하는 포맷
- [ ] ACID Transaction and Time Travel / 트랜잭션 보장과 과거 버전 조회 기능
- [ ] Schema Evolution / 기존 데이터를 안 깨고 스키마를 바꾸는 기능
- [ ] MERGE INTO / 조건에 따라 삽입·갱신·삭제를 한 번에 처리하는 upsert

## 14. MLlib and Graph `선택`

- [ ] Transformer, Estimator, Pipeline / 변환·학습 단계를 이어붙이는 ML 구성요소
- [ ] Feature Engineering / VectorAssembler·StringIndexer로 입력을 벡터화
- [ ] Algorithms / Regression·Classification·Clustering 등 분산 학습 알고리즘
- [ ] GraphFrames / DataFrame 위에서 그래프 연산을 하는 라이브러리

---

# PART 5 · Operations

## 15. Deployment

- [ ] Deploy Mode / client·cluster 중 드라이버 위치를 정하는 모드
- [ ] YARN / 하둡 클러스터의 자원 관리자에 얹어 실행
- [ ] Kubernetes / executor를 파드로 띄우는 클러스터 매니저 `추천`
- [ ] spark-submit Options / --conf·--jars·--packages로 넘기는 실행 설정
- [ ] Dependency Packaging / uber jar·virtualenv로 의존성을 함께 묶는 법

## 16. Monitoring and Debugging

- [ ] Spark UI / Jobs·Stages·SQL·Storage를 보는 실행 중 웹 화면
- [ ] Spark History Server / 끝난 잡의 UI 기록을 나중에 다시 보는 서버
- [ ] Driver and Executor Log / 프로세스별로 따로 남는 실행 로그
- [ ] Metrics System / JMX·Prometheus로 내보내는 클러스터 지표
- [ ] Common Failures / OOM·Shuffle Fetch Failed 등 자주 나는 실패 유형

## 17. Production Practices

- [ ] Idempotent Job Design / 같은 입력을 다시 돌려도 결과가 같은 설계
- [ ] Incremental Processing and Backfill / 새 데이터만 처리하거나 과거분 소급
- [ ] Cost Optimization / Spot Instance·Autoscaling으로 비용을 줄이는 법
- [ ] Testing / Local SparkSession·chispa로 잡을 검증하는 법

---

# 이 로드맵 밖

- 데이터 파이프라인 전반 `software/role-based/data-engineer.md`
- Kafka `software/skill-based/Data-DB/kafka.md`
- 워크플로 오케스트레이션 `software/skill-based/Data-DB/airflow.md`
- 매니지드 Spark 플랫폼 `software/skill-based/Data-DB/databricks.md`
- 언어 기초 `software/skill-based/Languages/python.md`, `scala.md`
- 실행 환경 `software/skill-based/Infra-DevOps/kubernetes.md`
