# Astro `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Astro

## 1. What is Astro?

### Overview of Astro / What is it?

- [ ] Content-driven Web Framework / 앱이 아니라 문서 더미를 굽는 데 맞춘 프레임워크
- [ ] Zero JS by Default / 아무 지시도 없으면 HTML만 내보내는 기본값
- [ ] Islands Architecture / 페이지를 섬 단위로만 살려 두는 설계
- [ ] Multi-framework Mixing / 한 사이트에 React와 Vue를 같이 얹는 방식
- [ ] Server-first Rendering / 브라우저가 아닌 빌드·서버에서 먼저 그리는 원칙

### Astro vs Others

- [ ] Astro vs Next.js / 콘텐츠 사이트와 앱 중 어디에 맞는지 가르는 기준
- [ ] Astro vs Static Site Generators / Hugo·Eleventy와 갈리는 컴포넌트 모델
- [ ] When to choose Astro? / JS 없는 페이지가 이득인 프로젝트를 가르는 선

## 2. Getting Started

- [ ] npm create astro / 대화형 마법사로 프로젝트 골격을 까는 명령
- [ ] Template Selection / minimal·blog 등 시작 템플릿을 고르는 기준
- [ ] CLI / dev·build·preview로 갈리는 실행 명령
- [ ] astro add and astro check / 통합 설치와 타입 검사를 맡는 명령
- [ ] TypeScript Configuration / 엄격도가 다른 tsconfig 프리셋 세 가지

## 3. Project Structure

- [ ] src/pages / 파일 하나가 곧 URL 하나가 되는 폴더
- [ ] src/components, src/layouts / 조각과 껍데기를 나눠 두는 관례
- [ ] src/content, src/styles / 글 원본과 전역 스타일이 사는 자리
- [ ] public vs src/assets / 그대로 복사할지 빌드에 태울지 가르는 기준
- [ ] astro.config.mjs / 통합·어댑터·빌드 설정이 모이는 한 파일

---

# PART 2 · Components and Pages

## 4. Astro Components

- [ ] .astro File Structure / 스크립트 울타리와 템플릿 두 칸으로 된 파일
- [ ] Frontmatter Fence / 울타리 안 코드가 서버에서만 도는 규칙
- [ ] Props / 부모가 넘긴 값을 받는 자리와 타입 선언
- [ ] Template Syntax / 중괄호 표현식과 조건·반복을 쓰는 표기
- [ ] Slots / 이름 붙은 구멍과 비었을 때의 대체 내용
- [ ] Astro Global / 현재 요청과 사이트 정보를 꺼내는 전역 객체
- [ ] set:html and set:text / 이스케이프를 끌지 켤지 정하는 지시어
- [ ] Component Script vs Client Script Tag / 빌드 때 도는 코드와 브라우저로 실려 가는 코드
- [ ] Scoped Style / 파일 안에 가두고 필요할 때만 전역으로 여는 규칙

## 5. Routing

- [ ] File-based Routes / 파일 이름이 URL 조각이 되는 대응 규칙
- [ ] Dynamic Routes / 대괄호로 경로 조각을 변수로 받는 표기
- [ ] getStaticPaths / 빌드 때 만들 경로 목록을 미리 뱉는 함수
- [ ] Pagination / 목록을 쪽으로 잘라 여러 경로로 굽는 방법
- [ ] Redirects Configuration / 옛 주소를 새 주소로 넘기는 설정
- [ ] Rewrite / 주소는 그대로 두고 다른 라우트를 그리는 방법
- [ ] i18n Routing / 로케일 접두사로 언어별 경로를 가르는 설정
- [ ] Error Page / 404·500 전용 페이지를 두는 자리

## 6. Layouts & Styling

- [ ] Layout Component Pattern / 슬롯 하나만 뚫어 둔 공통 껍데기
- [ ] Nested Layout / 껍데기 안에 껍데기를 겹쳐 쓰는 구성
- [ ] head Management / 페이지마다 title·meta를 갈아 끼우는 방법
- [ ] Styling Approach / 스코프 CSS·Tailwind 중 하나를 고르는 기준 `택 1`
- [ ] Global Stylesheet import / 레이아웃에서 한 번 불러 전역에 까는 방법
- [ ] CSS Bundling and Critical CSS Inlining / 첫 화면에 쓸 스타일만 문서에 박아 넣는 처리

---

# PART 3 · Islands and UI Frameworks

## 7. Islands Architecture

- [ ] Island Concept / 정적 HTML에 박힌 인터랙티브 조각 하나
- [ ] Hydration Directives / 섬을 언제 깨울지 고르는 client:* 지시어
- [ ] Directive Selection Criteria and Cost / 각 지시어가 JS를 언제 내려받는지 비교하는 기준
- [ ] Island Boundary Design / 어디까지를 한 섬으로 묶을지 정하는 단위
- [ ] Props Serialization Constraints / 함수를 못 넘기는 직렬화 제약
- [ ] Static Content Injection via Slot / 섬 안쪽을 정적 HTML로 채워 JS를 아끼는 방법
- [ ] Server Islands / 껍데기를 먼저 보내고 서버가 늦게 채우는 조각
- [ ] Partial Hydration Impact on Performance and SEO / 일부만 깨울 때 지표와 색인이 갈리는 지점

## 8. UI Framework Integrations

- [ ] Integration Installation / 프레임워크별 렌더러를 설정에 등록하는 방법
- [ ] Multiple Frameworks on One Page / 한 페이지에 서로 다른 섬을 섞어 두는 구성
- [ ] Renderer Configuration and Include Scope / 렌더러가 맡을 파일 범위를 좁히는 설정
- [ ] .astro Not Usable Inside Framework Components / 프레임워크 컴포넌트 안에 .astro를 못 넣는 이유
- [ ] children Passing / 슬롯을 프레임워크 children으로 옮기는 대응
- [ ] Duplicate Framework Bundle Cost / 프레임워크마다 런타임이 따로 실리는 비용

## 9. State Across Islands

- [ ] State Isolation Between Islands / 섬끼리 메모리를 공유하지 않는 성질
- [ ] Nano Stores / 섬 밖에 상태를 두고 여럿이 구독하는 저장소 `추천`
- [ ] Custom Event / 브라우저 이벤트로 섬끼리 신호를 넘기는 방법
- [ ] Web Components Usage / 브라우저 표준만으로 섬을 만드는 방식 `선택`
- [ ] View Transitions / ClientRouter로 이동 사이 화면을 잇는 기능
- [ ] State Persistence Across Transitions / 이동해도 특정 섬을 다시 안 만드는 표시

---

# PART 4 · Content and Data

## 10. Content Collections

- [ ] Collection Definition / 글 묶음 하나를 이름과 규칙으로 선언하는 방법
- [ ] Content Layer API / 파일 밖 원본까지 컬렉션으로 끌어오는 로더
- [ ] Schema Validation / zod로 프런트매터 형식을 못 박는 방법
- [ ] Frontmatter Type Safety / 스키마에서 자동으로 나오는 항목 타입
- [ ] Querying / 묶음 전체와 낱개 하나를 꺼내는 두 함수
- [ ] Rendering / 마크다운 본문을 HTML 컴포넌트로 바꾸는 단계
- [ ] Markdown & MDX / 본문 안에서 컴포넌트를 부를 수 있게 하는 확장
- [ ] remark · rehype Plugin / 마크다운과 HTML 단계에 변환을 끼우는 자리
- [ ] Syntax Highlighting / Shiki로 코드 색칠을 빌드 때 끝내는 처리
- [ ] Relation / 컬렉션끼리 서로를 가리키게 잇는 필드

## 11. Data Fetching

- [ ] Top-level Await in Frontmatter / 프런트매터에서 바로 기다렸다 그리는 방식
- [ ] Build Time Fetch vs Request Time Fetch / 데이터를 언제 가져올지 가르는 기준
- [ ] Local File Import / 폴더 안 파일 여럿을 한꺼번에 읽는 방법
- [ ] Headless CMS Integration / 외부 CMS 글을 빌드 때 끌어와 굽는 방법
- [ ] Environment Variables / 공개 변수와 서버 전용 변수를 가르는 규칙

## 12. Rendering Modes

- [ ] Static Output / 전부 미리 구워 파일로만 내보내는 기본값
- [ ] On-demand Rendering / 요청이 올 때 서버가 그때 그리는 모드
- [ ] Per-page Control / 페이지 하나만 정적·동적으로 뒤집는 선언
- [ ] Adapter Prerequisites / 서버 렌더링에 어댑터가 먼저 있어야 하는 이유
- [ ] Cache Header Control / 응답 헤더로 재사용 기간을 지정하는 방법

## 13. Endpoints, Middleware & Actions

- [ ] Static File Endpoint / 빌드 때 json 같은 파일을 만들어 내는 라우트
- [ ] Server Endpoint / HTML 대신 데이터를 돌려주는 요청 처리기
- [ ] APIContext / 요청·쿠키·locals를 담아 넘겨주는 인자
- [ ] Middleware / 요청 앞단에 공통 처리를 줄 세우는 자리
- [ ] Astro Actions / 서버 함수를 타입 안전하게 부르는 통로
- [ ] Session & Cookie Handling / 방문자 상태를 쿠키와 세션에 남기는 방법

---

# PART 5 · Optimization and Deployment

## 14. Integrations & Config

- [ ] astro.config Structure / 통합 목록과 vite 설정이 놓이는 자리
- [ ] Official Integrations / mdx·partytown 같은 공식 확장 묶음
- [ ] Direct Vite Plugin Usage / 통합 없이 vite 플러그인을 바로 끼우는 방법
- [ ] Custom Integration Hook / 빌드 단계에 내 코드를 끼워 넣는 훅 `선택`
- [ ] Image Optimization / 빌드 때 크기·포맷을 미리 바꿔 두는 처리
- [ ] Font Handling / 폰트 파일을 직접 받아 서빙하는 방법

## 15. Performance & SEO

- [ ] JS Payload Measurement / 섬 때문에 실려 나간 스크립트 양을 재는 방법
- [ ] Prefetch Configuration / 다음 페이지를 미리 받아 두는 설정
- [ ] Sitemap & RSS / 색인용 목록과 구독 피드를 만들어 내는 확장
- [ ] Canonical & Open Graph Meta / 대표 주소와 공유 미리보기를 적는 메타
- [ ] Core Web Vitals Audit / LCP·CLS 지표를 실제 페이지에서 재는 방법
- [ ] Third-party Script Isolation / 외부 스크립트를 워커로 밀어내는 방법

## 16. Deployment

### Adapter `택 1`

- [ ] Static Host / 구운 파일만 올려 두는 가장 싼 배포 `추천`
- [ ] @astrojs/node / 내 서버 프로세스로 직접 돌리는 어댑터
- [ ] Serverless Adapter / 함수 단위 플랫폼에 얹는 어댑터

### Operations

- [ ] Build Output / dist 안에 나오는 산출물 구조
- [ ] site and base Configuration / 절대 URL과 하위 경로를 알려 주는 설정
- [ ] Cache & CDN Strategy / 정적 파일과 HTML의 수명을 다르게 두는 방침
- [ ] Rebuild on Content Update / 글이 바뀌면 웹훅으로 다시 굽는 흐름

---

# 이 로드맵 밖

- 프론트엔드 전반 `software/role-based/frontend.md`
- Next.js `software/skill-based/Frameworks/nextjs.md`
- UI 프레임워크 `software/skill-based/Frameworks/react.md`, `vue.md`
- CSS `software/skill-based/Languages/css.md`
- 빌드 도구 `software/skill-based/Build-Tools/vite.md`
- 배포 `software/skill-based/Infra-DevOps/vercel.md`, `cloudflare.md`
