# MobX `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to MobX

## 1. What is MobX?

### Overview of MobX / What is it?

- [ ] Transparent Functional Reactive Programming / 읽은 값을 따라 갱신을 대신 이어주는 방식
- [ ] Automatic Dependency Tracking via Observable State / 실행 중 읽힌 값만 의존성으로 기록하는 구조
- [ ] Mutable State Allowance / 사본 대신 원본을 직접 고쳐도 되게 만든 설계
- [ ] MobX vs Redux, Zustand / 규율로 막는 쪽과 추적으로 따라가는 쪽을 가르는 기준

### Three Core Elements

- [ ] State / observable로 감싸 추적 대상이 되는 원본 값
- [ ] Derivations / 상태에서 저절로 따라 나오는 값과 부수효과 두 갈래
- [ ] Actions / 변경이 들어오는 입구를 한 갈래로 정하는 축

## 2. Getting Started

- [ ] mobx and mobx-react-lite / 코어와 리액트 연결을 나눠 넣는 두 패키지
- [ ] makeAutoObservable / 생성자에서 필드 역할을 알아서 정해주는 함수 `추천`
- [ ] makeObservable / 필드마다 observable·action·computed를 손으로 지정하는 방법
- [ ] Decorator Syntax / @observable 표기로 역할을 붙이던 옛 방식 `선택`
- [ ] Store Class Authoring / 상태와 그 조작을 한 클래스에 담는 구성

---

# PART 2 · Core Concepts

## 3. Observable State

- [ ] observable Object, Array, Map, Set / 자료구조별로 추적을 붙이는 래퍼 종류
- [ ] Deep vs Shallow Observability / 중첩 값까지 감쌀지 한 겹만 감쌀지 가르는 기준
- [ ] Annotation / ref·shallow·struct로 항목마다 추적 깊이를 정하는 표기
- [ ] observable.box / 원시값을 상자에 넣어 추적 대상으로 만드는 방법
- [ ] Proxy-Based Implementation and Limitations / 프록시로 접근을 가로채기에 생기는 제약
- [ ] Dynamic Property Addition Caveats / 나중에 붙인 속성이 추적에서 빠지는 이유

## 4. Actions

- [ ] action / 관찰 대상을 바꾸는 자리를 한 곳으로 모으는 규약
- [ ] runInAction / 액션 밖 코드 조각을 즉석에서 액션으로 감싸는 함수
- [ ] enforceActions Configuration / 액션 밖 변경을 경고나 오류로 막는 설정
- [ ] flow / 제너레이터로 비동기 단계마다 액션 자격을 잇는 방법
- [ ] State Update Handling After async-await / await 뒤 코드가 액션 밖으로 새는 문제
- [ ] action.bound / 메서드를 떼어 넘겨도 this를 잃지 않게 묶는 표기

## 5. Computed

- [ ] computed / 읽힐 때만 다시 계산하고 결과를 쥐고 있는 파생값
- [ ] Caching and Invalidation Rules / 쥐고 있던 값을 언제 버릴지 정하는 규칙
- [ ] Why Computed Must Be Pure / 파생값 안에 부수효과를 두면 안 되는 이유
- [ ] keepAlive and computedRequiresReaction / 관찰자 없는 파생값의 재계산을 다루는 설정
- [ ] Parameterized Derived Values / 인자마다 캐시를 따로 두는 파생값 구성

## 6. Reactions

- [ ] autorun / 안에서 읽은 값이 바뀔 때마다 통째로 다시 도는 반응
- [ ] reaction / 볼 값과 할 일을 두 함수로 나눠 거는 방식
- [ ] when / 조건이 참이 되는 순간 한 번만 도는 반응
- [ ] Disposer / 걸어둔 반응을 끊어 누수를 막는 반환 함수
- [ ] Reaction Options / 첫 실행 시점과 호출 간격을 정하는 인자
- [ ] Reaction Overuse Boundaries / 화면으로 될 일을 반응으로 만들지 않는 경계

---

# PART 3 · React Integration

## 7. mobx-react-lite

- [ ] observer HOC / 컴포넌트가 읽은 관찰값을 구독으로 바꾸는 감싸개
- [ ] Fine-Grained Re-render Granularity / 실제로 읽은 컴포넌트만 다시 그리게 되는 범위
- [ ] useLocalObservable / 컴포넌트 안에만 사는 관찰 상태를 만드는 훅
- [ ] Observer Component / 트리 일부만 감싸 갱신 범위를 좁히는 컴포넌트
- [ ] Props and Observable Boundary / props로 값을 꺼내 넘기는 순간 추적이 끊기는 지점
- [ ] React 18 / Strict Mode 이중 실행에서 반응이 겹치는 지점

## 8. Store Architecture

- [ ] Domain Store and UI Store / 도메인 데이터와 화면 상태를 다른 스토어로 가르는 기준
- [ ] Root Store Pattern / 여러 스토어를 하나가 들고 서로 잇게 하는 구성
- [ ] Cross-Store References and Dependency Injection / 스토어끼리 참조를 생성자로 받아 두는 방법
- [ ] Store Provision via Context / 스토어 인스턴스를 트리에 내려두는 방법
- [ ] Class-Based Model Design / 데이터와 메서드를 한 인스턴스에 붙이는 모델 설계
- [ ] Server Response to Model Conversion / 응답 JSON을 관찰 가능한 인스턴스로 바꾸는 절차

## 9. MobX-State-Tree `선택`

- [ ] types-Based Model Definition / 런타임 타입으로 모델 구조를 선언하는 방식
- [ ] Snapshot and Patch / 상태 전체 사본과 변경 조각으로 뽑아내는 형식
- [ ] Actions and Views / 모델 안에 변경과 파생을 함께 선언하는 자리
- [ ] Reference and Identifier / id로 다른 노드를 가리켜 중복을 없애는 방법
- [ ] Time Travel / 사본을 되감아 이전 상태로 돌리는 기능

---

# PART 4 · Advanced and Operations

## 10. Utilities

- [ ] toJS / 관찰 래퍼를 벗겨 평범한 객체로 뽑는 함수
- [ ] observe and intercept / 변경을 뒤에서 보거나 앞에서 가로채는 저수준 훅
- [ ] onBecomeObserved and onBecomeUnobserved / 관찰이 붙고 떨어질 때 자원을 여닫는 지점
- [ ] Batching and transaction / 여러 변경을 한 번의 반응으로 묶는 방식
- [ ] isObservable and getDebugName / 추적 대상 여부와 내부 이름을 확인하는 함수

## 11. Performance

- [ ] observer Granularity / 감싸는 단위를 잘게 나눠 갱신 범위를 줄이는 방법
- [ ] No Observable Reads Outside Rendering / 렌더 밖에서 읽은 값이 구독으로 안 잡히는 이유
- [ ] Large List Optimization / 행마다 관찰자를 두어 목록 전체 갱신을 피하는 방법
- [ ] Reaction Count Management / 늘어난 반응 개수가 갱신 비용이 되는 지점
- [ ] Reactivity Loss from Destructuring / 구조 분해로 값을 꺼내면 추적이 끊기는 이유

## 12. Debugging & Testing

- [ ] spy and trace / 어떤 값 때문에 반응이 돌았는지 되짚는 도구
- [ ] configure Development Warning Options / 개발 중에만 경고를 켜 실수를 잡는 설정
- [ ] Store Unit Testing / 화면 없이 스토어의 액션과 파생값만 검증하는 방법
- [ ] Reaction Testing / when으로 조건 충족을 기다려 결과를 보는 방법
- [ ] Store Injection in Component Tests / 테스트용 스토어를 대신 끼워 넣는 방법

## 13. Operational Considerations

- [ ] SSR / 요청마다 스토어를 새로 만들어 상태가 섞이지 않게 하는 방법
- [ ] Persistence / 관찰 상태를 저장소에 남겼다 되살리는 방법
- [ ] MobX 6 Migration / 데코레이터를 걷고 makeObservable로 옮기는 절차
- [ ] TypeScript Typing / 애노테이션과 파생값 타입을 맞춰 두는 방법

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 다른 상태 관리 `software/skill-based/Frameworks/redux.md`, `zustand.md`
- Next.js SSR `software/skill-based/Frameworks/nextjs.md`
- 프론트엔드 전반 `software/role-based/frontend.md`
