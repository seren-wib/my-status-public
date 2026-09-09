# Playwright `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Playwright

## 1. What is Playwright?

### Overview of Playwright / What is it?

- [ ] End-to-End Browser Automation / 실제 브라우저로 사용자 흐름을 끝까지 검증하는 방식
- [ ] Cross-Browser / 엔진 셋을 같은 코드로 돌리는 구조
- [ ] Single API, Multi-Language Bindings / 한 API를 JS·Python·Java·.NET에서 쓰는 구조

### Core Use Cases

- [ ] E2E Testing / 브라우저를 띄워 화면 흐름을 검증하는 용도
- [ ] Component Testing / 프레임워크 컴포넌트를 마운트해 단독 검증하는 용도
- [ ] API Testing / UI 없이 HTTP 요청·응답만 검증하는 용도
- [ ] Browser Automation / 테스트 밖에서 페이지를 자동 조작하는 용도

### Playwright vs Other Tools

- [ ] vs Cypress / 브라우저 안에서 도는 인프로세스 방식과의 차이
- [ ] vs Selenium / W3C WebDriver 표준 기반과의 차이
- [ ] vs Puppeteer / CDP 저수준 라이브러리와의 차이
- [ ] When to choose Playwright? / 멀티 엔진·자동 대기가 필요할 때 고르는 기준

## 2. Getting Started

### Installation `택 1`

- [ ] npm init playwright / 스캐폴딩까지 한 번에 끝내는 설치 명령 `추천`
- [ ] Manual Install / 러너 패키지를 직접 받아 붙이는 설치 방법
- [ ] Other Language Bindings / 파이썬·자바·닷넷에서도 같은 API를 쓰는 방법 `선택`

### Project Structure

- [ ] playwright.config / 브라우저·타임아웃·리포터를 설정하는 파일
- [ ] tests Directory Layout / 테스트 파일을 모아두는 기본 폴더 구조
- [ ] Browser Binaries / playwright install로 받는 실행용 브라우저 바이너리

### Running

- [ ] Running Tests / npx playwright test로 실행하는 기본 명령
- [ ] Headed vs Headless / 창을 띄워 보는지 백그라운드로 도는지 차이
- [ ] UI Mode / 타임라인과 결과를 화면으로 보며 디버깅하는 모드
- [ ] Test Filtering / 이름·파일·줄 번호로 실행 범위를 좁히는 방법

## 3. Test Anatomy

- [ ] test and expect Imports / 테스트 작성에 쓰는 기본 함수 두 개
- [ ] Grouping / test.describe로 관련 테스트를 묶는 방법
- [ ] Navigation / page.goto로 페이지를 이동시키는 방법
- [ ] Per-Test Isolation / 테스트마다 새 컨텍스트를 띄우는 격리 방식
- [ ] Codegen / 조작을 녹화해 코드로 재생하는 기능

---

# PART 2 · Working with Elements

## 4. Locators

### Recommended Locators

- [ ] Role-based / getByRole로 접근성 역할 기준으로 찾는 방법
- [ ] User-facing / getByText·getByLabel 등 화면 문구로 찾는 방법
- [ ] Test ID / getByTestId로 전용 속성값으로 찾는 방법
- [ ] CSS and XPath Selectors / 구조 기반으로 찾는 비권장 선택자

### Locator Manipulation

- [ ] Chaining and Filtering / filter·and·or로 조건을 좁혀가는 방법
- [ ] Lists / first·last·nth로 여러 요소 중 하나를 고르는 방법
- [ ] Strictness Mode / 로케이터가 요소 하나만 가리키게 강제하는 규칙
- [ ] Locator vs ElementHandle / 재평가되는 참조와 고정 참조의 차이

## 5. Actions

- [ ] Click and Input / click·fill·press로 하는 기본 조작
- [ ] Checkbox and Radio / check·uncheck로 상태를 강제하는 방법
- [ ] Dropdown / selectOption으로 옵션을 고르는 방법
- [ ] File Upload / setInputFiles로 파일을 주입하는 방법
- [ ] Drag and Drop / 요소를 끌어다 놓는 동작을 재현하는 기능
- [ ] Low-level Input / mouse·keyboard API로 하는 좌표 단위 조작
- [ ] Actionability Checks / 클릭 전 보임·활성 상태를 자동 확인하는 절차

## 6. Assertions

- [ ] Auto-retrying Assertions / 조건 충족까지 자동 재시도하는 단언
- [ ] Non-retrying Assertions / 값을 즉시 한 번만 비교하는 단언
- [ ] Negation / not으로 조건 반대를 확인하는 방법
- [ ] Soft Assertions / 실패해도 테스트를 계속 진행시키는 단언
- [ ] Per-Assertion Timeout / 단언마다 재시도 제한 시간을 따로 두는 설정
- [ ] Custom Matchers / 직접 정의해 쓰는 전용 단언 함수 `선택`

## 7. Auto-waiting and Timeouts

- [ ] Auto-waiting Mechanism / 조작 전 요소 준비를 자동으로 기다리는 기본 동작
- [ ] Timeout Types / 테스트·단언·동작·이동마다 따로인 제한 시간
- [ ] Event Waiting / waitForURL·waitForResponse로 특정 이벤트를 기다리는 방법
- [ ] waitForLoadState / 페이지 로드 단계까지 기다리는 함수
- [ ] Anti-pattern / 고정 시간 sleep으로 기다리는 나쁜 습관

---

# PART 3 · Structuring Tests

## 8. Fixtures and Hooks

- [ ] Built-in Fixtures / page·context·browser 등 기본 제공 값
- [ ] Custom Fixtures / test.extend로 직접 만드는 픽스처
- [ ] Worker-scoped Fixtures / 워커 하나당 한 번만 만들어지는 픽스처
- [ ] Hooks / beforeEach·afterEach 등 전후 실행 지점
- [ ] Automatic Fixtures / 명시 안 해도 매 테스트에 자동 적용되는 픽스처
- [ ] Fixture Override / 같은 이름 픽스처를 재정의하는 방법

## 9. Browser Context and State

- [ ] BrowserContext Isolation / 쿠키·스토리지를 컨텍스트별로 격리하는 구조
- [ ] Context Options / viewport·locale 등 컨텍스트 생성 옵션
- [ ] Permissions and Device Emulation / 권한·기기 사양을 가짜로 부여하는 기능
- [ ] Storage State Reuse / storageState로 로그인 상태를 재사용하는 방법
- [ ] Authentication Setup Project / 로그인만 먼저 끝내 상태를 저장하는 프로젝트
- [ ] Multiple User Roles / 역할별 로그인 상태를 따로 관리하는 방법
- [ ] Multiple Pages and Popups / 새 탭·팝업이 뜬 상황을 다루는 방법
- [ ] Frames and iframes / 중첩된 문서 안 요소에 접근하는 방법

## 10. Network

- [ ] Request Interception / page.route로 네트워크 요청을 가로채는 방법
- [ ] Response Mocking / route.fulfill로 가짜 응답을 돌려주는 방법
- [ ] Request Modification / route.continue로 요청을 바꿔 통과시키는 방법
- [ ] Aborting Requests / 특정 요청 자체를 막아버리는 방법
- [ ] HAR Record and Replay / 네트워크 기록을 저장했다 재생하는 기능
- [ ] WebSocket Routing / 웹소켓 메시지를 가로채고 조작하는 기능 `선택`

## 11. Test Design Patterns

- [ ] Page Object Model / 화면 요소·동작을 클래스로 캡슐화하는 패턴
- [ ] Component Object / 화면 일부 조각만 객체로 묶는 단위
- [ ] Test Data Management / Factory·Seed로 테스트용 데이터를 만드는 방법
- [ ] API-based Setup instead of UI / 화면 조작 대신 API로 사전 상태를 세팅하는 방법
- [ ] Avoiding Inter-test Dependency / 테스트끼리 순서·상태에 의존 안 하게 하는 원칙

---

# PART 4 · Advanced Features

## 12. Debugging

- [ ] Playwright Inspector / 단계별로 멈춰가며 로케이터를 확인하는 도구
- [ ] Trace Viewer / 실패한 테스트를 타임라인으로 되감아 보는 도구
- [ ] Debug Mode / PWDEBUG 환경변수로 켜는 디버그 모드
- [ ] VS Code Extension / 에디터에서 테스트를 실행·디버깅하는 확장
- [ ] Failure Artifacts / 실패한 테스트만 골라 trace·영상을 남기는 설정
- [ ] Console and Page Error Capture / 브라우저 콘솔·에러를 테스트에서 잡는 방법
- [ ] Verbose API Logs / 내부 호출까지 다 찍는 상세 로그 모드

## 13. Visual and Accessibility Testing

- [ ] Screenshot Assertion / toHaveScreenshot으로 기준 이미지와 비교하는 단언
- [ ] Baseline Management / update-snapshots로 기준 이미지를 갱신하는 방법
- [ ] Masking and Diff Threshold / 비교 제외 영역과 허용 오차를 정하는 설정
- [ ] Accessibility Scan / axe-core 엔진으로 접근성 위반을 검사하는 기능
- [ ] ARIA Snapshot / 접근성 트리 구조를 텍스트로 비교하는 방법

## 14. API Testing

- [ ] APIRequestContext / 브라우저 없이 HTTP 요청만 보내는 컨텍스트
- [ ] Standalone API Tests / UI 없이 API만 검증하는 테스트
- [ ] Mixing UI and API in One Test / 한 테스트 안에서 API로 세팅하고 UI로 검증하는 방식
- [ ] Auth Token Reuse / API로 받은 인증 토큰을 테스트 전반에 재사용하는 방법

## 15. Component Testing `선택`

- [ ] Experimental CT Runner / 컴포넌트 테스트 전용 실험적 실행기
- [ ] Mounting / React·Vue·Svelte 컴포넌트를 격리해 띄우는 방법
- [ ] Props and Event Assertions / 전달한 props와 발생한 이벤트를 검증하는 방법
- [ ] CT vs E2E Tradeoffs / 속도·범위 사이에서 무엇을 포기할지의 선택

---

# PART 5 · Operations and CI

## 16. Configuration

- [ ] Projects and Browser Matrix / 여러 브라우저·설정 조합을 프로젝트로 나누는 구조
- [ ] Project Dependencies / 다른 프로젝트가 먼저 끝나야 실행되는 의존 관계
- [ ] webServer Option / 테스트 전 서버를 자동으로 띄워주는 설정
- [ ] Shared Options / baseURL·use로 전체에 적용하는 공통 옵션
- [ ] Global Setup and Teardown / 전체 실행 전후 한 번씩 도는 훅
- [ ] Environment-specific Config / 개발·스테이징·운영별로 갈리는 설정

## 17. Parallelism and Retries

- [ ] Workers and Parallel Execution / 프로세스를 나눠 테스트를 동시에 돌리는 방식
- [ ] Serial and Parallel Mode / describe.configure로 순차·병렬을 정하는 방법
- [ ] Sharding across Machines / 테스트를 여러 머신에 나눠 돌리는 방법
- [ ] Retries / 재시도 횟수와 실패 때 trace를 남길지 정하는 설정
- [ ] Blob Report Merging / 샤딩된 결과 리포트를 하나로 합치는 방법

## 18. CI Integration and Reporting

- [ ] Official Docker Image / 브라우저까지 미리 깐 CI용 공식 이미지
- [ ] GitHub Actions Workflow / CI에서 테스트를 자동 실행하는 설정 예시
- [ ] Reporters / list·html·json 등 결과 출력 형식
- [ ] Artifact Upload / trace·video를 CI 산출물로 올리는 방법
- [ ] Flaky Test Detection / 재시도로 통과한 불안정 테스트를 표시하는 기능
- [ ] Annotations / skip·fixme 등으로 테스트 상태를 표시하는 방법
- [ ] Tagging and Test Selection / 태그를 붙여 원하는 테스트만 골라 돌리는 방법

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Cypress `software/skill-based/Testing/cypress.md`
- Puppeteer `software/skill-based/Testing/puppeteer.md`
- JavaScript `software/skill-based/Languages/javascript.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- CI 파이프라인 `software/role-based/devops.md`
