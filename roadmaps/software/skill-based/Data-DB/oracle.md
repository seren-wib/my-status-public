# Oracle Database `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Oracle

## 1. What is Oracle Database?

### Overview of Oracle / What is it?

- [ ] Relational Database Management System / 표 형태 데이터를 관계로 묶어 관리하는 방식
- [ ] Converged and Multi-model Database / 관계형·JSON·그래프를 한 DB에 담는 성격

### Editions and Licensing

- [ ] Editions / Enterprise·Standard Edition 2·XE로 나뉘는 제품 등급
- [ ] Licensing Metrics / 프로세서 수나 사용자 수로 매기는 과금 기준
- [ ] Priced Options / RAC·파티셔닝처럼 별도로 돈을 내는 기능

### Oracle vs Other RDBMS

- [ ] Oracle vs PostgreSQL and SQL Server / 다른 RDBMS와 구조·라이선스를 견주는 비교
- [ ] When to choose Oracle? / PL/SQL·RAC 같은 강점이 필요한지 따지는 기준

## 2. Getting Started

### Installation `택 1`

- [ ] Container Image / 컨테이너 이미지로 통째로 띄우는 설치 방식 `추천`
- [ ] Oracle Database XE Installer / 무료 버전을 직접 내려받아 까는 설치 방식
- [ ] Autonomous Database Free Tier / 클라우드가 운영을 대신 맡는 무료 티어

### Client Tools

- [ ] SQL*Plus / 명령줄에서 SQL과 관리 명령을 같이 치는 기본 도구
- [ ] SQLcl / 자바로 만든 최신 커맨드라인 클라이언트
- [ ] SQL Developer / GUI로 스키마와 쿼리를 다루는 개발 도구 `추천`

### Connection Configuration

- [ ] Listener / lsnrctl로 제어하는 접속 요청 수신 프로세스
- [ ] Naming Methods / tnsnames.ora나 Easy Connect로 주소를 찾는 방법
- [ ] Service Name vs SID / 인스턴스를 가리키는 두 가지 식별 방식
- [ ] Privileged Accounts / SYS·SYSTEM처럼 관리 권한을 가진 기본 계정

---

# PART 2 · Architecture and Storage Structure

## 3. Instance Architecture

### Memory Structures

- [ ] SGA / 버퍼 캐시·셰어드 풀을 담는 공유 메모리 영역
- [ ] PGA / 세션마다 정렬·해시 작업에 쓰는 개인 메모리
- [ ] Memory Management / SGA·PGA 크기를 자동으로 나눠 관리하는 기능
- [ ] Library Cache / 파싱된 SQL과 커서를 재사용하도록 캐싱하는 영역

### Background Processes

- [ ] Writer Processes / DBWn·LGWR처럼 디스크 쓰기를 맡는 프로세스
- [ ] Recovery and Cleanup / 인스턴스 복구와 죽은 세션 정리를 맡는 프로세스
- [ ] Archiver and Monitor / 리두 보관과 성능 통계 수집을 맡는 프로세스

### Connection Architecture `택 1`

- [ ] Dedicated Server / 세션마다 서버 프로세스를 하나씩 붙이는 방식 `추천`
- [ ] Shared Server / 여러 세션이 서버 프로세스를 나눠 쓰는 방식

## 4. Storage Structures

### Logical Structures

- [ ] Tablespace, Segment, Extent, Block / 논리 저장 구조를 이루는 4단계 층
- [ ] System Tablespaces / SYSTEM·SYSAUX처럼 용도가 정해진 기본 테이블스페이스
- [ ] Bigfile vs Smallfile Tablespace / 파일을 하나로 크게 두느냐 여러 개로 쪼개느냐

### Physical Structures

- [ ] Physical Files / 데이터파일·컨트롤파일·리두 로그로 이뤄진 실체 파일
- [ ] ARCHIVELOG Mode / 리두 로그를 지우기 전에 복사해 보관하는 모드

### Data Dictionary

- [ ] Static Views / DBA_·ALL_·USER_ 접두사로 나뉘는 메타데이터 뷰
- [ ] Dynamic Performance Views / v$session처럼 실시간 상태를 보여주는 뷰

## 5. Multitenant Architecture

- [ ] Container Database (CDB) and Pluggable Database (PDB) / 여러 PDB가 하나의 CDB를 공유하는 구조
- [ ] Container Hierarchy / CDB$ROOT와 PDB$SEED로 이뤄진 컨테이너 계층
- [ ] Common vs Local Users / 전체 컨테이너에 걸치는 계정과 PDB 전용 계정
- [ ] Plug and Unplug a PDB / PDB를 파일째 다른 CDB로 옮기는 작업
- [ ] PDB Cloning / 원본과 동기화되는 복제본을 만드는 기능

## 6. Transactions and Concurrency

### Transaction Control

- [ ] COMMIT, ROLLBACK, SAVEPOINT / 트랜잭션을 끝내거나 되돌리는 기본 명령
- [ ] Autonomous Transactions / 바깥 트랜잭션과 독립적으로 커밋되는 하위 트랜잭션

### Read Consistency

- [ ] Multiversion Read Consistency / 읽는 시점 기준의 스냅샷을 언두로 보여주는 방식
- [ ] Undo Segments / 변경 전 데이터를 보관해 읽기 일관성을 받치는 공간
- [ ] Snapshot Too Old / 언두가 모자라 오래된 스냅샷을 못 만드는 오류

### Locking

- [ ] Isolation Levels / READ COMMITTED·SERIALIZABLE로 나뉘는 격리 수준
- [ ] Enqueue Types / 행 잠금(TX)과 테이블 잠금(TM) 같은 대기 큐 종류
- [ ] Deadlock Detection / 교착 상태를 찾아 한쪽 트랜잭션을 강제로 죽이는 기능

---

# PART 3 · SQL and PL/SQL

## 7. Oracle SQL Extensions

### Oracle-Specific Syntax

- [ ] DUAL Table / 값 하나 계산할 때 쓰는 가상의 한 줄짜리 테이블
- [ ] Pseudocolumns / ROWNUM·ROWID처럼 테이블에 없는 가상 컬럼
- [ ] Hierarchical Queries / CONNECT BY로 트리 구조를 한 번에 펼치는 조회
- [ ] MERGE Statement / 있으면 갱신하고 없으면 넣는 조건부 병합 구문
- [ ] Legacy Outer Join Syntax / (+) 기호로 아우터 조인을 표시하던 옛 문법

### Data Types

- [ ] Oracle Types / NUMBER·VARCHAR2·CLOB 같은 오라클 고유 자료형
- [ ] DATE vs TIMESTAMP WITH TIME ZONE / 초 단위까지냐 시간대까지 담느냐의 차이
- [ ] NULL and Empty String Semantics / 빈 문자열을 NULL로 취급하는 오라클 특성

### Oracle Extension Features

- [ ] Flashback Query / 과거 시점 데이터를 AS OF로 그대로 조회하는 기능
- [ ] MODEL Clause / SELECT 결과를 스프레드시트처럼 셀 계산하는 절 `선택`

## 8. Schema Objects

- [ ] Sequences / NEXTVAL로 번호를 하나씩 자동으로 채번하는 객체
- [ ] Synonyms / 객체에 별명을 붙여 짧게 부르게 하는 기능
- [ ] Materialized Views / 쿼리 결과를 실체 테이블로 저장해 두는 뷰
- [ ] Database Links / 다른 오라클 DB의 객체를 내 DB처럼 참조하는 연결
- [ ] External Tables / OS 파일을 테이블처럼 읽어 조회하는 객체
- [ ] Temporary Tables / 세션이나 트랜잭션 동안만 데이터가 남는 테이블
- [ ] Index-Organized Tables (IOT) / 데이터 자체를 인덱스 구조로 저장하는 테이블

## 9. PL/SQL

### Block Structure

- [ ] Anonymous Block / 이름 없이 즉석에서 실행하는 PL/SQL 블록
- [ ] Anchored Declarations / 컬럼·행 타입을 따라가게 선언하는 방식
- [ ] Control Structures / IF·LOOP 같은 절차적 흐름 제어 구문

### SQL Integration

- [ ] SELECT INTO / 조회 결과 한 줄을 변수에 바로 담는 구문
- [ ] Implicit Cursor Attributes / 직전 SQL의 처리 결과를 알려주는 속성
- [ ] Explicit Cursors / 직접 열고 한 줄씩 가져오는 명시적 커서
- [ ] Cursor FOR Loop / OPEN·FETCH·CLOSE를 생략하는 반복 커서 구문

### Exception Handling

- [ ] Predefined Exceptions / 오라클이 미리 이름 붙여 둔 표준 예외
- [ ] RAISE_APPLICATION_ERROR / 사용자 정의 오류 번호와 메시지를 던지는 함수
- [ ] PRAGMA EXCEPTION_INIT / ORA 오류 번호에 사용자 예외 이름을 묶는 지시어
- [ ] Error Introspection / SQLCODE·SQLERRM으로 예외 정보를 꺼내는 방법

## 10. Advanced PL/SQL

### Stored Program Units

- [ ] Procedures and Functions / 값을 반환하지 않거나 반환하는 저장 프로그램
- [ ] Packages / 명세와 본문으로 나뉘는 프로시저 묶음
- [ ] Triggers / 이벤트 시점에 따라 자동 실행되는 코드
- [ ] Mutating Table Error / 트리거가 자신을 바꾸는 테이블을 조회해 나는 오류

### Bulk Processing

- [ ] Collection Types / 연관 배열·중첩 테이블 같은 PL/SQL 컬렉션
- [ ] BULK COLLECT / 쿼리 결과를 한 번에 컬렉션으로 퍼 담는 구문
- [ ] FORALL / 컬렉션 값을 한 번에 벌크로 DML 처리하는 구문

### Dynamic SQL

- [ ] EXECUTE IMMEDIATE / 문자열로 만든 SQL을 즉시 실행하는 구문
- [ ] Bind Variables and SQL Injection / 값을 바인딩해 SQL 삽입을 막는 방어

### Built-in Packages

- [ ] Utility Packages / 화면 출력·LOB·파일 처리를 돕는 내장 패키지
- [ ] Job Scheduling / DBMS_SCHEDULER로 작업을 예약 실행하는 기능
- [ ] Metadata and Stats / 객체 DDL 추출과 통계 수집을 맡는 패키지

---

# PART 4 · Performance and Tuning

## 11. Optimizer and Execution Plans

### Cost-Based Optimizer

- [ ] Cardinality, Selectivity, Cost / 옵티마이저가 계획을 셈할 때 쓰는 지표
- [ ] Optimizer Statistics / 테이블·컬럼·인덱스 단위로 모으는 통계 정보
- [ ] Histograms / 값이 고르지 않은 컬럼의 분포를 담는 통계
- [ ] Adaptive Query Optimization / 실행 도중 계획을 관찰해 스스로 바꾸는 최적화

### Reading Execution Plans

- [ ] EXPLAIN PLAN / 실행 전 예상 계획을 세워 보여주는 명령
- [ ] Actual Plan / 실제로 수행된 계획을 캐시에서 꺼내 보는 방법
- [ ] Access Paths / 풀 스캔·인덱스 스캔처럼 행을 찾는 경로
- [ ] Join Methods / 네스티드 루프·해시처럼 테이블을 합치는 방식

### Plan Stability

- [ ] Optimizer Hints / 주석으로 옵티마이저에게 계획을 지시하는 방법
- [ ] SQL Plan Baselines / 검증된 실행 계획을 고정해 변경을 막는 장치

## 12. Indexing and Partitioning

### Index Types

- [ ] B-Tree Index / 균형 트리로 값을 정렬해 찾는 기본 인덱스
- [ ] Bitmap Index / 값 종류가 적은 컬럼을 비트로 표현하는 인덱스
- [ ] Function-Based Index / 컬럼에 함수를 씌운 결과값으로 만든 인덱스
- [ ] Composite Index / 컬럼 순서가 성능을 가르는 복합 인덱스

### Partitioning

- [ ] Partitioning Strategies / 범위·목록·해시로 테이블을 나누는 전략
- [ ] Interval Partitioning / 새 값이 들어오면 파티션을 자동으로 늘리는 방식
- [ ] Partition Pruning / 조건에 안 맞는 파티션을 건너뛰는 최적화
- [ ] Local vs Global Index / 파티션마다 따로냐 테이블 전체로 하나냐인 인덱스
- [ ] Partition Exchange / 파티션과 일반 테이블을 순간적으로 맞바꾸는 기능

## 13. Performance Diagnostics

### Diagnostic Tools

- [ ] AWR Report / 일정 주기의 성능 통계를 스냅샷으로 남기는 보고서 `추천`
- [ ] ADDM / AWR 데이터를 분석해 병목 원인을 짚어주는 진단 도구
- [ ] ASH / 세션 대기 상태를 짧은 간격으로 표본 수집하는 기능

### Wait Event Analysis

- [ ] Wait Event Classes / 무엇을 기다리는지 이름 붙여 분류한 대기 이벤트
- [ ] Blocking Sessions / 다른 세션을 잠금으로 막고 있는 세션

### Session Tracing

- [ ] SQL Trace / 세션 하나의 SQL 실행 과정을 파일로 남기는 기능
- [ ] tkprof / SQL 트레이스 파일을 사람이 읽게 정리하는 도구

---

# PART 5 · Operations

## 14. Backup and Recovery

### RMAN

- [ ] Full and Incremental Backup / 전체를 다 받을지 바뀐 부분만 받을지의 구분
- [ ] Fast Recovery Area / 백업·리두·아카이브를 한 곳에 모아 두는 공간
- [ ] Retention Policy / 백업을 얼마나 오래 보관할지 정하는 규칙

### Recovery Scenarios

- [ ] Complete vs Incomplete Recovery / 끝까지 복구하느냐 특정 시점에서 멈추느냐
- [ ] Point-in-Time Recovery (PITR) / 장애 직전 특정 시각으로 되돌리는 복구
- [ ] Flashback Database and Flashback Table / DB나 테이블을 과거 상태로 되돌리는 기능

### Logical Backup

- [ ] Data Pump / expdp·impdp로 데이터를 파일로 내보내고 들이는 도구

## 15. High Availability

- [ ] Real Application Clusters (RAC) / 여러 인스턴스가 하나의 DB를 같이 여는 구조
- [ ] Cache Fusion / 인터커넥트로 노드끼리 버퍼 캐시를 주고받는 기술
- [ ] Data Guard / 대기 서버로 데이터를 실시간 복제해 두는 기능
- [ ] Protection Modes / 가용성과 성능 중 무엇을 우선할지 정하는 모드
- [ ] Switchover vs Failover / 계획된 전환이냐 장애로 인한 강제 전환이냐
- [ ] GoldenGate / 이기종 DB 간에도 실시간으로 데이터를 복제하는 도구 `선택`

## 16. Security and Auditing

- [ ] Users, Roles, Privileges / 계정과 권한을 묶어 관리하는 기본 단위
- [ ] Profiles / 비밀번호 정책과 자원 한도를 묶어 계정에 씌우는 것
- [ ] Virtual Private Database (VPD) / 쿼리에 조건을 자동으로 덧붙여 행을 숨기는 보안
- [ ] Transparent Data Encryption (TDE) / 수정 없이 파일 단위로 암호화하는 기능
- [ ] Unified Auditing / 여러 감사 방식을 하나의 체계로 통합한 기능

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- PostgreSQL 운영 · DBA 업무 전반 `software/role-based/postgresql-dba.md`
- 데이터 파이프라인 `software/role-based/data-engineer.md`
- 백엔드 전반 · 커넥션 풀 `software/role-based/backend.md`
- 확장 설계 `software/skill-based/CS-Theory/system-design.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
