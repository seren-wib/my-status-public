# Chakra UI `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Chakra UI

## 1. What is Chakra UI?

### Overview / What is it?

- [ ] React Component Library / 리액트 트리에 바로 끼우는 완성 컴포넌트 모음
- [ ] Style Props-based API / 스타일 값을 컴포넌트 인자로 넘기는 설계
- [ ] Ark UI / 컴포넌트 동작을 Zag.js 상태 기계로 정의한 층
- [ ] Panda CSS Style Engine / v3가 스타일을 정적 CSS로 뽑는 내부 엔진

### Comparison and Judgment

- [ ] Chakra UI vs MUI / 디자인 명세 유무로 갈리는 두 라이브러리의 차이
- [ ] Chakra UI vs Tailwind Combination / 클래스와 props 스타일을 섞을 때의 판단
- [ ] When to Choose Chakra UI / 이 라이브러리가 맞는 프로젝트를 가르는 기준

### Versions

- [ ] v2 / Emotion 런타임 위에 스타일을 얹던 구버전 구조
- [ ] v3 Changes / 스니펫과 슬롯 레시피로 바뀐 지점

## 2. Getting Started

### Installation

- [ ] @chakra-ui/react / 컴포넌트와 스타일 시스템을 함께 받는 단일 패키지
- [ ] Provider Setup / 앱 최상단에 스타일 시스템을 주입하는 감싸개
- [ ] defaultSystem / 기본 토큰과 레시피가 미리 담긴 시스템 객체
- [ ] CLI Snippet Addition / 부품 조립 코드를 내 소스로 받아오는 명령

### Initial Setup

- [ ] Color Mode Initialization / 모드 상태를 next-themes에 맡기는 초기화
- [ ] Framework Integration / Next.js·Vite마다 달라지는 프로바이더 배치

---

# PART 2 · Style System

## 3. Style Props

- [ ] Style Props Concept / CSS 속성 하나하나를 prop으로 넘기는 방식
- [ ] Shorthand / padding·margin을 한두 글자로 줄인 표기
- [ ] Token-aware Value / 숫자를 넘기면 테마 눈금 값으로 바뀌는 규칙
- [ ] Responsive Value / 화면 너비별 값을 배열이나 객체로 주는 문법
- [ ] Pseudo Props / 밑줄 접두사로 가상 클래스 상태에 스타일을 거는 표기
- [ ] Group, Peer Props, _groupHover, _peerChecked / 부모나 형제 상태에 따라 자기 스타일을 바꾸는 표기
- [ ] css Prop / style props로 안 되는 CSS를 넣는 통로

## 4. Layout Primitives

- [ ] Box / 모든 style props를 받는 최소 단위 상자
- [ ] Flex, Stack, HStack, VStack / 가로·세로 배치와 사이 간격을 맡는 상자
- [ ] Grid and SimpleGrid / 열 수와 최소 너비로 격자를 잡는 상자
- [ ] Container, Center, Spacer / 최대 너비·가운데 정렬·빈 자리를 맡는 조각
- [ ] AspectRatio and Wrap / 비율 고정과 넘칠 때 줄바꿈을 맡는 상자
- [ ] Utility Component / 반복과 조건 분기를 JSX 안에서 줄이는 조각 `선택`

## 5. Tokens

- [ ] Core Token vs Semantic Token / 원시 값과 용도 이름을 나눠 두는 두 층
- [ ] Color Palette / 한 컴포넌트의 색 계열을 통째로 바꾸는 지정
- [ ] Spacing and Sizing Scale / 간격과 크기를 정해진 눈금으로 고정하는 체계
- [ ] Typography Token / 글꼴·크기·행간을 묶어 이름 붙인 값
- [ ] Radius, Shadow, zIndex / 모서리·그림자·쌓임 순서를 값으로 통제하는 토큰
- [ ] Breakpoints / 반응형 값이 갈라지는 화면 너비 경계
- [ ] Conditions Definition / 상태 선택자에 내 이름을 붙여 두는 정의

---

# PART 3 · Component Usage

## 6. Component API Structure

- [ ] Compound Component / 한 컴포넌트를 여러 부품 태그로 쪼개 쓰는 구조
- [ ] asChild Prop / 자기 대신 자식 요소를 실제 태그로 쓰게 하는 지정
- [ ] Controlled vs Uncontrolled / 열림 상태를 밖에서 쥘지 안에 맡길지 가르는 기준
- [ ] Common Props / 컴포넌트마다 공통으로 뚫려 있는 변형 인자
- [ ] Portal Usage Rules / 겹침 요소를 body로 옮겨 잘림을 피하는 규칙

## 7. Core Component Groups

- [ ] Form Components / 라벨·오류 문구까지 묶어 주는 입력 부품
- [ ] Overlay Components / 포커스 가둠과 바깥 클릭 닫기를 맡는 겹침 층
- [ ] Feedback Components / 진행과 결과를 화면에 알리는 표시 부품
- [ ] Navigation Components / 화살표 키 이동과 열림 하나를 관리하는 이동 부품
- [ ] Data Display / 값을 읽기 전용으로 늘어놓는 표시 부품
- [ ] Typography Components / 글자 크기와 색을 토큰으로 고정한 텍스트 부품

## 8. Form Handling

- [ ] Field Structure / 라벨과 오류 문구를 id로 이어 붙이는 묶음
- [ ] react-hook-form Integration / 비제어 폼 라이브러리에 입력 부품을 물리는 방법
- [ ] Zod Validation / 스키마 검사 결과를 오류 문구로 옮기는 연결
- [ ] Native Element Delegation / asChild로 실제 input 요소에 넘기는 방법

---

# PART 4 · Theming and Recipes

## 9. System Configuration

- [ ] createSystem and defineConfig / 기본 시스템에 내 설정을 합쳐 만드는 함수
- [ ] Theme Extension / 기본 토큰 위에 내 값을 덧붙이는 자리
- [ ] globalCss / 시스템 안에서 전역 선택자 스타일을 두는 자리
- [ ] Preflight / 브라우저 기본 여백과 글꼴을 걷어내는 초기화
- [ ] Custom Condition / 데이터 속성으로 내 상태 선택자를 만드는 설정
- [ ] Cascade Layer Structure / 레이어로 스타일 우선순위를 층으로 나눈 구조

## 10. Recipes

- [ ] defineRecipe / 단일 요소 컴포넌트의 변형 규칙을 적는 정의
- [ ] defineSlotRecipe / 부품이 여럿인 컴포넌트를 부품별로 적는 정의
- [ ] base, variants, defaultVariants / 공통 스타일과 변형 목록·기본값을 나눠 적는 자리
- [ ] compoundVariants / 두 변형이 겹칠 때만 적용할 스타일 규칙
- [ ] useRecipe and useSlotRecipe / 레시피를 내 컴포넌트에서 직접 꺼내 쓰는 훅
- [ ] Overriding Built-in Component Recipes / 기본 제공 컴포넌트의 변형을 갈아끼우는 방법

## 11. Color Mode & Theming

- [ ] Light and Dark Semantic Token / 모드마다 다른 값을 한 이름에 묶는 토큰
- [ ] useColorMode and ColorModeButton / 현재 모드를 읽고 뒤집는 훅과 버튼
- [ ] SSR Flicker Prevention / 첫 그림에서 색이 한 번 튀는 것을 막는 방법
- [ ] Multi Brand Theme Composition / 브랜드마다 다른 토큰 묶음을 갈아 끼우는 구성
- [ ] Theme File Separation Strategy / 토큰과 레시피를 파일로 쪼개 두는 기준

---

# PART 5 · Production

## 12. TypeScript & Tools

- [ ] chakra typegen / 내 토큰 이름을 prop 타입으로 뽑아내는 명령
- [ ] chakra() Factory / 내 태그에 style props를 붙여 주는 함수
- [ ] ESLint Rules / 잘못된 prop과 구버전 API를 잡는 검사 규칙 `선택`
- [ ] Storybook Integration / 프로바이더를 데코레이터로 씌우는 연결 `선택`

## 13. Performance and SSR

- [ ] Bundle Size and Tree Shaking / 안 쓴 컴포넌트를 빌드에서 덜어내는 조건
- [ ] Runtime Style Cost / 렌더할 때마다 스타일 값을 계산하는 비용
- [ ] RSC / 서버 컴포넌트와 클라이언트를 가르는 경계
- [ ] Rerender Optimization / 매 렌더마다 새로 생기는 스타일 객체를 줄이는 방법
- [ ] Static CSS Extraction Strategy / 자주 쓰는 스타일을 빌드 때 미리 뽑는 전략

## 14. Accessibility and Migration

- [ ] Built-in Accessibility Scope / 라이브러리가 대신 처리해 주는 접근성 범위
- [ ] Focus Management and Keyboard Navigation / 포커스 순서와 키 이동을 넘겨받는 동작
- [ ] ARIA Attribute Customization / 자동으로 붙는 role과 aria 값을 바꾸는 방법
- [ ] v2 → v3 Migration / 구버전 코드를 자동 변환기로 옮기는 절차
- [ ] Deprecated API Cleanup / 사라진 prop과 컴포넌트를 걷어내는 정리

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- Next.js `software/skill-based/Frameworks/nextjs.md`
- 디자인 시스템 이론 `software/skill-based/CS-Theory/design-system.md`
- CSS 문법 전반 `software/skill-based/Languages/css.md`
- 대안 라이브러리 `software/skill-based/Frameworks/material-ui.md`, `shadcn-ui.md`
- TypeScript `software/skill-based/Languages/typescript.md`
