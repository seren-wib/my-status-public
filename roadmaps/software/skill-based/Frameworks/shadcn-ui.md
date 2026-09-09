# shadcn/ui `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to shadcn/ui

## 1. What is shadcn/ui?

### Overview / What is it?

- [ ] Not a Component Library / 설치해서 쓰는 패키지가 아니라는 성격
- [ ] Copy-Paste Component Collection / 완성된 컴포넌트 코드를 내 파일로 가져오는 모음
- [ ] Code Ownership Model / 받는 순간 유지보수 책임이 나에게 오는 모델
- [ ] Open Code Philosophy / 감춰진 내부 없이 전부 열어 두는 원칙

### Built On

- [ ] Radix UI Primitives / 겉모습 없이 열고 닫는 동작만 맡는 뼈대
- [ ] Tailwind CSS Styling / 겉모습을 전부 클래스 문자열로 얹는 층
- [ ] cva (class-variance-authority) / 갈래 이름과 클래스 묶음을 짝지어 두는 도구
- [ ] Lucide Icons / 예제 코드가 기본으로 쓰는 아이콘 세트

### Comparison and Judgment

- [ ] npm Dependency vs Vendored Code / 패키지로 받는 코드와 저장소에 박는 코드의 차이
- [ ] shadcn/ui vs MUI and Chakra UI / 업그레이드를 누가 떠안는지로 갈리는 차이
- [ ] Registry Concept / 컴포넌트 소스를 목록으로 배포하는 방식
- [ ] When It Is Not a Good Fit / 복사 방식이 손해가 되는 상황을 가르는 기준

---

# PART 2 · Installation and Code Structure

## 2. Getting Started

### Prerequisites

- [ ] Tailwind CSS Configuration / 붙여 넣을 코드가 전제하는 스타일 환경
- [ ] TypeScript and Path Alias / 생성 코드가 전제하는 타입 선언과 경로 별칭

### Initialization

- [ ] npx shadcn init / 설정 파일과 테마 변수를 처음 깔아 두는 명령
- [ ] Framework Preset / 프로젝트 종류마다 다른 경로와 설정을 고르는 값
- [ ] components.json / 별칭과 경로를 담아 CLI가 읽는 설정 파일
- [ ] Base Color / 테마 변수의 기준이 되는 중립 색 계열

### Adding Components

- [ ] npx shadcn add / 이름으로 고른 컴포넌트 소스를 써 넣는 명령
- [ ] Generated Path / 복사된 파일이 놓이는 components/ui 자리
- [ ] Automatic Dependency Installation / 컴포넌트가 필요로 하는 패키지를 함께 받는 동작
- [ ] cn() Utility / 겹치는 클래스를 뒤엣것으로 정리해 합치는 도우미

## 3. Reading the Generated Code

- [ ] Component File Anatomy / Root·Trigger·Content로 나뉜 파일 구성
- [ ] Radix Primitive Wrapping / 프리미티브에 클래스만 입혀 다시 내보내는 층
- [ ] forwardRef / 감싼 컴포넌트 너머로 ref를 넘겨주는 함수
- [ ] asChild Pattern / 자기 태그 대신 자식 요소에 동작을 얹는 방식
- [ ] Compound Component Pattern / 부모와 자식 부품이 맥락을 공유해 짝을 이루는 구조
- [ ] cva Variant Definition / 모양 갈래를 키와 클래스 표로 선언하는 방법
- [ ] VariantProps Type Inference / 선언한 갈래에서 props 타입을 뽑아내는 기능
- [ ] data-* State Attribute Styling / 열림·비활성 상태를 속성 선택자로 칠하는 규칙

---

# PART 3 · Component Usage

## 4. Form Composition

- [ ] Form Components / 값 하나씩을 받는 입력 부품 묶음
- [ ] react-hook-form Integration / 폼 상태 관리를 바깥 라이브러리에 맡기는 연결
- [ ] Zod Schema Validation / 입력 검증 규칙을 스키마 한 곳에 모으는 방법
- [ ] Form, FormField, FormMessage / 라벨·에러·컨트롤을 한 항목으로 묶는 부품
- [ ] Controlled vs Uncontrolled / 값을 상태로 들지 DOM에 맡길지 가르는 기준

## 5. Overlay & Navigation

- [ ] Overlay Components / 본문 위에 층을 띄워 보여주는 부품 묶음
- [ ] Menu Components / 키보드 이동과 선택을 갖춘 목록형 부품
- [ ] Navigation Components / 현재 위치를 드러내며 화면을 가르는 부품
- [ ] Portal and Focus Trap / 띄운 층을 트리 밖에 그리고 포커스를 가두는 처리
- [ ] Controlled State / 열림 여부를 바깥 상태로 끌어내는 prop 짝

## 6. Data Display

- [ ] Data Table / 행 로직을 TanStack Table에 맡긴 구성
- [ ] Table Feature / 행 목록을 정렬하고 걸러 나눠 주는 기능
- [ ] Feedback Components / 결과와 대기 상태를 사용자에게 알리는 부품
- [ ] Chart / Recharts에 테마 변수를 입힌 그래프 부품
- [ ] Calendar / react-day-picker를 감싼 날짜 선택 부품

---

# PART 4 · Theming and Customization

## 7. Theming

- [ ] CSS Variable Approach / 색을 클래스가 아니라 변수 값으로 두는 방식
- [ ] Semantic Token / 색을 용도 이름으로 부르는 변수 이름 규칙
- [ ] Radius Token / 모서리 곡률을 한 변수로 묶어 조절하는 값
- [ ] Dark Mode / next-themes로 루트 클래스를 갈아 끼우는 전환
- [ ] Multi Theme / 변수 묶음을 통째로 바꿔 팔레트를 가는 구성
- [ ] OKLCH Color Format / 밝기를 고르게 유지하며 색을 적는 표기

## 8. Modifying Components

- [ ] Direct File Editing as the Norm / 감싸지 않고 원본 파일을 직접 고치는 전제
- [ ] Adding Variants / 갈래 표에 키를 더해 모양을 늘리는 방법
- [ ] className Override and Precedence / 나중에 넘긴 클래스가 이기게 하는 우선순위
- [ ] Replacing the Rendered Element with asChild / 동작은 두고 그려질 태그만 바꾸는 방법
- [ ] Primitive Replacement / Radix 아닌 동작 라이브러리로 갈아 끼우는 작업
- [ ] Upstream Change Tracking Burden / 원본이 고쳐져도 내 파일엔 오지 않는 대가

---

# PART 5 · Extensions and Operations

## 9. Registry

- [ ] registry.json / 배포할 컴포넌트와 파일 위치를 적는 목록 파일
- [ ] Building a Custom Registry / 내 컴포넌트를 add 명령으로 받게 만드는 방법
- [ ] Namespaced Registry / 출처별 접두사로 이름 충돌을 피하는 규칙
- [ ] Private Registry / 인증을 붙여 사내에만 여는 배포 경로
- [ ] MCP Integration / 에이전트가 레지스트리를 직접 뒤지게 붙이는 연결 `선택`

## 10. Advanced CLI

- [ ] shadcn add <url> / 공식 목록 밖 주소에서 컴포넌트를 받는 방법
- [ ] shadcn build / 내 레지스트리를 배포용 json으로 굽는 명령
- [ ] diff / 내 파일과 원본이 벌어진 곳을 보여주는 명령
- [ ] Monorepo Configuration / 워크스페이스마다 다른 경로를 잡아 주는 설정

## 11. Real-World Considerations

- [ ] Accessibility Guarantees and Limits / 프리미티브가 보장하는 범위와 그 밖의 책임
- [ ] RSC / 상태를 쓰는 부품에 클라이언트 표시를 다는 경계
- [ ] Bundle Size Management / 안 쓰는 컴포넌트 파일이 쌓이는 것을 걷는 관리
- [ ] Version Control Strategy for Modified Components / 고친 부분을 커밋으로 구분해 남기는 전략
- [ ] Team Conventions / 누가 어디까지 고칠지 미리 정하는 규칙
- [ ] Blocks / 여러 컴포넌트를 엮은 화면 한 장 템플릿

---

# 이 로드맵 밖

- Tailwind CSS `software/skill-based/Frameworks/tailwind.md`
- React `software/skill-based/Frameworks/react.md`
- Next.js `software/skill-based/Frameworks/nextjs.md`
- 디자인 시스템 이론 `software/skill-based/CS-Theory/design-system.md`
- 대안 컴포넌트 라이브러리 `software/skill-based/Frameworks/material-ui.md`, `chakra-ui.md`
- TypeScript `software/skill-based/Languages/typescript.md`
