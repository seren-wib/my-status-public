# Appium `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Mobile E2E

## 1. What is Appium?

### Overview / What is it?

- [ ] Cross-platform Mobile Automation / 하나의 코드로 안드로이드·iOS를 동시에 미는 방식
- [ ] W3C WebDriver Protocol / Appium이 확장해서 쓰는 표준 통신 규격
- [ ] Client-Server Architecture / 클라이언트 명령을 서버가 기기에 전달하는 구조
- [ ] Appium 1.x vs 2.x / 드라이버·플러그인을 따로 설치하는 구조로 바뀐 변화

### Comparison with Other Tools

- [ ] Appium vs Espresso and XCUITest / 앱 밖에서 몰지 안에서 몰지 가르는 기준
- [ ] Appium vs Detox and Maestro / 범용 프로토콜과 RN 특화 도구를 가르는 기준
- [ ] When to Choose Appium / 팀 상황에 맞게 이 도구를 고르는 판단 기준

## 2. Mobile Testing Basics

- [ ] Native, Hybrid, Mobile Web App / 앱 구현 방식에 따라 테스트 전략이 갈리는 세 유형
- [ ] Emulator, Simulator vs Real Device / 가상 기기와 실기기 중 테스트 환경을 고르는 기준
- [ ] Position of E2E in the Test Pyramid / 단위·통합 테스트 위에 놓이는 E2E의 위치
- [ ] Android SDK / adb로 기기와 통신하는 안드로이드 개발 도구 묶음
- [ ] Xcode / simctl로 시뮬레이터를 다루는 애플 개발 환경
- [ ] Build Artifact / 안드로이드·iOS 배포 단위 파일 형식들

## 3. Getting Started

### Installation

- [ ] Node.js / npm install appium으로 서버를 설치하는 실행 환경
- [ ] appium-doctor / 설치 환경을 점검하고 드라이버 목록을 확인하는 명령
- [ ] Driver Installation / 안드로이드·iOS용 드라이버를 따로 설치하는 과정
- [ ] Appium Inspector / 요소 트리를 눈으로 보며 로케이터를 찾는 도구

### First Run

- [ ] Starting the Appium Server / 세션을 받을 수 있게 서버 프로세스를 띄우는 절차
- [ ] Session Creation and Teardown / 세션을 열고 정리해 리소스를 반납하는 흐름
- [ ] Running the First Script / 서버에 연결해 첫 자동화 명령을 실행하는 절차
- [ ] Reading Server Logs / 세션·명령 처리 과정을 서버 로그로 확인하는 방법

---

# PART 2 · Sessions and Element Control

## 4. Capabilities

- [ ] W3C Capabilities Structure / appium: 접두사로 벤더 확장을 표시하는 구조
- [ ] Common Capabilities / 플랫폼·드라이버·기기를 지정하는 필수 옵션들
- [ ] App Targeting / 실행할 앱 파일과 패키지를 지정하는 옵션들
- [ ] Session Reset / 세션마다 앱 상태를 초기화하는 정도를 정하는 옵션들
- [ ] Timeout / 명령이 없으면 세션을 끊는 대기 시간 설정
- [ ] Per-Environment Capability Profiles / 환경별로 capability 세트를 나눠 관리하는 방식

## 5. Element Locating

- [ ] Locator Strategy / 요소를 찾는 여러 식별 방식들
- [ ] Android UiAutomator Selector / 안드로이드 네이티브 셀렉터로 요소를 찾는 문법
- [ ] iOS Predicate String and Class Chain / 조건식과 계층 경로로 iOS 요소를 찾는 두 방식
- [ ] Accessibility ID First Principle / 접근성 ID를 최우선으로 쓰라는 로케이터 원칙
- [ ] Cost of XPath / 느리고 깨지기 쉬운 XPath 사용의 대가
- [ ] Tree Exploration with Appium Inspector / 인스펙터로 요소 트리를 뒤져 로케이터를 뽑는 방법
- [ ] Embedding Test IDs in the App / 앱 코드에 테스트용 식별자를 미리 심는 방법

## 6. Interactions

- [ ] Basic Interactions / 클릭·입력·지우기 같은 기본 조작 명령
- [ ] W3C Actions API / 포인터·키 입력을 조합해 만드는 저수준 조작
- [ ] Gesture / 스와이프·스크롤·핀치 같은 터치 동작들
- [ ] Mobile Command / mobile: 접두사로 실행하는 플랫폼 전용 확장 명령
- [ ] Scroll to Element Strategy / 화면 밖 요소를 찾아 스크롤하는 전략
- [ ] Keyboard Handling / 소프트 키보드를 열고 닫는 처리
- [ ] Device Control / 회전·잠금·백그라운드 전환 같은 기기 제어
- [ ] Permission and Alert Dialog / 권한 요청·경고 팝업을 자동 처리하는 방법
- [ ] Deep Link Launch / URL 스킴으로 특정 화면에 바로 진입하는 방법

---

# PART 3 · Writing Tests

## 7. Client / Test Runner

### Language Selection `택 1`

- JavaScript / WebdriverIO로 붙는 추천 클라이언트 언어 `software/skill-based/Languages/javascript.md` `추천` `위임`
- Java / JUnit·TestNG 러너와 함께 쓰는 언어 `software/skill-based/Languages/java.md` `위임`
- Python / pytest 러너와 함께 쓰는 언어 `software/skill-based/Languages/python.md` `위임`
- [ ] Ruby and C# / 상대적으로 적게 쓰이는 나머지 클라이언트 언어

### Runner Configuration

- [ ] Test Runner Integration / 훅·픽스처로 테스트 러너와 엮는 방법
- [ ] Driver Setup and Teardown / 테스트 전후로 드라이버를 만들고 정리하는 절차
- [ ] Config File Separation / 환경별 설정을 파일로 분리해 관리하는 방식

## 8. Waits / Synchronization

- [ ] Implicit Wait / 요소를 찾을 때까지 전역으로 기다리는 설정
- [ ] Explicit Wait / 조건이 참이 될 때까지 기다리는 대기 방식
- [ ] Fluent Wait / 주기적으로 조건을 확인하며 기다리는 방식
- [ ] No-Sleep Principle / 고정 시간 sleep 대신 조건 대기를 쓰라는 원칙
- [ ] App Ready Criteria / 앱이 조작 가능한 상태인지 판단하는 기준
- [ ] Stale Element and Retry / 갱신된 요소 참조 오류를 재시도로 넘기는 처리

## 9. Structural Design

- [ ] Page Object Model / 화면 구조를 클래스로 감싸 재사용하는 설계
- [ ] Screen and Component Object / 화면 단위와 부품 단위로 나눈 객체 설계
- [ ] Test Data Separation / 테스트 코드에서 데이터를 분리해 관리하는 방식
- [ ] App State Reset Strategy / 테스트마다 앱 상태를 초기화하는 전략
- [ ] Test Independence / 테스트끼리 순서·상태에 의존하지 않게 하는 원칙
- [ ] Helper and Custom Command / 반복 동작을 재사용 함수로 뽑아내는 방법
- [ ] Minimizing Platform Branching / 코드에서 안드로이드·iOS 분기를 최소화하는 설계

---

# PART 4 · Platform Deep Dive

## 10. Android Specifics

- [ ] UiAutomator2 Driver / 안드로이드 UI 트리를 조작하는 기본 드라이버
- [ ] Espresso Driver / 구글 Espresso 프레임워크로 도는 드라이버 `선택`
- [ ] Using adb / logcat·설치·shell 명령으로 기기를 다루는 방법
- [ ] Intent and Activity / 특정 화면을 인텐트로 바로 여는 방법
- [ ] Pre-Granting Permissions / 팝업 없이 앱 권한을 미리 부여하는 방법
- [ ] Emulator Management / avdmanager로 에뮬레이터를 만들고 관리하는 방법

## 11. iOS Specifics

- [ ] XCUITest Driver / 애플 XCUITest 프레임워크로 도는 기본 드라이버
- [ ] How WebDriverAgent Works / 기기에 상주하며 명령을 중계하는 원리
- [ ] Code Signing and Provisioning Profile / 실기기 설치를 위한 서명·인증 절차
- [ ] Simulator Management / simctl로 시뮬레이터를 만들고 관리하는 방법
- [ ] Real Device Connection / go-ios·devicectl로 실기기에 붙는 방법
- [ ] System Alert Handling / 권한 요청 같은 iOS 시스템 팝업을 처리하는 방법

## 12. Context / Hybrid

- [ ] Native vs WebView Context / 네이티브 영역과 웹뷰 영역을 구분하는 개념
- [ ] Context Switching / getContexts로 컨텍스트 목록을 받아 전환하는 방법
- [ ] Automatic Chromedriver Management / 웹뷰 버전에 맞는 크롬드라이버를 자동으로 맞추는 기능
- [ ] Safari and Mobile Web / iOS 사파리로 모바일 웹을 테스트하는 방법
- [ ] Accessibility Tree of React Native Apps / RN 앱이 접근성 트리에 노출되는 방식
- [ ] Flutter Integration Driver / 플러터 전용 프로토콜로 도는 드라이버 `선택`

---

# PART 5 · Running and Operations

## 13. Execution Infrastructure

- [ ] Local Server vs Grid / 로컬에서 돌릴지 분산 환경에 맡길지 가르는 기준
- [ ] Selenium Grid Integration / 셀레니움 그리드에 붙여 실행을 분산하는 방법
- [ ] Device Cloud / 실기기를 빌려주는 브라우저스택 등 클라우드 서비스
- [ ] AWS Device Farm and Firebase Test Lab / 클라우드 업체가 제공하는 실기기 팜
- [ ] Parallel Execution / 포트·기기를 나눠 테스트를 동시에 도는 방법
- [ ] Docker Android / 컨테이너 안에서 안드로이드 에뮬레이터를 도는 방법 `선택`

## 14. Stability and Debugging

- [ ] Flaky Causes / 네트워크, 애니메이션, 타이밍
- [ ] Disabling Animations / 애니메이션을 꺼서 테스트 흔들림을 줄이는 방법
- [ ] Retry Policy and Its Limits / 재시도로 커버되는 범위와 그 한계
- [ ] Screenshot and Video Recording / 실패 시점을 이미지·영상으로 남기는 방법
- [ ] Page Source Dump / 실패 시점 화면 구조를 텍스트로 덤프하는 방법
- [ ] Server and Device Log / 서버·기기 로그를 모아 원인을 추적하는 방법

## 15. Extended Testing

- [ ] Visual Regression / 화면 이미지를 비교해 시각적 회귀를 잡는 방법
- [ ] Performance Data Collection / 앱 실행 중 성능 지표를 수집하는 방법
- [ ] Network Condition Simulation / 느린 네트워크·오프라인 상황을 재현하는 방법
- [ ] Accessibility Auditing / 접근성 기준 위반 여부를 자동으로 점검하는 방법
- [ ] Localization and Multi-Resolution Scenarios / 언어·해상도별 화면을 검증하는 시나리오

## 16. CI Integration

- [ ] Execution Timing / 야간·배포 전 등 실행 시점을 정하는 기준
- [ ] Build Artifact Integration / CI에서 빌드 산출물을 받아 테스트에 연결하는 방법
- [ ] Report / Allure·JUnit XML로 결과를 정리하는 방식
- [ ] Failure Triage / 앱 버그 vs 테스트 버그
- [ ] Runtime and Cost Management / 실행 시간과 비용을 함께 관리하는 방법
- [ ] Suite Prioritization / 스모크·회귀 테스트 순서를 정하는 우선순위

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Android 개발 `software/role-based/android.md`
- iOS 개발 `software/role-based/ios.md`
- React Native `software/skill-based/Frameworks/react-native.md`
- Flutter `software/skill-based/Frameworks/flutter.md`
- Detox `software/skill-based/Testing/detox.md`
