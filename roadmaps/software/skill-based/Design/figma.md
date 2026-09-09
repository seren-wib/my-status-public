# Figma `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Figma

## 1. What is Figma?

### Overview of Figma / What is it?

- [ ] Browser-based Vector Design Tool / 설치 없이 브라우저에서 여는 벡터 편집기
- [ ] Real-time Multiplayer Editing / 여러 명이 동시에 같은 파일 편집
- [ ] UI / UX 디자인 · 프로토타이핑 통합

### Figma vs Other Tools

- [ ] Figma vs Sketch, Adobe XD, Balsamiq / 웹 기반 협업이라는 점에서 다른 툴과 구분

### Getting Started

- [ ] Desktop App vs Web / 네이티브 앱과 브라우저 버전 중 선택
- [ ] Plan / Starter·Professional·Organization 요금제
- [ ] Team, Project, File / 파일을 담는 세 단계 구조

## 2. Figma Interface

### Interface Layout

- [ ] Toolbar / 도형·텍스트 등 도구를 꺼내는 상단 바
- [ ] Layers Panel / 레이어 목록과 계층 구조를 보여주는 패널
- [ ] Assets Panel / 컴포넌트·스타일을 모아 꺼내 쓰는 패널
- [ ] Design Panel / 선택 요소 속성을 편집하는 오른쪽 패널
- [ ] Canvas Navigation / 확대·축소와 화면 이동 조작

### Basic Operations

- [ ] Frame vs Group / 리사이즈 기준이 되느냐로 갈리는 컨테이너
- [ ] Selection / 더블클릭 하위 선택과 동일 요소 일괄 선택
- [ ] Move, Resize, Rotate / 요소를 옮기고 크기·각도 바꾸기
- [ ] Alignment & Distribution / 요소 정렬과 간격 균등 배치
- [ ] Keyboard Shortcut Mastery / 단축키로 작업 속도 끌어올리기 `추천`

## 3. Files & Organization

- [ ] Page Separation / 파일 안을 페이지로 나눠 정리
- [ ] Layer Naming Convention / 레이어 이름 규칙으로 구조 파악 쉽게
- [ ] Grouping & Section / 레이어를 묶거나 캔버스 구역으로 나누기
- [ ] Version History / 저장된 이전 버전 확인하고 복원
- [ ] Branching / 메인과 분리해 실험하는 별도 흐름 `선택`
- [ ] File Sharing / 권한 설정과 링크로 공유

---

# PART 2 · Drawing and Layout

## 4. Shapes & Vector

### Basic Shapes

- [ ] Rectangle, Ellipse, Line, Polygon / 사각형·원·선·다각형 기본 도형 그리기
- [ ] Corner Radius / 모서리마다 다른 둥글기 값 지정
- [ ] Boolean Operation / 합치기·빼기·교차·제외로 도형 조합

### Vector

- [ ] Pen Tool / 점을 찍어 곡선 경로 직접 그리기
- [ ] Vector Network / 여러 경로가 교차·분기하는 벡터 구조
- [ ] Edit Mode / 고정점과 곡률 핸들로 경로 수정
- [ ] Outline Stroke / 선을 도형으로 바꾸고 하나로 합치기

### Images and Icons

- [ ] Image Fill / 이미지를 자르기·맞춤·타일로 채우기
- [ ] SVG Import / Icon 관리
- [ ] Mask / 위 레이어 모양대로 아래 내용 잘라내기

## 5. Text & Typography

- [ ] Text Tool / 고정폭 텍스트와 자동 줄바꿈 영역 텍스트
- [ ] Font Family, Weight, Size / 글꼴 종류·굵기·크기 지정
- [ ] Line Height, Letter Spacing, Paragraph Spacing / 행간·자간·문단 간격 조정
- [ ] Text Align / 정렬 방향과 텍스트 상하 여백 잘라내기
- [ ] Text Resizing / 너비·높이 자동 맞춤 또는 고정 크기
- [ ] Local Font vs Google Font / 내 컴퓨터 글꼴과 구글 폰트 연동 차이

## 6. Layout

### Constraints

- [ ] Constraint / 프레임 리사이즈 때 붙는 기준점 설정
- [ ] Frame Resizing Behavior / 동작 이해

### Auto Layout

- [ ] Auto Layout Basics / 방향·간격·여백으로 자동 정렬
- [ ] Alignment / Distribution 설정
- [ ] Resizing / 내용만큼·꽉 채움·고정 크기 중 선택
- [ ] Nested Auto Layout / 오토 레이아웃 안에 오토 레이아웃 중첩
- [ ] Absolute Position / 오토 레이아웃 흐름 무시하고 고정 배치
- [ ] Wrap / 너비 넘으면 다음 줄로 자동 개행

### Grid

- [ ] Layout Grid / 칼럼·로우·격자로 정렬 기준 잡기
- [ ] Responsive Breakpoint Design / 화면 폭 구간별 레이아웃 분기

## 7. Color, Fill & Effects

- [ ] Fill / 단색·그라디언트·이미지로 채우기
- [ ] Gradient Type / 직선·원형·각도·다이아몬드 그라디언트
- [ ] Stroke / 선 두께·정렬·점선 스타일 지정
- [ ] Opacity / 투명도 조절과 레이어 합성 모드
- [ ] Effect / 그림자·안쪽 그림자·블러 효과
- [ ] Color Picker / 스포이드·헥스·HSL로 색상 지정
- [ ] Contrast Validation / 명도 대비를 검사하는 접근성 플러그인

---

# PART 3 · Reuse System

## 8. Components

### Basics

- [ ] Component / Instance 관계
- [ ] Main Component Management / 관리
- [ ] Instance Override / 인스턴스만 수정하거나 초기화·반영
- [ ] Instance Swap / 인스턴스를 다른 컴포넌트로 교체
- [ ] Nested Component / 컴포넌트 안에 다른 컴포넌트 포함

### Variants

- [ ] Component Set / 배리언트를 묶은 컴포넌트 그룹
- [ ] Property / 배리언트·불리언·텍스트·스왑 속성 타입
- [ ] Naming Convention / Property 구성 설계
- [ ] Exposed Nested Property / 중첩 인스턴스 속성 상위로 노출

### Slot Pattern

- [ ] Base Component Pattern / 슬롯 패턴
- [ ] Component Description / 컴포넌트에 설명·문서 링크 붙이기

## 9. Styles & Variables

### Styles

- [ ] Color Style / 재사용할 색상을 이름 붙여 저장
- [ ] Text Style / 글꼴·크기 조합을 이름 붙여 저장
- [ ] Effect Style / 그림자 효과와 레이아웃 그리드 스타일

### Variables

- [ ] Variable Type / 색상·숫자·문자·불리언 변수 타입
- [ ] Collection / 변수를 묶고 모드별 값 관리
- [ ] Theming / Light, Dark Mode 전환
- [ ] Scoping / 변수 적용 범위 제한과 변수 간 참조
- [ ] Variable vs Style / 사용 기준

## 10. Libraries & Design System

- [ ] Team Library Publishing / 게시
- [ ] Library Update / 게시하고 변경 내역 검토
- [ ] Token Structure Design / 원시 값과 의미 단위 토큰 계층 설계
- [ ] Component Documentation / 컴포넌트 사용법을 문서로 남기기
- [ ] Design System Versioning / 버전 관리
- [ ] Adoption Tracking / 라이브러리 사용 현황 분석

---

# PART 4 · Prototyping and Collaboration

## 11. Prototyping

### Connections

- [ ] Prototype Tab / 플로우 구성과 시작 지점 지정
- [ ] Interaction Trigger / 클릭·호버·드래그·지연으로 동작 시작
- [ ] Action / 화면 이동·오버레이·뒤로가기·교체
- [ ] Overlay Settings / 오버레이 위치와 바깥 클릭 시 닫기

### Interactions

- [ ] Animation / 즉시·디졸브·밀고 들어옴·밀어내기
- [ ] Smart Animate / 같은 이름 레이어 속성 변화 자동 보간
- [ ] Easing, Duration, Spring / 가속 곡선·시간·스프링 물리감 조절
- [ ] Scroll Behavior / 스크롤 고정 위치와 가로 스크롤

### Advanced

- [ ] Component State Transition / 인터랙티브 컴포넌트로 상태 전환 구현
- [ ] Conditional / Variable 활용 Prototype
- [ ] Device Frame / 기기 프레임 씌워 발표용으로 보기
- [ ] Prototype Sharing / 링크나 임베드로 프로토타입 공유

## 12. Collaboration & Handoff

### Collaboration

- [ ] Comment / 멘션으로 알리고 해결 처리
- [ ] Multiplayer Cursor / 다른 사람 커서 보기와 관찰 모드
- [ ] Permission / 보기 전용과 편집 권한 구분
- [ ] FigJam / Whiteboard 활용

### Handoff

- [ ] Dev Mode / 개발자용 속성 검사 패널
- [ ] Ready for Dev / 개발 준비 완료 상태 표시
- [ ] CSS, iOS, Android Code Snippet / 플랫폼별 스타일 코드 자동 추출
- [ ] Measurement / Spacing 확인
- [ ] Export Setting / PNG·SVG·PDF와 슬라이스 범위 지정
- [ ] Export Scale / 해상도 배율 1x·2x·3x 지정

## 13. Plugins & Automation

- [ ] Plugin Installation and Run / 설치와 실행
- [ ] Everyday Plugins / Content 생성, Accessibility, Icon
- [ ] Widget / FigJam에 올리는 상호작용 도구 `선택`
- [ ] Figma REST API / 외부에서 파일 데이터 읽고 쓰는 API `선택`
- [ ] Plugin API / 커스텀 Plugin 제작 `선택`
- [ ] Design Token Export / 코드 연동

---

# 이 로드맵 밖

- UX 디자인 이론 `software/role-based/ux-design.md`
- 프로덕트 디자인 전반 `software/role-based/product-design.md`
- 디자인 시스템 이론 `software/skill-based/CS-Theory/design-system.md`
- 다른 디자인 툴 `software/skill-based/Design/sketch.md`, `adobe-xd.md`, `balsamiq.md`
- 프론트엔드 구현 `software/role-based/frontend.md`
- CSS `software/skill-based/Languages/css.md`
