# Microsoft SQL Server `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to SQL Server

## 1. What is SQL Server?

### Overview of SQL Server / What is it?

- [ ] Relational Database Management System / 데이터를 표로 나누고 관계로 엮는 관리 방식
- [ ] Database Engine and SQLOS / 질의를 처리하는 엔진과 그 아래 스레드·메모리 계층

### Product Lineup

- [ ] Editions / Enterprise·Standard 등 기능·가격이 다른 제품 등급
- [ ] Deployment Options / 온프레미스부터 매니지드까지 설치 형태 선택지
- [ ] Companion Services / ETL·리포팅·분석을 맡는 부속 서비스 묶음

### SQL Server vs Other RDBMS

- [ ] SQL Server vs Oracle / PostgreSQL까지 포함해 타 RDBMS와 강점을 비교
- [ ] When to choose SQL Server? / 언제 SQL Server를 선택할지 판단 기준

## 2. Getting Started

### Installation `택 1`

- [ ] Container Image / Docker 컨테이너로 즉시 띄우는 설치 방식 `추천`
- [ ] Developer Edition Installer / 무료로 전체 기능을 쓰는 개발자용 설치판
- [ ] Azure SQL Free Tier / 클라우드에서 무료로 써보는 체험 등급

### Tools

- [ ] SQL Server Management Studio (SSMS) / GUI로 질의·관리를 다루는 공식 도구 `추천`
- [ ] Azure Data Studio / 가볍고 크로스플랫폼인 질의 도구
- [ ] sqlcmd / 커맨드라인으로 질의를 실행하는 도구

### Initial Configuration

- [ ] Authentication Modes / Windows·SQL 인증 중 접속 방식을 고르는 설정
- [ ] Sample Databases / 연습용으로 제공되는 예제 데이터베이스

---

# PART 2 · Architecture and Storage Structure

## 3. Instance and Database Architecture

### System Databases

- [ ] System Databases / 인스턴스 운영에 쓰이는 내장 시스템 DB 묶음
- [ ] tempdb Contention and Sizing / 여러 세션이 몰려 병목이 되는 tempdb 용량 설계

### Memory and Scheduling

- [ ] Buffer Pool / 디스크 페이지를 메모리에 캐싱하는 영역
- [ ] Memory Configuration / 인스턴스가 쓸 메모리 상한을 정하는 설정
- [ ] SQLOS Scheduler and Worker Threads / 작업을 워커 스레드에 배분하는 자체 스케줄러
- [ ] MAXDOP and Cost Threshold for Parallelism / 병렬 실행 여부와 쓸 코어 수를 정하는 설정

## 4. Storage Internals

### File Structure

- [ ] Data File, Log File, Filegroup / 데이터·로그 파일과 이를 묶는 파일그룹 구성
- [ ] Page and Extent / 8KB 페이지와 이를 묶은 익스텐트라는 저장 단위

### Transaction Log

- [ ] Write-Ahead Logging / 데이터 반영 전에 로그부터 기록하는 원칙
- [ ] Virtual Log Files (VLF) / 트랜잭션 로그 파일을 나누는 내부 조각 단위
- [ ] Recovery Models / 로그를 얼마나 남길지, 복구 범위를 정하는 모델
- [ ] Log Truncation and Growth / 로그 공간을 비우고 늘리는 과정

### Table Structure

- [ ] Heap vs Clustered Table / 정렬 키 없이 쌓거나 키로 정렬해 저장하는 차이
- [ ] Row Store vs Columnstore / 행 단위와 열 단위 중 저장 방향을 고르는 선택
- [ ] Data Compression / 행·페이지 단위로 저장 공간을 줄이는 압축

## 5. Transactions and Concurrency

### Transactions

- [ ] Explicit, Implicit, Autocommit / 트랜잭션을 열고 닫는 시점을 정하는 방식

### Isolation

- [ ] Isolation Levels / 동시 트랜잭션 간 서로 보이는 범위를 정하는 수준
- [ ] Read Committed Snapshot Isolation (RCSI) / 잠금 대신 버전으로 커밋된 값만 읽는 옵션
- [ ] Version Store in tempdb / 행 버전을 임시로 보관하는 tempdb 안 공간

### Locking

- [ ] Lock Modes / 공유·배타 등 잠금이 취하는 여러 형태
- [ ] Lock Escalation / 행 단위 잠금이 많아지면 테이블 단위로 올리는 동작
- [ ] Blocking Analysis / 누가 누구를 막고 있는지 잠금 대기를 추적하는 분석
- [ ] Deadlock Graph / Trace Flag 1222로 남기는 교착 순환 관계 기록
- [ ] Optimistic Concurrency / 잠금 대신 rowversion으로 충돌만 나중에 확인하는 방식

---

# PART 3 · T-SQL and Programming

## 6. T-SQL Specifics

### T-SQL-Specific Syntax

- [ ] Identifier Quoting / 대괄호로 예약어·특수문자 식별자를 감싸는 표기
- [ ] TOP and OFFSET FETCH / 결과 행 수를 제한하거나 구간을 잘라내는 절
- [ ] OUTPUT Clause / INSERT·UPDATE 등이 바뀐 행을 즉시 돌려주는 절
- [ ] MERGE Statement / 삽입·수정·삭제를 조건 하나로 한 번에 처리하는 문
- [ ] APPLY Operator / 행마다 테이블 값 함수를 곁들여 조인하는 연산자
- [ ] Temporal Tables / 행 변경 이력을 자동 보관해 과거 시점을 조회하는 테이블

### Data Types

- [ ] String Types / 가변 길이·유니코드 여부로 나뉘는 문자열 타입
- [ ] Date Types / 정밀도·시간대 포함 여부가 다른 날짜 타입
- [ ] Special Types / 고유값·계층·가변 값 등 특수 목적 타입
- [ ] Collation and Case Sensitivity / 문자 정렬·비교 규칙과 대소문자 구분 여부

### Semi-structured Data

- [ ] JSON Support / JSON을 테이블로 풀거나 결과를 JSON으로 만드는 기능

## 7. Programmability

### Temporary Storage

- [ ] Temp Tables / 세션별·전역으로 나뉘는 임시 테이블
- [ ] Table Variables / 트랜잭션 로그 부담이 적은 변수형 임시 저장소
- [ ] Common Table Expressions / 쿼리 앞에 이름 붙여 재사용하는 임시 결과 집합

### Program Units

- [ ] Stored Procedures / 매개변수를 받아 실행하는 저장된 절차
- [ ] User-Defined Functions / 값 하나 또는 테이블을 반환하는 사용자 정의 함수
- [ ] Views / 질의를 이름 붙여 저장한, 인덱스도 걸 수 있는 가상 테이블
- [ ] Triggers / 이벤트 발생 시 자동으로 실행되는 절차
- [ ] inserted and deleted Pseudo Tables / 트리거에서 변경 전후 값을 담아주는 가상 테이블

### Cursors

- [ ] Cursors and Set-based Alternatives / 행 단위 순회 대신 집합 연산으로 대체하는 접근

## 8. Error Handling and Dynamic SQL

- [ ] TRY and CATCH / 예외를 잡아 처리 흐름을 분리하는 블록
- [ ] THROW vs RAISERROR / 사용자 오류를 던지는 두 방식의 차이
- [ ] Error Functions / CATCH 블록 안에서 오류 정보를 꺼내는 함수
- [ ] XACT_ABORT and XACT_STATE / 오류 시 트랜잭션을 자동 롤백하고 상태를 확인하는 설정
- [ ] Dynamic SQL / 문자열로 조립한 SQL을 실행 시점에 돌리는 방식
- [ ] Parameterization and SQL Injection / 매개변수화로 인젝션 공격을 막는 방어

---

# PART 4 · Performance and Tuning

## 9. Query Optimizer and Execution Plans

### Optimizer

- [ ] Cost-based Optimization / 예상 비용을 비교해 실행 계획을 고르는 방식
- [ ] Statistics / 데이터 분포를 요약해 최적화 근거로 쓰는 통계
- [ ] Cardinality Estimator Versions / 호환성 수준에 따라 바뀌는 행 수 추정 로직 버전
- [ ] Intelligent Query Processing / 실행 중 통계를 보고 계획을 스스로 보정하는 기능

### Execution Plans

- [ ] Estimated vs Actual Plan / 실행 전 예측과 실행 후 실제 계획의 비교
- [ ] Plan Operators / 테이블·인덱스를 훑거나 찾는 실행 계획 연산자
- [ ] Join Operators / 조인 방식에 따라 옵티마이저가 고르는 연산자
- [ ] Warning Signs / 실행 계획에서 성능 문제를 알리는 경고 표시

### Plan Cache

- [ ] Plan Reuse / 처음 들어온 매개변수로 굳어진 계획을 재사용하는 문제
- [ ] OPTION Hints / 질의에 힌트를 달아 옵티마이저 판단에 개입하는 절
- [ ] Query Store / 실행 계획 이력을 저장해 특정 계획을 강제하는 기능 `추천`

## 10. Indexing

- [ ] Clustered Index Design / 데이터 자체를 정렬해 저장하는 키 설계
- [ ] Nonclustered Index / 키 열과 포함 열을 나눠 담는 별도 인덱스
- [ ] Covering Index / 조회에 필요한 열을 전부 담아 테이블 접근을 없애는 인덱스
- [ ] Filtered Index / 조건에 맞는 일부 행만 담는 인덱스
- [ ] Columnstore Index / 분석 질의용으로 열 단위로 저장하는 인덱스
- [ ] Fragmentation / 조각난 인덱스를 재구성하거나 다시 만드는 정리
- [ ] Fill Factor / 페이지에 여유 공간을 남겨 두는 채움 비율
- [ ] Missing Index DMVs and Their Limits / 부족한 인덱스를 추천하되 신뢰할 수 없는 한계

## 11. Partitioning and Large Tables

- [ ] Partition Function and Partition Scheme / 경계값으로 나누고 파일그룹에 배치하는 두 정의
- [ ] Partition Elimination / 조건에 안 맞는 파티션은 아예 안 훑는 최적화
- [ ] Sliding Window / 오래된 파티션을 옮기고 비워 순환시키는 관리
- [ ] In-Memory OLTP / 테이블을 메모리에 상주시켜 잠금 없이 처리하는 기능 `선택`

## 12. Performance Diagnostics

### DMV-based Diagnostics

- [ ] Wait Statistics / 어디서 기다리는 시간이 쌓이는지 보여주는 통계
- [ ] Session and Request DMVs / 현재 실행 중인 세션·요청을 조회하는 뷰
- [ ] Query Stats DMVs / 누적 실행 통계로 비싼 질의를 찾는 뷰

### Tracing Tools

- [ ] Extended Events / 가볍게 이벤트를 수집하는 진단 프레임워크 `추천`
- [ ] SQL Server Profiler / 실행되는 질의를 실시간으로 캡처하는 구버전 도구 `선택`
- [ ] sp_whoisactive / 현재 활성 세션을 한눈에 보여주는 커뮤니티 프로시저

---

# PART 5 · Operations

## 13. Backup and Recovery

- [ ] Backup Types / 전체·차등·로그로 나뉘는 백업 종류
- [ ] Copy-only Backup / 백업 체인을 끊지 않고 따로 뜨는 백업
- [ ] Backup Compression and Encryption / 백업 용량을 줄이고 암호화하는 옵션
- [ ] Restore Sequence / 복원 도중과 완료 시점을 구분하는 순서
- [ ] Point-in-Time Restore / 로그를 원하는 시각까지만 재생하는 복원
- [ ] Page Restore / 손상된 페이지만 골라 복구하는 방식
- [ ] RTO and RPO Planning / 복구 소요 시간과 허용 데이터 손실을 정하는 목표
- [ ] Backup Verification / 백업 파일이 복원 가능한지 미리 확인하는 절차

## 14. High Availability

- [ ] Always On Availability Groups / 여러 복제본을 그룹으로 묶어 이중화하는 기능
- [ ] Synchronous vs Asynchronous Commit / 커밋을 복제본 응답까지 기다릴지 정하는 방식
- [ ] Readable Secondary Replicas / 대기 복제본에서 읽기 부하를 분산하는 구성
- [ ] Automatic vs Manual Failover / 장애 시 전환을 자동으로 할지 수동으로 할지
- [ ] Failover Cluster Instance (FCI) / 공유 스토리지로 인스턴스 자체를 전환하는 방식
- [ ] Replication / 변경분을 다른 서버로 지속 전파하는 복제 `선택`

## 15. Security

- [ ] Logins vs Database Users / 인스턴스 단위 로그인과 DB 단위 사용자의 구분
- [ ] Server Roles and Database Roles / 권한을 묶어 부여하는 인스턴스·DB 단위 역할
- [ ] Permission Model / 허용·거부·회수로 권한을 다루는 체계
- [ ] Ownership Chaining / 객체 간 소유자가 같으면 권한 검사를 건너뛰는 동작
- [ ] Transparent Data Encryption (TDE) / 디스크에 저장된 파일 전체를 암호화하는 기능
- [ ] Always Encrypted / 서버조차 평문을 못 보게 클라이언트에서 암호화하는 기능
- [ ] Dynamic Data Masking and Row-Level Security / 값을 가리거나 행 접근을 제한하는 접근 통제
- [ ] SQL Server Audit / 정해진 이벤트를 감사 로그로 남기는 기능

## 16. Operations and Automation

### Scheduled Tasks

- [ ] SQL Server Agent Jobs / 정해진 일정에 작업을 자동 실행하는 스케줄러
- [ ] Maintenance Plans / 백업·정리 작업을 마법사로 묶어 예약하는 기능
- [ ] Integrity Checks / 페이지 손상 여부를 검사하는 명령
- [ ] Statistics and Index Maintenance Schedule / 통계 갱신과 인덱스 정리를 도는 유지보수 일정

### Configuration Management

- [ ] Instance Configuration / 인스턴스 전역 옵션을 조회·변경하는 절차
- [ ] Database Scoped Configuration / 인스턴스 대신 DB 단위로 거는 설정 재정의
- [ ] Patching / 누적 업데이트로 버그·보안을 패치하는 주기

### Migration

- [ ] Data Migration Assistant / 다른 버전·DB에서 이전 시 호환성을 점검하는 도구
- [ ] Backup and Restore vs Detach and Attach / DB를 옮길 때 두 이전 방식의 차이
- [ ] Bulk Load / 대량 데이터를 한 번에 밀어 넣는 적재 방법

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- .NET 백엔드 연동 `software/skill-based/Frameworks/aspnet-core.md`
- PostgreSQL 운영 · DBA 업무 전반 `software/role-based/postgresql-dba.md`
- 데이터 파이프라인 `software/role-based/data-engineer.md`
- BI 리포팅 `software/skill-based/Data-DB/power-bi.md`
- 확장 설계 `software/skill-based/CS-Theory/system-design.md`
