# Express.js `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Express

## 1. What is Express?

### Overview of Express / What is it?

- [ ] Minimal Unopinionated Web Framework / 라우팅과 미들웨어만 주고 나머지는 안 정해주는 성격
- [ ] Middleware Pipeline Model / 요청이 함수 사슬을 순서대로 지나가는 구조
- [ ] Express 4 vs 5 Differences / 5에서 async 오류가 자동으로 잡히는 변화

### Express vs Others

- [ ] Express vs Fastify, Koa, Hono / 후발 주자가 기본으로 주는 것과의 차이
- [ ] Express vs NestJS / 폴더 배치를 강제하지 않는 점
- [ ] When to choose Express? / 작은 API에 붙일 때 고르는 기준

## 2. Getting Started

- [ ] npm i express / 패키지 하나만 받으면 끝나는 설치
- [ ] Application Creation / app 객체를 만들어 listen으로 띄우는 순서
- [ ] Writing the First Route / GET 하나로 응답을 돌려주는 최소 코드
- [ ] TypeScript Configuration / @types/express를 따로 받아야 하는 이유 `추천`
- [ ] Dev Watch / node --watch나 nodemon으로 자동 재시작하는 방법
- [ ] Separating app Definition from server Startup / 테스트에서 listen 없이 부르게 나누는 구조

---

# PART 2 · Routing and Middleware

## 3. Routing

- [ ] Route Methods / app.get·post·put·delete로 메서드를 거는 방법
- [ ] Route Path / 문자열·패턴·정규식으로 경로를 적는 세 방식
- [ ] Route Parameters / :id를 req.params로 꺼내 쓰는 방법
- [ ] Handler Chaining / 한 경로에 핸들러 여러 개를 배열로 거는 방법
- [ ] express.Router / 라우트 묶음을 파일 단위로 떼어내는 객체
- [ ] app.route Chainable / 같은 경로의 메서드를 이어 붙여 쓰는 문법
- [ ] Router Mounting / app.use로 라우터를 경로 아래 붙이는 방법
- [ ] 404 Catch-all and Registration Order / 등록 순서 때문에 맨 끝에 둬야 하는 처리

## 4. Request & Response

### Request

- [ ] Input Access / query·params·body 세 곳으로 나뉜 입력 위치
- [ ] Headers / req.get으로 대소문자 무시하고 읽는 방법
- [ ] Cookies / cookie-parser를 붙여야 req.cookies가 생기는 구조
- [ ] Client IP / trust proxy를 켜야 실제 주소가 잡히는 이유

### Response

- [ ] Body Sending / send는 타입을 추측하고 json은 못 박는 차이
- [ ] Status / res.status 체이닝과 sendStatus 한 줄의 차이
- [ ] Header & Cookie / res.set·res.cookie로 응답에 얹는 방법
- [ ] res.redirect / 상태 코드와 Location을 한 번에 넣는 응답
- [ ] File Sending / sendFile은 열어 보이고 download는 받게 하는 차이
- [ ] Streaming / 큰 응답을 pipeline으로 흘려보내는 방법

## 5. Middleware

- [ ] Middleware Signature / req·res·next 세 인자를 받는 함수 모양
- [ ] Application · Router · Route Level / 앱 전체·라우터·경로 하나 중 거는 자리
- [ ] Execution Order and next Rules / next를 안 부르면 요청이 멈춰 있는 규칙
- [ ] Built-in / json·urlencoded·static 셋만 기본으로 주는 이유
- [ ] Third-party / cors·compression·helmet을 직접 골라 붙이는 방법
- [ ] Writing Custom Middleware / 직접 만든 함수를 사슬에 끼우는 방법
- [ ] req Object Extension and Type Augmentation / req에 값을 얹을 때 타입을 넓히는 선언

## 6. Error Handling

- [ ] Error Middleware / 인자를 넷 받는 함수로만 인식되는 처리
- [ ] Sync vs Async Error Propagation / 던진 오류와 거절된 프로미스가 갈리는 지점
- [ ] Async Handler Wrapping / Express 4에서 async 오류를 직접 넘겨야 하는 이유
- [ ] Custom Error Class / 상태 코드를 오류 객체에 심는 클래스 설계
- [ ] Unified Error Response Format / 오류 응답 모양을 한 곳에서 정하는 방법
- [ ] Unhandled Rejection Handling / 사슬 밖에서 터진 거절을 잡는 방법

---

# PART 3 · Data and Security

## 7. Input Validation

### Validation Library `택 1`

- [ ] zod / 스키마에서 타입까지 뽑아내는 검증 라이브러리 `추천`
- [ ] joi / 객체 스키마를 체이닝으로 적는 검증 라이브러리
- [ ] express-validator / 미들웨어 형태로 거는 검증 라이브러리

### Input Handling

- [ ] Validation Middleware Pattern / 검증을 핸들러 앞으로 떼어내는 방법
- [ ] Body Size · Content-Type Limits / express.json의 limit으로 본문을 막는 설정
- [ ] File Upload / multer를 붙여야 multipart를 읽는 구조
- [ ] Sanitization / 저장 전에 위험한 문자를 걷어내는 방법

## 8. Databases

### Driver / ORM `택 1`

- Prisma / 스키마 파일에서 클라이언트를 생성하는 ORM `software/skill-based/Frameworks/prisma.md` `추천` `위임`
- [ ] Drizzle ORM / SQL에 가깝게 쓰는 타입 안전 질의 빌더
- [ ] TypeORM and Sequelize / 데코레이터·모델 정의로 쓰는 앞 세대 ORM
- [ ] Mongoose / MongoDB 문서에 스키마를 씌우는 ODM

### Integration Patterns

- [ ] Connection Pool Management / 앱 시작 때 한 번만 열어 재사용하는 방법
- [ ] Migration Workflow / 스키마 변경을 파일로 남겨 배포에 태우는 절차
- [ ] Repository Layer Separation / 질의를 라우터 밖 모듈로 몰아두는 구조
- [ ] Transaction Handling / 요청 하나를 한 트랜잭션으로 묶는 방법

## 9. Authentication & Sessions

- [ ] Cookie vs Token Strategy / 세션을 서버에 둘지 토큰에 담을지 고르는 기준
- [ ] express-session / 기본 저장소가 메모리라 교체해야 하는 이유
- [ ] Password Hashing / bcrypt·argon2로 되돌릴 수 없게 저장하는 방법
- [ ] JWT Issuance and Verification / 짧은 접근 토큰과 갱신 토큰을 나누는 방식
- [ ] Passport.js Strategy / 로그인 방식마다 전략 모듈을 갈아 끼우는 구조 `선택`
- [ ] OAuth and OIDC / 남의 계정으로 로그인시키는 연동 절차
- [ ] Authorization Middleware / 역할·권한을 핸들러 앞에서 거르는 함수

## 10. Security

- [ ] Security Headers / helmet 하나로 기본 보안 헤더를 다는 방법
- [ ] CORS Configuration / 허용 출처와 쿠키 전달 여부를 정하는 설정
- [ ] CSRF Protection / SameSite 쿠키나 토큰으로 막는 방법
- [ ] Rate Limiting / 주소별 요청 수를 미들웨어로 막는 방법
- [ ] Injection & XSS Defense / 값을 그대로 질의·HTML에 넣지 않는 규칙
- [ ] Secret Management / 키를 코드가 아닌 환경변수로 빼는 방법
- [ ] trust proxy and HTTPS Enforcement / 프록시 뒤에서 원래 프로토콜을 알아내는 설정

---

# PART 4 · Structure and Quality

## 11. Application Structure

- [ ] Layer Separation / 라우터·컨트롤러·서비스·저장소로 나누는 구조
- [ ] Feature-based Module Directories / 기능 단위로 폴더를 묶는 배치
- [ ] Config Loading and Environment Branching / 환경별 설정을 한 곳에서 읽는 방법
- [ ] Dependency Injection Pattern / 의존성을 밖에서 넣어주는 구성 `선택`
- [ ] API Versioning / /v1을 경로 앞에 붙여 나누는 방법
- [ ] Common Response Wrapper Design / 성공 응답 모양을 하나로 맞추는 설계

## 12. Views & Static `선택`

- [ ] Template Engine / EJS·Pug·Handlebars 중 골라 붙이는 방법
- [ ] View Engine Configuration / res.render가 찾을 폴더와 엔진을 정하는 설정
- [ ] express.static / 정적 파일 응답에 캐시 헤더를 붙이는 설정
- [ ] SPA Fallback Routing / 없는 경로를 index.html로 넘기는 처리

## 13. Testing

- [ ] Test Runner / vitest·jest·내장 node:test 중 고르는 기준 `택 1`
- [ ] HTTP Integration Testing / supertest로 포트를 안 열고 부르는 방법
- [ ] Middleware Unit Testing / next를 가짜로 넣어 함수만 시험하는 방법
- [ ] DB Isolation / 테스트마다 DB를 새로 띄워 격리하는 방법
- [ ] External API Mocking / 바깥 호출을 가로채 가짜 응답을 주는 방법

## 14. Logging & Observability

- [ ] Request Logging / morgan·pino-http를 미들웨어로 거는 방법
- [ ] Structured Logger / 로그를 JSON 한 줄로 남기는 라이브러리
- [ ] Request ID and Correlation ID / 요청마다 번호를 붙여 로그를 잇는 방법
- [ ] Metrics & Tracing / OpenTelemetry로 구간별 시간을 재는 방법
- [ ] Error Reporting / 잡힌 오류를 Sentry로 모아 보내는 설정

---

# PART 5 · Performance and Deployment

## 15. Performance

- [ ] Compression / gzip·brotli로 응답 본문을 줄이는 미들웨어
- [ ] HTTP Caching / ETag와 Cache-Control로 재요청을 줄이는 방법
- [ ] Response Caching / 계산한 응답을 Redis에 남겨 다시 쓰는 방법
- [ ] Clustering & Load Balancing / 코어 수만큼 프로세스를 띄워 나누는 방법
- [ ] Keep-Alive & Timeout Configuration / 연결 유지 시간과 응답 제한을 정하는 설정
- [ ] Bottleneck Profiling / autocannon으로 때리고 clinic으로 찾는 순서

## 16. Deployment

- [ ] Production Configuration / NODE_ENV에 따라 캐시·오류 출력이 바뀌는 동작
- [ ] Process Manager / pm2·systemd로 죽으면 다시 띄우는 방법
- [ ] Reverse Proxy / Nginx를 앞에 두고 정적·TLS를 넘기는 구성
- [ ] Docker Multi-stage Image / 빌드 단계와 실행 단계를 나눠 굽는 방법
- [ ] Graceful Shutdown / SIGTERM에 처리 중 요청을 마치고 닫는 순서
- [ ] Health Check Endpoint / 살아있는지 확인하는 응답 경로

---

# 이 로드맵 밖

- Node.js 런타임 `software/skill-based/Frameworks/nodejs.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 백엔드 전반 `software/role-based/backend.md`
- NestJS `software/skill-based/Frameworks/nestjs.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
- 배포 인프라 `software/skill-based/Infra-DevOps/docker.md`, `nginx.md`
