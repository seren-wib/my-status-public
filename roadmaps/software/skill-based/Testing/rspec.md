# RSpec `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to RSpec

## 1. What is RSpec?

### Overview / What is it?

- [ ] BDD Testing Framework for Ruby / 행동을 문장으로 기술하는 루비 테스트 프레임워크
- [ ] Minitest vs RSpec / 내장형과 DSL형으로 갈리는 문체·확장성 차이
- [ ] rspec-core, rspec-expectations, rspec-mocks / 실행·매처·더블로 나뉜 3대 gem 구성
- [ ] Executable Specification Concept / 명세 자체가 실행되는 테스트라는 개념

### Testing Fundamentals

- [ ] Unit vs Integration vs System / 범위가 좁을수록 빠르고 넓을수록 느린 계층
- [ ] Test Pyramid / 단위를 많이, 시스템 테스트를 적게 두는 배분 원칙
- [ ] Given-When-Then / 준비-실행-검증 3단으로 나누는 서술 구조
- [ ] TDD and BDD Cycle / 동작을 문장으로 먼저 적고 구현으로 가는 순서

## 2. Getting Started

### Installation and Configuration

- [ ] Gemfile / group :test에 넣어 테스트에서만 쓰게 하는 방법
- [ ] rspec --init / 기본 설정 파일들을 생성하는 초기화 명령
- [ ] .rspec and spec_helper.rb / 실행 옵션과 공통 설정을 나눠 두는 두 파일
- [ ] rails_helper.rb / Rails 환경까지 로드하는 spec_helper 확장판 `선택`

### Running

- [ ] rspec CLI / 스펙을 실행하는 커맨드라인 도구
- [ ] File and Line Number / 파일 경로나 특정 줄만 콕 집어 실행하는 방법
- [ ] Formatter / progress·documentation 등 출력 형식을 고르는 옵션
- [ ] --fail-fast and --only-failures / 첫 실패에서 멈추거나 이전 실패만 재실행
- [ ] Random Order and Seed / 실행 순서를 섞고 seed로 재현하는 방식

## 3. First Spec

- [ ] spec/ Directory Layout / 스펙 파일을 기능별로 정리하는 폴더 구조
- [ ] _spec.rb Naming / 파일명 규칙으로 테스트 파일을 자동 인식시키는 방법
- [ ] describe and it / 최소 구성으로 짜는 스펙 한 벌
- [ ] Reading Failure Output / 실패 메시지에서 기대값·실제값을 읽는 법
- [ ] Pending and Skipped Example / 보류·제외 상태로 실행에서 빼는 방법

---

# PART 2 · Writing Specs

## 4. Example Group Structure

- [ ] describe and context / 검증 대상과 조건을 나누는 관용적 그룹 이름
- [ ] it, specify, example / 같은 기능을 갖는 예제 선언 별칭 셋
- [ ] Nested Group Design / describe를 겹쳐 조건을 좁혀가는 설계
- [ ] Description Writing Convention / 문장으로 읽히게 짓는 설명 작성법
- [ ] aggregate_failures / 한 예제 안 여러 실패를 한번에 모아 보는 기능
- [ ] One Expectation per Example Debate / 예제당 검증 하나로 제한할지의 논쟁

## 5. Expectations / Matchers

- [ ] expect(...).to and not_to / 성립·불성립을 검증하는 두 방향 문법
- [ ] Equality Matchers / eq·eql·equal·be로 갈리는 동등성 비교 수준
- [ ] Predicate Matchers / valid?·has_key?를 매처처럼 쓰는 방식
- [ ] Collection Matchers / include·match_array·all로 배열·집합 검증
- [ ] Error Matchers / 예외 발생과 심볼 throw를 검증하는 매처
- [ ] Change Matcher / 실행 전후 값 변화량·전이를 검증하는 매처
- [ ] Output and Yield Matchers / 표준출력·블록 yield 여부를 검증
- [ ] Compound Matchers / 매처를 and·or로 묶어 조건을 합성
- [ ] Defining Custom Matchers / 도메인에 맞는 매처를 직접 정의하는 방법
- [ ] Migrating should Syntax to expect Syntax / 구식 should 문법을 expect로 전환

## 6. Hooks / Helper

- [ ] before, after, around / 실행 전후·감싸기로 나뉜 3종 훅
- [ ] Hook Scope / example·context·suite로 갈리는 훅 적용 범위
- [ ] Helper Method / spec/support에 공용 메서드를 모아두는 관례
- [ ] Shared Examples / it_behaves_like로 명세를 재사용하는 방법
- [ ] Shared Context / include_context로 공통 설정을 불러오는 방법
- [ ] Metadata and Tag Filtering / 태그를 붙여 원하는 예제만 골라 실행

## 7. let / subject

- [ ] let and let! / 지연 평가와 즉시 평가를 가르는 두 헬퍼
- [ ] Understanding Lazy Evaluation / 호출되는 순간에야 값이 계산되는 원리
- [ ] subject and named subject / 암묵적 대상과 이름 붙인 대상의 차이
- [ ] is_expected.to / subject를 생략하고 바로 검증하는 축약 문법
- [ ] Instance Variable vs let / @var 대신 let을 쓰는 이유
- [ ] Over-Abstraction and Mystery Guest / 값의 출처가 안 보이게 되는 안티패턴

---

# PART 3 · Test Doubles

## 8. Doubles / Stubs

- [ ] Test Double Types / Dummy·Stub·Spy·Fake·Mock 다섯 유형
- [ ] double and instance_double / 자유형과 실제 클래스로 검증하는 더블 차이
- [ ] Verifying Double / class_double·object_double로 확장한 검증형 더블
- [ ] allow(...).to receive / 특정 메서드 호출에 응답을 미리 정해두는 문법
- [ ] and_return, and_raise, and_call_original / 반환·예외·원본 호출로 갈리는 응답
- [ ] Argument Constraints / with로 특정 인자일 때만 반응하게 제한

## 9. Message Expectations

- [ ] expect(...).to receive / 호출됐는지 자체를 검증하는 메시지 기대
- [ ] Spy / have_received로 사후에 호출 여부를 확인하는 방식
- [ ] Count Constraint / once·twice·exactly·at_least로 호출 횟수 제한
- [ ] Argument Matching / anything·hash_including으로 느슨하게 매칭
- [ ] Partial Double / 실제 객체 일부 메서드만 스텁으로 바꿔치기
- [ ] Mocking Overuse Warning and London vs Chicago School / 목 과용 문제와 두 유파의 입장 차이

---

# PART 4 · Rails and External Dependencies

## 10. rspec-rails `선택`

### Spec Type

- [ ] Model Spec / 모델의 검증·연관관계를 확인하는 스펙
- [ ] Request Spec / HTTP 요청·응답을 통째로 검증하는 스펙
- [ ] System Spec / Capybara로 브라우저 흐름까지 검증하는 스펙
- [ ] Job and Mailer Spec / 비동기 작업과 메일 발송을 검증하는 스펙
- [ ] Controller and View Spec / Request·System에 밀려 지양되는 스펙

### Rails-specific

- [ ] type Metadata and Inferred Type / 파일 위치로 스펙 종류를 자동 추론
- [ ] Transactional Fixture / 각 테스트를 트랜잭션으로 감싸 롤백하는 방식
- [ ] DatabaseCleaner Strategies / truncation 등으로 DB를 정리하는 전략
- [ ] ActiveJob and ActionMailer Test Helper / 잡 실행·메일 발송을 검증하는 헬퍼

## 11. Test Data

- [ ] Fixture vs Factory / 정적 데이터와 동적 생성 중 택하는 방식 `택 1`
- [ ] FactoryBot / build·create로 메모리·DB에 객체를 만드는 gem `추천`
- [ ] Trait, Association, Sequence / 변형·연관·고유값을 다루는 팩토리 기능
- [ ] build_stubbed / DB 저장 없이 저장된 것처럼 흉내내는 방식
- [ ] Faker / 랜덤한 가짜 데이터를 생성하는 라이브러리
- [ ] Factory Overuse and Slow Tests / 팩토리 남용이 테스트를 느리게 만드는 문제

## 12. External Systems

- [ ] HTTP Stubbing / WebMock으로 외부 요청을 가짜로 응답시키는 방법
- [ ] Cassette-Based Replay / VCR로 실제 응답을 녹화해 재생하는 방식
- [ ] Time Control / TimeHelpers·Timecop으로 시간을 고정·이동
- [ ] File and Storage Fake / 파일·스토리지 접근을 가짜로 대체하는 방법
- [ ] External Service Adapter Isolation / 외부 서비스 호출을 어댑터 뒤로 감추는 설계

---

# PART 5 · Quality and Operations

## 13. Execution Control

- [ ] Seed Reproduction / 같은 seed로 실행 순서를 재현하는 방법
- [ ] focus and Filtering / 특정 예제만 골라 집중 실행하는 방법
- [ ] Profiling / --profile로 느린 예제 상위 목록을 뽑는 기능
- [ ] Parallel Execution / parallel_tests·flatware로 프로세스 분산
- [ ] Bisect / --bisect로 실패 재현에 필요한 최소 조합 탐색
- [ ] Persistence File / --only-failures가 참조하는 실패 기록 파일

## 14. Advanced Techniques

- [ ] Property-based Testing / rantly로 무작위 입력을 생성해 검증 `선택`
- [ ] Approval and Snapshot Testing / 출력 전체를 저장해두고 비교하는 방식
- [ ] Mutation Testing / mutant로 코드를 일부러 망가뜨려 검증력 측정
- [ ] Contract Testing / Pact로 소비자·제공자 간 계약을 검증 `선택`
- [ ] Flaky Spec Causes / 순서 의존·시간·전역 상태로 생기는 불안정

## 15. Coverage / Lint

- [ ] SimpleCov / 실행된 코드 비율을 측정하는 커버리지 도구
- [ ] Line vs Branch Coverage / 줄 단위와 분기 단위로 재는 커버리지 차이
- [ ] Coverage Target Trap / 수치만 채우는 무의미한 테스트로 흐르는 함정
- [ ] RuboCop / rubocop-rspec으로 스펙 코드 스타일까지 검사
- [ ] Spec Style Consistency / 팀 전체 스펙의 문체·구조를 통일하는 일

## 16. CI Integration

- [ ] Suite Split Execution / 전체 스펙을 여러 묶음으로 나눠 실행하는 방법
- [ ] JUnit XML Formatter / CI가 읽는 JUnit 형식으로 결과를 출력
- [ ] Test Sharding / 러너 여러 개에 스펙을 나눠 병렬 처리
- [ ] Retry Strategy / rspec-retry로 실패 예제를 자동 재시도
- [ ] Slow Spec Management / 느린 스펙을 찾아내 별도로 관리하는 방법
- [ ] Local Boot Acceleration / Spring으로 앱 로딩을 미리 띄워두는 가속 `선택`

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Ruby `software/skill-based/Languages/ruby.md`
- Ruby on Rails `software/skill-based/Frameworks/ruby-on-rails.md`
- 백엔드 전반 `software/role-based/backend.md`
- 코드 리뷰 `software/skill-based/CS-Theory/code-review.md`
- CI 파이프라인 `software/role-based/devops.md`
