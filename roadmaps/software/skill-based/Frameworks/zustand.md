# Zustand `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Zustand

## 1. What is Zustand?

- [ ] Minimal State Management Library / 프로바이더도 리듀서도 없는 최소 스토어
- [ ] Hook-based API / 컴포넌트에서 훅 하나로 꺼내 쓰는 인터페이스
- [ ] Provider-free Global Store / 트리를 감싸지 않고 모듈 스코프에 두는 스토어
- [ ] Zustand vs Redux, Jotai, MobX / 강제하는 규율의 양으로 갈리는 선택 기준
- [ ] Bundle Size / 붙이는 값에 비해 늘어나는 번들 무게

## 2. Getting Started

- [ ] Installation / 패키지 하나만 받으면 끝나는 설치 구성
- [ ] create / 초기 상태와 액션을 담아 훅을 만드는 함수
- [ ] set and get / 상태를 갱신하는 함수와 즉시 읽는 함수
- [ ] Calling the Store Hook / 쓸 컴포넌트에서 직접 구독을 여는 호출
- [ ] Defining Actions Inside the Store / 상태 옆에 갱신 함수를 같이 두는 구성

---

# PART 2 · Core Usage

## 3. State Updates

- [ ] Partial Update and Shallow Merge / 넘긴 키만 최상위에서 덮어쓰는 갱신
- [ ] replace Flag / 병합 대신 상태 전체를 갈아 끼우는 옵션
- [ ] Functional Update / 이전 상태를 인자로 받아 새 값을 만드는 형태
- [ ] Nested State Update Problem / 깊은 객체를 손으로 다시 펼쳐야 하는 부담
- [ ] Async Action / 액션 안에서 await 뒤 set을 부르는 방식

## 4. Selectors & Re-rendering

- [ ] Selector Function / 구독할 조각만 좁혀 뽑아 오는 함수
- [ ] Whole-Store Subscription Re-render Problem / 통째로 받아 모든 변경에 다시 그리는 문제
- [ ] useShallow / 뽑은 객체를 한 겹만 비교해 헛렌더를 막는 훅
- [ ] Atomic Selector Pattern / 값 하나씩 따로 구독해 비교를 없애는 방식
- [ ] Object and Array Return / 매번 새 참조가 생겨 도는 헛렌더
- [ ] Store Access Outside React / 훅을 안 거치고 현재 값을 읽고 쓰는 통로
- [ ] subscribe / 렌더와 무관하게 변경 알림을 받는 구독 함수

## 5. Store Design

- [ ] Slice Pattern / 스토어를 조각 함수로 나눠 합치는 구조
- [ ] Split Stores vs Single Store / 도메인마다 나눌지 하나로 둘지 가르는 기준
- [ ] State and Action Separation / 값과 갱신 함수를 스토어 안에서 나누는 규약
- [ ] Computing Derived State in Selectors / 저장 대신 뽑을 때 계산해 내는 파생값
- [ ] Reset / 초기 상태 스냅샷을 되돌려 넣는 방법

---

# PART 3 · Advanced

## 6. Middleware

- [ ] persist / 저장할 조각만 골라 스토리지에 남기는 미들웨어
- [ ] devtools / 상태 변화를 브라우저 확장에 흘려보내는 미들웨어
- [ ] immer / 불변 갱신을 변경 문법으로 쓰게 하는 미들웨어
- [ ] subscribeWithSelector / 고른 조각이 바뀔 때만 알림받게 하는 미들웨어
- [ ] combine / 초기 상태와 액션의 타입을 자동으로 합치는 래퍼
- [ ] Custom Middleware Authoring / set과 get을 감싸 기능을 덧대는 방법
- [ ] Middleware Composition Order / 미들웨어를 겹칠 때 지켜야 하는 순서

## 7. TypeScript

- [ ] Curried create Form / 타입만 먼저 주고 함수를 다시 부르는 표기
- [ ] StateCreator / 슬라이스 하나의 형을 적는 제네릭 타입
- [ ] Typing Issues with Middleware / 미들웨어를 겹칠 때 추론이 끊기는 지점
- [ ] Selector Return Type Inference / 뽑은 값의 형이 자동으로 잡히는 원리

## 8. Scoped Store

- [ ] Vanilla Store / 리액트 밖에서 만들어 두는 스토어 본체
- [ ] useStore / 바닐라 스토어를 컴포넌트에 붙이는 훅
- [ ] Store Injection via Context / 전역 대신 컨텍스트로 인스턴스를 내리는 방식
- [ ] Per-component Store Instance / 컴포넌트마다 스토어를 따로 두는 구성
- [ ] SSR and Hydration / 서버에서 만든 스토어를 요청마다 새로 두는 이유

## 9. Using React Outside Components

- [ ] zustand/vanilla / 리액트 의존 없이 도는 코어 진입점
- [ ] Subscribing from Non-React Code / 소켓·핸들러에서 상태 변화를 듣는 방법
- [ ] useSyncExternalStore Foundation / 외부 저장소를 렌더와 맞추는 훅 토대
- [ ] Transient Update / 다시 그리지 않고 값만 흘려보내는 갱신

---

# PART 4 · Operations

## 10. Testing

- [ ] Store Unit Testing / 컴포넌트 없이 스토어 함수만 검증하는 방법
- [ ] Store Reset Between Tests / 모듈 스코프에 남은 상태를 지우는 처리
- [ ] Store Mocking / 실제 스토어 대신 가짜 구현을 끼우는 방법
- [ ] State Injection in Component Tests / 렌더 전에 원하는 상태를 심어 두는 방법

## 11. Best Practices

- [ ] Delegating Server State to a Data Fetching Library / 서버 캐시를 스토어 밖에 두는 경계
- [ ] Not Storing Derived Values in the Store / 계산으로 얻을 값을 저장하지 않는 규칙
- [ ] Globalization Scope Boundary / 전역과 지역에 둘 상태를 가르는 기준
- [ ] Migrating from Redux / 리듀서에 흩어진 전이를 액션 함수로 옮기는 절차

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 다른 상태 관리 `software/skill-based/Frameworks/redux.md`, `mobx.md`
- Next.js SSR `software/skill-based/Frameworks/nextjs.md`
- 프론트엔드 전반 `software/role-based/frontend.md`
