# PHPUnit `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to PHPUnit

## 1. What is PHPUnit?

### Overview / What is it?

- [ ] Unit Testing Framework for PHP / 함수·클래스 단위로 동작을 검증하는 프레임워크
- [ ] xUnit Family / JUnit 설계를 이어받은 테스트 프레임워크 계보
- [ ] PHPUnit 10 and 11 / PHP 8.1+ 전용화로 구문법을 정리한 버전

### Testing Fundamentals

- [ ] Unit vs Integration vs Functional / 격리 범위로 테스트 종류를 나누는 기준
- [ ] Test Pyramid / 단위테스트는 많이, E2E는 적게 두는 비율 원칙
- [ ] Arrange-Act-Assert / 준비·실행·검증 세 단계로 테스트를 쓰는 구조
- [ ] TDD Cycle / 실패·통과·정리 세 단계를 반복하는 순서

## 2. Getting Started

### Installation `택 1`

- [ ] Composer require-dev / 개발 의존성으로 설치하는 방법 `추천`
- [ ] PHAR / PHP 아카이브 파일 하나로 실행하는 방식

### Configuration

- [ ] phpunit.xml and phpunit.xml.dist / 저장소 공용 설정과 개인 설정을 나누는 두 파일
- [ ] Test Suite Definition / 디렉터리나 파일 단위로 스위트를 묶는 방법
- [ ] Bootstrap / 실행 전 클래스 오토로더를 불러오는 설정 파일
- [ ] Source Include-Exclude / 커버리지 대상 파일을 포함·제외하는 설정
- [ ] Environment Variable / php.ini 값을 테스트 환경에 주입하는 설정

### Running

- [ ] CLI / vendor/bin/phpunit로 실행하는 명령줄 도구
- [ ] Filtering / --filter·--group로 실행 대상을 좁히는 옵션
- [ ] Output / --testdox로 명세처럼 보여주는 출력 형식
- [ ] Report / JUnit XML·TeamCity 형식으로 결과를 내보내는 기능

## 3. First Test

- [ ] Extending TestCase / TestCase 상속으로 테스트 클래스를 만드는 방법
- [ ] Test Method Naming / test 접두사나 #[Test] 속성으로 인식시키는 방법
- [ ] tests/ Directory Layout / 테스트 파일을 담는 표준 디렉터리 구조
- [ ] PSR-4 for Tests / 테스트 클래스에도 네임스페이스를 맞추는 규칙
- [ ] Failure, Error, Risky, Warning / 테스트 결과 상태를 가르는 구분

---

# PART 2 · Writing Tests

## 4. Lifecycle / Fixture

- [ ] setUp and tearDown / 각 테스트 전후에 실행되는 훅
- [ ] setUpBeforeClass and tearDownAfterClass / 클래스 전체에 한 번만 도는 훅
- [ ] Risk of Shared Fixtures / 훅으로 공유한 상태가 테스트를 오염시키는 위험
- [ ] Test Isolation / processIsolation으로 프로세스를 분리하는 옵션
- [ ] Global State / backupGlobals 등으로 전역 상태를 복원하는 옵션

## 5. Assertions

- [ ] Core Assertions / assertSame·assertEquals 등 기본 비교 단언
- [ ] Type Assertions / assertInstanceOf 등 타입을 검사하는 단언
- [ ] Collection, String Assertions / assertContains 등 배열·문자열 단언
- [ ] Exception Assertions / expectException 등으로 예외 발생을 검증하는 단언
- [ ] File, JSON, XML Assertions / 파일·JSON·XML 형식을 비교하는 전용 단언
- [ ] Writing Custom Constraints / Constraint 클래스를 만들어 단언을 확장하는 방법
- [ ] markTestIncomplete and markTestSkipped / 미완성·건너뛴 테스트로 표시하는 방법
- [ ] Strict vs Loose Comparison Pitfalls / ==와 === 비교 차이로 생기는 단언 함정

## 6. Attributes / Data Providers

- [ ] Migrating Annotations to Attributes / 독블록 주석을 #[Attribute] 문법으로 옮기는 작업
- [ ] Data Provider / #[DataProvider]로 같은 메서드에 케이스를 공급하는 기능
- [ ] Named Data Set / 데이터 세트에 이름을 붙여 결과를 구분하는 방법
- [ ] Inline Data / #[TestWith]로 케이스를 메서드 위에 바로 적는 방법
- [ ] Test Dependency / #[Depends]로 앞 테스트 결과를 다음에 넘기는 기능
- [ ] Grouping / #[Group]으로 태그를 붙여 묶어 실행하는 기능
- [ ] Requirement-Based Skip / #[RequiresPhp] 등 조건에 따라 건너뛰는 기능

## 7. Test Organization

- [ ] Unit and Feature Suite / 성격이 다른 테스트를 스위트로 나누는 방법
- [ ] Base TestCase and Trait / 공통 로직을 베이스 클래스나 Trait으로 공유하는 방식
- [ ] Test Data Builder and Object Mother / 복잡한 테스트 객체를 만드는 패턴
- [ ] Faker / 가짜 데이터를 대량으로 생성하는 라이브러리
- [ ] Random Order / --order-by로 실행 순서를 매번 섞는 옵션
- [ ] Parallel Execution / ParaTest로 테스트를 병렬 실행하는 확장 도구 `선택`

---

# PART 3 · Test Doubles and External Dependencies

## 8. Test Doubles

- [ ] Dummy, Stub, Spy, Fake, Mock / 역할별로 나뉘는 테스트 더블의 다섯 종류
- [ ] createMock and createStub / 목·스텁 객체를 만드는 메서드
- [ ] Stubbing / willReturn 등으로 가짜 반환값을 정하는 방법
- [ ] Expectation / expects·with로 호출 조건을 검증하는 방법
- [ ] Invocation Count / once·never 등으로 호출 횟수를 검증하는 옵션
- [ ] createPartialMock / 일부 메서드만 목으로 바꾸는 부분 목 생성 방법
- [ ] Criteria for Choosing What to Mock / 무엇을 목으로 바꿀지 정하는 판단 기준

## 9. Alternative Mocking Tools `택 1`

- [ ] Mockery / PHPUnit 목 대신 쓰는 유연한 목 라이브러리 `추천`
- [ ] Prophecy / Symfony 계열에서 쓰던 별도 목 라이브러리
- [ ] uopz and AspectMock / static·final도 바꿔치는 확장 `선택`

## 10. Database Testing

- [ ] In-memory SQLite / 디스크 없이 메모리에서 도는 DB로 테스트하는 방법
- [ ] Transaction Rollback Strategy / 트랜잭션을 걸고 테스트 후 롤백하는 전략
- [ ] Migration and Seeding / 테스트 DB 스키마를 만들고 데이터를 채우는 작업
- [ ] Fixture and Factory / 테스트용 데이터를 정의·생성하는 두 방식
- [ ] Isolation via Repository Abstraction / 저장소 계층을 추상화해 DB 의존을 격리하는 방법

## 11. External Systems

- [ ] HTTP Client Mocking / Guzzle MockHandler로 응답을 가짜로 만드는 방법
- [ ] Mock Server / WireMock 같은 서버로 외부 API를 흉내내는 방법
- [ ] Filesystem / vfsStream으로 가상 파일시스템을 만드는 방법
- [ ] Time Control / Clock을 추상화해 현재 시각을 통제하는 방법
- [ ] Static Call and Global Function / static·전역 함수라 목으로 바꾸기 어려운 문제

---

# PART 4 · Framework Integration

## 12. Laravel Testing `선택`

- [ ] TestCase / 애플리케이션 전체를 부트스트랩하는 기반 클래스
- [ ] HTTP Test / get·post 호출 후 상태를 검증하는 API 테스트 방법
- [ ] RefreshDatabase and DatabaseTransactions / 테스트마다 DB를 초기화하는 두 트레이트
- [ ] Model Factory / 모델 인스턴스를 정의 규칙대로 대량 생성하는 기능
- [ ] Fake Facade / Mail·Queue 등 파사드를 가짜로 바꿔 검증하는 기능
- [ ] Browser Test / Dusk로 실제 브라우저를 띄워 검증하는 E2E 테스트 `별도`

## 13. Symfony Testing `선택`

- [ ] KernelTestCase / 커널만 부팅해 서비스를 테스트하는 기반 클래스
- [ ] WebTestCase / Client·Crawler로 HTTP 요청을 흉내내는 기반 클래스
- [ ] Service Container in Tests / 테스트 안에서 DI 컨테이너 서비스를 꺼내 쓰는 방법
- [ ] Doctrine Fixtures / Doctrine으로 테스트용 초기 데이터를 적재하는 방법

## 14. Pest `선택`

- [ ] Built on Top of PHPUnit / PHPUnit 엔진 위에 문법만 얹은 구조
- [ ] Function-style Test / it·test 함수로 클래스 없이 테스트를 쓰는 방식
- [ ] Expectation API / expect() 체이닝으로 단언을 읽기 쉽게 쓰는 API
- [ ] Dataset / 같은 테스트에 여러 값을 반복 공급하는 기능
- [ ] Higher Order Test / 여러 테스트에 메서드 체인을 한 번에 적용하는 문법

---

# PART 5 · Quality and Operations

## 15. Quality Metrics

### Coverage

- [ ] Coverage Driver / Xdebug·PCOV 중 커버리지를 측정할 엔진 `택 1`
- [ ] Line, Branch, Path Coverage / 줄·분기·경로 단위로 커버리지를 재는 기준
- [ ] Report Format / HTML·Clover 등으로 커버리지를 출력하는 형식
- [ ] Coverage Target Trap / 수치만 채우려다 무의미한 테스트가 느는 함정
- [ ] Mutation Testing / Infection으로 코드를 일부러 망가뜨려 검증하는 기법

### Complementary Static Analysis

- [ ] PHPStan and Psalm / 실행 없이 타입 오류를 잡는 정적 분석 도구
- [ ] Architecture Test / Deptrac으로 계층 간 의존 규칙을 검증하는 방법
- [ ] What Tests Miss vs What Static Analysis Misses / 테스트와 정적 분석이 서로 못 잡는 영역 차이

## 16. CI Integration

- [ ] GitHub Actions Matrix / 여러 PHP 버전으로 동시에 돌리는 매트릭스 설정
- [ ] Suite Split Execution / 스위트를 나눠 여러 잡에서 병렬로 도는 방법
- [ ] Test Report Collection / CI에서 실행 결과를 모아 아티팩트로 남기는 방법
- [ ] Composer Install / vendor 캐시를 재사용해 설치 시간을 줄이는 방법
- [ ] Flaky Test Detection and Quarantine / 불안정한 테스트를 찾아 격리하는 절차
- [ ] Runtime Management / PHP 버전·확장 등 실행 환경을 관리하는 일

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- PHP `software/skill-based/Languages/php.md`
- Laravel `software/skill-based/Frameworks/laravel.md`
- 백엔드 전반 `software/role-based/backend.md`
- 코드 리뷰 `software/skill-based/CS-Theory/code-review.md`
- CI 파이프라인 `software/role-based/devops.md`
