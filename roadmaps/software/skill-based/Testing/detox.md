# Detox `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Detox

## 1. What is Detox?

### Overview / What is it?

- [ ] Gray Box E2E for React Native / 앱 내부에 붙어 상태를 아는 테스트 방식
- [ ] Automatic Synchronization Concept / 네이티브 작업 종료를 앱이 직접 알리는 개념
- [ ] Runs on a Native Test Runner / 러너를 새로 안 만들고 Jest에 얹는 구조
- [ ] Detox vs Appium and Maestro / 앱 안에 붙을지 밖에서 몰지 가르는 기준

### When to Use

- [ ] Deciding E2E Coverage Scope / 전체 대신 핵심 플로우만 고르는 기준
- [ ] Role Split with Jest and React Native Testing Library / 단위·통합과 E2E 책임 분리
- [ ] Maintenance Cost and ROI / 깨지기 쉬운 테스트 유지비 대비 효과

## 2. Prerequisites

- [ ] React Native Build Structure / 네이티브 빌드 산출물이 나오는 구조
- [ ] Debug vs Release Build / 최적화 여부로 갈리는 두 빌드 모드
- [ ] Metro Bundler / JS 번들을 서빙하는 RN 개발 서버
- [ ] Xcode and Android Studio Toolchain / iOS·안드로이드 빌드용 IDE 도구모음
- [ ] Simulator and Emulator / iOS·안드로이드 가상 기기를 관리하는 방법
- [ ] Meaning of the testID Prop / 뷰를 안정적으로 찾기 위한 식별자 역할

## 3. Getting Started

### Installation

- [ ] detox and detox-cli / 라이브러리와 명령줄 도구로 나뉜 설치 단위
- [ ] Test Runner / 러너를 직접 안 만들고 외부 러너에 얹는 구조
- [ ] detox init / 초기 설정 파일과 예시 테스트를 만드는 명령
- [ ] applesimutils / iOS 시뮬레이터를 명령줄로 제어하는 유틸

### First Run

- [ ] detox build / 네이티브 앱을 테스트용으로 빌드하는 명령
- [ ] detox test / 빌드된 앱을 시뮬레이터에서 실행하는 명령
- [ ] .detoxrc and detox.config.js / 디바이스·빌드 설정을 담는 파일 형식
- [ ] Writing and Running the First Spec / 첫 테스트 코드 작성과 실행 절차

---

# PART 2 · Writing Tests

## 4. Matchers

- [ ] by.id / testID로 우선 매칭해 요소를 찾는 원칙
- [ ] by.text, by.label, by.type, by.traits / 텍스트·라벨·타입·속성으로 찾는 매처
- [ ] Matcher Composition / and·withAncestor·withDescendant로 조건 조합
- [ ] atIndex / 같은 매처에 걸린 여러 요소 중 하나를 고르는 방법
- [ ] testID Naming Convention / 화면·컴포넌트별 식별자 이름 규칙

## 5. Actions

- [ ] tap, multiTap, longPress / 탭·연속 탭·길게 누르기 동작
- [ ] typeText, replaceText, clearText / 입력창에 글자를 넣고 지우는 동작
- [ ] scroll and scrollTo / 방향 스크롤과 특정 위치까지 스크롤
- [ ] swipe and pinch / 스와이프와 확대·축소 제스처
- [ ] Coordinate-Based Actions / 좌표를 지정해 탭하는 tapAtPoint 방식
- [ ] whileElement / 요소가 나올 때까지 스크롤을 반복하는 방법
- [ ] Slider and Picker / 슬라이더와 피커 값을 조작하는 동작

## 6. Expectations

- [ ] toBeVisible and toExist / 화면에 보이는지와 존재하는지 구분
- [ ] toHaveText, toHaveLabel, toHaveId / 텍스트·라벨·id 값을 검증하는 단언
- [ ] toHaveValue and toHaveToggleValue / 입력값과 토글 상태를 검증하는 단언
- [ ] Negation with not / 단언 앞에 붙여 반대 조건을 검증하는 방법
- [ ] waitFor and withTimeout / 조건이 될 때까지 정해진 시간 기다리는 단언
- [ ] Reading Assertion Failure Messages / 실패 로그에서 원인 요소를 찾는 방법

## 7. Test Structure

- [ ] describe and it / 테스트를 그룹과 개별 케이스로 나누는 구조
- [ ] beforeAll and beforeEach / 전체 한 번과 매 테스트마다 도는 초기화
- [ ] Page Object and Screen Object / 화면 요소를 클래스로 감싸는 패턴
- [ ] Test Independence and State Reset / 이전 테스트 상태가 안 남게 만드는 원칙
- [ ] Splitting by Scenario / 시나리오 단위로 테스트 파일을 나누는 기준
- [ ] Test Data Preparation Strategy / 테스트에 쓸 계정·데이터를 준비하는 방법

---

# PART 3 · Synchronization and App Control

## 8. Synchronization

- [ ] How Automatic Synchronization Works / 네이티브 작업 완료를 앱이 감지해 알리는 원리
- [ ] Tracked Resources / 네트워크·타이머·애니메이션·JS 스레드 추적 대상
- [ ] Idle Detection Failure Cases / 대기 상태를 못 알아채 멈추는 상황들
- [ ] When to Use disableSynchronization / 자동 동기화를 끄고 수동 대기할 때
- [ ] waitFor Overuse Warning / 동기화 대신 waitFor로 땜질하는 문제
- [ ] Infinite Animation and setInterval / 안 끝나 동기화가 멈추는 대표 원인

## 9. Device API

- [ ] launchApp / 실행과 실행 인자로 초기 상태를 넘기는 방법
- [ ] reloadReactNative / JS 번들만 다시 로드해 앱 상태를 초기화하는 명령
- [ ] terminateApp and sendToHome / 앱 종료와 백그라운드 전환 제어
- [ ] Permission Specification / 실행 전에 권한 허용 여부를 미리 지정하는 방법
- [ ] setLocation and Deep Link / 위치 좌표와 딥링크로 진입 상태 제어
- [ ] Push Notification Simulation / 실제 서버 없이 푸시 수신을 재현하는 방법
- [ ] Orientation and setStatusBar / 화면 방향과 상태바 표시를 바꾸는 제어
- [ ] Biometric Authentication Simulation / 지문·얼굴 인증을 통과시키는 시뮬레이션

## 10. External Dependency Control

- [ ] Mock Server / 실서버 대신 로컬에서 응답을 대신하는 서버
- [ ] Mock Mode Injection via Launch Args / 실행 인자로 목 모드 여부를 앱에 전달
- [ ] Network Stub Strategy / API 응답을 고정값으로 대체하는 전략
- [ ] Test Account and Seed Data / 테스트 전용 계정과 초기 데이터 준비
- [ ] Time and Random / 시간과 난수를 고정해 결과를 재현 가능하게
- [ ] E2E-Only Build Flag / E2E 전용 코드만 켜는 빌드 플래그

---

# PART 4 · Configuration and Platforms

## 11. Configuration

- [ ] Device Config / type·device 값으로 테스트 대상 기기를 지정
- [ ] App Config / binaryPath·build 값으로 앱 빌드 경로 지정
- [ ] Configuration Composition / 여러 설정을 조합해 하나로 합치는 방법
- [ ] Behavior / init·cleanup·launchApp 생명주기 훅 설정
- [ ] Artifacts Configuration / 로그·영상 저장 방식을 정하는 설정
- [ ] Session and Test Runner / 세션 서버와 러너 연동 관련 옵션

## 12. iOS

- [ ] Xcode Scheme and Build Setting / 빌드 대상과 옵션을 지정하는 설정
- [ ] Simulator Targeting / os·type 값으로 시뮬레이터를 지정
- [ ] Running E2E on a Release Build / 최적화된 릴리스 빌드로 테스트하는 방법
- [ ] applesimutils Permission Control / 시뮬레이터 권한을 미리 부여하는 제어
- [ ] Real Device Support Limitations / 실기기에서 못 쓰는 기능들의 한계

## 13. Android

- [ ] androidTest and Gradle / 안드로이드 테스트 빌드를 위한 설정
- [ ] Emulator AVD Preparation / 테스트용 가상 기기를 미리 만드는 과정
- [ ] Headless Emulator / 화면 없이 백그라운드로 도는 에뮬레이터
- [ ] adb reverse / 에뮬레이터가 로컬 서버에 접속하게 잇는 명령
- [ ] Release Build Signing / 릴리스 빌드에 서명을 붙이는 절차
- [ ] Disabling Animation Scale / 애니메이션을 꺼서 테스트를 안정화하는 설정

---

# PART 5 · Operations

## 14. Debugging and Stability

- [ ] Log Level / --loglevel trace로 상세 로그를 켜는 옵션
- [ ] Artifacts / 스크린샷·영상·뷰 계층을 남기는 기록
- [ ] Device Log Inspection / 기기 네이티브 로그로 원인을 추적하는 방법
- [ ] Flaky Cause Classification / 간헐적 실패 원인을 유형별로 나누는 방법
- [ ] Retry Criteria / --retries로 실패 시 재시도 횟수를 정하는 기준
- [ ] Failure Reproduction Procedure / 실패한 테스트를 로컬에서 재현하는 절차

## 15. Performance and Extension

- [ ] Reducing Execution Time / 전체 테스트 실행 시간을 줄이는 방법
- [ ] Parallel Execution / --workers로 여러 기기에서 동시 실행
- [ ] Test Sharding / 테스트를 나눠 여러 러너에 분산 실행하는 방법
- [ ] Visual Regression Integration / 화면 스크린샷 차이를 비교하는 확장 `선택`
- [ ] Custom Matcher and Detox Plugin / 기본 매처 밖의 기능을 확장하는 방법 `선택`
- [ ] Constraints of the Expo Environment / Expo에서 못 쓰는 기능들의 제약 `선택`

## 16. CI Integration

- [ ] macOS Runner Requirement / iOS 빌드가 macOS 러너에서만 도는 이유
- [ ] Emulator Boot Automation / CI에서 에뮬레이터를 자동으로 띄우는 절차
- [ ] Build Cache Strategy / 매번 새로 빌드하지 않도록 캐시하는 전략
- [ ] Execution Timing / PR마다·야간 배치로 실행 시점을 정하는 방법
- [ ] Report Collection / jest-junit·Allure로 결과를 모으는 방법
- [ ] Failure Notification and Triage Process / 실패를 알리고 원인을 분류하는 절차

---

# 이 로드맵 밖

- React Native `software/skill-based/Frameworks/react-native.md`
- QA 전반 `software/role-based/qa.md`
- Jest `software/skill-based/Testing/jest.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- Android 개발 `software/role-based/android.md`
- iOS 개발 `software/role-based/ios.md`
