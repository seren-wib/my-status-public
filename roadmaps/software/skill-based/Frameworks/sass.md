# Sass / SCSS `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Sass

## 1. What is Sass?

### Overview of Sass / What is it?

- [ ] CSS Preprocessor / CSS에 없는 문법을 얹어 미리 푸는 도구
- [ ] Compile to Plain CSS / 빌드 때 평범한 CSS로 바뀌어 나가는 과정
- [ ] Sass vs Native CSS Feature / 브라우저가 따라잡은 기능과 남은 기능의 경계
- [ ] Sass vs PostCSS and Less / 같은 자리를 노리는 도구들의 접근 차이

### Syntax Variants `택 1`

- [ ] SCSS Syntax / CSS 문법을 그대로 두고 확장한 표기 `추천`
- [ ] Indented Syntax / 중괄호 없이 들여쓰기로 블록을 나누는 표기

### Implementations

- [ ] Dart Sass / 지금 유일하게 관리되는 공식 구현 `추천`
- [ ] LibSass and Ruby Sass / 개발이 멈춰 새 문법을 못 따라가는 구현

## 2. Getting Started

### Runtime Environment `택 1`

- [ ] Bundler Integration / 번들러 플러그인에 컴파일을 맡기는 방식 `추천`
- [ ] sass CLI / 파일·폴더를 지정해 직접 변환하는 명령
- [ ] Node API / 스크립트에서 컴파일러를 직접 부르는 경로

### Compilation

- [ ] Watch Mode / 바뀐 파일만 감지해 다시 컴파일하는 모드
- [ ] Output Style / 산출 CSS의 공백과 줄바꿈을 정하는 선택
- [ ] Source Map / 컴파일된 CSS를 원본 scss 줄로 되짚는 지도
- [ ] Partial / 앞에 _를 붙여 단독 출력에서 빼는 파일

---

# PART 2 · Core Syntax

## 3. Variables

- [ ] Variable Declaration / 값에 이름을 붙여 컴파일 때 치환하는 선언
- [ ] Default Value / 이미 값이 있으면 덮지 않는 대입 규칙
- [ ] Global Flag / 안쪽 블록에서 바깥 변수를 고쳐 쓰는 표시
- [ ] Scope and Shadowing / 안쪽 선언이 같은 이름의 바깥 값을 가리는 범위
- [ ] Sass Variable vs CSS Custom Property / 빌드 때 사라지는 값과 런타임에 남는 값의 차이
- [ ] Interpolation / 선택자·속성명 자리에 값을 끼워 넣는 표기

## 4. Nesting

- [ ] Selector Nesting / 부모 선택자를 반복해 쓰지 않게 접는 구조
- [ ] Parent Selector / 중첩 안에서 바깥 선택자를 가리키는 기호
- [ ] Suffix Nesting / 부모 기호에 문자를 이어 붙여 클래스명을 만드는 방법
- [ ] Property Nesting / 같은 접두사를 가진 속성들을 묶어 쓰는 표기
- [ ] Nesting Depth Antipattern / 중첩이 깊을수록 선택자가 길고 무거워지는 대가

## 5. Mixins & Functions

### @mixin / @include

- [ ] Mixin Definition and Invocation / 선언 묶음을 이름으로 복사해 넣는 재사용 단위
- [ ] Argument and Default Value / 인자를 받고 안 넘겼을 때 쓸 값을 정하는 방법
- [ ] Keyword Argument / 이름으로 인자를 지정해 순서를 벗어나는 호출
- [ ] Arbitrary Argument / 개수가 정해지지 않은 인자를 한 변수로 받는 표기
- [ ] Content Block / 호출 쪽 스타일 블록을 믹스인 안에 심는 자리

### @function

- [ ] Custom Function Definition / 값을 계산해 돌려주는 이름 붙은 식
- [ ] @return / 함수가 값 하나를 내보내고 끝나는 지점
- [ ] Function vs Mixin Selection Criteria / 값을 돌려줄지 선언을 뱉을지 가르는 기준

## 6. Inheritance

- [ ] @extend / 다른 선택자 목록에 자기 이름을 얹는 상속
- [ ] Placeholder Selector / 상속에만 쓰이고 출력엔 안 나오는 선택자
- [ ] Extend vs Mixin Tradeoff / 선택자를 합칠지 선언을 복사할지 가르는 기준
- [ ] Selector Bloat Problem / 상속이 선택자 조합을 폭발시키는 문제

## 7. Control Flow

- [ ] @if, @else if, @else / 조건에 따라 낼 선언을 고르는 분기
- [ ] @each / 리스트·맵 항목마다 규칙을 찍어내는 반복
- [ ] @for / 정해진 횟수만큼 번호를 세며 도는 반복
- [ ] @while / 조건이 참인 동안 계속 도는 반복
- [ ] Operator and Expression / 산술·비교로 값을 계산하는 식
- [ ] Truthiness / null과 false만 거짓으로 치는 판정 규칙

## 8. Data Types

- [ ] Number / 단위를 달고 계산되며 단위끼리 약분되는 수
- [ ] String / 따옴표 유무가 출력에 그대로 남는 문자열
- [ ] Color / 색 공간 값으로 다뤄져 계산이 되는 형
- [ ] List / 공백이나 쉼표로 구분된 값들의 나열
- [ ] Map / 키로 값을 꺼내 쓰는 짝 모음
- [ ] Boolean and null / 참·거짓과 값 없음을 나타내는 형

---

# PART 3 · Module System

## 9. Module System

### Loading Methods `택 1`

- [ ] @use / 파일을 이름공간 아래로 한 번만 불러오는 규칙 `추천`
- [ ] @import (Deprecated) / 전역에 다 풀리고 중복 로드되는 옛 방식
- [ ] @forward / 불러온 멤버를 다시 밖으로 내보내는 규칙

### Detailed Rules

- [ ] Namespace / 모듈 멤버 앞에 붙는 이름을 바꾸거나 없애는 방법
- [ ] Configuration / 불러오는 쪽에서 모듈 기본 변수를 바꾸는 방법
- [ ] Member Privacy / 이름 앞 하이픈으로 밖에서 못 쓰게 막는 규칙
- [ ] show and hide / 내보낼 멤버를 골라내거나 가리는 지정
- [ ] Load Path and Index File / 파일을 찾는 경로와 폴더 대표 파일 규칙

## 10. Built-in Modules

- [ ] sass:math / 나눗셈과 반올림 등 수 계산을 모은 모듈
- [ ] sass:color / 색을 밝기·채도 단위로 바꾸는 모듈
- [ ] sass:map / 키로 값을 꺼내고 맵을 합치는 모듈
- [ ] sass:list / 나열에 값을 붙이고 위치를 찾는 모듈
- [ ] sass:string / 따옴표를 떼고 문자를 찾는 모듈
- [ ] sass:meta / 값의 형과 내부를 들여다보는 모듈
- [ ] Deprecated Global Function / 모듈 함수로 대체돼 사라질 전역 색 함수

---

# PART 4 · Structure and Design

## 11. Project Structure

- [ ] 7-1 Pattern / 폴더 일곱에 진입 파일 하나로 나누는 관례
- [ ] Directory Classification / 값·기본·부품·레이아웃으로 폴더를 가르는 기준
- [ ] Entry File Composition / 진입 파일이 로드 순서만 담는 구성
- [ ] Index and Barrel File / 폴더 하나를 한 이름으로 불러오게 하는 파일
- [ ] File Splitting Criteria / 파일을 언제 쪼갤지 정하는 기준

## 12. Token Management

- [ ] Map-based Token Definition / 디자인 값을 맵 한 곳에 모으는 정의
- [ ] Color Palette Generation Function / 기준색에서 단계별 색을 뽑아내는 함수
- [ ] Spacing and Typography Scale / 여백과 글자 크기를 일정 비율로 만든 단계
- [ ] Breakpoint Map + Responsive Mixin / 기준 폭을 맵에 두고 미디어쿼리를 찍는 조합
- [ ] Theme Map / 테마별 값 묶음을 골라 적용하는 구조
- [ ] Exporting Sass Map to CSS Variables / 빌드 때 사라질 값을 런타임 변수로 내보내는 방법

## 13. Combining with Methodologies

- [ ] BEM + Nesting / 바깥 선택자 기호로 블록·요소 이름을 이어 붙이는 조합
- [ ] CSS Modules + SCSS / 클래스 이름 격리와 전처리를 함께 쓰는 구성
- [ ] ITCSS and SMACSS / 구체성이 낮은 층부터 쌓는 스타일 분류법 `선택`
- [ ] Automated Utility Class Generation / 맵을 돌려 한 속성짜리 클래스를 찍어내는 방법

---

# PART 5 · Real-World Use

## 14. Debugging and Quality

- [ ] @debug, @warn, @error / 컴파일 도중 값을 찍거나 멈추는 지시자
- [ ] Handling Deprecation Warnings / 곧 없어질 문법 경고를 읽고 대응하는 방법
- [ ] Stylelint and stylelint-scss / scss 문법까지 검사하는 린터 구성
- [ ] Formatter Configuration / 들여쓰기·따옴표 표기를 도구로 통일하는 설정

## 15. Build and Optimization

- [ ] Compile Performance / 파일 수와 로드 깊이가 컴파일 시간을 늘리는 이유
- [ ] Autoprefixer / 컴파일 뒤 벤더 접두사를 덧대는 후처리 단계
- [ ] CSS Minification / 산출 CSS의 공백과 중복을 걷어내는 단계
- [ ] Critical CSS / 첫 화면에 필요한 규칙만 먼저 심는 방법 `선택`
- [ ] Framework Integration / 프레임워크 빌드 설정에 컴파일을 끼우는 방법

## 16. Migration

- [ ] sass-migrator / 문법 전환을 자동으로 고쳐주는 공식 도구
- [ ] @import to @use Migration / 전역 이름을 모듈 이름공간으로 옮기는 절차
- [ ] Legacy Global Function Cleanup / 전역 색 함수를 모듈 함수로 바꾸는 정리
- [ ] Native CSS Nesting Migration Decision / 브라우저 중첩으로 갈아탈지 가르는 기준

---

# 이 로드맵 밖

- CSS 문법 전반 `software/skill-based/Languages/css.md`
- 디자인 시스템 이론 `software/skill-based/CS-Theory/design-system.md`
- 유틸리티 우선 대안 `software/skill-based/Frameworks/tailwind.md`
- 번들러 설정 `software/skill-based/Build-Tools/vite.md`, `webpack.md`
- 프론트엔드 전반 `software/role-based/frontend.md`
