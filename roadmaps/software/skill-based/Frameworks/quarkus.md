# Quarkus `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Quarkus

## 1. What is Quarkus?

### Overview

- [ ] Kubernetes-Native Java Framework / 컨테이너에 얹을 것을 전제로 만든 자바 틀
- [ ] Build-Time Processing / 런타임에 할 배선을 빌드 단계로 옮기는 처리
- [ ] Startup Time · Memory Footprint Characteristics / 뜨는 시간과 상주 메모리가 작아지는 이유
- [ ] Imperative · Reactive Dual Support / 명령형과 리액티브를 한 앱에 같이 두는 지원
- [ ] Jakarta EE · MicroProfile Standards Adoption / 자체 API 대신 표준 규격을 가져다 쓰는 선택
- [ ] Differences from Spring Boot / 런타임 리플렉션 배선을 빌드로 옮긴 차이

### When to Use

- [ ] Serverless · FaaS / 첫 요청 지연이 곧 비용이 되는 실행 환경
- [ ] Container Density / 같은 노드에 인스턴스를 더 많이 꽂는 이점
- [ ] Migration Decision Criteria / 돌아가는 앱을 옮길지 가르는 판단 기준

## 2. Getting Started

### Project Creation `택 1`

- [ ] code.quarkus.io / 확장을 골라 초기 프로젝트를 받는 웹 생성기 `추천`
- [ ] Quarkus CLI / 생성·확장 추가·실행을 터미널에서 하는 도구
- [ ] Maven · Gradle Plugin / 쓰던 빌드 도구로 프로젝트를 만드는 방법
- [ ] Project Structure / 소스·자원·설정 파일이 나뉘어 놓이는 배치

### Dev Mode

- [ ] quarkus dev / 코드를 고치면 다음 요청에 바로 반영되는 실행
- [ ] Continuous Testing / 고친 코드에 걸린 테스트만 저절로 다시 도는 기능
- [ ] Dev UI / 깔린 확장의 상태와 설정을 브라우저에서 보는 화면
- [ ] Dev Services / 필요한 DB·브로커 컨테이너를 알아서 띄우는 기능
- [ ] Remote Dev Mode / 원격에 띄운 앱에 로컬 변경을 밀어 넣는 방식 `선택`
- [ ] Debugging / 개발 모드가 열어 둔 디버그 포트에 붙는 방법

## 3. Build-time Optimization

- [ ] Augmentation Phase / 애너테이션 훑기와 배선을 빌드에서 끝내는 단계
- [ ] Bytecode Recording / 빌드에서 정한 일을 시작 코드로 찍어 두는 방식
- [ ] Build Item · Build Step / 확장이 빌드 과정에 끼어드는 입출력 단위
- [ ] Closed-World Assumption / 빌드 뒤로는 클래스가 안 늘어난다고 보는 전제
- [ ] Class Scanning / Jandex 색인으로 애너테이션을 미리 찾아 두는 처리
- [ ] Runtime vs Build-time Configuration / 다시 빌드해야 바뀌는 설정을 가르는 기준
- [ ] Reflection Reduction Rationale / 리플렉션을 걷어 기동을 앞당기는 이유

## 4. Extension System

- [ ] Extension Concept / 라이브러리에 빌드타임 처리를 입혀 붙이는 단위
- [ ] Adding Extensions / 필요한 확장을 골라 의존성에 넣는 명령
- [ ] Quarkus Platform BOM / 확장 버전을 한 묶음으로 맞춰 주는 목록
- [ ] Quarkiverse / 코어 밖 커뮤니티 확장이 모인 저장소
- [ ] Risks of Libraries Without Extensions / 확장 없는 라이브러리가 네이티브에서 깨지는 이유
- [ ] Custom Extension Authoring Overview / 직접 확장을 만들 때 거치는 단계 `선택`

---

# PART 2 · Application Development

## 5. CDI and Configuration

- [ ] ArC / 프록시와 주입을 빌드 때 만들어 두는 CDI 구현
- [ ] CDI Annotations / 어떤 빈으로 등록할지 클래스에 다는 표식
- [ ] Scope / 빈 하나가 살아 있는 범위를 정하는 구분
- [ ] Producer Method / 직접 못 만드는 객체를 메서드로 내주는 방법
- [ ] Qualifier / 같은 타입 빈 여럿 중 하나를 고르는 표식
- [ ] Interceptor · Decorator / 호출 앞뒤에 공통 처리를 끼우는 방법
- [ ] Unremovable Bean / 안 쓰는 줄 알고 빌드에서 잘리는 빈을 남기는 표시
- [ ] MicroProfile Config / 설정 값 하나를 필드에 바로 꽂아 받는 표준
- [ ] Config Source Priority / 여러 곳에 적힌 같은 키의 승자를 정하는 순서
- [ ] Config Mapping / 접두사가 같은 설정을 인터페이스로 묶는 방법
- [ ] Profile / 환경마다 다른 설정을 한 파일에 나눠 적는 방식

## 6. REST Endpoints

- [ ] Quarkus REST / 경로 배선을 빌드에 굳혀 리플렉션을 없앤 구현
- [ ] Resource Annotations / 경로와 HTTP 메서드를 클래스에 다는 선언
- [ ] Parameter Binding / 주소·질의·헤더 값을 함수 인자로 받는 표식
- [ ] Request · Response Body / 본문 JSON을 객체로 바꿔 주고받는 처리
- [ ] Jackson vs JSON-B Selection / 직렬화 라이브러리 둘을 가르는 기준
- [ ] Exception Mapper / 예외를 정해진 오류 응답으로 바꾸는 자리
- [ ] Bean Validation / 입력 조건을 표식으로 적어 검사하는 방법
- [ ] Content Negotiation / 요청 헤더에 맞춰 응답 형식을 고르는 규칙
- [ ] OpenAPI · Swagger UI / 코드에서 명세와 시험 화면을 뽑아내는 기능
- [ ] REST Client / 인터페이스 선언만으로 바깥 API를 부르는 방법
- [ ] Execution Mode Designation / 이 메서드를 워커 스레드로 넘길지 정하는 표식

## 7. Reactive with Mutiny

- [ ] Rationale for Reactive / 스레드를 적게 쓰고 연결을 많이 받는 이유
- [ ] Uni · Multi / 값 하나와 흐르는 값을 나눠 담는 두 타입
- [ ] Mutiny Operators / 결과를 바꾸고 잇고 실패를 다루는 연산자
- [ ] Blocking Code Isolation / 막히는 호출을 워커 풀로 밀어내는 방법
- [ ] Vert.x-Based Underlying Runtime / 밑에서 이벤트 루프를 돌리는 엔진
- [ ] Server-Sent Events / 서버가 한 방향으로 계속 밀어 보내는 응답
- [ ] When Not to Use Reactive / 명령형으로 두는 편이 나은 경우

## 8. Data Access

- [ ] Hibernate ORM / 테이블과 클래스를 짝지어 다루는 표준 ORM
- [ ] Panache / 엔티티에 조회·저장 메서드를 직접 다는 단축 방식
- [ ] Panache Repository Pattern / 엔티티를 안 건드리고 조회를 따로 두는 구성
- [ ] Panache Query / where 절 조각만 적어 조회를 줄이는 문법
- [ ] Transaction / 메서드 하나를 통째로 커밋 단위로 묶는 표식
- [ ] Datasource Configuration / 접속 정보와 커넥션 풀을 설정에 적는 방법
- [ ] Migration / 스키마 변경을 버전 스크립트로 쌓아 올리는 도구
- [ ] Hibernate Reactive / 세션까지 논블로킹으로 돌리는 ORM 방식 `선택`
- [ ] MongoDB · Redis Client / 문서 DB와 캐시에 붙는 전용 확장 `선택`
- [ ] Caching / 메서드 결과를 키로 남겨 다시 쓰는 표식

---

# PART 3 · Integration and Quality

## 9. Messaging and Integration

- [ ] SmallRye Reactive Messaging / 메서드에 표식을 달아 채널에 잇는 방식
- [ ] Kafka Connector / 채널을 카프카 토픽에 매다는 확장
- [ ] AMQP · MQTT / 큐와 경량 기기 통신에 붙는 커넥터 `선택`
- [ ] Channel · Emitter / 코드에서 직접 메시지를 밀어 넣는 통로
- [ ] gRPC Service · Client / 스키마에서 뽑은 코드로 함수처럼 부르는 방식
- [ ] Scheduler / 정해진 주기마다 메서드를 돌리는 표식
- [ ] Fault Tolerance / 재시도·시간 제한·차단기를 표식으로 거는 방법
- [ ] Mailer · Qute Template / 메일 발송과 빌드에서 검사되는 템플릿 `선택`

## 10. Security

- [ ] Identity Provider Model / 자격 증명을 신원 객체로 바꾸는 내부 구조
- [ ] Authentication Mechanisms / 누구인지 확인하는 방식의 종류
- [ ] SmallRye JWT / 서명한 토큰을 검증해 신원으로 삼는 확장
- [ ] OIDC · Keycloak Integration / 로그인을 외부 인증 서버에 맡기는 연동
- [ ] Authorization / 역할과 경로로 접근을 가르는 정책
- [ ] SecurityIdentity Injection / 지금 요청한 사람 정보를 코드에서 꺼내는 방법
- [ ] Secret Management / 비밀 값을 코드 밖 금고에서 받아 오는 방식 `선택`
- [ ] TLS Configuration / 인증서를 걸어 암호화 연결을 여는 설정

## 11. Testing

- [ ] @QuarkusTest / 앱을 한 번 띄워 두고 도는 테스트 표식
- [ ] Test Profile / 테스트에만 다른 설정을 물리는 방법
- [ ] REST Assured / 실제 요청을 보내 응답을 검증하는 도구
- [ ] Mocking / 빈 하나만 가짜로 갈아 끼우는 방법
- [ ] Dev Services-Based Integration Testing / 진짜 DB 컨테이너를 띄워 붙이는 테스트
- [ ] @QuarkusIntegrationTest / 빌드된 산출물을 그대로 띄워 재는 테스트
- [ ] Native Test / 네이티브 바이너리로도 같은 검증을 돌리는 시험

---

# PART 4 · Native and Operations

## 12. Native Image

- [ ] GraalVM · Mandrel Differences / 네이티브 빌드용으로 깎아 낸 배포판의 차이
- [ ] Ahead-of-Time Compilation Concepts / 실행 전에 기계어로 다 컴파일해 두는 방식
- [ ] Native Build / 컨테이너 안에서 실행 파일을 뽑아내는 방법
- [ ] Native Constraints / 실행 중에 클래스를 만들어 내는 코드가 막히는 제약
- [ ] @RegisterForReflection / 리플렉션으로 쓸 클래스를 미리 알리는 표식
- [ ] Resource Inclusion Configuration / 실행 파일에 넣을 자원 파일을 지정하는 설정
- [ ] Build Time · Memory Requirements / 빌드가 오래 걸리고 램을 크게 먹는 대가
- [ ] Native Build Failure Diagnosis / 어느 클래스에서 막혔는지 되짚는 방법
- [ ] JVM Mode vs Native / 처리량과 기동 시간을 맞바꾸는 선택 기준
- [ ] Class Data Sharing / JVM 모드에서 클래스 적재를 앞당기는 방법 `선택`

## 13. Observability

- [ ] Health Check / 살아있음과 받을 준비를 따로 알리는 엔드포인트
- [ ] Micrometer Metrics / 수집기가 긁어 갈 수치를 노출하는 방법
- [ ] OpenTelemetry Tracing / 요청 하나가 지나간 구간을 이어 보는 방법
- [ ] Logging / 카테고리별 수준과 JSON 출력을 정하는 설정
- [ ] Dev UI Diagnostics / 개발 중 빈과 설정 상태를 들여다보는 화면

## 14. Container and Kubernetes

- [ ] Image Build Extensions / 도커 파일 없이 컨테이너 이미지를 굽는 확장
- [ ] Kubernetes Extension / 배포 매니페스트를 빌드에서 뽑아내는 확장
- [ ] ConfigMap · Secret Injection / 클러스터에 둔 값을 설정 소스로 읽는 방법
- [ ] Knative · Serverless Deployment / 요청이 없으면 0으로 줄이는 배포 방식 `선택`
- [ ] AWS Lambda Extension / 함수 런타임 규격에 맞춰 앱을 싸는 확장 `선택`
- [ ] Helm · OpenShift / 차트 패키징과 사내 배포판용 산출물 `선택`

## 15. Production Concerns

- [ ] Packaging Types / 산출물을 어떤 형태로 뽑을지 고르는 종류
- [ ] Startup Time · Memory Measurement / 뜨는 시간과 상주 메모리를 실제로 재는 방법
- [ ] JVM Tuning / 컨테이너 메모리 한도에 힙을 맞추는 설정
- [ ] Graceful Shutdown / 처리 중인 요청을 마치고 내려가는 절차
- [ ] Lifecycle Event / 앱이 뜨고 질 때 한 번씩 도는 자리
- [ ] Version Upgrade / 확장과 코드까지 같이 올려 주는 명령
- [ ] Limits of Spring Compatibility Extensions / 스프링 애너테이션 일부만 받아 주는 한계

---

# 이 로드맵 밖

- Java `software/skill-based/Languages/java.md`
- Spring Boot `software/skill-based/Frameworks/spring-boot.md`
- Ktor `software/skill-based/Frameworks/ktor.md`
- Maven · Gradle `software/skill-based/Build-Tools/maven.md`, `software/skill-based/Build-Tools/gradle.md`
- Docker · Kubernetes `software/skill-based/Infra-DevOps/docker.md`, `software/skill-based/Infra-DevOps/kubernetes.md`
- 백엔드 전반 `software/role-based/backend.md`
