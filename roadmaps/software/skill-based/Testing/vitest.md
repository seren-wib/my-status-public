# Vitest `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Vitest

## 1. What is Vitest?

### Overview of Vitest / What is it?

- [ ] Vite-native Test Runner / Vite 설정을 그대로 이어받는 실행기
- [ ] ESM and TypeScript First / 별도 컴파일 없이 ESM·TS를 바로 도는 방식
- [ ] Jest-compatible API Surface / describe·it·expect를 그대로 쓰는 호환 API

### Core Use Cases

- [ ] Unit Testing / 함수·모듈 단위로 격리해 검증하는 범위
- [ ] Component Testing / DOM 붙여 컴포넌트 동작을 검증하는 범위
- [ ] Integration Testing / 여러 모듈을 묶어 흐름을 검증하는 범위

### Vitest vs Other Tools

- [ ] vs Jest / API는 같고 실행기·변환 방식만 다른 지점
- [ ] Config Shared with the Vite Build / 빌드 설정을 테스트에도 그대로 쓰는 구조
- [ ] When to choose Vitest? / 이미 Vite 쓰는 프로젝트에 맞는 선택 기준

## 2. Getting Started

### Installation

- [ ] npm install vitest
- [ ] Config Location / 기존 vite 설정에 얹을지 따로 뗄지 정하는 기준
- [ ] Scripts / 워치로 돌지 한 번만 돌지 나누는 실행 스크립트

### Running

- [ ] Watch Mode by Default / 파일 저장하면 바로 재실행되는 기본 동작
- [ ] Vitest UI / 브라우저에서 결과를 보는 대시보드
- [ ] Filtering / 파일 이름이나 -t 패턴으로 돌릴 테스트만 고르는 방법

## 3. First Test

- [ ] File Conventions / test·spec 붙은 파일만 테스트로 인식하는 규칙
- [ ] Imports / 테스트 작성에 쓰는 기본 함수 3종
- [ ] globals Option / import 없이 전역으로 API를 쓰는 설정
- [ ] Reading the Failure Diff / 기대값과 실제값 차이를 보여주는 출력

---

# PART 2 · Writing Tests

## 4. Assertions

- [ ] Equality / 참조·값·타입까지 비교 강도가 다른 동등 검사
- [ ] Numbers and Strings / 소수 오차 허용과 문자열 패턴 매칭
- [ ] Collections / 배열·문자열의 포함 여부와 길이 검사
- [ ] Exceptions / 함수 호출이 에러를 던지는지 검사하는 방법
- [ ] Asymmetric Matchers / 값 전체가 아니라 형태만 맞춰 비교하는 방법
- [ ] Soft Assertions / 실패해도 멈추지 않고 끝까지 모아 보고하는 방식
- [ ] Assertion Count / 비동기 콜백 안 검증이 실행됐는지 세는 방법
- [ ] Custom Matchers / 직접 만든 매칭 함수를 expect에 등록하는 방법

## 5. Async and Concurrency

- [ ] Async Test Functions / async 함수로 비동기 흐름을 기다리는 테스트
- [ ] Promise Matchers / 프로미스의 성공·실패 값을 바로 검사하는 방법
- [ ] Timeout and Retry Options / 제한 시간을 넘기거나 실패 시 재시도하는 설정
- [ ] Concurrent Tests / 같은 파일 안 테스트를 동시에 돌리는 방법
- [ ] Local expect in Concurrent Mode / 동시 실행 시 컨텍스트별 expect를 써야 하는 이유
- [ ] Polling Assertions / 조건이 참이 될 때까지 반복 검사하는 방법

## 6. Test Structure and Hooks

- [ ] Grouping / 관련 테스트를 묶어 구조를 만드는 방법
- [ ] Hooks / 테스트 전후에 준비·정리를 끼우는 시점 4종
- [ ] Focus and Skip / 특정 테스트만 돌리거나 건너뛰는 표시
- [ ] Parameterized Tests / 같은 로직을 여러 입력값으로 반복 실행하는 방법
- [ ] Test Context and Fixtures / 테스트마다 주입할 공용 자원을 정의하는 방법
- [ ] setupFiles and globalSetup / 테스트 전체·환경 시작 전 실행할 초기화 파일

## 7. Snapshot Testing

- [ ] toMatchSnapshot / 이전 출력과 비교해 변경 여부를 잡는 방법
- [ ] Inline Snapshots / 스냅샷 값을 테스트 코드 안에 직접 저장하는 방식
- [ ] File Snapshots / 스냅샷을 별도 파일로 저장해 비교하는 방법
- [ ] Updating Snapshots / 저장된 스냅샷을 현재 출력으로 갱신하는 옵션
- [ ] Custom Serializers / 스냅샷 출력 형식을 직접 정의하는 방법

---

# PART 3 · Mocking

## 8. Mock Functions and Spies

- [ ] Creating Mocks / 호출을 기록하는 가짜 함수를 만드는 방법
- [ ] Return Control / 목 함수가 반환할 값을 고정하는 방법
- [ ] Implementation Control / 목 함수의 동작 로직을 직접 정의하는 방법
- [ ] Call Assertions / 목 함수가 어떻게 호출됐는지 검사하는 방법
- [ ] Spying / 기존 함수 동작은 두고 호출만 감시하는 방법
- [ ] Reset APIs / 목 상태를 테스트 사이에 초기화하는 범위 3단계

## 9. Module Mocking

- [ ] Module Mock / 모듈 전체를 가짜 구현으로 바꿔치는 방법
- [ ] Hoisting and vi.hoisted / vi.mock이 import보다 먼저 끌어올려지는 규칙
- [ ] Partial Mock / 일부만 목으로 바꾸고 나머지는 실제를 쓰는 방법
- [ ] Dynamic Mock / 호이스팅 없이 실행 시점에 모듈을 바꾸는 방법
- [ ] __mocks__ Directory / 모듈별 목 구현을 미리 파일로 두는 관례
- [ ] Dependency Replacement via Alias `선택` / Vite alias로 의존성 자체를 통째로 바꾸는 방법

## 10. Timers and Environment Stubs

- [ ] Fake Timers / setTimeout 등을 가짜 시계로 바꾸는 방법
- [ ] Advancing Time / 가짜 시계를 강제로 앞당기는 방법
- [ ] System Time / 현재 시각 자체를 특정 값으로 고정하는 방법
- [ ] Global and Env Stubs / 전역 객체·환경 변수를 테스트용으로 치환하는 방법
- [ ] Network Mocking / 네트워크 요청을 가로채 가짜 응답을 주는 방법

---

# PART 4 · Vite Integration and Advanced Topics

## 11. Configuration and Vite Integration

- [ ] test Block in Vite Config / vite.config 안에 테스트 전용 설정을 넣는 위치
- [ ] Include and Exclude Patterns / 테스트로 잡을 파일과 뺄 파일의 패턴
- [ ] Alias and Path Resolution / 빌드와 같은 경로 별칭을 테스트에도 쓰는 방법
- [ ] Reusing Vite Plugins / 앱에 쓰던 플러그인을 테스트도 그대로 타는 구조
- [ ] Environment Option / 테스트가 도는 실행 환경을 고르는 옵션
- [ ] Dependency Handling / node_modules를 변환할지 그대로 둘지 정하는 설정
- [ ] Workspace and Projects `선택` / 한 설정 안에 여러 테스트 환경을 묶는 구조
- [ ] Reporters / 결과를 출력하는 형식을 고르는 옵션

## 12. Component Testing

- [ ] DOM Environment Choice / 가짜 DOM 구현체를 속도·호환성으로 고르는 기준
- [ ] Testing Library Integration / 컴포넌트를 렌더링해 화면 상태로 조회하는 방법
- [ ] Queries and User Interaction / 실제 클릭·입력처럼 이벤트를 흉내내는 방법
- [ ] DOM Matchers / DOM 요소 상태를 검사하는 확장 매처 모음
- [ ] Framework Adapters / 프레임워크별 컴포넌트를 마운트하는 어댑터
- [ ] Auto Cleanup between Tests / 테스트마다 마운트된 DOM을 자동으로 정리하는 기능

## 13. Browser Mode

- [ ] Real Browser Execution vs jsdom / 가짜 DOM 대신 실제 브라우저에서 돌리는 방식
- [ ] Providers / 실제 브라우저를 띄우는 드라이버를 고르는 옵션
- [ ] Headless and Headed Runs / 브라우저 창을 띄울지 숨길지 정하는 실행 모드
- [ ] Browser-side Locators and Commands / 브라우저 안 요소를 찾고 조작하는 API
- [ ] Screenshot on Failure / 테스트 실패 시점의 화면을 자동으로 저장하는 기능
- [ ] Limitations and Stability / 실제 브라우저라 느리고 불안정할 수 있는 지점

## 14. In-source, Type and Benchmark Testing `선택`

- [ ] In-source Tests / 테스트를 소스 파일 안에 같이 두는 방식
- [ ] Excluding from Production Build / 인소스 테스트 코드를 배포 빌드에서 빼는 설정
- [ ] Type Testing / 런타임이 아니라 타입 자체를 검사하는 방법
- [ ] typecheck Option / tsc로 타입 에러를 테스트 실패로 잡는 옵션
- [ ] Benchmarking / 함수 성능을 반복 측정해 비교하는 기능
- [ ] Benchmark Comparison Output / 여러 벤치마크 결과를 나란히 비교하는 출력

---

# PART 5 · Operations and CI

## 15. Coverage and Debugging

- [ ] Coverage Providers / 커버리지를 계산하는 엔진을 고르는 옵션
- [ ] Metrics and Thresholds / 라인·브랜치별 커버리지 목표치를 정하는 기준
- [ ] Coverage Reporters / 커버리지 결과를 보여줄 출력 형식
- [ ] Include and Exclude Rules / 커버리지 계산에 넣고 뺄 파일 범위
- [ ] Debugging / 테스트 실행 중 중단점을 걸어 디버깅하는 방법
- [ ] Console Output Capture Control / 테스트 중 console 출력을 숨기거나 모으는 설정

## 16. Performance, CI and Migration

- [ ] Pools / 테스트를 병렬로 돌릴 실행 단위를 고르는 옵션
- [ ] Isolation Tradeoffs / 격리를 강하게 할수록 느려지는 성능과의 절충
- [ ] File and Test Parallelism / 파일 단위·테스트 단위로 동시 실행하는 범위
- [ ] Sharding across Machines / --shard로 조각 번호를 받아 나눠 도는 방법
- [ ] CI Run Mode / 워치 없이 한 번만 돌고 끝내는 CI 전용 모드
- [ ] Flaky Test Handling / 가끔 실패하는 테스트를 재시도로 넘기는 방법
- [ ] Jest Migration Points / Jest에서 옮길 때 설정·API 차이가 나는 지점

---

# 이 로드맵 밖

- Jest `software/skill-based/Testing/jest.md`
- Playwright `software/skill-based/Testing/playwright.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- JavaScript `software/skill-based/Languages/javascript.md`
- Vue `software/skill-based/Frameworks/vue.md`
- React `software/skill-based/Frameworks/react.md`
