# Cypress `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Cypress

## 1. What is Cypress?

### Overview of Cypress / What is it?

- [ ] In-Browser Test Runner / 테스트가 앱과 같은 브라우저 안에서 도는 방식
- [ ] Runs in the Same Run Loop as the App / DOM·네트워크에 직접 개입 가능한 구조
- [ ] Bundled Stack / 러너·단언·스텁 라이브러리가 함께 딸려오는 구성

### Core Use Cases

- [ ] E2E Testing / 화면을 처음부터 끝까지 실제로 흘려보는 테스트
- [ ] Component Testing / 컴포넌트 하나만 격리해 마운트하는 테스트
- [ ] UI Integration Testing / 여러 컴포넌트가 얽힌 화면 단위 검증

### Cypress vs Other Tools

- [ ] vs Selenium / 브라우저 밖 드라이버냐 안 러너냐의 차이
- [ ] vs Playwright / 단일 엔진 전용이냐 멀티 엔진이냐의 차이
- [ ] Architectural Limits / 탭 여러 개와 도메인 이동이 막히는 이유
- [ ] When to choose Cypress? / 프론트 중심 팀에 적합한 선택 기준

## 2. Getting Started

### Installation and Running

- [ ] npm install cypress
- [ ] Interactive Runner / 창을 띄워 명령을 눈으로 따라가는 실행 방식
- [ ] Headless Run / 화면 없이 CI에서 돌리는 실행 방식

### Project Structure

- [ ] cypress.config / 브라우저·타임아웃·플러그인을 설정하는 파일
- [ ] e2e and fixtures Folders / 스펙 파일과 목 데이터를 담는 폴더 구조
- [ ] support/e2e and support/commands / 전역 훅과 커스텀 커맨드를 두는 위치
- [ ] Spec File Naming / 러너가 테스트 파일을 찾는 확장자 규칙

## 3. First Test

- [ ] describe and it Blocks / 테스트 묶음과 개별 케이스를 정의하는 구조
- [ ] Page Visit / cy.visit로 baseUrl 기준 페이지에 진입하는 방법
- [ ] baseUrl Setting / visit마다 전체 URL을 안 써도 되게 하는 설정
- [ ] Runner UI / 명령 로그와 각 시점 화면을 되감아 보는 창
- [ ] Test Isolation and State Reset / 테스트마다 쿠키·상태를 초기화하는 구조

---

# PART 2 · Core Concepts

## 4. Querying Elements

- [ ] Selector Query / cy.get으로 셀렉터에 맞는 요소를 찾는 방법
- [ ] Text Query / cy.contains로 텍스트 내용 기준으로 찾는 방법
- [ ] Traversal / 찾은 요소 기준 상하위·N번째를 탐색하는 방법
- [ ] Scoping / within으로 조회 범위를 특정 요소 안으로 좁히는 방법
- [ ] data-cy Selector Strategy / 스타일·구조 변경에 안 흔들리는 셀렉터 전략
- [ ] Cypress Testing Library / 역할·텍스트 기준으로 조회하는 라이브러리 `선택`

## 5. Actions

- [ ] Basic Actions / click·type·clear로 클릭과 입력을 실행하는 방법
- [ ] Form Controls / 체크박스·라디오·셀렉트를 조작하는 방법
- [ ] Scroll and Hover Limitations / 실제 마우스 이동이 없어 생기는 한계
- [ ] Drag and Drop / 네이티브 드래그 이벤트를 시뮬레이션하는 방법
- [ ] File Upload / selectFile로 파일 입력을 채우는 방법
- [ ] Raw Events / trigger로 임의 DOM 이벤트를 직접 발생시키는 방법
- [ ] Actionability Checks / force로 가시성·가림 검사를 건너뛰는 옵션

## 6. Assertions

- [ ] Implicit Assertions / should·and를 체인에 이어 붙이는 검증
- [ ] Explicit Assertions / expect·assert로 값을 직접 검증하는 방법
- [ ] Matcher Sets / Chai와 Chai-jQuery가 제공하는 매처 모음
- [ ] Assertion Retry Behavior / 조건이 맞을 때까지 자동 재시도하는 동작
- [ ] Callback Assertion / should에 함수를 넘겨 여러 조건을 한 번에 검증

## 7. Command Chain and Retry-ability

- [ ] Commands are Queued, not Promises / cy 명령이 즉시 실행 안 되고 쌓이는 구조
- [ ] Yielded Subject Chaining / 앞 명령의 결과를 다음 명령에 넘기는 방식
- [ ] Retry Rules / 조회 명령만 재시도하고 액션은 안 하는 구분
- [ ] Aliases / as로 값을 저장해 @alias로 재사용하는 방법
- [ ] Escaping the Chain / then·wrap으로 체인을 벗어나 값을 다루는 방법
- [ ] Return Value Anti-pattern / 명령 결과를 변수에 바로 대입하면 안 되는 이유
- [ ] Fixed Wait Anti-pattern / 고정 시간 대기가 재시도 대신 쓰이면 안 되는 이유

---

# PART 3 · Structuring Tests

## 8. Test Organization

- [ ] Hooks / 테스트 전후로 공통 준비·정리를 실행하는 함수
- [ ] Focus and Skip / only·skip으로 실행 범위를 좁히거나 빼는 방법
- [ ] Fixture Data / cy.fixture로 고정 목 데이터를 불러오는 방법
- [ ] Page Object vs App Actions / 화면 구조 vs 행동 단위로 묶는 패턴 차이
- [ ] Avoiding Test Interdependency / 앞 테스트 결과에 다음이 기대면 안 되는 이유

## 9. Network Requests

- [ ] Interception / cy.intercept로 네트워크 요청을 가로채는 방법
- [ ] Response Stubbing / 고정값이나 fixture로 응답을 대체하는 방법
- [ ] Waiting on Aliased Requests / 별칭 붙인 요청이 끝날 때까지 기다리는 방법
- [ ] Asserting Request Body and Headers / 가로챈 요청의 본문·헤더를 검증하는 방법
- [ ] Dynamic Response Callback / 요청 내용에 따라 응답을 함수로 만드는 방법
- [ ] Direct HTTP Calls / cy.request로 UI 없이 API를 직접 호출하는 방법
- [ ] Stubbed vs Real Server Tradeoffs / 속도·격리와 실제 통합 신뢰도의 상충

## 10. Authentication and State

- [ ] Login via UI vs API / 매번 화면으로 vs 요청으로 로그인하는 차이
- [ ] Session Caching / cy.session으로 로그인 상태를 재사용하는 방법
- [ ] Cookie Control / getCookie·setCookie로 쿠키를 직접 조작하는 방법
- [ ] Local Storage Handling / 로컬 스토리지 값을 읽고 쓰는 방법
- [ ] Cross-origin Flow / cy.origin으로 다른 도메인 안에서 명령을 실행하는 방법
- [ ] Backend Seeding / cy.task로 Node 코드를 실행해 DB를 채우는 방법

## 11. Custom Commands

- [ ] Adding Commands / Cypress.Commands.add로 재사용 명령을 정의하는 방법
- [ ] Overwriting Built-in Commands / 기존 명령의 동작을 바꿔치는 방법
- [ ] Child and Dual Commands / 체인 안에서만 vs 단독으로도 쓰는 명령 종류
- [ ] TypeScript Typings for Commands / 커스텀 명령에 타입을 선언하는 방법
- [ ] Plain Utilities vs Commands / 체인에 넣을지 그냥 함수로 둘지의 기준

---

# PART 4 · Advanced Features

## 12. Debugging

- [ ] Pausing Execution / cy.pause·cy.debug로 실행을 멈추고 살펴보는 방법
- [ ] Chain Debugging / 체인 중간에 상태를 콘솔로 찍어보는 방법
- [ ] Browser DevTools Integration / 실행 중인 브라우저 개발자도구를 그대로 쓰는 방식
- [ ] Failure Artifacts / 실패 시 자동 저장되는 스크린샷·영상
- [ ] Command Snapshot Inspection / 각 명령 시점의 DOM 스냅샷을 확인하는 방법
- [ ] Uncaught Exception Handling / 앱 에러로 테스트가 죽는 걸 막는 예외 처리

## 13. Spies, Stubs and Clock

- [ ] Spies / cy.spy로 함수 호출 여부·인자를 관찰하는 방법
- [ ] Stubs / cy.stub으로 함수 동작을 가짜로 대체하는 방법
- [ ] Time Control / cy.clock·cy.tick으로 시간을 가짜로 흘려보내는 방법
- [ ] Stubbing window Methods / alert·confirm 같은 브라우저 함수를 가로채는 방법

## 14. Component Testing

- [ ] Component vs E2E Runner / 컴포넌트만 마운트 vs 전체 앱을 도는 러너 차이
- [ ] Framework Adapters / 프레임워크별로 컴포넌트를 마운트해주는 어댑터
- [ ] Mounting / cy.mount로 컴포넌트 하나를 격리해 렌더하는 방법
- [ ] Props, Slots, Event Spies / 마운트 시 props·슬롯·이벤트를 넘기고 감시하는 방법
- [ ] Style and Provider Wrapping / 스타일·컨텍스트 프로바이더로 감싸 마운트하는 방법

## 15. Visual and Accessibility Testing `선택`

- [ ] Visual Regression Plugins / 화면 변화를 스크린샷으로 비교하는 도구
- [ ] Baseline Review Workflow / 기준 화면과 차이를 사람이 승인하는 절차
- [ ] Accessibility Checks / cypress-axe로 접근성 위반을 자동 검사하는 방법

---

# PART 5 · Operations and CI

## 16. Configuration and Environment

- [ ] Config Resolution Order / 설정 파일·환경변수·CLI 값이 겹칠 때 우선순위
- [ ] Environment Variables / env 객체와 CYPRESS_ 접두사로 값을 주입하는 방법
- [ ] Viewport and Browser Selection / 화면 크기와 실행 브라우저를 지정하는 방법
- [ ] Timeouts / 명령·요청별로 재시도 대기 시간을 조절하는 설정
- [ ] Retry Configuration / 실패한 테스트를 자동으로 다시 돌리는 설정
- [ ] Node Events / setupNodeEvents로 Node 환경 훅을 등록하는 방법

## 17. CI Integration

- [ ] Running in CI / 헤드리스로 파이프라인 안에서 돌리는 실행
- [ ] Official Docker Images / 브라우저까지 포함해 미리 구성된 실행 이미지
- [ ] GitHub Actions Workflow / GitHub Actions에서 테스트를 돌리는 설정 예시
- [ ] Caching the Cypress Binary / 매 빌드마다 바이너리를 새로 안 받게 캐싱하는 방법
- [ ] Parallelization and Load Balancing / 스펙을 여러 머신에 나눠 병렬로 돌리는 방법
- [ ] Cypress Cloud / 실행 기록·병렬 조율을 관리해주는 대시보드 `선택`
- [ ] Reporters / mochawesome·junit 형식으로 결과를 출력하는 방법

## 18. Flakiness and Best Practices

- [ ] Retries vs Root Cause Fixing / 재시도로 덮을지 원인을 고칠지의 판단
- [ ] Deterministic Test Data / 매번 같은 결과가 나오게 데이터를 고정하는 방법
- [ ] Selector Stability / 구조 변경에도 안 깨지는 셀렉터를 고르는 기준
- [ ] Choosing What Not to E2E / 굳이 E2E로 안 덮어도 되는 범위를 가르는 기준
- [ ] Suite Runtime Budget / 전체 스위트 실행 시간을 관리하는 기준

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Playwright `software/skill-based/Testing/playwright.md`
- Jest `software/skill-based/Testing/jest.md`
- JavaScript `software/skill-based/Languages/javascript.md`
- React `software/skill-based/Frameworks/react.md`
- CI 파이프라인 `software/role-based/devops.md`
