# Sequelize `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Sequelize

## 1. What is Sequelize?

- [ ] Promise-based Node.js ORM / 콜백 없이 프라미스로 질의를 돌려주는 ORM
- [ ] Active Record Pattern / 인스턴스가 자기 행을 직접 저장하는 방식
- [ ] JavaScript-first / 타입 정보가 뒤늦게 덧붙는 자바스크립트 우선 설계
- [ ] Sequelize vs Prisma and TypeORM / 모델을 런타임에 만드는 쪽과 미리 선언하는 쪽의 갈림
- [ ] Supported Dialects / 같은 코드가 방언마다 다른 SQL로 나가는 범위

## 2. Getting Started

### Installation / Connection

- [ ] Sequelize Installation and Dialect Driver / 방언마다 드라이버 패키지를 따로 까는 규칙
- [ ] Sequelize Instance and Connection URI / 접속 정보 하나로 모델 전체를 묶는 객체
- [ ] authenticate / 연결이 실제로 열리는지 미리 던져 보는 확인
- [ ] Connection Pool Options / 연결을 재사용하려고 미리 열어 두는 개수 설정
- [ ] Logging Options / 나가는 SQL을 콘솔이나 함수로 뽑는 설정

### CLI `선택`

- [ ] sequelize-cli and db:migrate / 스키마 변경을 셸에서 굴리는 별도 도구
- [ ] .sequelizerc / 설정과 마이그레이션 폴더 경로를 CLI에 알리는 파일

## 3. Model Definition Styles `택 1`

- [ ] sequelize.define / 이름과 속성 객체로 모델을 찍어내는 함수 `추천`
- [ ] Model.init and Class Extends / 클래스를 상속해 인스턴스 메서드를 붙이는 방식
- [ ] sequelize-typescript Decorators / 클래스 필드 표기로 모델을 선언하는 확장 패키지 `선택`

---

# PART 2 · Models and Associations

## 4. Model Definition

### Attribute Definition

- [ ] DataTypes / JS 값을 방언별 컬럼 타입으로 옮기는 대응표
- [ ] allowNull, defaultValue, unique / 널 허용과 기본값과 중복 금지를 속성에 박는 선언
- [ ] primaryKey and autoIncrement / 기본키를 DB 증가 번호에 맡기는 선언
- [ ] field and Column Name Mapping / JS 속성명과 실제 컬럼명을 따로 두는 매핑
- [ ] Getters and Setters / 읽고 쓸 때 값을 가공해 내보내는 자리
- [ ] Virtual Field and DataTypes.VIRTUAL / 컬럼 없이 다른 값에서 계산해 두는 속성

### Model Options

- [ ] tableName and freezeTableName / 모델 이름을 복수형으로 바꾸는 것을 막는 설정
- [ ] timestamps and createdAt, updatedAt / 생성과 수정 시각 컬럼을 자동으로 다는 설정
- [ ] paranoid and Soft Delete / 행을 지우는 대신 삭제 시각만 남기는 방식
- [ ] underscored / 캐멀케이스 속성을 스네이크 컬럼으로 굳히는 설정
- [ ] indexes / 모델 선언 안에서 인덱스를 함께 적는 자리
- [ ] defaultScope / 모든 조회에 조건이 몰래 따라붙는 함정

### Validation

- [ ] Attribute Validators / isEmail·len으로 저장 전 값을 거르는 검사
- [ ] Custom Validator / 직접 짠 함수로 값의 조건을 판별하는 자리
- [ ] Model-level Validation / 여러 속성을 함께 봐야 하는 조건의 자리
- [ ] Validation vs Database Constraint / 앱에서 막을지 DB에 박을지 가르는 기준

## 5. Synchronization & Migrations

- [ ] sync / 모델 선언을 테이블로 바로 밀어 넣는 지름길
- [ ] Migration File Structure / 되돌릴 수 있게 up과 down 한 쌍으로 적는 구조
- [ ] queryInterface API / 마이그레이션 안에서 스키마를 고치는 명령 묶음
- [ ] migration:generate and db:migrate:undo / 빈 파일을 만들고 마지막 적용을 되감는 명령
- [ ] SequelizeMeta Table / 적용한 마이그레이션 파일명을 DB에 남기는 표
- [ ] Seeders and db:seed / 초기 데이터 투입을 스키마 변경과 갈라 굴리는 갈래
- [ ] Production Migration Strategy / 무중단으로 컬럼을 더하고 지우는 순서

## 6. Associations

- [ ] hasOne and belongsTo / 외래키를 어느 쪽 테이블에 두느냐로 갈리는 1대1
- [ ] hasMany and belongsToMany / 중간 테이블이 필요한지로 갈리는 두 다중 관계
- [ ] through Model / 중간 테이블 자체에 컬럼을 붙이는 방법
- [ ] foreignKey, sourceKey, targetKey / 관계가 이을 컬럼을 직접 지정하는 옵션
- [ ] as and Alias / 같은 모델을 여러 관계로 붙일 때 가르는 이름
- [ ] onDelete and onUpdate / 부모 행이 사라질 때 자식을 처리하는 규칙
- [ ] Self-association / 같은 모델끼리 부모와 자식으로 잇는 관계
- [ ] Polymorphic Association Pattern / 여러 모델을 한 컬럼으로 가리키는 우회 방식
- [ ] Association Mixins / 관계 선언에서 인스턴스 메서드가 생겨나는 규칙
- [ ] Model Registration Order and Circular References / 모델이 서로를 참조해 로딩 순서가 꼬이는 함정

---

# PART 3 · Queries

## 7. Basic Queries

- [ ] CRUD / SQL 대신 모델 메서드로 행을 다루는 창구
- [ ] findByPk and findOrCreate / 키로 한 행을 집거나 없으면 만드는 조회
- [ ] upsert / 방언마다 다른 중복 키 처리에 한 메서드를 씌운 것
- [ ] bulkCreate / 여러 행을 질의 하나로 몰아 넣는 메서드
- [ ] count and findAndCountAll / 목록과 전체 개수를 함께 받는 페이지 조회
- [ ] increment and decrement / 값을 읽지 않고 DB에서 더하고 빼는 메서드

## 8. Query Options

- [ ] Where Clause Composition / 조건을 객체 중첩으로 쌓아 올리는 방법
- [ ] Operators / 비교와 범위 연산자를 Op 심볼 키로 적는 방식
- [ ] Op.and, Op.or, Op.not / 조건 묶음을 논리 연산으로 겹치는 방법
- [ ] attributes and exclude / 가져올 컬럼을 고르거나 빼는 선택
- [ ] order, group, having / 정렬과 묶음과 묶음 조건을 옵션으로 넘기는 자리
- [ ] limit and offset / 뒷장으로 갈수록 느려지는 페이지 자르기
- [ ] raw and nest / 인스턴스 대신 순수 객체로 결과를 받는 옵션
- [ ] Sequelize.literal, fn, col / 객체로 못 적는 SQL 조각을 끼워 넣는 도구

## 9. Eager & Lazy Loading

- [ ] include and Eager Loading / 관계를 조인 한 번으로 함께 끌어오는 옵션
- [ ] Nested include / 관계의 관계까지 파고들어 붙이는 중첩
- [ ] required / 조인을 안쪽으로 바꿔 부모까지 걸러내는 옵션
- [ ] Where Conditions Inside include / 자식 조건이 부모 결과를 줄이는 지점
- [ ] separate / 조인 대신 질의를 나눠 중복 행을 피하는 옵션
- [ ] Lazy Loading / 필요해질 때 관계를 따로 불러오는 호출
- [ ] limit with include Duplicate Row Pitfall / 조인 중복 탓에 잘라낸 개수가 어긋나는 함정

## 10. Instances

- [ ] Model Instance vs Plain Object / dataValues를 품은 객체와 순수 객체의 차이
- [ ] save, reload, destroy / 인스턴스가 스스로 자기 행을 다루는 메서드
- [ ] changed and previous / 바뀐 필드만 골라 UPDATE에 싣는 추적
- [ ] toJSON / 응답에 실을 때 dataValues만 꺼내는 변환
- [ ] Instance Methods and Class Methods / 행 하나에 붙일지 모델에 붙일지 가르는 자리

## 11. Transactions

- [ ] Unmanaged Transaction / 커밋과 롤백을 손으로 불러야 하는 트랜잭션
- [ ] Managed Transaction / 콜백이 끝나면 알아서 커밋되는 트랜잭션
- [ ] Transaction Option Propagation / 질의마다 트랜잭션 객체를 넘겨야 하는 부담
- [ ] CLS / 트랜잭션을 인자 없이 물려주는 문맥 저장소
- [ ] Isolation Level / 동시 트랜잭션이 서로를 얼마나 보는지 정하는 단계
- [ ] Row Lock / 조회한 행을 다른 트랜잭션이 못 건드리게 잡는 옵션

---

# PART 4 · Advanced and Operations

## 12. Hooks

- [ ] Hook Types / 저장 앞뒤 어느 시점에 끼어들지 고르는 종류
- [ ] Bulk Hooks and individualHooks / 묶음 처리에서 행별 훅이 건너뛰어지는 함정
- [ ] Model Hooks vs Global Hooks / 모델 하나에 걸지 전체에 걸지 가르는 범위
- [ ] Passing Transaction Inside Hooks / 훅 안 질의가 트랜잭션 밖으로 새는 문제
- [ ] Password Hashing Pattern / 저장 직전에 값을 바꿔치기하는 훅 용례
- [ ] Debugging Problems from Hook Overuse / 숨은 부수효과 탓에 원인을 못 찾는 대가

## 13. Scopes

- [ ] Named Scope / 자주 쓰는 조회 조건에 이름을 붙여 두는 것
- [ ] Scope Merging and withScope / 스코프를 겹칠 때 조건이 덮이는 규칙
- [ ] unscoped / 기본 스코프가 붙인 조건을 벗겨 내는 호출
- [ ] Function Scope and Parameterized / 인자를 받아 조건을 만들어 내는 스코프

## 14. Raw & Advanced

- [ ] sequelize.query / 원문 SQL에 값을 안전하게 끼워 넣는 두 방식
- [ ] QueryTypes / 원문 질의 결과를 무슨 모양으로 받을지 정하는 표시
- [ ] Writing Subqueries / 옵션으로 못 짜는 질의를 안쪽에 끼워 넣는 방법
- [ ] JSON and JSONB Query / 방언별 JSON 연산자를 감싸 조회하는 방법 `선택`
- [ ] Custom DataType / 방언 타입과 JS 값 사이 변환을 직접 짜는 확장

## 15. Performance & Operations

- [ ] N+1 Problem Diagnosis / 로그에 같은 질의가 반복되는지 보고 잡는 진단
- [ ] benchmark and Query Logging / 질의마다 걸린 시간을 로그에 함께 찍는 옵션
- [ ] Pool Tuning / 커넥션이 모자라 대기가 터질 때 맞추는 수치
- [ ] Read Replica Configuration / 읽기 질의를 복제본으로 흘려보내는 설정
- [ ] retry / 교착이나 일시 오류에 걸린 질의를 다시 던지는 설정

## 16. Testing & TypeScript

- [ ] SQLite in-memory Test / 운영 방언과 다른 DB로 검사할 때 생기는 차이
- [ ] Transaction Rollback Isolation / 검사마다 롤백해 데이터를 되돌리는 방법
- [ ] Factory / 검증용 행을 규칙대로 찍어내는 생성기
- [ ] Model Typing / 런타임 모델에서 속성 타입을 끌어내는 선언
- [ ] Migration in CI/CD / 배포 전에 스키마 적용을 자동으로 거는 단계

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- JavaScript · TypeScript `software/skill-based/Languages/javascript.md`, `typescript.md`
- Node.js `software/skill-based/Frameworks/nodejs.md`
- 다른 ORM `software/skill-based/Frameworks/prisma.md`, `typeorm.md`
- MySQL · PostgreSQL `software/skill-based/Data-DB/mysql.md`, `software/role-based/postgresql-dba.md`
- 백엔드 전반 `software/role-based/backend.md`
