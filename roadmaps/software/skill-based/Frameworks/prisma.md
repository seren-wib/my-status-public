# Prisma `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Prisma

## 1. What is Prisma?

### Overview of Prisma / What is it?

- [ ] Type-safe ORM for Node.js and TypeScript / 질의 결과 모양까지 타입으로 좁히는 ORM
- [ ] Schema-first Approach / 스키마 파일 하나를 진실의 원본으로 두는 방식
- [ ] Generated Client and Code Generation / 스키마에서 뽑아낸 코드를 가져다 쓰는 구조
- [ ] Prisma vs TypeORM, Sequelize, Query Builder / 클래스가 아니라 생성물을 쓰는 쪽의 갈림

### Components

- [ ] Prisma Schema / 모델과 접속 정보를 한 파일에 모아 적는 원본
- [ ] Prisma Client / 모든 질의가 반드시 거쳐 가는 생성된 창구
- [ ] Prisma Migrate / 스키마 차이를 비교해 SQL을 뽑는 도구
- [ ] Prisma Studio / 브라우저에서 표로 행을 열어 고치는 도구

### Supported Databases

- [ ] Relational / 커넥터로 붙는 PostgreSQL·MySQL 계열 DB
- [ ] Non-relational / MongoDB 지원에서 빠지는 기능의 범위

## 2. Getting Started

### Installation / Initialization

- [ ] prisma CLI / schema.prisma와 .env 뼈대를 깔아 주는 명령
- [ ] @prisma/client Installation / 생성된 코드가 담기는 패키지를 까는 순서
- [ ] Environment Variables / 접속 문자열을 스키마 밖으로 빼 두는 이유

### First Run

- [ ] datasource Block / 어느 DB에 붙을지 스키마 안에서 고르는 선언
- [ ] generator Block / 무엇을 어디에 생성할지 정하는 선언
- [ ] prisma generate / 스키마를 읽어 클라이언트를 다시 찍는 명령
- [ ] Running Prisma Studio / 로컬 포트로 데이터 편집 화면을 여는 방법

### Starting Approach `택 1`

- [ ] Greenfield / 빈 DB에 스키마부터 적고 내려보내는 시작 `추천`
- [ ] Brownfield / 있는 DB를 읽어 스키마를 역으로 뽑는 시작

---

# PART 2 · Schema and Migrations

## 3. Prisma Schema Language

### Model Definition

- [ ] model Block / 테이블 하나를 스키마 안에서 선언하는 단위
- [ ] Scalar Types / DB 타입을 가린 공통 필드 형의 목록
- [ ] Optional vs Required Field / 물음표로 NULL 허용을 가르는 표기
- [ ] List Field / 관계 배열과 스칼라 배열이 갈리는 표기
- [ ] enum / 허용값 목록을 스키마에 박고 타입으로 뽑는 선언

### Field Attributes

- [ ] @id and @@id Composite Key / 단일 키와 컬럼 묶음 키를 표시하는 속성
- [ ] @default / 값을 DB와 클라이언트 중 어디서 채울지 정하는 속성
- [ ] @unique and @@unique / 중복 금지를 한 컬럼과 조합에 거는 속성
- [ ] @updatedAt / 쓸 때마다 시각을 클라이언트가 채우는 속성
- [ ] @map and @@map / 코드 이름과 실제 컬럼 이름을 갈라 두는 속성
- [ ] @@index / 인덱스를 스키마에 적어 마이그레이션에 태우는 속성
- [ ] Native Type Attributes / 공통 형 대신 DB 고유 타입을 지정하는 속성

## 4. Relations

- [ ] @relation Attribute / 어느 필드가 어느 키를 가리키는지 적는 속성
- [ ] One-to-One / 한쪽에만 유일 외래키를 두는 관계 모양
- [ ] One-to-Many / 배열 쪽에는 컬럼이 안 생기는 관계 모양
- [ ] Many-to-Many / 중간 테이블을 숨길지 모델로 적을지의 갈림
- [ ] Self-relation / 같은 모델끼리 이을 때 이름을 붙이는 규칙
- [ ] Relation Scalar and Foreign Key Field / 관계 필드와 짝을 이루는 실제 키 컬럼
- [ ] Referential Actions / 부모 행이 지워질 때 자식을 처리하는 규칙

## 5. Migrations

### Development Workflow

- [ ] prisma migrate dev / 스키마와 DB 차이를 비교해 SQL을 뽑는 명령
- [ ] Migration History / 적용한 파일을 DB 표에 남겨 대조하는 구조
- [ ] prisma migrate reset / 데이터를 버리고 이력을 처음부터 다시 도는 명령

### Deployment Workflow

- [ ] prisma migrate deploy / 새 SQL을 만들지 않고 남은 것만 적용하는 명령
- [ ] prisma migrate status and resolve / 어긋난 이력을 확인하고 손으로 표시하는 명령

### Advanced

- [ ] Custom SQL Migration Editing / 생성된 SQL을 적용 전에 손보는 자리
- [ ] Prototyping / 이력 파일 없이 스키마를 DB에 바로 미는 방식
- [ ] Baselining an Existing Database / 이미 있는 DB를 첫 이력으로 인정시키는 절차
- [ ] Seeding / 초기 데이터를 스크립트로 채워 넣는 자리

---

# PART 3 · Prisma Client

## 6. Basic Queries

- [ ] PrismaClient Instantiation and Singleton Pattern / 인스턴스 하나를 앱 전체가 나눠 쓰는 방식
- [ ] CRUD Queries / 모델별 객체에 붙어 나오는 기본 질의 메서드
- [ ] upsert / 조회 없이 삽입과 수정을 한 호출에 맡기는 질의
- [ ] Bulk Operations / 여러 행을 한 문장으로 처리하고 개수만 받는 질의
- [ ] count / 조건에 맞는 행 수만 세어 오는 질의

## 7. Filtering & Pagination

- [ ] where Conditions / 조건을 SQL이 아닌 중첩 객체로 적는 방식
- [ ] Comparison Operators / 크기와 포함 비교를 키 이름으로 적는 표기
- [ ] String Filters / 부분 일치와 대소문자 무시를 고르는 표기
- [ ] Logical Operators / 조건들을 배열로 묶어 겹쳐 거는 표기
- [ ] Relation Filters / 관계 행의 존재 조건으로 부모를 거르는 표기
- [ ] orderBy and Nested Sorting / 관계 필드까지 정렬 기준으로 쓰는 표기
- [ ] Pagination / 건너뛰기와 커서 기준 페이지의 갈림

## 8. Relation Queries

- [ ] include / 관계 행을 결과에 통째로 붙여 오는 옵션
- [ ] select / 고른 컬럼만 남겨 결과 타입까지 좁히는 옵션
- [ ] Nested include and select / 관계 안에서 다시 관계를 고르는 중첩 표기
- [ ] Nested Writes / 부모와 자식을 한 호출로 함께 만드는 표기
- [ ] Nested Updates / 관계를 끊고 갈아 끼우는 수정 표기
- [ ] Fluent API Traversal / 조회 결과에서 관계를 이어 타고 가는 호출

## 9. Advanced Queries

- [ ] Aggregations / 합계와 평균을 밑줄 붙은 키로 받는 질의
- [ ] groupBy and having / 묶어 집계한 뒤 집계값으로 거르는 질의
- [ ] distinct / 중복 행을 접어 하나만 남기는 옵션
- [ ] Atomic Number Operations / 읽어 오지 않고 DB에서 바로 더하는 수정
- [ ] Json Field Queries / Json 컬럼 안 경로를 조건으로 쓰는 질의
- [ ] Full-text Search / DB마다 지원이 갈리는 미리보기 검색 기능 `선택`
- [ ] Raw Queries / 생성 API로 안 되는 SQL을 직접 내려보내는 탈출구

## 10. Transactions

- [ ] Sequential Operations / 질의 배열을 한 묶음으로 순서대로 도는 방식
- [ ] Interactive Transactions / 중간 결과를 보고 다음 질의를 정하는 방식
- [ ] Isolation Level / 트랜잭션끼리 서로를 얼마나 볼지 정하는 설정
- [ ] Nested Write as Implicit Transaction / 중첩 쓰기가 알아서 한 묶음으로 도는 동작
- [ ] Optimistic Concurrency Control / 버전 컬럼을 조건에 넣어 덮어쓰기를 막는 방식

## 11. Generated Types

- [ ] Model Types / 모델 선언에서 그대로 뽑혀 나온 결과 형
- [ ] Prisma Namespace Types / 인자와 조건의 형이 모여 있는 이름 공간
- [ ] Payload Types and GetPayload / 관계를 낀 결과의 형을 끌어내는 타입
- [ ] Prisma.validator / 조건 조각을 타입 검사 붙은 채 재사용하는 함수

---

# PART 4 · Advanced and Operations

## 12. Client Extensions

- [ ] $extends Structure / 클라이언트를 감싸 새 클라이언트를 만드는 구조
- [ ] result, model, query, client Component / 확장이 끼어들 수 있는 네 지점
- [ ] Computed Field / 저장 없이 조회 결과에 덧붙이는 계산 필드
- [ ] Soft Delete Pattern / 삭제 질의를 플래그 수정으로 바꿔치는 확장

## 13. Connection & Performance

- [ ] Connection Pool / 쿼리 엔진이 쥐고 있을 연결 수의 한도
- [ ] $connect and $disconnect / 연결을 미리 열고 끝에 닫는 두 호출
- [ ] N+1 Problem and Query Batching / 같은 관계 조회를 모아 한 번에 보내는 완화
- [ ] relationLoadStrategy / 관계를 조인으로 붙일지 따로 물을지의 갈림
- [ ] Serverless / 호출마다 인스턴스가 떠 연결이 쌓이는 환경
- [ ] Prisma Accelerate / 연결 풀과 캐시를 대행하는 유료 프록시 `선택`

## 14. Logging & Error Handling

- [ ] log Levels / 실행된 SQL까지 찍을지 고르는 단계
- [ ] Event-based Logging / 로그를 콘솔 대신 이벤트로 받아 다루는 방식
- [ ] PrismaClientKnownRequestError / 코드가 붙은 예측된 실패를 담는 예외 형
- [ ] Error Codes / 유일성 위반과 대상 없음을 가르는 코드
- [ ] Validation and Initialization Error / 인자 형과 접속 실패를 가르는 예외 종류

## 15. Testing & Deployment

### Testing

- [ ] Test Database / 테스트마다 실제 DB를 컨테이너로 띄우는 방식
- [ ] Mocking Prisma Client / 생성된 클라이언트를 가짜로 바꿔 끼우는 방법
- [ ] Transaction Rollback Isolation / 테스트를 트랜잭션에 넣고 되돌려 격리하는 방법

### Deployment

- [ ] prisma generate in Build Step / 생성물이 저장소에 없어 빌드에 넣어야 하는 이유
- [ ] Migration in CI/CD / 배포 파이프라인에서 이력을 적용하는 자리
- [ ] Monorepo / 스키마를 나눠 두고 생성물을 공유하는 배치
- [ ] Next.js Hot Reload Instance Problem / 리로드마다 클라이언트가 쌓여 연결이 새는 문제

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- Node.js `software/skill-based/Frameworks/nodejs.md`
- PostgreSQL 운영 `software/role-based/postgresql-dba.md`
- 다른 ORM `software/skill-based/Frameworks/typeorm.md`, `sequelize.md`
- 백엔드 전반 `software/role-based/backend.md`
