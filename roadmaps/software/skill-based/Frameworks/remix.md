# Remix `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Remix

## 1. What is Remix?

### Overview

- [ ] Web Standards-based Full-stack React Framework / 요청과 응답을 웹 표준 객체로 다루는 구조
- [ ] Server-first Rendering / 첫 화면을 서버 응답으로 완성해 내려보내는 방식
- [ ] Nested Routing-centric Design / URL 조각마다 화면과 데이터를 함께 붙이는 설계
- [ ] Progressive Enhancement / JS가 안 떠도 폼과 링크로 도는 성질
- [ ] Differences from Next.js / 캐시 대신 요청마다 읽고 쓰는 모델로 갈리는 지점
- [ ] Relationship with React Router 7 / Remix가 라우터 본체로 흡수된 경위

### When to Use

- [ ] Form and Mutation-centric Applications / 읽기보다 쓰기가 잦은 화면에 맞는 이유
- [ ] Edge Runtime Deployment / 무거운 Node 없이 얇은 런타임에 올리는 선택지
- [ ] Multi-runtime Portability / Node·Deno·Workers에 같은 코드를 얹는 성질

## 2. Project Setup

### Project Creation

- [ ] create-remix / 템플릿을 골라 프로젝트 뼈대를 까는 명령
- [ ] Directory Structure / app·public·build로 갈리는 폴더 역할
- [ ] Vite Plugin-based Build / 플러그인 하나로 서버와 클라이언트를 함께 묶는 구성
- [ ] TypeScript Configuration / 라우트 타입을 생성해 물리는 설정

### Execution Flow

- [ ] Dev Server / 화면 상태를 두고 코드만 갈아 끼우는 개발 서버
- [ ] entry.client.tsx and entry.server.tsx / 브라우저와 서버의 진입점을 직접 여는 자리
- [ ] root.tsx / html 문서 전체를 감싸는 최상위 라우트
- [ ] Document Components / Meta·Links·Scripts로 문서 뼈대를 그리는 부품

## 3. Routing Fundamentals

### Route Definitions

- [ ] File-based Routing / 파일 이름으로 URL을 정하는 flat routes 규칙
- [ ] Dot Delimiter / 점으로 중첩 세그먼트를 표현하는 표기
- [ ] Dynamic Segment / $param으로 URL 값을 받는 자리
- [ ] Splat Route / 남은 경로 전체를 하나로 받는 라우트
- [ ] Optional Segment / 괄호로 있어도 없어도 되게 만드는 표기
- [ ] Pathless Layout Route / URL에 안 드러나면서 레이아웃만 씌우는 라우트
- [ ] Index Route / 부모 경로에 정확히 맞을 때 그릴 자식
- [ ] Escaping / 대괄호로 특수문자를 글자 그대로 쓰는 표기
- [ ] routes.ts / 파일 이름 규칙 대신 손으로 적는 라우트 표 `선택`

### Nested Routing

- [ ] Outlet / 부모 화면 안에 자식 라우트가 들어갈 구멍
- [ ] Mapping URL Segments to UI Hierarchy / URL 계층을 그대로 화면 중첩으로 옮기는 규칙
- [ ] Parallel Data Loading / 중첩 loader를 동시에 돌려 워터폴을 없애는 방식

---

# PART 2 · Data Flow

## 4. Loaders

- [ ] Loader Function / 라우트가 그려지기 전 서버에서 읽기만 맡는 자리
- [ ] LoaderFunctionArgs / request·params·context가 넘어오는 인자 형태
- [ ] useLoaderData / 그 라우트의 loader 결과를 꺼내는 훅
- [ ] Return Value Serialization / 서버 값이 브라우저까지 실려 오는 직렬화 규칙
- [ ] Reading URL Search Params / 필터·페이지 상태를 쿼리스트링에서 읽는 방법
- [ ] Returning Response / 데이터 대신 리다이렉트·404를 던지는 방법
- [ ] useRouteLoaderData / 상위 라우트가 읽어 둔 데이터를 꺼내 쓰는 훅
- [ ] clientLoader / 서버를 안 거치고 브라우저에서만 읽는 loader `선택`
- [ ] Deferred Data / 느린 값을 나중에 흘려보내고 먼저 그리는 방법
- [ ] Headers Function / 라우트마다 응답 헤더를 정하는 자리

## 5. Actions and Forms

- [ ] Action Function / 라우트에서 쓰기 요청만 받는 자리
- [ ] Form Component / 폼 제출을 그 라우트 action으로 보내는 부품
- [ ] request.formData() / 제출된 입력을 웹 표준 객체로 꺼내는 호출
- [ ] Intent Pattern / 숨은 필드로 한 라우트에서 여러 동작을 가르는 방법
- [ ] useActionData / action이 돌려준 검증 결과를 꺼내는 훅
- [ ] Server-side Validation / 실패를 예외 대신 응답 데이터로 돌려주는 구조
- [ ] redirect / 쓰기 후 새로고침 재제출을 막는 응답
- [ ] File Upload / multipart 본문을 흘려 받아 저장하는 방법
- [ ] Why Forms Over Fetch / 폼 제출을 직접 fetch보다 앞에 두는 이유

## 6. Mutations and Revalidation

- [ ] Automatic Revalidation / 액션이 끝난 뒤 화면의 loader를 다시 읽는 규칙
- [ ] shouldRevalidate / 다시 읽을 loader를 골라 줄이는 함수
- [ ] useNavigation / 전이 중인지 읽어 대기 화면을 붙이는 훅
- [ ] useFetcher / 주소를 안 바꾸고 loader·action만 부르는 훅
- [ ] fetcher.Form / 페이지 이동 없이 제출하는 인라인 폼
- [ ] Optimistic UI / 응답 전에 제출한 formData로 화면을 바꾸는 방법
- [ ] useSubmit / 폼 없이 코드로 제출을 일으키는 훅
- [ ] Concurrent Mutation / 제출이 겹칠 때 마지막 결과를 지키는 처리
- [ ] useRevalidator / 액션과 무관하게 loader를 다시 부르는 훅

---

# PART 3 · Web Standards and Authentication

## 7. Web Standards

- [ ] Fetch API Request and Response / loader와 action이 그대로 주고받는 표준 객체
- [ ] Headers / Set-Cookie 같은 헤더를 직접 붙이고 읽는 방법
- [ ] URL and URLSearchParams / 요청 주소를 쪼개고 쿼리를 다루는 표준 객체
- [ ] FormData / 폼 입력을 키와 값으로 담는 표준 객체
- [ ] Web Streams / 응답 본문을 조각으로 흘려보내는 표준
- [ ] AbortSignal / 끊긴 요청을 서버 작업까지 취소하는 신호
- [ ] Runtime Differences / 표준 API가 내장인지 폴리필인지 갈리는 지점

## 8. Sessions and Cookies

- [ ] createCookie / 서명과 만료를 붙여 쿠키를 정의하는 함수
- [ ] Session Storage Types / 세션 값을 쿠키에 담을지 서버에 둘지 고르는 종류
- [ ] createCookieSessionStorage / 세션 내용을 쿠키 안에 통째로 넣는 저장소
- [ ] Session Lifecycle / 세션을 읽고 고쳐 쿠키로 되돌리는 순서
- [ ] Flash Message / 한 번 읽으면 사라지는 세션 값
- [ ] Secret Rotation / 서명 키를 갈면서 옛 쿠키도 받아 주는 방법
- [ ] AppLoadContext / loader·action에 의존성을 넘기는 통로

## 9. Authentication and Authorization

- [ ] Form-based Login / 로그인을 action의 폼 제출로 처리하는 방식
- [ ] Password Hashing / 비밀번호를 되돌릴 수 없게 저장하는 방법
- [ ] requireUser Pattern / loader 첫 줄에서 미인증을 되돌려보내는 관용구
- [ ] OAuth / 남의 서비스 계정으로 신원을 받아오는 절차
- [ ] remix-auth / 전략 단위로 로그인 방식을 갈아 끼우는 라이브러리 `선택`
- [ ] CSRF Protection / 남의 사이트에서 온 폼 제출을 막는 방법
- [ ] Authorization Layer / 중첩 라우트마다 권한을 나눠 검사하는 배치

---

# PART 4 · UI and Quality

## 10. Error Handling

- [ ] ErrorBoundary / 라우트별로 에러 화면을 대신 그리는 export
- [ ] Error Type Detection / 던진 응답과 실제 예외를 갈라 보는 방법
- [ ] 404 and 405 Handling / 없는 경로와 안 받는 메서드를 돌려주는 방법
- [ ] Error Propagation and Nested Route Boundaries / 에러가 가장 가까운 부모 경계까지 오르는 순서
- [ ] Server Error Logging / 서버 로그에만 남기고 화면엔 안 내보내는 규칙

## 11. Styling and Assets

- [ ] Links Function / 라우트가 쓸 스타일시트를 문서 head에 다는 자리
- [ ] CSS Import / import한 css를 링크 태그로 바꾸는 처리
- [ ] CSS Modules · Vanilla Extract / 클래스 이름 충돌을 빌드에서 없애는 방식
- [ ] Tailwind Integration / 유틸리티 클래스 빌드를 붙이는 설정
- [ ] Route-based Code Splitting / 라우트 단위로 번들을 쪼개 받는 구조
- [ ] Asset Fingerprinting / 파일 이름에 해시를 박아 옛 사본을 밀어내는 방식
- [ ] Font and Image Optimization / 폰트·이미지를 미리 실어 화면 흔들림을 줄이는 방법 `선택`

## 12. Meta and SEO

- [ ] Meta Function / 라우트마다 타이틀·설명 태그를 정하는 자리
- [ ] Parent Meta Merging / 부모가 정한 meta를 자식이 덮거나 물려받는 규칙
- [ ] Open Graph · Twitter Card / 링크 공유 미리보기를 정하는 태그
- [ ] Canonical Link / 같은 내용의 대표 주소를 하나로 지정하는 태그
- [ ] Resource Route / 화면 없이 응답만 돌려주는 라우트
- [ ] Serving sitemap.xml and robots.txt / 크롤러용 파일을 라우트로 내주는 방법

## 13. Testing

- [ ] Vitest / 로더와 유틸을 함수 단위로 돌려 보는 러너
- [ ] Direct Loader and Action Call Testing / Request를 만들어 loader를 직접 부르는 시험
- [ ] Testing Library / 사용자가 보는 대로 컴포넌트를 확인하는 도구
- [ ] createRemixStub / 라우터 문맥을 가짜로 세워 컴포넌트를 띄우는 도구
- [ ] E2E / 브라우저를 실제로 몰아 화면 흐름을 확인하는 시험
- [ ] Typecheck as a Quality Gate / 타입 검사를 통과 조건으로 거는 방법

---

# PART 5 · Deployment and Operations

## 14. Deployment

- [ ] Adapter Concept / 런타임별 요청을 표준 Request로 바꿔 주는 층
- [ ] Node Server / Express 위에 핸들러를 얹어 직접 띄우는 방식
- [ ] Serverless / 요청마다 함수가 깨어나 응답하는 배포 방식
- [ ] Edge / 사용자 가까운 노드에서 실행하는 배포 방식
- [ ] Docker Image Build / 런타임과 산출물을 이미지 하나로 묶는 방법
- [ ] Build Artifacts / 서버 번들과 클라이언트 정적 파일로 갈리는 산출물
- [ ] Environment Variable / 서버에만 둘 값과 브라우저로 내보낼 값의 경계

## 15. Performance and Caching

- [ ] HTTP Cache-Control / loader 응답에 재사용 기간을 헤더로 붙이는 방법
- [ ] ETag and Conditional Request / 안 바뀐 응답을 304로 끊는 방법
- [ ] Streaming SSR / 첫 바이트를 먼저 보내 대기 시간을 줄이는 방식
- [ ] Prefetch / 링크에 닿을 때 그 라우트 데이터를 미리 받는 옵션
- [ ] Single Fetch / 중첩 loader 결과를 한 요청에 몰아 받는 방식
- [ ] CDN Caching Strategy / 정적 파일과 문서 응답을 갈라 앞단에 두는 배치
- [ ] Bundle Size Audit / 브라우저로 새는 서버 코드까지 재는 점검

## 16. Beyond Remix

- [ ] React Router 7 / Remix 코드를 라우터 프레임워크 모드로 옮기는 경로
- [ ] Migration / Remix v2에서 바뀐 규칙을 따라 고치는 절차
- [ ] Type-safe Route / 생성된 타입으로 params와 데이터를 물리는 방법
- [ ] SPA Mode / 서버 없이 클라이언트 라우팅만으로 돌리는 모드 `선택`
- [ ] Pre-rendering / 빌드 때 loader를 돌려 html을 미리 뽑는 모드 `선택`

---

# 이 로드맵 밖

- React `software/skill-based/Frameworks/react.md`
- Next.js `software/skill-based/Frameworks/nextjs.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 프론트엔드 전반 `software/role-based/frontend.md`
- 풀스택 `software/role-based/full-stack.md`
- Vite · Vercel `software/skill-based/Build-Tools/vite.md`, `software/skill-based/Infra-DevOps/vercel.md`
