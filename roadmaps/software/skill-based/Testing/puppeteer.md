# Puppeteer `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Puppeteer

## 1. What is Puppeteer?

### Overview of Puppeteer / What is it?

- [ ] Node.js Browser Automation Library / 브라우저를 코드로 조작하는 Node.js 라이브러리
- [ ] Built on the Chrome DevTools Protocol / CDP로 크롬을 직접 제어하는 기반 구조
- [ ] Chrome and Firefox Support / 크롬 외 파이어폭스도 실험적으로 지원하는 범위

### Core Use Cases

- [ ] Web Scraping / 페이지를 렌더링해 데이터를 뽑아내는 용도
- [ ] PDF and Screenshot Generation / 페이지를 PDF·이미지로 뽑아내는 용도
- [ ] Automated UI Testing / 브라우저 동작을 코드로 재현하는 용도
- [ ] Performance Auditing / 로딩 성능 지표를 코드로 수집하는 용도

### Puppeteer vs Other Tools

- [ ] vs Playwright / 단일 엔진 대 멀티 엔진 지원의 차이
- [ ] vs Selenium / CDP 직접 제어 대 W3C 표준 프로토콜의 차이
- [ ] Library vs Test Framework / 러너·단언 없이 API만 제공하는 위치
- [ ] When to choose Puppeteer? / 크롬 전용 저수준 제어가 필요한 상황

## 2. Getting Started

### Installation `택 1`

- [ ] puppeteer with Bundled Browser / 크로미움까지 한 번에 설치하는 기본 방식 `추천`
- [ ] puppeteer-core with Existing Browser / 설치된 브라우저에만 붙는 경량 패키지
- [ ] Browser Download Cache Control / 다운로드한 크로미움을 저장할 경로 지정

### First Script

- [ ] Launching a Browser / launch로 브라우저 프로세스를 띄우는 단계
- [ ] Opening a Page / 새 탭에 해당하는 Page 객체 생성
- [ ] Navigating and Capturing / URL 이동 후 결과를 캡처하는 흐름
- [ ] Closing Resources / 브라우저·페이지를 정리해 프로세스를 안 남기는 절차

## 3. Browser and Page Lifecycle

- [ ] Launch Options / 헤드리스 여부·실행 인자·브라우저 경로를 정하는 옵션
- [ ] Connecting to a Running Browser / 이미 떠 있는 브라우저에 소켓으로 붙는 방법
- [ ] BrowserContext Isolation / 쿠키·캐시를 공유하지 않는 격리된 세션 단위
- [ ] Page vs Target / 탭 하나 대 CDP가 보는 대상 전체의 차이
- [ ] Cleanup and Leaked Processes / 제대로 안 닫으면 크롬 프로세스가 남는 문제

---

# PART 2 · Page Manipulation

## 4. Navigation and Waiting

- [ ] Navigation / goto·reload로 페이지를 옮겨 다니는 방법
- [ ] Wait Until Conditions / 언제를 로딩 완료로 볼지 정하는 기준
- [ ] Waiting for Selectors / 특정 요소가 나타날 때까지 기다리는 방법
- [ ] Waiting for Functions and Events / 조건식·이동 이벤트가 참이 될 때까지 기다리는 API
- [ ] Default and Per-call Timeouts / 호출마다 다르게 걸 수 있는 대기 시간 한도
- [ ] Race between Click and Navigation / 클릭과 페이지 이동이 겹칠 때 생기는 경쟁 상태

## 5. Selecting Elements

- [ ] Query Selectors / CSS 선택자로 요소 하나·여러 개를 찾는 API
- [ ] Selector Syntax / 텍스트·접근성 속성·xpath로 찾는 문법
- [ ] ElementHandle vs JSHandle / DOM 요소 참조 대 임의 JS 값 참조의 차이
- [ ] Locator API and Auto-retry / 요소가 준비될 때까지 자동으로 재시도하는 상위 API
- [ ] Handle Disposal / 안 쓰는 핸들을 해제해 메모리를 돌려주는 절차

## 6. Interactions

- [ ] Click and Type / 요소를 클릭하고 값을 입력하는 기본 동작
- [ ] Keyboard API / 키를 누르고 떼는 동작을 나눠 제어하는 API
- [ ] Mouse API / 커서 이동·클릭·휠을 좌표 단위로 제어하는 API
- [ ] Form Controls / 셀렉트박스·체크박스 값을 다루는 방법
- [ ] File Upload / input에 파일을 직접 지정해 올리는 방법
- [ ] Drag and Drop / 마우스 이동으로 드래그 앤 드롭을 흉내내는 방법
- [ ] Scrolling into View / 가려진 요소를 화면 안으로 스크롤하는 방법

## 7. Evaluating JavaScript in the Page

- [ ] page.evaluate and Serialization Rules / 실행 결과를 값으로 직렬화하는 규칙
- [ ] evaluateHandle for Non-serializable Values / 직렬화 안 되는 DOM·함수를 핸들로 받는 방법
- [ ] Passing Arguments into Page Context / Node 쪽 값을 페이지 실행 컨텍스트로 넘기는 방법
- [ ] Element-scoped Evaluation / 선택한 요소를 인자로 받아 평가하는 API
- [ ] Exposing Node Functions / 페이지에서 Node 함수를 호출하게 노출하는 방법
- [ ] Script Injection on New Document / 매 페이지 로드 전에 스크립트를 미리 심는 방법

---

# PART 3 · Advanced Control

## 8. Network Control

- [ ] Request Interception / 나가는 요청을 가로채 제어하는 기능
- [ ] Aborting and Blocking Resources / 특정 요청을 중단시켜 로딩을 막는 방법
- [ ] Response Mocking / 실제 응답 대신 가짜 데이터를 돌려주는 방법
- [ ] Modifying Headers and Post Data / 요청 헤더·바디를 가로채 바꾸는 방법
- [ ] Request and Response Events / 요청·응답 발생 시점을 이벤트로 받는 방법
- [ ] Cookie and Storage Control / 쿠키·로컬스토리지를 코드로 읽고 쓰는 방법
- [ ] Basic Auth and Proxy / 인증 창·프록시 서버를 거쳐 접속하는 설정
- [ ] Interception Performance Cost / 요청 가로채기가 로딩 속도에 주는 부담

## 9. Frames, Dialogs and Multiple Pages

- [ ] Frame Tree / 페이지 안 iframe들이 이루는 계층 구조
- [ ] Working inside iframes / iframe 내부 요소에 접근해 조작하는 방법
- [ ] Dialog Handling / 브라우저 팝업창을 자동으로 처리하는 방법
- [ ] Popup and New Tab Handling / window.open으로 열리는 새 탭을 잡아내는 방법
- [ ] Page Events / 콘솔 로그·에러·요청 실패를 감지하는 이벤트
- [ ] Download Handling / 브라우저가 받는 파일을 지정 경로로 저장하는 방법

## 10. Emulation

- [ ] Device Emulation / 미리 정의된 기기 프로필을 그대로 흉내내는 방법
- [ ] Viewport and Device Scale Factor / 화면 크기와 픽셀 밀도를 임의로 지정하는 설정
- [ ] User Agent Override / 브라우저가 보내는 UA 문자열을 바꿔치는 방법
- [ ] Geolocation and Permissions / 위치 정보와 권한 요청 결과를 미리 정하는 설정
- [ ] Network and CPU Throttling / 느린 회선·저사양 기기를 흉내내는 제한
- [ ] Media and Color Scheme Emulation / 인쇄 모드·다크모드 등 미디어 조건을 흉내내는 설정
- [ ] Timezone and Locale / 시간대·지역 설정을 바꿔 테스트하는 방법

## 11. CDP Access

- [ ] CDP Session / 고수준 API를 건너뛰고 프로토콜에 직접 붙는 통로
- [ ] Domains and Commands / CDP가 기능별로 나눈 도메인과 그 명령들
- [ ] Coverage API / 실행되지 않은 JS·CSS 코드를 찾아내는 기능
- [ ] Accessibility Snapshot / 접근성 트리를 그대로 덤프해 확인하는 방법
- [ ] When Raw CDP Beats the High-level API / Puppeteer API에 없는 기능을 직접 여는 상황

---

# PART 4 · Usage

## 12. Scraping Patterns

- [ ] Static vs Client-rendered Pages / 서버가 완성해주는 페이지 대 JS로 그리는 페이지 차이
- [ ] Pagination and Infinite Scroll / 페이지 넘김·무한 스크롤로 흩어진 데이터를 모으는 방법
- [ ] Structured Data Extraction / 뽑아낸 값을 정해진 형식으로 정리하는 작업
- [ ] Concurrency with Multiple Pages / 페이지 여러 개를 동시에 열어 속도를 높이는 방법
- [ ] Retry and Backoff / 실패한 요청을 간격을 늘려가며 재시도하는 전략
- [ ] Rate Limiting and robots.txt / 요청 빈도를 제한하고 크롤링 허용 범위를 지키는 규칙
- [ ] Legal and Ethical Boundaries / 스크래핑이 넘지 말아야 할 법적·윤리적 선

## 13. PDF and Screenshot Generation

- [ ] Screenshot Options / 전체 페이지·특정 영역·요소 단위로 찍는 옵션
- [ ] Image Format and Quality / PNG·JPEG 형식과 압축 품질을 정하는 설정
- [ ] PDF Options / 용지 크기·여백·배경 인쇄 여부를 정하는 옵션
- [ ] Header and Footer Templates / PDF 상단·하단에 반복되는 템플릿을 넣는 방법
- [ ] Waiting for Fonts and Images / 캡처 전에 폰트·이미지 로딩을 기다리는 이유
- [ ] Print Media Emulation / 화면용 대신 인쇄용 CSS를 적용해 캡처하는 방법

## 14. Performance and Tracing

- [ ] Tracing / 구간을 정해 성능 기록을 남기는 방법
- [ ] Runtime Metrics / 메모리·노드 수 등 런타임 수치를 읽는 API
- [ ] Lighthouse Integration / 라이트하우스 감사를 코드로 자동 실행하는 방법 `선택`
- [ ] Memory and Handle Leak Detection / 닫히지 않은 핸들·메모리 누수를 찾아내는 방법
- [ ] Reducing Launch Overhead and Browser Reuse / 매번 새로 안 띄우고 재사용해 속도를 아끼는 방법

---

# PART 5 · Testing and Operations

## 15. Testing with Puppeteer

- [ ] Pairing with a Runner / 러너·단언이 없어 Jest 같은 도구를 따로 붙이는 방식
- [ ] jest-puppeteer Preset / 브라우저 기동·전역 설정을 대신 해주는 Jest 프리셋 `선택`
- [ ] Visual Regression / 스크린샷을 픽셀 단위로 비교해 회귀를 잡는 방법
- [ ] Isolation via BrowserContext / 테스트마다 컨텍스트를 새로 만들어 상태를 격리하는 방법
- [ ] Where Playwright Fits Better / 러너·자동 대기가 필요하면 Playwright가 나은 지점

## 16. Deployment and Reliability

- [ ] Docker Image and Chrome Dependencies / 컨테이너 안에서 크롬 실행에 필요한 라이브러리 설치
- [ ] Sandbox Flags and Security Tradeoffs / 보안을 낮춰 실행 환경에 맞추는 절충
- [ ] Serverless / Lambda 환경에 맞춘 경량 크로미움 레이어
- [ ] Headless Shell vs Full Chrome / 경량 헤드리스 전용 빌드 대 일반 크롬의 차이
- [ ] Browser Pooling / 브라우저 인스턴스를 재사용해 여러 작업을 처리하는 방법
- [ ] Zombie Processes and Memory Growth / 제대로 안 닫혀 쌓이는 프로세스·메모리 증가 문제
- [ ] Bot Detection Reality / 자동화 탐지를 완전히 못 피한다는 현실과 우회 플러그인
- [ ] Debugging / 창을 띄우고 느리게 실행해 동작을 눈으로 보는 방법

---

# 이 로드맵 밖

- Playwright `software/skill-based/Testing/playwright.md`
- Selenium `software/skill-based/Testing/selenium.md`
- Jest `software/skill-based/Testing/jest.md`
- Node.js `software/skill-based/Frameworks/nodejs.md`
- JavaScript `software/skill-based/Languages/javascript.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
