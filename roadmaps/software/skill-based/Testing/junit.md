# JUnit `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to JUnit

## 1. What is JUnit?

### Overview / What is it?

- [ ] Unit Testing Framework for Java / 자바 코드 단위를 자동 검증하는 프레임워크
- [ ] xUnit Family / SUnit 계보를 잇는 테스트 프레임워크 계열
- [ ] JUnit 4 vs JUnit 5 / 애노테이션과 구조가 갈리는 두 세대

### JUnit 5 Architecture

- [ ] JUnit Platform / 여러 테스트 엔진을 구동하는 실행 기반
- [ ] JUnit Jupiter / JUnit 5의 애노테이션·API를 담은 엔진
- [ ] JUnit Vintage / JUnit 3·4 테스트를 5에서 돌리는 엔진

### Testing Fundamentals

- [ ] Unit vs Integration vs E2E / 검증 범위가 넓어지는 세 테스트 층위
- [ ] Test Pyramid / 단위 테스트를 가장 많이 두는 비율 모델
- [ ] Arrange-Act-Assert and Given-When-Then / 준비·실행·검증 세 토막으로 본문을 나누는 규칙
- [ ] F.I.R.S.T Principles / 빠르고 독립적이며 반복 가능해야 한다는 다섯 원칙

## 2. Getting Started

### Build Tools `택 1`

- Gradle / 스크립트 기반으로 빌드를 정의하는 도구 `software/skill-based/Build-Tools/gradle.md` `추천` `위임`
- Maven / XML pom으로 빌드를 정의하는 도구 `software/skill-based/Build-Tools/maven.md` `위임`

### Dependencies and Configuration

- [ ] junit-jupiter Aggregate Artifact / api·params·engine을 한 번에 묶는 의존성
- [ ] JUnit BOM / 여러 모듈 버전을 한곳에서 맞추는 관리 방식
- [ ] Surefire and Gradle Test Task / 빌드 툴이 테스트를 실행하는 연결 지점
- [ ] junit-platform.properties / 실행 옵션을 파일로 미리 지정하는 방법

### Running

- [ ] IDE Test Runner / IDE 안에서 클릭 한 번으로 돌리는 실행기
- [ ] CLI / gradle test·mvn test로 터미널에서 돌리는 방법
- [ ] Test Report / 결과를 HTML·XML 형식으로 남기는 보고서

## 3. First Test

- [ ] @Test / 메서드를 테스트 케이스로 지정하는 애노테이션
- [ ] src/test/java Layout / 테스트 코드를 프로덕션과 나눠 두는 표준 위치
- [ ] Test Class and Method Naming Conventions / 클래스·메서드 이름으로 의도를 드러내는 규칙
- [ ] Failure vs Error / 단언 실패와 예외 발생을 구분하는 개념
- [ ] Reading Stack Traces / 실패 지점을 스택 추적으로 역추적하는 방법

---

# PART 2 · Writing Tests

## 4. Lifecycle / Fixture

- [ ] @BeforeEach and @AfterEach / 매 테스트 메서드 전후에 도는 훅
- [ ] @BeforeAll and @AfterAll / 클래스 전체 시작·종료에 한 번 도는 훅
- [ ] Test Instance Lifecycle and @TestInstance / 테스트 인스턴스를 매번 새로 만들지 정하는 설정
- [ ] Test Execution Order / @Order·MethodOrderer로 실행 순서를 정하는 방법
- [ ] Fixture Design and the Risk of Sharing / 픽스처를 공유할 때 생기는 테스트 간 오염 위험

## 5. Assertions

- [ ] Core Assertions / assertEquals·assertTrue 같은 기본 검증 메서드
- [ ] Exception Assertions / assertThrows로 예외 발생을 검증하는 방법
- [ ] Grouped Assertions / assertAll로 여러 단언을 한 번에 실행하는 방법
- [ ] Timeout Assertions / 제한 시간 안에 끝나는지 검증하는 방법
- [ ] Custom Failure Message / Supplier로 지연 평가해 붙이는 실패 메시지

### Assertion Libraries `택 1`

- [ ] AssertJ / 메서드 체이닝으로 읽기 쉬운 단언을 만드는 라이브러리 `추천`
- [ ] Hamcrest / Matcher 조합으로 단언 조건을 표현하는 라이브러리
- [ ] Truth / 구글이 만든 가독성 중심 단언 라이브러리

### Advanced

- [ ] Fluent Assertion Chaining / 단언을 메서드 체인으로 이어 쓰는 스타일
- [ ] Soft Assertions / 실패해도 멈추지 않고 끝까지 모아 보는 단언
- [ ] Writing Custom Assertions / 도메인에 맞는 단언 메서드를 직접 만드는 방법

## 6. Assumptions / Conditional Execution

- [ ] Assumptions / assumeTrue로 조건 안 맞으면 테스트를 건너뛰는 방법
- [ ] @Disabled / 특정 테스트를 실행 대상에서 빼는 애노테이션
- [ ] OS, JRE Conditions, @EnabledOnOs, @EnabledOnJre / 운영체제·JRE 버전에 따라 실행을 가르는 조건
- [ ] Environment Conditions / 시스템 프로퍼티·환경 변수로 실행을 가르는 조건
- [ ] Custom ExecutionCondition / 직접 구현해 실행 조건을 만드는 인터페이스

## 7. Parameterized / Repeated Tests

- [ ] @RepeatedTest / 같은 테스트를 지정 횟수만큼 반복 실행하는 애노테이션
- [ ] @ParameterizedTest / 여러 입력값으로 같은 테스트를 반복하는 애노테이션
- [ ] Argument Sources / @ValueSource·@CsvSource로 입력값을 공급하는 방법
- [ ] @ArgumentsSource and ArgumentsProvider / 커스텀 로직으로 인자를 직접 공급하는 확장점
- [ ] Argument Conversion and Aggregation / 문자열 인자를 타입 변환하거나 객체로 묶는 방법
- [ ] Dynamic Tests / @TestFactory로 실행 시점에 테스트를 생성하는 방법

### Test Data Generation

- [ ] Object Mother and Test Data Builder / 복잡한 테스트 객체를 만드는 생성 패턴
- [ ] Java Faker / 이름·주소 같은 가짜 데이터를 생성하는 라이브러리
- [ ] Property-based Testing / jqwik으로 무작위 입력을 자동 생성해 검증하는 방식 `선택`

## 8. Test Organization

- [ ] @DisplayName and DisplayNameGenerator / 테스트 이름을 사람이 읽기 좋게 바꾸는 기능
- [ ] @Nested / 내부 클래스로 테스트를 계층 구조로 묶는 애노테이션
- [ ] @Tag and Tag Expression Filtering / 태그로 테스트를 묶어 선택 실행하는 방법
- [ ] Test Suite and @Suite / 여러 테스트 클래스를 묶어 한 번에 돌리는 단위
- [ ] Parallel Execution / Concurrency Mode 설정으로 테스트를 동시 실행하는 방법

---

# PART 3 · Test Doubles and Integration Testing

## 9. Test Doubles

- [ ] Dummy, Stub, Spy, Fake, Mock / 대역이 실제와 얼마나 가까운지로 나눈 다섯 종류
- [ ] Dependency Injection for Testability / 의존성을 갈아끼울 수 있게 만드는 설계
- [ ] Seam / 코드 수정 없이 동작을 바꿔치기할 수 있는 지점

## 10. Mockito

- [ ] mock(), @Mock, MockitoExtension / 가짜 객체를 만드는 세 가지 방법
- [ ] Stubbing / thenReturn·thenThrow로 가짜 응답을 정하는 방법
- [ ] Verification / verify로 메서드 호출 여부·횟수를 확인하는 방법
- [ ] Argument Matchers / any·eq로 조건에 맞는 인자를 매칭하는 방법
- [ ] @Spy and Partial Mock / 실제 객체 일부만 가짜로 바꾸는 방법
- [ ] @InjectMocks / 만들어둔 목을 대상 객체에 자동 주입하는 애노테이션
- [ ] Static, Final Mocking, mockStatic / 정적·final 메서드까지 가짜로 바꾸는 방법
- [ ] Mocking Overuse Warning / 목을 과하게 쓰면 구현에 결합되는 부작용

## 11. Spring Boot Testing `선택`

- [ ] @SpringBootTest / 전체 스프링 컨텍스트를 띄워 통합 테스트하는 애노테이션
- [ ] Test Slices / @WebMvcTest처럼 계층 하나만 띄워 테스트하는 방법
- [ ] @MockBean and @SpyBean / 스프링 빈을 가짜로 바꿔치는 애노테이션
- [ ] MockMvc and WebTestClient / 서버 없이 HTTP 요청을 흉내 내는 도구
- [ ] Test Context Caching and @DirtiesContext / 스프링 컨텍스트 재사용과 강제 초기화
- [ ] @TestConfiguration and Test Profile / 테스트 전용 빈·설정을 분리하는 방법
- [ ] @Transactional Rollback / 테스트가 끝나면 DB 변경을 자동으로 되돌리는 방식

## 12. Testing External Dependencies

- [ ] In-memory DB and H2 / 메모리에서 뜨고 사라지는 테스트 전용 DB
- [ ] Testcontainers / 도커 컨테이너로 실제 인프라를 띄워 테스트하는 도구
- [ ] HTTP Stubbing and WireMock / 외부 API 응답을 가짜 서버로 흉내 내는 방법
- [ ] Embedded Kafka and Redis / 브로커·캐시를 인메모리로 띄워 테스트하는 방법
- [ ] Fixed Clock and Time Control / 시각을 고정해 시간 의존 로직을 검증하는 방법

---

# PART 4 · Advanced Topics and Operations

## 13. Extension Model

- [ ] @ExtendWith and @RegisterExtension / 확장 기능을 테스트에 등록하는 두 방법
- [ ] Lifecycle Callbacks / BeforeEachCallback처럼 훅에 끼어드는 콜백
- [ ] ParameterResolver / 테스트 메서드 파라미터를 동적으로 채워주는 인터페이스
- [ ] TestExecutionExceptionHandler / 테스트 중 던진 예외를 가로채 처리하는 인터페이스
- [ ] ExtensionContext and Store / 확장 간에 상태를 주고받는 저장소
- [ ] Automatic Extension Registration / META-INF 설정으로 확장을 자동 등록하는 방식

## 14. Quality Metrics and Advanced Techniques

- [ ] Code Coverage and JaCoCo / 실행된 코드 비율을 측정하는 도구
- [ ] Line vs Branch Coverage / 줄 단위와 분기 단위로 갈리는 커버리지 기준
- [ ] Coverage Target Trap / 수치만 채우려다 테스트 품질이 떨어지는 함정
- [ ] Mutation Testing and PIT / 코드를 일부러 망가뜨려 테스트 힘을 재는 방법
- [ ] Architecture Testing and ArchUnit / 패키지·의존 규칙을 코드로 검증하는 도구
- [ ] Contract Testing / Pact로 서비스 간 API 계약을 검증하는 방식 `선택`
- [ ] Approval Testing / 결과 전체를 스냅샷과 비교해 승인하는 방식

## 15. Migration / Interop

- [ ] JUnit 4 → 5 Migration / 애노테이션·API를 4에서 5로 옮기는 작업
- [ ] Vintage Engine / JUnit 4 테스트를 5 플랫폼 위에서 돌리는 엔진
- [ ] Rule to Extension Mapping / 4의 @Rule을 5의 Extension으로 바꾸는 대응
- [ ] TestNG Comparison / 애노테이션·실행 모델이 갈리는 경쟁 프레임워크

## 16. CI Integration

- [ ] Separating Unit and Integration Tasks / 느린 통합 테스트를 별도 태스크로 분리하는 방법
- [ ] Fail-fast and Retry Strategy / 실패 즉시 중단할지 재시도할지 정하는 전략
- [ ] Test Report Collection / JUnit XML로 결과를 모아 CI에 넘기는 방법
- [ ] Parallel and Sharding / 테스트를 여러 워커로 쪼개 동시에 돌리는 방법
- [ ] Flaky Test Detection and Quarantine / 불안정한 테스트를 찾아 격리하는 방법
- [ ] Test Runtime Management / 테스트 전체 실행 시간을 추적·관리하는 방법

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Java `software/skill-based/Languages/java.md`
- Spring Boot `software/skill-based/Frameworks/spring-boot.md`
- 백엔드 전반 `software/role-based/backend.md`
- 코드 리뷰 `software/skill-based/CS-Theory/code-review.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
