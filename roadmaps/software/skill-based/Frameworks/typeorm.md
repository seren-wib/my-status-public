# TypeORM `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to TypeORM

## 1. What is TypeORM?

### Overview of TypeORM / What is it?

- [ ] Decorator-based ORM for TypeScript / 클래스에 표시를 달아 테이블을 유추하는 ORM
- [ ] Metadata and Reflection / 데코레이터가 남긴 타입 정보를 실행 중에 읽는 구조
- [ ] Data Mapper and Active Record Dual Support / 두 접근 방식을 한 라이브러리에 함께 둔 구성
- [ ] TypeORM vs Prisma and Sequelize / 스키마를 어디에 적는지로 갈리는 세 ORM의 차이

### Supported Drivers

- [ ] PostgreSQL, MySQL, MariaDB / 기능 지원이 가장 온전한 주력 드라이버 묶음
- [ ] SQLite, SQL Server, Oracle / 방언 차이로 컬럼 타입이 어긋나는 나머지 드라이버
- [ ] MongoDB / 관계 대신 문서를 다뤄 기능이 좁아지는 드라이버 `선택`

## 2. Getting Started

### Installation / Configuration

- [ ] typeorm Installation and reflect-metadata / 타입 정보를 읽으려 함께 까는 짝 패키지
- [ ] tsconfig, experimentalDecorators, emitDecoratorMetadata / 컴파일러가 타입 정보를 남기게 켜는 설정
- [ ] typeorm CLI and init / 설정·엔티티·마이그레이션 뼈대를 찍어내는 명령

### DataSource

- [ ] DataSource Definition / 연결 정보와 엔티티 목록을 한 곳에 모은 선언
- [ ] Connection Options, host, entities, migrations / 어디에 붙고 무엇을 읽을지 적는 자리
- [ ] initialize and destroy / 메타데이터 수집과 풀 정리를 여닫는 두 시점
- [ ] synchronize Option and Production Risk / 스키마를 엔티티에 맞추다 데이터를 날리는 위험

## 3. Access Patterns `택 1`

- [ ] Data Mapper and Repository / 엔티티에서 저장 책임을 떼어 창구로 옮기는 방식 `추천`
- [ ] Active Record and BaseEntity / 엔티티 클래스가 저장 메서드를 직접 물고 있는 방식

---

# PART 2 · Entity Modeling

## 4. Entity Basics

### Entity Definition

- [ ] @Entity / 클래스 하나를 테이블 하나로 등록하는 표시
- [ ] @Column / 속성을 컬럼으로 올리고 저장 형을 정하는 표시
- [ ] @PrimaryColumn and @PrimaryGeneratedColumn / 키 값을 직접 넣을지 DB 생성에 맡길지의 선택
- [ ] Column Types and Type Mapping / TS 타입을 드라이버별 컬럼 타입으로 옮기는 규칙
- [ ] Column Options, nullable, default, length, unique / 제약을 스키마 대신 클래스에 적는 자리

### Special Columns

- [ ] Timestamp Columns, @CreateDateColumn, @UpdateDateColumn, @DeleteDateColumn / 생성·수정·삭제 시각을 자동으로 채우는 컬럼
- [ ] @VersionColumn / 저장할 때마다 올라가는 낙관적 잠금용 번호
- [ ] @Generated, uuid, increment / 키가 아닌 컬럼에도 자동 값을 붙이는 표시

### Structuring

- [ ] Embedded Entity / 여러 엔티티가 공유하는 컬럼 묶음을 빼낸 클래스
- [ ] Entity Inheritance, Single Table, Concrete Table / 상속 계층을 한 테이블에 담을지 나눌지의 전략
- [ ] EntitySchema / 데코레이터 대신 객체로 매핑을 적는 선언 방식

## 5. Relations

- [ ] @OneToOne and @JoinColumn / 외래키를 어느 쪽에 둘지 지정하는 짝
- [ ] @OneToMany and @ManyToOne / 외래키를 쥔 쪽을 기준으로 양방향을 잇는 짝
- [ ] @ManyToMany and @JoinTable / 중간 테이블을 대신 만들어 주는 선언
- [ ] Self-referencing Relation / 같은 엔티티끼리 부모와 자식으로 잇는 관계
- [ ] Cascade Options / 부모를 저장할 때 자식까지 함께 반영하는 범위
- [ ] onDelete and onUpdate / 부모 행이 사라질 때 DB가 할 동작 지정
- [ ] Eager vs Lazy Relations / 항상 함께 불러올지 접근할 때 부를지의 선택
- [ ] @RelationId / 관계 객체 없이 외래키 값만 꺼내 두는 표시
- [ ] Tree Entities and Closure Table / 계층 구조를 경로 테이블로 대신 관리하는 방식 `선택`

## 6. Indices & Constraints

- [ ] @Index and Composite Index / 인덱스를 스키마가 아닌 클래스에 붙이는 표시
- [ ] @Unique / 여러 컬럼을 묶어 중복을 막는 제약 선언
- [ ] @Check and @Exclusion / 값 조건과 범위 겹침을 DB에 맡기는 제약
- [ ] Constraint Naming Strategy / 자동 생성 이름이 DB마다 어긋나는 것을 고정하는 규칙

## 7. Migrations

- [ ] migration:generate / 엔티티와 실제 스키마의 차이를 SQL로 뽑는 명령
- [ ] migration:create / 내용이 빈 마이그레이션 파일만 만드는 명령
- [ ] migration:run and migration:revert / 적용 이력을 테이블에 남기고 되감는 명령
- [ ] up and down / 되돌릴 수 있게 반대 연산을 함께 적는 자리
- [ ] QueryRunner in Migration / 마이그레이션 안에서 원시 SQL을 실행하는 통로
- [ ] migrationsRun and migrationsTableName / 실행 시점과 이력 테이블 이름을 정하는 설정
- [ ] synchronize vs Migration Operational Strategy / 개발 편의와 운영 안전 중 무엇을 택할지의 기준
- [ ] Seeding Strategy / 초기 데이터를 마이그레이션과 분리해 넣는 방법

---

# PART 3 · Data Manipulation

## 8. Repository API

- [ ] DataSource.getRepository / 엔티티 종류마다 창구 객체를 꺼내 오는 함수
- [ ] Read, find, findOne, findBy, findAndCount / 조건 객체만 넘겨 조회하는 읽기 함수 묶음
- [ ] Write, save, insert, update, delete, remove / 엔티티를 거치는 쓰기와 바로 SQL을 쏘는 쓰기의 구분
- [ ] upsert / 충돌 컬럼을 지정해 넣거나 고치게 하는 함수
- [ ] Soft Delete, softDelete, restore / 행을 지우지 않고 삭제 시각만 남기는 방식
- [ ] count and exists / 본체를 안 읽고 개수와 존재만 확인하는 함수
- [ ] Custom Repository and extend / 자주 쓰는 질의를 창구에 붙여 두는 확장 방법

## 9. Find Options

- [ ] FindOptionsWhere Structure / 조건을 SQL 대신 중첩 객체로 적는 모양
- [ ] Find Operators, In, Like, Between, MoreThan, IsNull, Not / 비교 연산을 함수 호출로 감싼 조건 표현
- [ ] select and Partial Selection / 필요한 컬럼만 골라 반쪽 객체로 받는 옵션
- [ ] relations Option / 함께 채울 관계를 이름으로 적어 조인하는 옵션
- [ ] order, skip, take / 정렬과 페이지 구간을 옵션으로 넘기는 자리
- [ ] withDeleted / 소프트 삭제된 행까지 조회에 포함하는 옵션
- [ ] Nested Relation Conditions / 관계 안쪽 컬럼을 조건으로 걸 때의 중첩 규칙

## 10. QueryBuilder

### Basics

- [ ] createQueryBuilder and Alias / 별칭을 붙여 SQL을 조립해 나가는 시작점
- [ ] select and addSelect / 가져올 컬럼을 덮어쓸지 덧붙일지의 구분
- [ ] where, andWhere, orWhere / 조건을 이어 붙일 때 괄호가 안 잡히는 함정
- [ ] Parameter Binding and setParameter / 값을 문자열로 잇지 않고 이름으로 넘기는 방법
- [ ] orderBy, groupBy, having / 집계와 정렬 절을 메서드로 옮겨 적는 자리
- [ ] limit-offset vs take-skip Difference / 조인이 있을 때 결과 수가 어긋나는 두 절의 차이

### Join

- [ ] innerJoin and leftJoin / 관계 없는 행을 버릴지 남길지 정하는 두 조인
- [ ] leftJoinAndSelect / 조인한 테이블 컬럼까지 엔티티에 채워 주는 호출
- [ ] Join Condition / 관계 밖 조건을 ON에 붙여 조인을 좁히는 방법
- [ ] Subquery and Subselect / 질의 하나를 조건이나 컬럼 자리에 끼우는 방법

### Execution and Mutation

- [ ] Result Retrieval, getOne, getMany, getRawMany, getManyAndCount / 엔티티로 받을지 원시 행으로 받을지 정하는 호출
- [ ] Insert, Update, Delete QueryBuilder / 엔티티를 안 거치고 바로 쓰기 SQL을 짜는 방법
- [ ] Relation QueryBuilder, add, remove / 양쪽을 다 안 불러오고 관계만 고치는 방법
- [ ] Join + Pagination Duplicate Row Pitfall / 조인으로 행이 불어나 take 개수가 어긋나는 함정

## 11. Transactions

- [ ] DataSource.transaction / 콜백 하나로 커밋과 롤백을 감싸는 방법
- [ ] QueryRunner Manual Control / 시작·커밋·해제를 직접 잡고 놓는 저수준 통로
- [ ] Isolation Level / 다른 트랜잭션의 변경을 어디까지 볼지 정하는 단계
- [ ] Pessimistic Lock and Optimistic Lock / 미리 잠글지 버전 충돌로 잡을지의 선택
- [ ] Transaction Context Propagation and typeorm-transactional / 매니저를 인자로 안 넘기고 이어 주는 방법

---

# PART 4 · Advanced and Operations

## 12. Subscribers & Listeners

- [ ] Entity Listeners, @BeforeInsert, @AfterLoad, @BeforeUpdate / 저장 전후 시점에 엔티티 메서드를 끼우는 표시
- [ ] EventSubscriberInterface / 엔티티 밖에서 전 이벤트를 받아 처리하는 클래스
- [ ] Audit Log Implementation Pattern / 변경 이력을 구독자로 자동 남기는 구성

## 13. Performance

- [ ] N+1 Problem / 관계마다 질의가 따로 나가 횟수가 불어나는 함정
- [ ] Query Logging / 실제로 나간 SQL을 눈으로 확인하는 설정
- [ ] Query Result Cache / 같은 질의 결과를 정해진 시간 동안 재사용하는 기능
- [ ] Connection Pool Configuration / 동시에 붙는 연결 수와 대기 한도를 정하는 설정
- [ ] Raw Query and DataSource.query / 매핑을 포기하고 SQL을 그대로 보내는 통로
- [ ] Bulk Insert Optimization and chunk / 행을 나눠 담아 파라미터 한도를 피하는 방법

## 14. Framework Integration

- [ ] NestJS and @nestjs/typeorm / 창구 객체를 의존성 주입으로 받는 연동 모듈 `추천`
- [ ] Express / 앱이 뜰 때 연 연결을 직접 들고 다니는 방식
- [ ] Multiple DataSource and Multi-tenant / 테넌트마다 연결을 나눠 잡는 구성

## 15. Testing & Operations

- [ ] SQLite in-memory Test Database / 드라이버 방언 차이로 검증이 새는 대체 수단
- [ ] Docker-based Integration Test / 실제 DB를 컨테이너로 띄워 맞춰 보는 검증
- [ ] Transaction Rollback Isolation / 테스트마다 롤백해 데이터를 되돌리는 격리
- [ ] Migration in CI/CD / 배포 파이프라인에서 스키마 적용을 거는 자리
- [ ] Schema Drift Check and schema:log / 엔티티와 실제 스키마가 벌어졌는지 보는 명령

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- Node.js `software/skill-based/Frameworks/nodejs.md`
- 다른 ORM `software/skill-based/Frameworks/prisma.md`, `sequelize.md`
- 백엔드 전반 `software/role-based/backend.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
