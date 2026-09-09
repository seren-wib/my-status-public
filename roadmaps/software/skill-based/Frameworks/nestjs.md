# NestJS `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to NestJS

## 1. What is NestJS?

### Overview of NestJS / What is it?

- [ ] Opinionated Architecture Framework / 폴더와 계층 배치를 프레임워크가 정해 주는 방식
- [ ] Decorator + Dependency Injection Model / 클래스에 표식을 달아 조립하는 모델
- [ ] TypeScript-First Design / 타입 정보를 실행 중 조립에 쓰는 설계
- [ ] HTTP Adapter / Express나 Fastify로 갈아 끼우는 서버 계층

### NestJS vs Others

- [ ] NestJS vs Express / 자유를 줄여 일관성을 얻는 맞바꿈
- [ ] When to choose NestJS? / 팀 규모와 수명으로 도입을 가르는 기준

## 2. Getting Started

- [ ] Nest CLI / nest new와 generate로 뼈대를 찍어내는 도구
- [ ] Project Layout / main.ts와 app.module.ts에서 시작하는 배치
- [ ] bootstrap / NestFactory로 앱 인스턴스를 세우는 시작점
- [ ] Decorator Compilation Settings / 타입 정보를 컴파일 결과에 남기는 설정
- [ ] nest start --watch / 파일이 바뀌면 서버를 다시 띄우는 개발 실행

---

# PART 2 · Core Building Blocks

## 3. Modules

- [ ] @Module Metadata / 들여올 것과 내보낼 것을 네 칸으로 적는 표식
- [ ] Root Module and Feature Module / 루트 하나에 기능 상자를 매다는 구조
- [ ] Shared Module Pattern / 공용 제공자를 한 상자에 모아 내보내는 방식
- [ ] Global Module / 들여오지 않아도 어디서나 쓰게 여는 상자
- [ ] Dynamic Module / 설정을 인자로 받아 그때 조립되는 상자
- [ ] Circular Reference Resolution / 서로 참조하는 상자를 나중에 잇는 방법

## 4. Controllers

- [ ] @Controller / 클래스 하나에 URL 앞부분을 붙이는 표식
- [ ] Route Decorators / 메서드 위에 HTTP 동사를 붙이는 표식
- [ ] Param Decorators / 요청의 어느 부분을 받을지 인자에 적는 표식
- [ ] Response Control / 반환값 대신 표식으로 응답 형태를 정하는 방법
- [ ] API Versioning / URL이나 헤더로 버전별 핸들러를 가르는 기능
- [ ] Async Handler / Promise와 Observable을 둘 다 받아 주는 반환 규칙

## 5. Providers & Dependency Injection

- [ ] @Injectable / 주입 대상으로 등록되는 클래스 표식
- [ ] Constructor Injection / 필요한 것을 생성자 인자로 받아 오는 방식
- [ ] Provider Registration Methods / 클래스·값·공장 중 무엇을 줄지 고르는 등록
- [ ] Injection Token / 클래스가 아닌 이름표로 주입 대상을 가리키는 키
- [ ] Provider Scope / 인스턴스를 앱·요청 중 어느 단위로 만들지 정하는 설정
- [ ] Optional Dependency and Circular Injection / 대상이 없거나 서로 물렸을 때의 처리 규칙

## 6. Request Lifecycle

### Execution Order

- [ ] Middleware → Guard → Interceptor → Pipe → Handler → Filter / 요청이 핸들러에 닿기까지 거치는 고정 순서

### Components

- [ ] Middleware / 라우팅 전에 원본 요청 객체를 만지는 층
- [ ] Guards / 요청을 핸들러에 넘길지 참·거짓으로 판정하는 층
- [ ] Interceptors / 핸들러 앞뒤를 감싸 반환값을 바꾸는 층
- [ ] Pipes / 핸들러 인자를 검사하고 형을 바꾸는 층
- [ ] Exception Filters / 던져진 예외를 응답 형태로 바꾸는 층
- [ ] Application Scope / 층을 전역부터 핸들러까지 어디에 걸지 정하는 범위
- [ ] Custom Decorator / 요청에서 값을 꺼내는 표식을 직접 만드는 방법

---

# PART 3 · Data and Authentication

## 7. Configuration

- [ ] ConfigModule / 환경 변수를 주입 가능한 제공자로 감싸는 상자
- [ ] Per-Environment .env Loading / 실행 환경에 따라 다른 .env를 고르는 방법
- [ ] Schema Validation / 앱이 뜨기 전에 설정값 누락을 잡아내는 검사
- [ ] Namespaced Config / 설정을 이름 붙인 묶음으로 쪼개는 방법
- [ ] ConfigService Injection and Typing / 설정값을 타입 있는 서비스로 꺼내 쓰는 방법

## 8. Databases

### ORM `택 1`

- Prisma / 스키마 파일에서 타입 있는 클라이언트를 뽑는 ORM `software/skill-based/Frameworks/prisma.md` `추천` `위임`
- TypeORM / 엔티티 클래스에 표식을 달아 테이블로 삼는 ORM `software/skill-based/Frameworks/typeorm.md` `위임`
- [ ] Drizzle / SQL에 가까운 문법을 타입으로 감싼 쿼리 빌더
- [ ] Mongoose / MongoDB 문서에 스키마를 씌우는 라이브러리

### Integration Patterns

- [ ] Entity · Schema Definition / 저장할 형태를 클래스와 표식으로 적는 방법
- [ ] Repository Injection / 테이블 접근 객체를 제공자로 등록해 받는 방법
- [ ] Migration Workflow / 엔티티 변경을 스키마 변경 파일로 옮기는 순서
- [ ] Transaction and Unit of Work / 여러 저장소 호출을 한 작업 단위로 묶는 방법
- [ ] Multiple Database Connection / 연결마다 이름을 붙여 여러 DB를 함께 쓰는 방법

## 9. Validation & Serialization

- [ ] ValidationPipe / DTO 표식대로 본문을 검사하고 걸러 내는 층
- [ ] class-validator Decorator / 필드 위에 조건 표식을 달아 검사하는 방법
- [ ] class-transformer / 들어온 JSON을 DTO 클래스 인스턴스로 바꾸는 도구
- [ ] DTO Design / 생성·수정·응답 형태를 각각 클래스로 나누는 방법
- [ ] Mapped Types / 있는 DTO에서 골라내고 덜어내 새 DTO를 만드는 기능
- [ ] ClassSerializerInterceptor / 응답에서 비밀번호 같은 필드를 빼고 내보내는 층

## 10. Authentication & Authorization

- [ ] @nestjs/passport / Passport 전략을 제공자로 감싸 등록하는 모듈
- [ ] Local Strategy / 아이디와 비밀번호를 확인해 사용자를 붙이는 전략
- [ ] JWT Strategy / 서명된 토큰을 검증해 요청 주인을 정하는 전략
- [ ] AuthGuard Application and Public Route Exceptions / 전역 가드를 걸고 공개 경로만 빼는 방법
- [ ] Role-based Guard / 핸들러에 붙인 역할 표식을 가드가 읽는 구조
- [ ] CASL-Based Authorization / 누가 무엇에 무엇을 할 수 있는지 규칙으로 적는 방식 `선택`
- [ ] Security Configuration / 보안 헤더와 요청 횟수 제한을 앱 전역에 거는 설정

---

# PART 4 · Extended Features

## 11. Advanced Techniques

- [ ] Lifecycle Hooks / 앱이 뜨고 질 때 제공자가 받는 호출 지점
- [ ] Async Provider Initialization / 준비가 끝나야 주입되는 제공자를 만드는 방법
- [ ] Execution Context / HTTP·소켓·RPC 중 어느 통로인지 알아내는 객체
- [ ] Reflector & Discovery Usage / 실행 중에 표식과 제공자 목록을 훑는 방법
- [ ] Caching / 계산해 둔 응답을 저장소에 남겨 다시 쓰는 모듈
- [ ] Switching to Fastify Adapter / 어댑터만 갈아 HTTP 엔진을 바꾸는 방법

## 12. Async Work & Events

- [ ] Task Scheduling / 정해진 시각마다 메서드를 부르게 하는 표식
- [ ] Queues / 오래 걸리는 일을 Redis 대기열로 넘기는 모듈
- [ ] Event Emitter / 상자끼리 직접 안 부르고 사건으로 알리는 방법
- [ ] Streaming File Response / 파일을 통째로 안 올리고 흘려보내는 응답
- [ ] RxJS Basics / 인터셉터가 쓰는 스트림 연산의 기초

## 13. Transport Layers `선택`

### GraphQL

- [ ] @nestjs/graphql / 스키마를 클래스에서 뽑을지 파일로 적을지 고르는 방식
- [ ] Resolver / 컨트롤러 대신 필드 단위로 응답을 만드는 클래스
- [ ] N+1 Resolution with DataLoader / 자식 조회를 한 번에 모아 부르는 방법

### WebSockets

- [ ] Gateway / 소켓 메시지를 받는 컨트롤러 격 클래스
- [ ] Adapter Selection / 소켓 구현을 갈아 끼우는 어댑터 선택

### Microservices

- [ ] Transport / 코드는 그대로 두고 통신 수단만 고르는 설정
- [ ] Message Pattern / 응답을 기다리는 호출과 던지고 마는 알림의 구분
- [ ] Hybrid Application / HTTP 서버와 마이크로서비스를 한 앱에 띄우는 방식

---

# PART 5 · Quality and Deployment

## 14. Testing

- [ ] Test.createTestingModule / 테스트용 상자를 따로 조립하는 방법
- [ ] Provider Mocking / 주입될 제공자를 가짜로 갈아 끼우는 방법
- [ ] Service Unit Testing / 의존을 전부 가짜로 두고 서비스만 재는 시험
- [ ] E2E Test / 앱을 실제로 띄워 HTTP로 두드리는 시험
- [ ] Guard · Pipe · Interceptor Testing / 층을 컨트롤러 없이 따로 부르는 시험
- [ ] Test Database Isolation / 테스트마다 DB 상태를 되돌리는 방법

## 15. Documentation & Observability

- [ ] SwaggerModule / DTO 표식을 읽어 API 문서를 자동으로 뽑는 모듈
- [ ] API Decorator / 문서에 나올 필드와 응답을 표식으로 적는 방법
- [ ] Logger / 내장 로거를 pino 같은 구현으로 갈아 끼우는 방법
- [ ] Health Check / DB와 디스크 상태를 한 경로로 보고하는 모듈
- [ ] Metrics & Tracing / 요청 하나가 지나간 구간을 수치로 남기는 방법

## 16. Deployment

- [ ] Build Artifacts / TypeScript를 dist 폴더로 미리 컴파일한 산출물
- [ ] Standalone Application / HTTP 없이 상자만 띄워 스크립트로 쓰는 방식
- [ ] Docker Multi-Stage Image / 빌드 단계와 실행 단계를 나눠 이미지를 줄이는 방법
- [ ] Monorepo Mode / 한 저장소에 여러 앱과 공용 라이브러리를 두는 구성 `선택`
- [ ] Graceful Shutdown / 종료 신호를 받아 연결을 정리하고 내리는 기능
- [ ] Per-Environment Deployment Checklist / 환경마다 설정과 마이그레이션을 점검하는 목록

---

# 이 로드맵 밖

- Node.js 런타임 `software/skill-based/Frameworks/nodejs.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- Express `software/skill-based/Frameworks/express.md`
- 백엔드 전반 `software/role-based/backend.md`
- GraphQL `software/skill-based/CS-Theory/graphql.md`
- 아키텍처 `software/skill-based/CS-Theory/software-design-architecture.md`
