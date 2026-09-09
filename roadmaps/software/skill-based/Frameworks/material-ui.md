# Material UI (MUI) `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to MUI

## 1. What is Material UI?

### Overview / What is it?

- [ ] React Component Library / 완성된 컴포넌트를 그대로 받아 쓰는 배포 형태
- [ ] Material Design Implementation / 구글 디자인 명세를 코드로 옮겨 놓은 결과물
- [ ] Emotion-Based CSS-in-JS / 스타일을 런타임에 클래스로 만들어 붙이는 엔진
- [ ] Product Family / Material UI·Base UI·Joy UI·MUI X로 갈리는 제품 계열

### Comparison and Judgment

- [ ] MUI vs Chakra UI / 정해진 디자인을 받을지 직접 조립할지의 갈림
- [ ] MUI vs shadcn/ui / 라이브러리에 의존할지 코드를 소유할지의 갈림
- [ ] Suitable Use Cases / 디자이너 없이 화면 수만 많은 프로젝트에 맞는 이유

### Versions

- [ ] Changes Since v5 / makeStyles가 빠지고 emotion으로 옮겨 간 변화
- [ ] Pigment CSS / 런타임 없이 빌드 때 CSS를 뽑는 차세대 엔진 `선택`

## 2. Getting Started

### Installation

- [ ] @mui/material + @emotion / 본체와 스타일 엔진을 짝으로 깔아야 하는 이유
- [ ] Icon Package / 머티리얼 아이콘을 컴포넌트로 받는 별도 패키지
- [ ] Font / 명세가 전제하는 Roboto를 따로 얹어야 하는 이유

### Basic Setup

- [ ] ThemeProvider / 테마 객체를 트리 전체에 내려보내는 통로
- [ ] CssBaseline / 브라우저 기본 스타일을 명세 기준으로 재설정하는 층
- [ ] StyledEngineProvider / 내 CSS가 이기도록 주입 순서를 뒤집는 설정
- [ ] Next.js App Router Integration / 서버 컴포넌트에서 emotion 캐시를 넘기는 방법

---

# PART 2 · Styling System

## 3. sx Prop

- [ ] sx Prop Basics / 테마를 아는 스타일을 컴포넌트에 직접 붙이는 prop
- [ ] Theme-aware Value / 색·간격을 실제 값 대신 테마 키로 적는 표기
- [ ] Responsive Value / 중단점별 값을 배열이나 객체로 한 번에 적는 표기
- [ ] Shorthand / p·m·bgcolor처럼 자주 쓰는 속성을 줄인 이름
- [ ] Nested Selector / 하위 Mui 클래스와 상태를 sx 안에서 겨냥하는 문법
- [ ] sx Runtime Cost / 렌더마다 스타일 객체를 새로 만드는 데 드는 값

## 4. styled() API

- [ ] styled() Usage / 스타일을 입혀 새 컴포넌트로 굳히는 방법
- [ ] Theme Access / 스타일 함수 인자로 테마 값을 받아 쓰는 통로
- [ ] shouldForwardProp / 스타일용 prop이 DOM 속성으로 새는 것을 막는 규칙
- [ ] Custom Variant Registration / 내가 만든 variant 값을 컴포넌트에 새로 여는 방법
- [ ] styled vs sx Selection Criteria / 재사용 여부로 두 방식을 가르는 기준

## 5. System Components

- [ ] Box / sx를 붙이려고 두는 가장 얇은 래퍼 엘리먼트
- [ ] Stack / 자식 사이 간격과 방향만 맡는 배치 컴포넌트
- [ ] Container / 본문 최대 폭을 중단점에 맞춰 잡는 컴포넌트
- [ ] Grid / 12칸 기준으로 열 너비를 나누는 배치 체계
- [ ] Breakpoint Helper / 중단점 미디어 쿼리 문자열을 만들어 주는 함수
- [ ] useMediaQuery / 중단점 판정을 JS 값으로 받아 분기하는 훅

---

# PART 3 · Component Usage

## 6. Component API Structure

- [ ] Slot / 컴포넌트 내부 조각을 지정한 요소로 갈아 끼우는 자리
- [ ] component Prop / 겉을 감싸는 태그를 다른 엘리먼트로 바꾸는 prop
- [ ] Global Class Name / 내부 요소를 밖에서 겨냥하게 열어 둔 고정 클래스
- [ ] Ownership State / 현재 prop 값에 따라 스타일이 갈리는 상태 묶음
- [ ] Base UI Unstyled / 스타일 없이 동작과 접근성만 남긴 뼈대 `선택`

## 7. Core Component Groups

- [ ] Input Components / 라벨과 검증 표시까지 묶어 주는 입력 컴포넌트군
- [ ] Feedback Components / 결과와 대기 상태를 화면에 알리는 컴포넌트군
- [ ] Navigation Components / 이동 경로를 드러내고 여닫는 컴포넌트군
- [ ] Surface Components / 그림자와 테두리로 내용 덩어리를 구분하는 컴포넌트군
- [ ] Data Display / 표·목록·꼬리표로 데이터를 늘어놓는 컴포넌트군
- [ ] Transition Components / 등장과 사라짐 타이밍을 명세대로 맞추는 컴포넌트군

## 8. Form Handling

- [ ] Controlled Component Pattern / 입력 값을 상태로 붙잡아 되돌려 주는 구조
- [ ] react-hook-form Integration / 비제어 폼과 제어 입력을 이어 붙이는 어댑터
- [ ] Validation / 검증 실패를 error prop과 문구로 드러내는 방법
- [ ] FormControl / 라벨·입력·도움말의 상태를 함께 묶는 구조

## 9. MUI X `선택`

- [ ] Data Grid / 정렬·필터·가상 스크롤을 갖춘 대용량 표
- [ ] Date and Time Pickers / 달력 입력과 날짜 라이브러리를 잇는 컴포넌트
- [ ] Charts / MUI 테마 위에서 도표를 그리는 컴포넌트 묶음
- [ ] Tree View / 접히는 계층 목록을 다루는 컴포넌트
- [ ] License Policy / 무료와 유료 컴포넌트를 가르는 경계

---

# PART 4 · Theming System

## 10. Theme Structure

- [ ] createTheme / 일부만 적어도 나머지를 채워 주는 테마 생성 함수
- [ ] Palette / 주·보조 색에서 명암 단계를 파생시키는 색 체계
- [ ] Typography Variant / 글자 크기와 굵기를 이름 붙인 단계로 고정한 표
- [ ] Spacing Scale / 간격 숫자를 8px 배수로 환산하는 함수
- [ ] Breakpoints / 화면 폭을 다섯 구간으로 자르는 기준값
- [ ] Shape / 모서리 둥글기를 한 값으로 통일하는 자리
- [ ] Shadows, zIndex, transitions / 깊이·겹침·속도를 숫자 표로 고정한 테마 값
- [ ] useTheme / 렌더 안에서 현재 테마 값을 꺼내는 훅

## 11. Component Default Overrides

- [ ] theme.components / 컴포넌트별 덮어쓰기를 테마 한 곳에 모으는 자리
- [ ] defaultProps / 컴포넌트가 받을 prop 기본값을 전역으로 바꾸는 설정
- [ ] styleOverrides / 컴포넌트 내부 슬롯별로 CSS를 덮어쓰는 자리
- [ ] variants / prop 조합이 맞을 때만 붙는 스타일 규칙
- [ ] Theme Nesting / 하위 트리에만 다른 테마를 겹쳐 적용하는 방법

## 12. Color Scheme & Extensions

- [ ] colorSchemes / 라이트·다크 값을 CSS 변수로 함께 내보내는 설정
- [ ] InitColorSchemeScript / 첫 페인트 전에 모드를 정해 깜빡임을 없애는 스크립트
- [ ] useColorScheme / 현재 색 모드를 읽고 사용자 선택으로 바꾸는 훅
- [ ] Palette Extension / 팔레트에 없는 색 이름을 새로 여는 방법
- [ ] TypeScript Module Augmentation / 늘린 테마 키를 타입 정의에 이어 붙이는 선언

---

# PART 5 · Production

## 13. Performance Optimization

- [ ] Bundle Size / 안 쓰는 컴포넌트가 번들에서 빠지는 조건
- [ ] Import Path Rules / 묶음 경로 대신 개별 경로로 가져와야 하는 이유
- [ ] Emotion Runtime Cost / 클래스 직렬화와 주입이 렌더에 얹는 부담
- [ ] Rerender Optimization / sx 객체를 렌더 밖으로 빼 재생성을 막는 방법
- [ ] Virtualization / 보이는 행만 그려 긴 목록을 버티는 방식

## 14. SSR & Accessibility

- [ ] Emotion Cache / 서버에서 만든 스타일을 모아 HTML에 싣는 저장소
- [ ] Hydration Mismatch Handling / 서버와 클라이언트의 클래스 이름이 어긋나는 원인
- [ ] Accessibility / 컴포넌트가 이미 붙여 둔 ARIA와 초점 처리
- [ ] Keyboard Navigation / 화살표와 Tab으로 컴포넌트를 옮겨 다니는 규칙
- [ ] Locale Text / 컴포넌트 안 고정 문구를 언어별로 바꾸는 방법

## 15. Migration and Operations

- [ ] makeStyles Removal and Replacement / v4 스타일 API를 sx와 styled로 옮기는 절차
- [ ] codemod Usage / 옛 문법을 스크립트로 일괄 치환하는 방법
- [ ] Design Token and Theme Synchronization / 디자인 도구의 토큰을 테마 객체로 옮기는 경로
- [ ] Storybook Integration / 테마를 입힌 컴포넌트를 따로 띄워 보는 구성 `선택`
- [ ] In-House Theme Packaging / 사내 테마를 패키지로 떼어 공유하는 구성

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- Next.js `software/skill-based/Frameworks/nextjs.md`
- 디자인 시스템 이론 `software/skill-based/CS-Theory/design-system.md`
- CSS 문법 전반 `software/skill-based/Languages/css.md`
- 대안 라이브러리 `software/skill-based/Frameworks/chakra-ui.md`, `shadcn-ui.md`
- TypeScript `software/skill-based/Languages/typescript.md`
