# MariaDB `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to MariaDB

## 1. What is MariaDB?

### Overview of MariaDB / What is it?

- [ ] MySQL Fork / 소스 코드가 갈라져 나온 배경
- [ ] MariaDB Foundation / 비영리 재단이 운영을 주도하는 구조
- [ ] Server vs Enterprise vs SkySQL / 커뮤니티·기업·클라우드 제품 구분
- [ ] Licensing / GPLv2와 BSL이 섞인 라이선스 체계

### Relationship with MySQL

- [ ] Wire Protocol Compatibility / MySQL 클라이언트가 그대로 붙는 이유
- [ ] Version Divergence / 5.5 분기 이후 벌어진 기능 격차
- [ ] Feature Gaps / JSON·GTID·복제 구현이 서로 다른 지점
- [ ] Migration Path / MySQL에서 옮겨오는 절차
- [ ] Compatibility Checkpoints / 버전마다 달라진 호환 확인 지점

## 2. Getting Started

### Installation `택 1`

- [ ] Docker and Docker Compose / 컨테이너로 격리해 띄우는 방법 `추천`
- [ ] Official Repository / OS 기본 패키지 대신 MariaDB 저장소를 쓰는 이유
- [ ] Binary Tarball / 압축 파일을 풀어 수동 배치하는 방식

### Basic Configuration

- [ ] mariadb CLI / mysql 명령과 심볼릭 링크로 묶인 구조
- [ ] Configuration Layout / my.cnf와 conf.d로 나뉜 설정 구조
- [ ] mariadb-secure-installation / 설치 직후 취약 설정을 없애는 절차
- [ ] Version Selection / LTS와 롤링 릴리스 중 고르는 기준

## 3. MariaDB-Specific Features

### SQL Extensions

- [ ] Sequences / 테이블 없이 증가값을 관리하는 객체
- [ ] Virtual and Persistent Columns / 계산식으로 값을 채우는 컬럼
- [ ] System-Versioned Tables / 과거 시점 값을 그대로 조회하는 기능
- [ ] Application-Time Period Tables / 유효기간을 컬럼으로 관리하는 테이블
- [ ] Invisible Columns / SELECT *에서 숨기는 컬럼 속성
- [ ] RETURNING Clause / INSERT·UPDATE 결과를 바로 돌려받는 절
- [ ] Oracle Compatibility Mode / sql_mode를 ORACLE로 바꾸는 옵션 `선택`

### Data Type Differences

- [ ] JSON as LONGTEXT / MySQL과 달리 텍스트 타입에 함수만 얹은 방식
- [ ] UUID Type / 문자열 대신 전용 타입으로 저장하는 UUID
- [ ] INET4 and INET6 Types / IP 주소를 전용 타입으로 저장하는 기능
- [ ] Dynamic Columns / 한 컬럼에 이름·값 쌍을 가변으로 담는 기능 `선택`

---

# PART 2 · Storage Engines and Optimizer

## 4. Storage Engine Architecture

- [ ] Pluggable Engine API / 저장 엔진을 갈아 끼우는 구조
- [ ] Per-table Engine Assignment / 테이블마다 다른 엔진을 쓰는 설정
- [ ] Workload-based Engine Selection / 작업 성격에 맞춰 엔진을 고르는 기준

## 5. Transactional Engines

- [ ] InnoDB / 트랜잭션이 필요할 때 쓰는 기본 엔진 `추천`
- [ ] XtraDB / 한때 기본이었던 InnoDB 포크 엔진
- [ ] MyRocks / 쓰기 몰릴 때 유리한 LSM 트리 엔진
- [ ] Aria / 장애에도 안전한 MyISAM 후속 엔진

## 6. Analytical and Special Engines

- [ ] ColumnStore / 집계 분석에 유리한 컬럼 저장 엔진
- [ ] Spider / 여러 서버로 테이블을 쪼개 붙이는 엔진
- [ ] CONNECT / 외부 파일·DB를 테이블처럼 읽는 엔진
- [ ] FederatedX / 원격 테이블을 로컬처럼 연결하는 엔진
- [ ] S3 Storage Engine / 안 쓰는 테이블을 S3로 옮겨 보관하는 엔진
- [ ] Sequence Engine / 시퀀스 객체를 테이블처럼 다루는 내부 엔진

## 7. Optimizer Differences

- [ ] Optimizer Switch / 최적화 기법을 개별로 켜고 끄는 설정
- [ ] Subquery Optimization / 세미조인·구체화로 서브쿼리를 접는 기법
- [ ] Join Optimization / 해시로 블록 단위 조인을 묶는 기법
- [ ] Index Condition Pushdown and Multi-Range Read / 정렬 접근으로 스토리지 왕복을 줄이는 기법
- [ ] Engine-independent Statistics / 엔진과 무관하게 별도로 쌓는 통계
- [ ] ANALYZE Statement / 예측과 실제 행수 차이를 보여주는 문
- [ ] EXPLAIN FORMAT=JSON / 실행 계획을 구조화된 형태로 보는 방법
- [ ] Optimizer Trace / 옵티마이저가 고려한 후보 계획을 남기는 로그

---

# PART 3 · Replication and Clustering

## 8. Replication

- [ ] Binary Log Formats / 변경분을 행·문장·혼합으로 기록하는 방식
- [ ] MariaDB GTID / 도메인·서버·순번 세 값으로 된 트랜잭션 ID
- [ ] Incompatibility with MySQL GTID / MySQL과 GTID 형식이 달라 안 섞이는 지점
- [ ] Multi-Source Replication / 여러 마스터에서 한 레플리카로 받는 복제
- [ ] Parallel Replication / 낙관·보수 두 방식으로 병렬 적용하는 복제
- [ ] Semi-Sync Replication / 레플리카 수신까지 확인하고 커밋하는 복제
- [ ] Delayed Replica / 실수 복구용으로 일부러 지연시킨 복제본
- [ ] Replication Interop Constraints with MySQL / MySQL과 복제로 못 섞이는 제약

## 9. Galera Cluster

### Concepts

- [ ] Virtually Synchronous Multi-Master / 모든 노드에 동시에 쓰는 다중 마스터 구조
- [ ] Certification-based Replication / 커밋 시점에 충돌 여부를 심사하는 복제
- [ ] Write Set / 트랜잭션 변경분을 묶어 전파하는 단위
- [ ] Global Transaction Ordering / 전 노드가 합의하는 커밋 순서

### Configuration

- [ ] Node Bootstrap / 첫 노드를 새 클러스터로 띄우는 절차
- [ ] State Transfer / 합류 노드가 데이터를 통째로 받는 과정
- [ ] SST Methods / 전체 상태를 넘기는 백업·복사 수단
- [ ] Quorum and Split-brain / 과반 유실 시 갈라짐을 막는 감시자 노드

### Operational Considerations

- [ ] Cluster-wide Conflict / 같은 행에 몰려 인증 실패가 잦은 지점
- [ ] Flow Control / 느린 노드에 맞춰 쓰기를 멈추는 제어
- [ ] DDL Handling / 전체 동기 방식과 개별 실행 방식 중 고르는 처리
- [ ] Limitations / InnoDB 전용이고 외래키가 불안정한 제약
- [ ] Rolling Restart and Upgrade / 노드를 한 대씩 내려 갈아치우는 절차

## 10. MaxScale

- [ ] Read/Write Split Router / 읽기와 쓰기를 다른 노드로 나누는 라우터
- [ ] Connection Router / 연결을 그대로 전달만 하는 라우터
- [ ] Monitor / 노드 상태를 감시해 자동으로 승격시키는 기능
- [ ] Filters / 쿼리를 가로채 막거나 캐싱하는 모듈
- [ ] Binlog Router / 바이너리 로그를 대신 중계하는 라우터

---

# PART 4 · Operations

## 11. Configuration and Tuning

- [ ] Memory Configuration / 엔진별 버퍼 크기를 나눠 배분하는 설정
- [ ] Thread Pool / 연결마다 스레드를 안 만들고 재사용하는 방식
- [ ] Durability / 커밋마다 디스크에 내려쓰는 정도를 정하는 설정
- [ ] Query Cache Status / 병목만 키워 폐기 수순인 캐시 기능
- [ ] Slow Query Log / 느린 쿼리를 남기는 로그의 상세도 설정
- [ ] Information Schema Extensions / 성능 스키마 등 MariaDB 전용 확장 뷰

## 12. Backup and Recovery

- [ ] mariabackup / 파일 단위로 통째로 뜨는 물리 백업 `추천`
- [ ] mariadb-dump / SQL 문으로 데이터를 뽑는 논리 백업
- [ ] Point-in-Time Recovery / 바이너리 로그로 특정 시점까지 되돌리는 복구
- [ ] Backup in a Galera Cluster / 노드 한 대를 빼서 뜨는 백업 방식
- [ ] Restore Verification / 복구본이 실제로 살아나는지 확인하는 절차

## 13. Security

- [ ] Authentication Plugins / 인증 방식을 플러그인으로 바꿔 끼는 구조
- [ ] Roles and Privileges / 권한을 묶어 역할로 부여하는 체계
- [ ] TLS Configuration / 접속 구간을 암호화하는 인증서 설정
- [ ] Data-at-Rest Encryption / 저장 파일 자체를 암호화하는 키 관리 체계
- [ ] Audit Plugin / 접속·쿼리 이력을 남기는 감사 플러그인

## 14. Upgrade and Migration

- [ ] mariadb-upgrade / 업그레이드 후 시스템 테이블을 맞추는 도구
- [ ] Major Version Upgrade Path / 메이저 버전을 순서대로 건너는 절차
- [ ] MySQL to MariaDB Migration Procedure / 데이터를 옮기고 호환성을 검증하는 순서
- [ ] MariaDB to MySQL Rollback Constraints / 되돌아갈 때 못 쓰는 MariaDB 전용 기능
- [ ] Deprecated Feature Review / 버전마다 사라진 기능을 점검하는 작업

---

# 이 로드맵 밖

- MySQL 엔진 · 인덱스 · InnoDB 내부 `software/skill-based/Data-DB/mysql.md`
- SQL 문법 `software/skill-based/Languages/sql.md`
- PostgreSQL 운영 `software/role-based/postgresql-dba.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
- 서버 운영 기초 `software/skill-based/Infra-DevOps/linux.md`
- 백엔드 전반 `software/role-based/backend.md`
