# Selenium `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Selenium

## 1. What is Selenium?

### Overview of Selenium / What is it?

- [ ] Browser Automation Suite / 여러 도구를 묶은 브라우저 자동화 툴체인
- [ ] W3C WebDriver Protocol / 브라우저 제어를 표준화한 HTTP 프로토콜
- [ ] Components / 제어·분산·녹화 세 갈래로 나뉜 제품 구성

### Core Use Cases

- [ ] Cross-Browser E2E Testing / 여러 브라우저에서 같은 시나리오를 검증
- [ ] Legacy and Enterprise Environments / IE 등 구형 브라우저가 남은 사내 환경 대응
- [ ] Browser Task Automation / 테스트가 아닌 반복 브라우저 작업 자동화

### Selenium vs Other Tools

- [ ] vs Playwright / 표준 프로토콜 vs 자체 프로토콜·자동 대기 차이
- [ ] vs Cypress / 외부 제어 vs 브라우저 내 인프로세스 실행 차이
- [ ] Language and Browser Coverage / 지원 언어·브라우저 조합이 가장 넓은 강점
- [ ] When to choose Selenium? / 레거시·다언어·Grid 분산이 필요할 때 선택

## 2. WebDriver Setup

### Language Bindings `택 1`

- Java / 레퍼런스가 가장 많은 표준 바인딩 `software/skill-based/Languages/java.md` `추천` `위임`
- Python / 스크립트가 간결한 바인딩 `software/skill-based/Languages/python.md` `위임`
- JavaScript / selenium-webdriver로 붙는 JS 바인딩 `software/skill-based/Languages/javascript.md` `위임`
- [ ] C#, Ruby / 사용자가 상대적으로 적은 나머지 공식 바인딩

### Driver Setup

- [ ] Selenium Manager / 드라이버를 자동으로 찾아 내려받는 도구 `추천`
- [ ] Manual Driver Binaries / 브라우저마다 드라이버 실행 파일을 맞춰 까는 방법
- [ ] Driver and Browser Version Matching / 드라이버·브라우저 버전이 어긋나면 나는 오류

## 3. First Script

- [ ] Creating a Driver Instance / 브라우저 프로세스를 띄우는 진입점
- [ ] Navigation / get·back 등으로 페이지를 이동하는 방법
- [ ] Page State / title 등 페이지 정보를 읽는 속성
- [ ] Session Teardown / quit는 세션 종료, close는 창만 닫는 차이

---

# PART 2 · Elements and Interactions

## 4. Locating Elements

### Locator Strategies

- [ ] ID and Name / 가장 빠르고 안정적인 기본 로케이터
- [ ] CSS Selector / 클래스·속성으로 찾는 표준 방식 `추천`
- [ ] XPath / 절대 경로·상대 경로 두 방식이 있는 로케이터
- [ ] Link Text and Partial Link Text / 링크의 전체·부분 텍스트로 찾는 방법
- [ ] Class Name and Tag Name / 클래스명·태그명만으로 찾는 방법

### Element Search Usage

- [ ] Single vs Multiple / 단수 조회, 복수 조회를 구분하는 메서드
- [ ] Nested Element Search / 찾은 요소 안에서 하위 요소를 다시 찾는 방법
- [ ] Relative Locators / 다른 요소 기준 위·아래·근처로 찾는 방법
- [ ] Locator Stability and data Attributes / data-* 속성으로 변경에 강한 로케이터 만드는 방법

## 5. Element Interactions

- [ ] Basic Actions / click·sendKeys·clear로 하는 기본 조작
- [ ] Reading State / 텍스트·속성·CSS값을 읽는 API 묶음
- [ ] Predicates / 표시·활성·선택 여부를 판정하는 API
- [ ] Dropdowns / Select 클래스로 옵션을 선택하는 방법
- [ ] File Upload via sendKeys / 파일 선택창 없이 경로를 직접 입력하는 방법
- [ ] Form Submission / 버튼 클릭 대신 폼 자체를 제출하는 방법
- [ ] Stale Element Reference Handling / DOM 갱신 후 옛 참조가 무효화되는 오류 대응

## 6. Waits and Synchronization

- [ ] Implicit Wait / 드라이버 전역에 거는 자동 재시도 대기
- [ ] Explicit Wait / 조건이 맞을 때까지만 기다리는 대기
- [ ] Expected Conditions / 클릭 가능·visible 등 대기 조건 모음
- [ ] Fluent Wait / 폴링 주기와 무시할 예외를 지정하는 대기
- [ ] Custom Condition Functions / 직접 정의한 조건으로 기다리는 방법
- [ ] Page Load and Script Timeouts / 페이지 로드·스크립트 실행 제한 시간
- [ ] Anti-pattern / Fixed Sleep처럼 무조건 재우는 방식의 문제
- [ ] Danger of Mixing Implicit and Explicit Waits / 두 대기를 섞으면 생기는 타이밍 버그

## 7. Browser and Window Control

- [ ] Window Size and Position / 창 크기·위치를 코드로 지정하는 방법
- [ ] Maximize and Fullscreen / 창을 최대화·전체화면으로 만드는 방법
- [ ] Screenshots / 전체 페이지·특정 요소 단위 캡처
- [ ] Cookie Management / 세션 쿠키를 읽고 넣는 방법
- [ ] JavaScript Execution / 임의 스크립트를 실행하는 방법
- [ ] Async Script Execution / 콜백이 끝날 때까지 기다리는 비동기 실행
- [ ] Print to PDF / 페이지를 PDF로 저장하는 기능 `선택`

---

# PART 3 · Advanced Manipulation

## 8. Frames, Windows and Alerts

- [ ] iframe Switching / switchTo로 프레임 안팎을 오가는 방법
- [ ] Window and Tab Handles / 여러 창·탭을 식별하는 핸들 값
- [ ] Opening New Windows / 새 창·탭을 열고 전환하는 방법
- [ ] JavaScript Alerts / accept·dismiss로 다루는 네이티브 알림
- [ ] Authentication Popups / URL에 인증정보를 넣어 우회하는 팝업 처리

## 9. Advanced User Interactions

- [ ] Actions API / 여러 동작을 체이닝해 실행하는 저수준 API
- [ ] Mouse / hover·더블클릭·우클릭을 흉내내는 방법
- [ ] Drag and Drop / 요소를 잡아 다른 위치로 옮기는 동작
- [ ] Keyboard Modifiers / Shift·Ctrl을 누른 채 조작하는 방법
- [ ] Scroll Actions / 특정 요소가 보이게 스크롤하는 방법
- [ ] Pen and Touch Input / 스타일러스·터치 입력을 흉내내는 기능 `선택`

## 10. Browser Options and Capabilities

- [ ] Options Classes per Browser / 브라우저마다 다른 옵션 설정 클래스
- [ ] Headless Mode / 화면 없이 브라우저를 구동하는 모드
- [ ] Arguments and Preferences / 실행 인자와 브라우저 내부 설정값
- [ ] Extensions and User Profiles / 확장 프로그램·기존 프로필을 불러오는 방법
- [ ] Proxy Configuration / 브라우저 트래픽을 프록시로 우회하는 설정
- [ ] Download Directory and File Handling / 다운로드 경로 지정과 파일 검증 방법
- [ ] Insecure Certificates and Timeouts / 인증서 오류 무시·타임아웃 값 설정

## 11. CDP and WebDriver BiDi `선택`

- [ ] DevTools Protocol Access / WebDriver 우회해 브라우저 내부에 직접 접근
- [ ] Network Interception and Throttling / 요청을 가로채고 속도를 제한하는 기능
- [ ] Console and JS Exception Capture / 콘솔 로그·JS 예외를 수집하는 방법
- [ ] Basic Auth Injection / 팝업 없이 인증 헤더를 주입하는 방법
- [ ] BiDi Direction and Migration / CDP 대신 표준 양방향 프로토콜로 옮겨가는 흐름

---

# PART 4 · Test Framework Integration

## 12. Test Framework Integration

- [ ] Runner Choice / JUnit 등 실행기 중 하나를 선택
- [ ] Setup and Teardown Hooks / 테스트 전후 드라이버를 준비·정리하는 훅
- [ ] Assertion Library / 검증 문법을 담당하는 별도 라이브러리
- [ ] Parallel Execution Setup / 테스트를 동시에 여러 개 돌리는 설정
- [ ] Driver Lifecycle / 테스트마다 vs 클래스마다 드라이버를 새로 만들지 결정
- [ ] ThreadLocal Driver for Parallelism / 스레드마다 별도 드라이버를 두어 충돌 방지
- [ ] BDD Layer / Cucumber로 시나리오를 자연어로 쓰는 계층 `선택`

## 13. Page Object Model

- [ ] Page Object Basics / 화면 요소를 클래스로 감싸는 기본 패턴
- [ ] PageFactory and Lazy Elements / 요소를 실제 사용 시점에 찾는 지연 초기화
- [ ] Component and Fragment Objects / 페이지 일부를 재사용 가능한 조각으로 분리
- [ ] Fluent Page Navigation / 다음 페이지 객체를 반환해 체이닝하는 방식
- [ ] Keeping Assertions out of Page Objects / 검증 로직을 페이지 객체에 넣지 않는 원칙

## 14. Test Data and Configuration

- [ ] Environment-specific Config Files / 운영·스테이징 환경별 설정 분리
- [ ] Credential and Secret Handling / 계정·키를 코드에 노출하지 않는 관리 방법
- [ ] Data-driven Tests / 외부 파일로 입력값을 바꿔가며 반복 실행
- [ ] Setup via API or Database / UI 대신 API·DB로 테스트 데이터를 준비
- [ ] Test Independence and Cleanup / 테스트끼리 상태를 공유하지 않도록 정리

---

# PART 5 · Operations and CI

## 15. Selenium Grid

- [ ] Grid Architecture / 라우터·분배·노드로 나뉜 분산 구조
- [ ] Standalone, Hub and Node Modes / Grid를 단일·허브-노드로 구성하는 방식
- [ ] Fully Distributed Mode / 역할별 컴포넌트를 각각 독립 배포하는 방식
- [ ] RemoteWebDriver Usage / 로컬 대신 원격 Grid 노드에 접속하는 방법
- [ ] Docker-based Grid / 컨테이너로 Grid를 띄우는 구성
- [ ] Kubernetes Deployment / Grid를 K8s 클러스터에 배포하는 방법 `선택`
- [ ] Cloud Providers / BrowserStack 같은 관리형 Grid 서비스
- [ ] Session Queue and Concurrency Limits / 노드가 부족하면 세션이 쌓이는 대기열 한도

## 16. CI, Reporting and Maintenance

- [ ] Headless Runs in CI / CI 파이프라인에서 화면 없이 실행하는 방식
- [ ] Container Images / 공식 이미지로 Grid를 실행하는 방법
- [ ] Reporting / Allure 등으로 결과를 보고서화
- [ ] Failure Artifacts / 실패 시 스크린샷·로그를 남기는 방법
- [ ] Retry Strategy for Flaky Tests / 불안정한 테스트를 재시도하는 전략
- [ ] Suite Runtime Budget / 전체 스위트 실행 시간의 상한 관리
- [ ] Selenium 3 to 4 Migration Points / 구버전에서 W3C 표준으로 넘어갈 때 바뀐 점

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Playwright `software/skill-based/Testing/playwright.md`
- Cypress `software/skill-based/Testing/cypress.md`
- Java `software/skill-based/Languages/java.md`
- Python `software/skill-based/Languages/python.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
