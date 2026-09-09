# Ktor `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Ktor

## 1. What is Ktor?

- [ ] Kotlin-Based Asynchronous Framework / 서버를 코틀린 코드로 조립하는 프레임워크
- [ ] Coroutine-Centric Design / 라우트 안에서 suspend 함수를 그냥 부르는 설계
- [ ] Lightweight and Composable / 기본 탑재 없이 쓸 기능만 붙이는 구성 방식
- [ ] Server and Client Both Provided / 서버와 클라이언트가 같은 API를 쓰는 구조
- [ ] Differences From Spring Boot / 자동 설정 없이 기동 코드를 직접 적는 차이
- [ ] Multiplatform Support Scope / JVM 밖 네이티브·JS까지 도는 범위

## 2. Setup and Structure

### Project Setup `택 1`

- [ ] Ktor Project Generator / 웹에서 플러그인을 골라 프로젝트를 받는 방법 `추천`
- [ ] IntelliJ Plugin / IDE 안에서 같은 생성기를 부르는 방법
- [ ] Manual Gradle Configuration / 엔진·플러그인 의존성을 직접 적는 방법

### Running

- [ ] Engine / 실제 소켓을 다루는 서버 구현을 갈아 끼우는 자리
- [ ] embeddedServer / main 함수 안에서 서버를 직접 띄우는 방법
- [ ] EngineMain / 설정 파일이 모듈을 찾아 띄우게 하는 방법
- [ ] Configuration / HOCON·YAML 파일에서 설정 값을 읽는 방법
- [ ] Application Module / 설치와 라우팅을 확장 함수로 쪼개는 단위
- [ ] Development Mode / 클래스 변경을 감지해 다시 읽는 설정

## 3. Plugins and Pipeline

- [ ] Plugin Concept / install로 기능을 파이프라인에 끼우는 확장
- [ ] Application Pipeline / 요청을 Phase 순서대로 통과시키는 구조
- [ ] Execution Order / install 순서가 동작을 바꾸는 이유
- [ ] Route-scoped Plugin / 특정 라우트 아래에만 거는 설치 범위
- [ ] Custom Plugin / createApplicationPlugin으로 훅을 직접 만드는 방법
- [ ] ApplicationCall / 요청과 응답을 한 객체로 들고 다니는 단위

---

# PART 2 · Server Development

## 4. Routing

- [ ] Routing Block / 경로를 중첩 블록으로 코드에 적는 DSL
- [ ] HTTP Method DSL / get·post 함수 자체가 경로를 여는 방식
- [ ] Path Parameter / {id}와 tailcard로 경로 조각을 받는 방법
- [ ] Nested Route / route를 겹쳐 접두사를 물려주는 방법
- [ ] Route Grouping / 인증·공통 설정을 하위 경로에 한 번에 거는 방법
- [ ] Type-safe Routing / Resources로 경로를 클래스로 못 박는 방식
- [ ] Static Content / 파일·리소스 폴더를 경로에 통째로 붙이는 방법
- [ ] URL Building / 라우트 정의에서 링크 주소를 되뽑는 방법

## 5. Requests and Responses

- [ ] Query Parameter · Header Reading / call에서 질의 문자열과 헤더를 꺼내는 방법
- [ ] Request Body Receiving / receive로 본문을 원하는 타입으로 받는 방법
- [ ] Form Data / receiveParameters로 폼 필드를 꺼내는 방법
- [ ] Multipart Upload / 파일 조각을 순서대로 읽어 내리는 방법
- [ ] Response Sending / respond 계열로 응답 본문을 내보내는 방법
- [ ] Status Code · Redirect / 상태 코드와 이동 응답을 지정하는 방법
- [ ] Response Header · Cookie Configuration / 응답에 헤더와 쿠키를 붙이는 방법
- [ ] Streaming Response / 본문을 다 만들기 전에 흘려보내는 방법

## 6. Serialization and Negotiation

- [ ] ContentNegotiation Plugin / Accept 헤더를 보고 변환기를 고르는 설치
- [ ] kotlinx.serialization / 컴파일 때 변환 코드를 만들어 두는 방식
- [ ] Jackson · Gson Alternatives / 리플렉션 기반 변환기를 대신 끼우는 선택 `선택`
- [ ] Data Class Based DTO Design / 요청·응답 형을 데이터 클래스로 두는 방법
- [ ] Custom Serializer / 날짜·값 타입의 변환 규칙을 직접 적는 방법
- [ ] Compression / 응답 본문을 gzip·deflate로 줄이는 설치
- [ ] CORS Configuration / 다른 출처의 요청을 허용하는 규칙
- [ ] DefaultHeaders · CachingHeaders / 응답마다 붙일 공통 헤더를 정하는 설치

## 7. Error Handling and Validation

- [ ] StatusPages Plugin / 예외를 잡아 응답으로 바꾸는 설치
- [ ] Exception → Response Mapping / 예외 종류별로 상태 코드를 짝짓는 규칙
- [ ] Domain Exception Design / 업무 오류를 예외 타입으로 나누는 방법
- [ ] RequestValidation Plugin / 받은 본문을 처리 전에 검사하는 설치
- [ ] 404 · 405 Handling / 맞는 라우트가 없을 때의 응답을 정하는 방법
- [ ] Error Response Format Unification / 오류 본문 형태를 하나로 맞추는 규칙

---

# PART 3 · Authentication and Data

## 8. Authentication

- [ ] Authentication Plugin / 인증 방식을 이름 붙여 등록하는 설치
- [ ] Basic · Digest Authentication / 헤더의 아이디·비밀번호로 검증하는 방식
- [ ] Form Authentication / 로그인 폼 필드를 받아 검증하는 방식
- [ ] JWT / 서명한 토큰을 발급하고 되검증하는 방식
- [ ] OAuth / 외부 제공자에게 로그인을 넘기는 절차
- [ ] Bearer Token / 토큰 검증 로직을 직접 적는 방식
- [ ] Authenticate Block / 등록한 인증을 라우트 묶음에 거는 블록
- [ ] Principal / 검증된 주체를 call에서 꺼내는 방법
- [ ] Role-Based Authorization / 권한 등급으로 접근을 가르는 방법

## 9. Sessions

- [ ] Sessions Plugin / 세션으로 쓸 데이터 타입을 등록하는 설치
- [ ] Cookie vs Header Sessions / 세션을 쿠키에 둘지 헤더에 둘지 가르는 기준
- [ ] Session Storage / 세션 본문을 서버 어디에 둘지 정하는 자리
- [ ] Serializer · Signing · Encryption / 세션 값의 변조와 열람을 막는 방법
- [ ] Session Expiration and Invalidation / 만료 시각을 주고 강제로 지우는 방법

## 10. Database Integration

- [ ] Exposed / 테이블을 코틀린 객체로 두고 질의하는 라이브러리
- [ ] JDBC · HikariCP Connection Pool / 커넥션을 미리 만들어 돌려 쓰는 구성
- [ ] Coroutines and Blocking IO / 막히는 호출을 Dispatchers.IO로 내보내는 이유
- [ ] Transaction Management / 여러 질의를 한 트랜잭션으로 묶는 방법
- [ ] Migration / 스키마 변경을 순서대로 적용해 나가는 방법
- [ ] Repository Layer Separation / 질의를 라우트에서 떼어 두는 구조
- [ ] Dependency Injection Adoption / Koin으로 의존 객체를 모듈에서 주입하는 방식 `선택`

## 11. WebSockets and Realtime

- [ ] WebSockets Plugin / 연결을 유지하는 양방향 경로를 여는 설치
- [ ] Frame Handling / 텍스트·바이너리 프레임을 채널에서 읽는 방법
- [ ] Connection Management / 접속 세션을 모아 두고 함께 보내는 방법
- [ ] Server-Sent Events / 서버가 한쪽으로만 계속 흘려보내는 방식
- [ ] Timeout · Ping Configuration / 죽은 연결을 핑으로 걸러내는 설정

---

# PART 4 · Client and Operations

## 12. Ktor Client

- [ ] HttpClient / 요청을 보내는 쪽에 엔진을 끼워 만드는 객체
- [ ] Request Building / 주소·헤더·본문을 블록으로 조립하는 방법
- [ ] Client Plugins / 서버와 같은 방식으로 클라이언트에 거는 확장
- [ ] Retry · Timeout Configuration / 재시도 횟수와 대기 한계를 정하는 설정
- [ ] Response Handling / body로 응답을 원하는 타입으로 받는 방법
- [ ] Usage In Multiplatform Shared Code / 안드로이드·iOS 공용 코드에서 부르는 방식
- [ ] MockEngine / 실제 통신 없이 응답을 지어내는 엔진

## 13. Testing

- [ ] testApplication / 포트를 열지 않고 앱을 띄워 부르는 방식
- [ ] Endpoint Calls With Test Client / 테스트용 클라이언트로 라우트를 두드리는 방법
- [ ] Test Configuration Separation / 테스트 전용 환경 설정을 따로 두는 방법
- [ ] Authentication · Session Testing / 인증이 걸린 경로를 통과시켜 보는 방법
- [ ] Testcontainers Integration / 실제 DB를 컨테이너로 띄워 붙이는 방법 `선택`

## 14. Observability and Operations

- [ ] CallLogging / 요청 한 건을 로그 한 줄로 남기는 설치
- [ ] CallId / 요청마다 식별자를 붙여 로그를 잇는 설치
- [ ] Logback Configuration / 로그 형식과 출력 대상을 정하는 설정
- [ ] Micrometer Metrics / 요청 수·지연을 지표로 뽑아내는 설치
- [ ] Graceful Shutdown / 처리 중인 요청을 마치고 내리는 절차

## 15. Deployment

- [ ] Fat JAR / 의존성까지 한 파일에 담아 만드는 실행 묶음
- [ ] Docker Image Build / 컨테이너 이미지로 감싸 올리는 방법
- [ ] GraalVM Native Image / 미리 컴파일해 기동 시간을 줄이는 방법 `선택`
- [ ] Servlet Container Deployment / WAR로 말아 기존 컨테이너에 얹는 방법 `선택`
- [ ] Configuration Externalization / 설정 값을 환경변수로 빼는 방법
- [ ] Operating Behind Reverse Proxy / 프록시가 넘긴 원 클라이언트 주소를 읽는 설정

---

# 이 로드맵 밖

- Kotlin `software/skill-based/Languages/kotlin.md`
- Java `software/skill-based/Languages/java.md`
- Gradle `software/skill-based/Build-Tools/gradle.md`
- Spring Boot · Quarkus `software/skill-based/Frameworks/spring-boot.md`, `software/skill-based/Frameworks/quarkus.md`
- 백엔드 전반 `software/role-based/backend.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
