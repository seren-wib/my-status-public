# Jest `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Jest

## 1. What is Jest?

### Overview of Jest / What is it?

- [ ] JavaScript Testing Framework / JS 코드를 검증하는 테스트 도구 전반
- [ ] Zero-config Philosophy / 설정 없이 바로 돌아가는 기본 방침
- [ ] All-in-one / 러너·단언·모킹·커버리지가 한 패키지에 든 구성

### Core Use Cases

- [ ] Unit Testing / 함수·모듈 하나만 떼어 검증하는 방식
- [ ] Integration Testing / 여러 모듈이 맞물려 도는지 검증하는 방식
- [ ] Snapshot Testing / 출력 결과를 저장해두고 변화를 비교하는 방식

### Jest vs Other Tools

- [ ] vs Vitest / Babel 변환과 격리 런타임이 Vite 상속과 갈리는 지점
- [ ] vs Mocha and Chai / 러너와 단언 라이브러리가 분리된 조합과의 차이
- [ ] When to choose Jest? / 성숙한 생태계·리액트 진영이 필요할 때 기준

## 2. Getting Started

### Installation `택 1`

- [ ] npm install jest / 패키지 하나만 설치해 바로 쓰는 방법 `추천`
- [ ] Framework Preset / CRA·Next.js가 미리 잡아둔 설정을 물려받는 방식
- [ ] TypeScript Setup / ts-jest나 babel-jest로 타입 코드를 변환하는 방법

### Running

- [ ] Running Tests / jest CLI로 테스트 파일을 실행하는 방법
- [ ] Watch Mode / watch와 watchAll로 변경 파일만 재실행하는 방법
- [ ] Filtering / testPathPattern이나 -t로 대상을 좁히는 방법

## 3. First Test

- [ ] File Conventions / *.test.js나 __tests__ 폴더로 인식하는 규칙
- [ ] test and it / 테스트 하나를 정의하는 두 별칭 함수
- [ ] expect Basics / 값을 검증문에 넣어 단언을 시작하는 함수
- [ ] Reading Failure Output / 실패 시 기대값과 실제값 diff를 읽는 방법

---

# PART 2 · Writing Tests

## 4. Matchers

- [ ] Equality / toBe·toEqual·toStrictEqual 세 강도의 비교 단언
- [ ] Truthiness / toBeNull·toBeUndefined·toBeTruthy로 참거짓을 가리는 단언
- [ ] Numbers / toBeGreaterThan·toBeCloseTo로 대소·근사값을 비교하는 단언
- [ ] Strings and Collections / toMatch·toContain로 패턴·포함 여부를 검증하는 단언
- [ ] Exceptions / toThrow로 예외가 던져지는지 검증하는 단언
- [ ] Negation / not을 붙여 단언 결과를 뒤집는 수식어
- [ ] Asymmetric Matchers / expect.any·objectContaining으로 부분만 비교하는 단언
- [ ] Custom Matchers / expect.extend로 단언을 직접 추가하는 방법

## 5. Async Testing

- [ ] Returning a Promise / 콜백 대신 프로미스를 반환해 대기시키는 방법
- [ ] async and await / 비동기 테스트를 동기 코드처럼 쓰는 문법
- [ ] done Callback / 콜백 인자를 호출해 완료를 알리는 구식 방식
- [ ] Promise Matchers / resolves·rejects로 이행·거부 결과를 단언하는 방법
- [ ] Common Pitfall / await를 빠뜨려 거짓 통과가 나는 함정

## 6. Test Structure and Hooks

- [ ] Grouping / describe로 관련 테스트를 하나로 묶는 방법
- [ ] Setup and Teardown / beforeEach·afterEach·beforeAll·afterAll 준비·정리 훅
- [ ] Scope and Execution Order / 훅과 테스트가 실행되는 순서 규칙
- [ ] Focus and Skip / only·skip·todo로 실행 범위를 지정하는 방법
- [ ] Parameterized Tests / test.each로 같은 테스트를 여러 값에 반복하는 방법
- [ ] setupFiles vs setupFilesAfterEnv / 실행 환경 전후로 나뉜 초기화 시점

## 7. Snapshot Testing

- [ ] toMatchSnapshot / 출력을 파일로 저장해 다음 실행과 비교하는 단언
- [ ] Inline Snapshots / 스냅샷을 별도 파일 없이 테스트 코드에 박는 방식
- [ ] Updating Snapshots / -u 플래그로 저장된 스냅샷을 갱신하는 방법
- [ ] Property Matchers in Snapshots / 매번 바뀌는 값만 느슨하게 비교하는 방법
- [ ] Snapshot Review Discipline / 갱신된 스냅샷을 리뷰에서 눈으로 확인하는 습관
- [ ] When Snapshots Hurt / 거대 스냅샷이 리뷰를 무의미하게 만드는 상황

---

# PART 3 · Mocking and Isolation

## 8. Mock Functions

- [ ] Creating Mocks / jest.fn으로 가짜 함수를 만드는 방법
- [ ] Return Control / mockReturnValue·mockResolvedValue로 반환값을 지정하는 방법
- [ ] Implementation Control / mockImplementation·mockImplementationOnce로 동작을 넣는 방법
- [ ] Call Inspection / mock.calls·mock.results로 호출 기록을 들여다보는 속성
- [ ] Call Assertions / toHaveBeenCalledWith·toHaveBeenCalledTimes로 호출을 검증하는 단언
- [ ] Reset APIs / mockClear·mockReset·mockRestore로 강도가 다른 초기화
- [ ] Spying / jest.spyOn으로 실제 구현을 유지한 채 감시하는 방법

## 9. Module Mocking

- [ ] Automatic Mock / jest.mock으로 모듈 전체를 자동 대체하는 방법
- [ ] Factory Mock / jest.mock에 팩토리 함수로 직접 구현을 넣는 방식
- [ ] Partial Mock / requireActual로 일부만 남기고 나머지만 바꾸는 방법
- [ ] Manual Mocks / __mocks__ 폴더에 고정 대역을 미리 두는 방식
- [ ] Node Core Module Mocking / fs·path 같은 내장 모듈을 대체하는 방법
- [ ] jest.mock Hoisting Behavior / 호출 위치와 상관없이 최상단으로 끌어올려지는 동작
- [ ] ESM Mocking Caveats / ESM 모듈에서 mock이 제대로 안 먹는 한계

## 10. Timers and Global Stubs

- [ ] Fake Timers / useFakeTimers로 실제 시간 흐름을 멈추는 방법
- [ ] Advancing Time / advanceTimersByTime·runAllTimers로 시계를 흘려보내는 방법
- [ ] Mocking Date / Date 객체를 고정값으로 대체하는 방법
- [ ] Global Stubs / fetch·localStorage 같은 전역 객체를 대체하는 방법
- [ ] Cleanup between Tests / restoreMocks·resetModules로 캐시를 초기화하는 옵션

## 11. Test Double Strategy

- [ ] Unit vs Integration Boundary / 어디까지 목으로 대체할지 가르는 기준
- [ ] Cost of Over-mocking / 과도한 모킹이 실제 버그를 놓치게 하는 대가
- [ ] Dependency Injection for Testability / 의존성을 주입 가능하게 짜서 테스트하기 쉽게 만드는 방법
- [ ] Network Mocking / msw로 네트워크 요청 자체를 가로채는 방법
- [ ] Deterministic Test Data / 매번 같은 결과가 나오게 고정한 테스트 데이터

---

# PART 4 · Practical Application and Configuration

## 12. Testing DOM and Components

- [ ] jsdom Environment / 브라우저 없이 DOM API를 흉내내는 실행 환경
- [ ] Testing Library / render와 screen으로 컴포넌트를 그려 조회하는 도구
- [ ] Query Variants / getBy·findBy·queryBy로 갈리는 조회 방식
- [ ] User Interaction / user-event로 클릭·입력 같은 실제 동작을 흉내내는 방법
- [ ] Async UI Assertions / waitFor로 화면이 바뀔 때까지 기다리는 단언
- [ ] DOM Matchers / jest-dom으로 DOM 상태를 검증하는 확장 단언
- [ ] Hook and Context Testing / 커스텀 훅과 컨텍스트 값을 따로 검증하는 방법

## 13. Coverage

- [ ] Enabling Coverage / --coverage 옵션으로 커버리지 집계를 켜는 방법
- [ ] Metrics / statement·branch·function·line 네 기준의 커버리지
- [ ] Thresholds / coverageThreshold로 최소 커버리지를 강제하는 방법
- [ ] Reporters / text·lcov·html 등 커버리지 출력 형식
- [ ] Scope Control / collectCoverageFrom으로 집계 대상을 좁히는 방법
- [ ] Coverage Percentage as a Trap / 수치는 높아도 검증이 부실할 수 있는 함정

## 14. Configuration

- [ ] Config Location / jest.config나 package.json에 두는 설정 위치
- [ ] Test Discovery / testMatch·testPathIgnorePatterns로 대상을 정하는 설정
- [ ] Module Resolution / moduleNameMapper·moduleDirectories로 경로를 잡는 설정
- [ ] Presets and Projects / 설정 묶음 재사용과 모노레포 분리 실행 단위
- [ ] Global Setup and Teardown / 전체 실행 전후 한 번만 도는 초기화·정리
- [ ] Reporter Configuration / 결과 출력 방식을 커스텀 리포터로 바꾸는 설정

## 15. Transforms and Environments

- [ ] Transform Pipeline / babel-jest·ts-jest·SWC로 코드를 변환하는 단계
- [ ] transformIgnorePatterns and node_modules / node_modules 변환을 건너뛰는 예외 패턴
- [ ] Test Environment / node와 jsdom 중 실행 환경을 고르는 설정
- [ ] Custom Environment / 직접 만든 실행 환경을 등록하는 방법 `선택`
- [ ] ESM Support Status / 아직 실험적인 ES 모듈 지원 현황

---

# PART 5 · Operations and CI

## 16. Performance

- [ ] Worker Processes / maxWorkers로 병렬 실행 프로세스 수를 정하는 방법
- [ ] Per-File Isolation Cost / 파일마다 새 런타임을 띄워 드는 비용
- [ ] Module Map and Cache / haste 모듈 지도를 캐싱해 재사용하는 구조
- [ ] Finding Slow Tests / 실행 시간이 긴 테스트를 찾아내는 방법
- [ ] Open Handle Detection / 종료 안 된 핸들을 감지해 알려주는 옵션
- [ ] Sharding / 테스트를 여러 머신에 나눠 병렬 실행하는 방식

## 17. CI Integration

- [ ] CI Flags / ci·runInBand로 CI 환경에 맞춰 돌리는 옵션
- [ ] JUnit Reporter / CI 도구가 읽는 XML 형식으로 결과를 내보내는 리포터
- [ ] Coverage Upload / 커버리지 결과를 외부 서비스로 전송하는 단계
- [ ] Changed-file Runs / onlyChanged로 변경 관련 테스트만 도는 방법
- [ ] Flaky Test Handling / 간헐적으로 실패하는 테스트를 재시도·격리하는 대응

## 18. Ecosystem and Migration `선택`

- [ ] Monorepo Setup / projects 설정으로 여러 패키지를 한 번에 돌리는 방법
- [ ] Jest to Vitest Migration Points / 이전 시 API 차이가 걸리는 지점
- [ ] Custom Reporters and Plugins / 리포터·플러그인을 직접 만들어 확장하는 방법
- [ ] Unit, Integration, E2E Split / 세 종류 테스트를 분리해 관리하는 전략

---

# 이 로드맵 밖

- Vitest `software/skill-based/Testing/vitest.md`
- Cypress `software/skill-based/Testing/cypress.md`
- JavaScript `software/skill-based/Languages/javascript.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- React `software/skill-based/Frameworks/react.md`
- Node.js `software/skill-based/Frameworks/nodejs.md`
