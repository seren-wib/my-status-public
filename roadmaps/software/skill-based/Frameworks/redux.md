# Redux `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Redux

## 1. What is Redux?

### Overview of Redux / What is it?

- [ ] Predictable State Container / 같은 액션 순서면 같은 상태가 나오는 저장소
- [ ] Single Source of Truth / 앱 상태 전체를 스토어 한 곳에 모으는 원칙
- [ ] State is Read-only / 상태를 직접 못 고치게 막고 액션만 받는 규칙
- [ ] Changes via Pure Reducers / 변경을 부수효과 없는 함수 하나로 좁히는 규칙
- [ ] Unidirectional Data Flow / 액션에서 스토어를 거쳐 화면으로만 도는 흐름

### When to Use

- [ ] Server Cache State vs Client State Distinction / 서버에서 받아온 값과 화면 전용 값을 가르는 선
- [ ] Redux vs Zustand and MobX / 규율을 강제하는 쪽과 편의를 주는 쪽의 갈림
- [ ] Boilerplate Cost and Adoption Criteria / 늘어나는 코드량을 감수할지 정하는 도입 기준

## 2. Core Concepts

- [ ] Store / 상태 트리 하나와 디스패치 창구를 함께 쥔 객체
- [ ] Action / 일어난 일을 type으로 적은 객체와 그 생성 함수
- [ ] Action Type Naming Convention / 기능 이름과 사건 이름을 이어 붙이는 규약
- [ ] Reducer / 이전 상태와 액션으로 다음 상태를 만드는 순수 함수
- [ ] dispatch / 액션을 스토어에 밀어 넣는 유일한 통로
- [ ] getState and subscribe / 현재 상태를 읽고 변경 알림을 받는 스토어 창구
- [ ] Immutability Principle / 이전 상태 객체를 남겨 두고 새 객체를 만드는 원칙

## 3. Vanilla Redux `선택`

- [ ] createStore (Legacy) / RTK 이전에 스토어를 직접 만들던 함수
- [ ] combineReducers / 리듀서들을 키별로 묶어 하나로 만드는 함수
- [ ] Switch-based Reducer / 액션 type을 switch로 갈라 쓰던 작성 방식
- [ ] Manual Immutable Update / 전개 연산자로 중첩 객체를 손수 복사하는 방식
- [ ] Boilerplate Problem Awareness / 액션·타입·리듀서를 세 곳에 나눠 적는 부담

---

# PART 2 · Redux Toolkit

## 4. Redux Toolkit Basics

- [ ] configureStore / 미들웨어와 DevTools를 기본으로 끼워 주는 생성기
- [ ] Default Middleware / 불변성과 직렬화 위반을 개발 중에 잡아내는 검사
- [ ] createSlice / 리듀서와 액션을 한 선언에서 뽑아내는 함수
- [ ] Reducer / 슬라이스 함수 이름에서 액션 type을 뽑는 규칙
- [ ] Immer-based Mutable Syntax / 고치는 것처럼 써도 새 객체가 나오는 문법
- [ ] createAction and createReducer / 슬라이스 없이 액션과 리듀서를 따로 만드는 함수
- [ ] prepare Callback / 액션을 만들 때 payload 모양을 손보는 자리

## 5. Store Design

- [ ] Feature Folder / 기능 폴더마다 슬라이스를 한 벌씩 두는 배치
- [ ] Normalized State Shape / 목록을 id 배열과 id별 객체로 나눠 담는 모양
- [ ] createEntityAdapter / 정규화된 목록의 추가·수정·조회를 찍어내는 도구
- [ ] Root Reducer Composition / 슬라이스 리듀서를 하나의 상태 트리로 합치는 방법
- [ ] Preloaded State / 서버나 저장소에서 가져온 값으로 스토어를 여는 초기값
- [ ] State Serializability Constraint / 클래스나 함수를 상태에 담지 못하게 하는 제약

## 6. React Bindings

- [ ] Provider / 스토어를 컴포넌트 트리 전체에 물려 주는 껍데기
- [ ] useSelector / 스토어에서 필요한 조각만 골라 구독하는 훅
- [ ] useDispatch / 컴포넌트에서 디스패치 함수를 꺼내는 훅
- [ ] Selector Reference Identity and Re-render / 새 객체를 돌려주면 매번 다시 그려지는 이유
- [ ] shallowEqual / 객체 한 겹만 비교해 재렌더를 줄이는 비교 함수
- [ ] connect / 상태를 props로 매핑해 넘기던 옛 결합 방식

## 7. Selectors

- [ ] Selector Function Extraction / 상태 접근 코드를 컴포넌트 밖으로 빼는 방법
- [ ] createSelector / 입력이 그대로면 계산 결과를 재사용하는 셀렉터
- [ ] Input Selector Design / 결과가 덜 바뀌도록 입력 조각을 잘게 고르는 방법
- [ ] Parameterized Selector / 인자를 받는 셀렉터를 호출마다 찍어내는 공장
- [ ] Memoization Cache Size Pitfall / 캐시 한 칸이라 인자가 갈리면 매번 무효가 되는 함정
- [ ] Computing Derived Data in Selectors / 합계와 정렬을 셀렉터 안에서 계산해 두는 자리

---

# PART 3 · Async and Middleware

## 8. Middleware

- [ ] Middleware Signature / 스토어와 다음 단계를 차례로 받는 삼중 함수 꼴
- [ ] applyMiddleware / 미들웨어 목록을 dispatch에 겹쳐 감는 함수
- [ ] Writing Custom Middleware / 지나가는 액션을 가로채 로그로 남기는 함수 작성법
- [ ] Middleware Execution Order / 등록 순서대로 감싸이고 역순으로 돌아오는 순서
- [ ] Store Enhancer vs Middleware / 스토어 생성 자체를 감싸는 더 바깥 층

## 9. Async Libraries `택 1`

- [ ] Redux Thunk / 액션 대신 함수를 디스패치해 비동기를 넣는 방식 `추천`
- [ ] Redux Saga / 제너레이터로 비동기 흐름을 절차처럼 적는 라이브러리
- [ ] Redux Observable / 액션 스트림을 rxjs 연산자로 다루는 라이브러리

## 10. createAsyncThunk

- [ ] Thunk Function / 디스패치와 현재 상태를 인자로 받는 비동기 함수
- [ ] pending, fulfilled, rejected Action / 요청 한 번이 세 액션으로 갈라져 나오는 규칙
- [ ] extraReducers / 슬라이스 밖에서 온 액션을 받아 처리하는 자리
- [ ] Loading and Error State / 요청 진행과 실패를 슬라이스 필드로 남기는 방법
- [ ] rejectWithValue / 실패 이유를 액션 payload로 실어 보내는 함수
- [ ] condition / 이미 도는 요청이면 디스패치를 걸러 내는 옵션
- [ ] AbortController / 진행 중인 요청을 신호 하나로 끊는 취소 방법

## 11. Redux Saga `선택`

- [ ] Generator Function / 실행을 중간에 멈췄다 다시 잇는 함수 형태
- [ ] Effects / 호출·디스패치·조회를 객체로 적어 넘기는 명령
- [ ] takeEvery and takeLatest / 액션마다 띄울지 마지막 것만 남길지 정하는 감시
- [ ] fork and cancel / 사가를 따로 띄워 두고 필요할 때 끊는 명령
- [ ] Saga Testing / 이펙트 객체를 순서대로 비교하는 검증 방법

## 12. RTK Query

- [ ] createApi / 엔드포인트 묶음과 공통 요청 함수를 선언하는 자리
- [ ] Endpoint Definition / 읽기와 쓰기를 나눠 적는 엔드포인트 선언
- [ ] Auto-generated Hooks / 엔드포인트 이름에서 훅을 찍어내는 규칙
- [ ] Cache Key / 인자를 문자열로 굳혀 캐시 칸을 가르는 키
- [ ] Tag Invalidation / 태그로 캐시를 묶어 두고 한꺼번에 버리는 방식
- [ ] Refetch Options / 화면 복귀와 일정 간격으로 다시 받아오는 설정
- [ ] Optimistic Update / 응답 전에 캐시를 먼저 고치고 실패 시 되돌리는 방식
- [ ] Prefetching / 화면에 필요해지기 전에 캐시를 미리 채우는 방법
- [ ] fetchBaseQuery / 헤더에 토큰을 싣고 만료 시 다시 받는 요청 함수

---

# PART 4 · Advanced and Operations

## 13. Persistence & SSR

- [ ] redux-persist / 스토어 상태를 저장소에 담고 다시 꺼내는 라이브러리
- [ ] whitelist and blacklist / 저장할 것과 뺄 것을 골라 적는 두 목록
- [ ] Persist Migration / 버전을 올려 옛 저장 상태를 새 모양으로 옮기는 절차
- [ ] SSR Store Instance Separation / 요청마다 새 스토어를 만들어 상태 섞임을 막는 구조

## 14. TypeScript

- [ ] RootState / 스토어에서 상태와 디스패치 타입을 끌어내는 선언
- [ ] Typed Hooks / 타입을 미리 박아 다시 감싼 스토어 접근 훅
- [ ] PayloadAction / 액션 payload의 형을 지정하는 제네릭 타입
- [ ] Thunk Generics / 반환값과 인자와 거절 값의 형을 채우는 자리

## 15. DevTools & Debugging

- [ ] Redux DevTools Extension / 디스패치된 액션과 그때 상태를 나란히 보는 도구
- [ ] Time Travel Debugging / 액션 목록을 되감아 그때 화면을 보는 기능
- [ ] Action Trace / 어느 코드가 액션을 쐈는지 스택으로 찾는 기능
- [ ] Resolving Serializability Warnings / 직렬화 못 하는 값이 들어와 뜨는 경고를 없애는 방법

## 16. Testing & Design Principles

### Testing

- [ ] Reducer Unit Testing / 상태와 액션을 넣어 결과 상태만 비교하는 검증
- [ ] Selector Testing / 가짜 상태를 넣어 파생값과 캐시 동작을 보는 검증
- [ ] Component Testing with Store / 스토어를 씌운 렌더 도우미로 화면을 검사하는 방법
- [ ] API Mocking / 네트워크 계층에서 응답을 가로채 대신 주는 방법

### Design Principles

- [ ] Naming Actions as Events / 명령이 아니라 일어난 일로 액션 이름을 짓는 원칙
- [ ] No Side Effects in Reducers / 요청·난수·시각을 리듀서 밖으로 밀어내는 원칙
- [ ] No Derived Values in State / 계산해서 얻을 값을 상태에 두지 않는 원칙
- [ ] Ducks / 액션·리듀서를 기능 파일 하나에 모아 두는 규약

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 다른 상태 관리 `software/skill-based/Frameworks/zustand.md`, `mobx.md`
- Next.js SSR `software/skill-based/Frameworks/nextjs.md`
- 프론트엔드 전반 `software/role-based/frontend.md`
- 테스트 도구 `software/skill-based/Testing/vitest.md`, `jest.md`
