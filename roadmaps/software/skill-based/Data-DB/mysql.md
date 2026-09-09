# MySQL `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to MySQL

## 1. What is MySQL?

### Overview of MySQL / What is it?

- [ ] Relational Database Management System / 행과 열의 관계형 모델로 다루는 DB
- [ ] Client-Server Architecture / 클라이언트가 네트워크로 서버에 접속하는 구조
- [ ] Pluggable Storage Engine Architecture / 저장 엔진을 갈아끼울 수 있게 분리한 구조

### Distributions and Lineage

- [ ] Oracle MySQL / 오라클이 배포하는 공식 MySQL
- [ ] Percona Server for MySQL / 성능 패치를 더한 MySQL 포크
- [ ] MariaDB Fork / MySQL에서 갈라져 독자 노선을 탄 포크
- [ ] MySQL vs PostgreSQL / 엔진 다중 지원과 확장성으로 갈리는 지향점

### Version Selection

- [ ] MySQL 5.7 vs 8.0 vs 8.4 LTS / 윈도우 함수·역할 지원 여부로 갈리는 버전

## 2. Getting Started

### Installation `택 1`

- [ ] Docker and Docker Compose / 컨테이너로 즉시 띄우는 설치 방식 `추천`
- [ ] Package Manager / apt·yum 등 OS 패키지로 설치하는 방식
- [ ] Managed Service / RDS·Cloud SQL처럼 운영을 대신 맡기는 서비스

### Client Tools

- [ ] mysql CLI / 명령줄로 서버에 접속하는 클라이언트
- [ ] MySQL Workbench / GUI로 스키마와 쿼리를 다루는 도구
- [ ] Connection Endpoint / 로컬 소켓과 TCP로 갈리는 접속 통로

### Initial Configuration

- [ ] Option Files / my.cnf 같은 서버 시작 옵션 파일
- [ ] mysql_secure_installation / 설치 직후 취약점을 없애는 스크립트

## 3. Data Types and Schema Design

### Type Selection

- [ ] Numeric Types / INT·BIGINT 같은 정수·고정소수점 타입
- [ ] String Types / CHAR·VARCHAR 등 고정·가변 문자열 타입
- [ ] Binary Types / BINARY·BLOB 같은 이진 데이터 타입
- [ ] Date and Time Types / DATE·TIMESTAMP 등 날짜시간 타입
- [ ] ENUM and SET / 정해진 값 목록 안에서만 고르는 타입
- [ ] JSON Type / 스키마 없는 문서를 컬럼 하나에 담는 타입

### Character Set / Collation

- [ ] utf8mb4 vs utf8mb3 / 이모지까지 담을 수 있는지가 갈리는 문자셋
- [ ] Collation and Comparison Rules / 정렬과 비교 기준을 정하는 규칙
- [ ] Scope of Application / 서버·DB·테이블·컬럼 단위로 걸리는 범위

### Table Design

- [ ] Primary Key Design / 클러스터형 인덱스라 짧게 잡아야 하는 설계
- [ ] Foreign Key Constraints / 다른 테이블 값 존재를 강제하는 제약
- [ ] Generated Columns / 다른 컬럼 값으로 자동 계산되는 컬럼
- [ ] Table Partitioning / RANGE·HASH 등 기준으로 테이블을 쪼개는 방식

---

# PART 2 · Query Execution and Indexes

## 4. Query Execution Flow

- [ ] Connection Handling / 접속마다 스레드 하나씩 붙이는 처리
- [ ] Parser and Preprocessor / SQL을 구문 분석해 트리로 바꾸는 단계
- [ ] Optimizer / 비용 낮은 실행 계획을 고르는 단계
- [ ] Execution Engine / 선택된 계획대로 행을 가져오는 단계
- [ ] Handler API / 옵티마이저와 저장 엔진을 잇는 내부 인터페이스
- [ ] Prepared Statements / SQL을 미리 준비해 반복 실행하는 방식

## 5. Indexing

### Index Structures

- [ ] B+Tree Index / 정렬된 키를 트리로 찾는 인덱스 구조
- [ ] Clustered Index / 기본 키 순서로 데이터를 저장하는 인덱스
- [ ] Secondary Index and PK Lookup / 보조 인덱스가 기본 키를 들고 있는 구조
- [ ] Hash Index (MEMORY Engine) / 동등 비교만 빠른 해시 인덱스
- [ ] Full-Text Index / 단어 단위로 찾는 텍스트 검색 인덱스

### Index Design

- [ ] Composite Index / 앞쪽 컬럼부터만 활용되는 복합 인덱스
- [ ] Covering Index / 인덱스만으로 쿼리가 끝나는 구성
- [ ] Selectivity and Cardinality / 값이 얼마나 흩어져 있는지 보는 지표
- [ ] Prefix Index / 문자열 앞부분만 잘라 거는 인덱스
- [ ] Invisible Index / 삭제 없이 옵티마이저에서 숨기는 인덱스
- [ ] Functional Index / 표현식 결과에 거는 인덱스
- [ ] Write Amplification from Indexes / 인덱스가 늘수록 커지는 쓰기 부담

## 6. Query Optimization

### Reading Execution Plans

- [ ] EXPLAIN / 실행 계획을 표나 JSON으로 보는 명령
- [ ] EXPLAIN ANALYZE / 실제 실행하며 계획과 실측을 함께 보는 명령
- [ ] Access Types / const·ref·range 등 행 접근 방식 등급
- [ ] Extra Column / filesort·temporary 등 추가 비용 표시

### Optimizer Behavior

- [ ] Cost Model / 접근 방식마다 비용을 매겨 비교하는 모델
- [ ] Statistics / ANALYZE TABLE로 모으는 값 분포 통계
- [ ] Join Algorithms / Nested Loop·Hash Join 등 조인 방식
- [ ] Index Condition Pushdown / 인덱스 단계에서 조건을 먼저 거르는 최적화
- [ ] Optimizer Hints / 실행 계획을 강제로 바꾸는 힌트

### Tuning Patterns

- [ ] Pagination / Keyset과 OFFSET으로 갈리는 페이지 넘김
- [ ] Slow Query Log / 느린 쿼리를 자동 기록하는 로그
- [ ] Performance Schema and sys Schema / 서버 내부 지표를 조회하는 스키마

---

# PART 3 · Storage Engines and Transactions

## 7. Storage Engines

- [ ] InnoDB / 트랜잭션과 잠금을 지원하는 기본 엔진 `추천`
- [ ] MyISAM / 트랜잭션 없이 테이블째 잠그는 옛 엔진
- [ ] MEMORY / 데이터를 메모리에만 두는 휘발성 엔진
- [ ] Engine Selection Tradeoffs / 트랜잭션과 속도 사이 엔진 선택 기준

## 8. InnoDB Internals

### Memory Structures

- [ ] Buffer Pool / 자주 쓰는 페이지를 메모리에 붙드는 영역
- [ ] Change Buffer / 보조 인덱스 변경을 모아뒀다 반영하는 버퍼
- [ ] Adaptive Hash Index / 자주 찾는 경로를 해시로 캐싱하는 기능

### Disk Structures

- [ ] Tablespaces / 파일 단위로 데이터를 담는 저장 공간
- [ ] Redo Log / 변경을 먼저 적고 나중에 반영하는 로그
- [ ] Undo Log / 옛 값을 남겨 읽기를 막지 않는 로그
- [ ] Doublewrite Buffer / 페이지 쓰기 중 손상을 막는 이중 쓰기
- [ ] Row Format / DYNAMIC 등 행을 저장하는 형식

### Operational Flow

- [ ] Checkpoint and Flushing / 더티 페이지를 디스크로 내리는 시점
- [ ] Crash Recovery / 리두·언두 로그로 장애 후 복구하는 절차

## 9. Transactions and Locking

### Transactions

- [ ] ACID / 트랜잭션이 지켜야 할 네 가지 성질
- [ ] Isolation Levels / READ COMMITTED 등 간섭 허용 수준
- [ ] MVCC / 잠금 없이 과거 스냅샷을 읽는 방식
- [ ] Read Phenomena / Dirty Read 등 격리 수준별 이상 현상

### Locking

- [ ] Shared and Exclusive Lock / 읽기와 쓰기가 갈리는 잠금 두 종류
- [ ] Record Lock, Gap Lock, Next-Key Lock / 인덱스 레코드와 그 틈을 잠그는 방식
- [ ] Locking Reads / FOR UPDATE 등 읽으며 잠금까지 거는 조회
- [ ] Metadata Lock / DDL과 DML 충돌을 막는 스키마 잠금
- [ ] Deadlock Detection / 교착 상태를 찾아내 롤백하는 기능
- [ ] Lock Wait Timeout / 잠금 대기 한도를 넘기면 실패시키는 설정

---

# PART 4 · Replication and Scaling

## 10. Replication

### Basic Structure

- [ ] Binary Log / 데이터 변경을 순서대로 남기는 로그
- [ ] Binlog Format / 문장과 행 단위로 갈리는 로그 기록 방식
- [ ] Source and Replica Roles / 원본과 복제본으로 나뉘는 역할
- [ ] Replication Threads / 로그를 받아오고 적용하는 두 스레드

### Method Selection

- [ ] Asynchronous Replication / 반영 확인 없이 흘려보내는 기본 복제
- [ ] Semi-Synchronous Replication / 최소 한 대의 수신 확인을 기다리는 복제
- [ ] GTID-based Replication / 전역 트랜잭션 ID로 위치를 추적하는 복제 `추천`
- [ ] Binlog Position-based Replication / 파일명과 오프셋으로 위치를 추적하는 복제

### Replication Operations

- [ ] Parallel Replication / 여러 스레드로 로그를 병렬 적용하는 방식
- [ ] Replication Lag / 원본과 복제본 사이 지연 지표
- [ ] Multi-Source Replication / 여러 원본에서 한 복제본으로 모으는 구성

## 11. High Availability

- [ ] Failover Strategy / 수동과 자동으로 갈리는 장애 전환 방식
- [ ] MySQL Group Replication / 다수 노드가 합의로 동기화하는 복제
- [ ] InnoDB Cluster / Shell·Router를 묶은 고가용성 관리 도구
- [ ] ProxySQL / 쿼리를 보고 라우팅하는 프록시
- [ ] Managed HA / RDS Multi-AZ 등 클라우드가 대신하는 고가용성

## 12. Scaling

- [ ] Read Scaling / 읽기를 복제본으로 흩뿌리는 확장
- [ ] Connection Pooling / 연결을 재사용해 접속 비용을 줄이는 기법
- [ ] Sharding Strategy / Range·Hash 등 데이터를 나눠 담는 기준
- [ ] Vitess / 샤딩을 자동화하는 MySQL 클러스터링 계층 `선택`
- [ ] Cache Layer Integration / DB 앞에 캐시를 붙이는 구성 `별도`

---

# PART 5 · Operations

## 13. Configuration and Tuning

- [ ] Memory Configuration / buffer_pool_size 등 메모리 할당 설정
- [ ] Connection Configuration / max_connections 등 접속 관련 설정
- [ ] Durability Settings / 커밋 시 디스크 반영 강도를 정하는 설정
- [ ] I/O Configuration / 디스크 입출력 방식을 조절하는 설정
- [ ] Persisted System Variables / 재시작해도 남는 설정 변경 방식
- [ ] Benchmarking / sysbench 등으로 부하를 걸어 재는 성능 측정

## 14. Backup and Recovery

- [ ] Logical Backup / mysqldump로 SQL 문을 뽑는 백업
- [ ] Physical Backup / 파일을 그대로 복사하는 백업 `추천`
- [ ] Point-in-Time Recovery / 백업 이후 로그를 재생해 시점 복구
- [ ] Restore Drill / 복구가 실제로 되는지 확인하는 훈련

## 15. Security

- [ ] User Accounts / 접속 허용 호스트까지 포함한 계정 구분
- [ ] Privilege System / GRANT와 역할로 권한을 부여하는 체계
- [ ] Authentication Plugins / 비밀번호 인증 방식을 바꾸는 플러그인
- [ ] TLS Connections / 접속 구간을 암호화하는 연결
- [ ] Data-at-Rest Encryption / 디스크에 저장된 데이터를 암호화하는 기능
- [ ] Audit Logging / 접속과 쿼리 이력을 남기는 감사 로그
- [ ] Network Hardening / 접속 가능한 네트워크를 좁히는 설정

## 16. Operations and Troubleshooting

- [ ] Online DDL / 중단 없이 스키마를 바꾸는 방식
- [ ] Zero-downtime Schema Change / gh-ost 등 트리거로 무중단 변경하는 도구
- [ ] Version Upgrade / 제자리와 복제본 우선으로 갈리는 순서
- [ ] Key Metrics / QPS 등 상태 판단에 쓰는 핵심 지표
- [ ] Monitoring Stack / mysqld_exporter 등 지표 수집 도구
- [ ] Percona Toolkit / 느린 쿼리를 모아 분석하는 도구
- [ ] Common Incidents / 접속 고갈·폭주 쿼리 등 자주 겪는 장애

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- PostgreSQL 운영 `software/role-based/postgresql-dba.md`
- MariaDB 고유 기능 `software/skill-based/Data-DB/mariadb.md`
- 캐시 계층 `software/skill-based/Data-DB/redis.md`
- 백엔드 전반 · ORM과 커넥션 관리 `software/role-based/backend.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
