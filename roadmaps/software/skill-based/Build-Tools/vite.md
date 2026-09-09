# Vite `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Vite

## 1. What is Vite?

### Overview of Vite / What is it?

- [ ] Native ESM Dev Server / 브라우저 네이티브 ESM으로 그대로 서빙하는 개발 서버
- [ ] No-bundle Development / 소스를 번들 없이 그대로 제공하는 개발 방식
- [ ] Rollup-Based Production Build / 프로덕션 빌드만 Rollup이 전담하는 구조
- [ ] esbuild-Based Pre-bundling / 의존성만 미리 묶어 요청 수를 줄이는 단계

### Problems It Solves

- [ ] Bundler Dev Server Cold Start / 프로젝트 전체를 먼저 번들해야 뜨는 문제
- [ ] HMR Slowdown At Scale / 파일이 늘수록 HMR 반영이 느려지는 문제
- [ ] Dev / Build를 한 파이프라인이 함께 처리해 최적화가 부딪히는 문제

### Vite vs Others

- [ ] Vite vs Webpack Dev Server / 번들 여부로 갈리는 시작 속도 차이
- [ ] Vite vs Parcel / 둘 다 제로 설정이지만 다른 처리 방식 비교
- [ ] When to choose Vite? / 신규 프로젝트나 빠른 시작이 필요할 때 고르는 기준

## 2. Getting Started

### Project Creation

- [ ] npm create vite / 대화형으로 템플릿을 골라 뼈대를 만드는 명령
- [ ] Template / 프레임워크별 초기 뼈대를 골라 프로젝트를 까는 방법
- [ ] index.html as Entry Point / 번들러와 달리 HTML을 진입점으로 삼는 방식

### Commands

- [ ] vite and dev / 개발 서버를 띄우는 기본 명령
- [ ] vite build / Rollup으로 프로덕션 번들을 만드는 명령
- [ ] vite preview / 빌드 결과물을 로컬에서 확인하는 명령
- [ ] vite optimize / 의존성 프리번들을 수동으로 강제하는 명령

## 3. Config File

### vite.config.ts Structure

- [ ] defineConfig / 설정 객체에 타입 힌트를 주는 헬퍼 함수
- [ ] Conditional Config / command·mode 값에 따라 설정을 분기하는 방법
- [ ] Async Config / 비동기 로직이 필요한 설정을 함수로 반환하는 방식

### Core Options

- [ ] Path Configuration / 프로젝트 루트·배포 경로·정적 폴더 지정
- [ ] resolve / 경로 별칭·확장자 생략·중복 패키지 단일화 설정
- [ ] define / 빌드 시점에 전역 상수를 문자열로 치환하는 옵션
- [ ] envPrefix / 환경변수 노출을 접두사로 제한하는 설정

### Environment Variables

- [ ] .env, .env.local, .env.[mode] / 환경별로 겹쳐 로드되는 환경변수 파일 규칙
- [ ] import.meta.env / VITE_ 접두사가 붙은 변수만 클라이언트에 노출하는 객체
- [ ] mode / --mode 플래그로 환경 설정 파일을 고르는 값
- [ ] Secret Bundle Exposure Risk / 민감 값이 실수로 클라이언트 번들에 섞이는 위험

---

# PART 2 · Dev Server

## 4. Dev Server

### How It Works

- [ ] Native ESM Serving / 요청된 모듈만 그때그때 ESM으로 응답하는 방식
- [ ] On-demand Transform / 요청이 올 때만 파일을 변환하는 방식
- [ ] Bare Import Rewriting / import 'react' 같은 경로를 브라우저용 URL로 바꾸는 처리
- [ ] Transform Result Cache / 변경 없으면 304로 재변환을 건너뛰는 캐시

### server Options

- [ ] Network / host·port·strictPort로 접속 주소를 고정하는 옵션
- [ ] open and cors / 서버 자동 오픈과 교차 출처 허용 옵션
- [ ] https / 로컬 개발 서버에 TLS를 붙이는 옵션
- [ ] watch / usePolling으로 네트워크 드라이브 변경 감지를 강제하는 옵션

### Proxy

- [ ] server.proxy / target·changeOrigin·rewrite로 API 요청을 중계하는 설정
- [ ] WebSocket Proxy / HMR 소켓 연결을 프록시 뒤로 통과시키는 처리
- [ ] CORS Bypass Strategy / 프록시로 출처 제한을 개발 중에 우회하는 방법

## 5. Dependency Pre-Bundling

- [ ] CommonJS and UMD / ESM으로 바꿔주는 사전 변환 과정
- [ ] Request Count Reduction / 수백 개 모듈 요청을 소수 청크로 줄이는 목적
- [ ] node_modules/.vite Cache / 프리번들 결과를 저장해두는 캐시 폴더
- [ ] optimizeDeps / include·exclude로 프리번들 대상을 조정하는 옵션
- [ ] Cache Invalidation / --force로 프리번들 캐시를 강제로 지우는 방법
- [ ] Monorepo Linked Package Handling / 심볼릭 링크로 연결된 로컬 패키지 처리 방식

## 6. HMR

- [ ] HMR Boundary Propagation / 변경이 부모로 전파되는 범위를 정하는 경계
- [ ] import.meta.hot / accept·dispose·invalidate로 갱신을 제어하는 API
- [ ] Framework HMR / React Fast Refresh·Vue SFC 등 프레임워크별 갱신 처리
- [ ] Full Reload Fallback Causes / 부분 갱신이 안 돼 전체 새로고침으로 빠지는 원인
- [ ] HMR Debugging / 갱신이 안 먹힐 때 원인을 추적하는 방법

## 7. Asset Handling

- [ ] Static Asset Import / import하면 파일 경로를 URL 문자열로 돌려주는 방식
- [ ] public Directory / 변환 없이 그대로 복사되는 정적 폴더
- [ ] Query Suffix / ?url·?raw·?inline으로 임포트 방식을 바꾸는 접미사
- [ ] ?worker / 워커 스크립트를 별도 번들로 만들어 임포트하는 접미사
- [ ] JSON and WASM Import / 두 포맷을 모듈처럼 바로 불러오는 지원
- [ ] import.meta.glob / 패턴에 맞는 여러 파일을 한 번에 동적 임포트하는 함수
- [ ] assetsInlineLimit / 이 크기 이하 자산을 base64로 인라인하는 기준

## 8. CSS

- [ ] CSS Import / import한 CSS를 별도 처리 없이 페이지에 자동 삽입하는 방식
- [ ] CSS Modules / *.module.css로 클래스명을 파일마다 고유하게 만드는 방식
- [ ] Preprocessor / Sass·Less·Stylus를 별도 설정 없이 바로 쓰는 지원
- [ ] PostCSS Config Integration / 기존 postcss.config를 자동으로 인식하는 연동
- [ ] css.devSourcemap / 개발 중 CSS에도 소스맵을 켜는 옵션
- [ ] Lightning CSS / Rust 기반으로 더 빠르게 처리하는 대체 CSS 엔진 `선택`

---

# PART 3 · Production Build

## 9. Build Pipeline

### Basic Options

- [ ] Rollup-Based Bundling / 프로덕션 산출물을 Rollup으로 묶는 방식
- [ ] index.html Entry Discovery / HTML에서 스크립트·링크를 찾아 진입점으로 삼는 과정
- [ ] Output Paths / outDir·assetsDir·emptyOutDir로 출력 위치를 정하는 옵션
- [ ] target / 지원할 브라우저 범위에 맞춰 변환 수준을 정하는 옵션
- [ ] sourcemap / 빌드 결과에 원본 위치 정보를 남기는 옵션
- [ ] minify / esbuild·terser 중 압축 엔진을 고르는 옵션

### Exposed Rollup Options

- [ ] build.rollupOptions / input·output·external로 Rollup 설정을 직접 넘기는 통로
- [ ] Multi-page App / 여러 HTML을 각각 input으로 등록해 빌드하는 방식
- [ ] Library Mode / build.lib·formats로 배포용 라이브러리를 빌드하는 모드

## 10. Code Splitting / Optimization

- [ ] Dynamic Import Chunking / import() 지점을 기준으로 청크를 나누는 방식
- [ ] manualChunks / 특정 모듈을 원하는 청크로 직접 묶는 함수
- [ ] CSS Code Splitting / 페이지별로 쓰이는 CSS만 따로 나누는 방식
- [ ] Modulepreload Polyfill / 구형 브라우저에도 모듈 프리로드를 흉내내는 폴리필
- [ ] Tree Shaking Conditions / package.json sideEffects로 제거 가능 범위를 정하는 조건
- [ ] Chunk Size Warning / 청크가 기준 용량을 넘으면 경고를 띄우는 기능

## 11. Legacy / Compatibility

- [ ] @vitejs/plugin-legacy / 구형 브라우저용 폴백 번들을 추가로 만드는 공식 플러그인
- [ ] Browserslist To Target Mapping / browserslist 설정을 빌드 target으로 바꾸는 과정
- [ ] Polyfill Injection Cost / 레거시 지원을 위해 늘어나는 번들 용량 비용

---

# PART 4 · Extensions and Framework Integration

## 12. Plugin System

### Basics

- [ ] Rollup Plugin Compatibility / Rollup 플러그인을 대부분 그대로 쓸 수 있는 호환성
- [ ] Plugin Definition / name·setup 필드로 플러그인을 정의하는 형식
- [ ] enforce / pre·normal·post로 플러그인 실행 순서를 정하는 옵션
- [ ] apply / serve·build 중 어느 단계에만 적용할지 정하는 옵션

### Hook

- [ ] Rollup Build Hook / resolveId·load·transform 등 Rollup 표준 훅
- [ ] Vite-Specific Hook / config·configResolved·configureServer 등 Vite 전용 훅
- [ ] transformIndexHtml / index.html 내용을 플러그인이 직접 조작하는 훅
- [ ] handleHotUpdate / HMR 갱신 대상을 플러그인이 가로채 제어하는 훅

### Commonly Used Plugins

- [ ] Framework Plugin / plugin-react·plugin-vue 등 프레임워크 지원 플러그인
- [ ] Asset Transform Plugin / vite-plugin-svgr처럼 자산을 컴포넌트로 바꾸는 플러그인
- [ ] vite-tsconfig-paths / tsconfig의 경로 별칭을 그대로 인식시키는 플러그인
- [ ] Bundle Visualizer / 청크별 용량을 시각화해 확인하는 도구

## 13. SSR

- [ ] ssrLoadModule / 개발 중 서버에서 모듈을 즉석으로 실행하는 함수
- [ ] Server Entry / Client Entry 분리
- [ ] SSR Manifest Preload / SSR용 청크 매핑으로 필요한 자산을 미리 로드하는 방식
- [ ] ssr.noExternal and ssr.external / 의존성을 SSR 번들에 포함할지 반대로 지정하는 옵션 쌍
- [ ] Hydration Mismatch Issues / 서버·클라이언트 렌더링 결과가 달라 생기는 오류
- [ ] Meta-framework Delegation / Nuxt·SvelteKit·Remix가 SSR 설정을 대신 감싸는 방식

## 14. Testing Integration

- [ ] Vitest / vite.config를 그대로 이어받아 쓰는 테스트 러너
- [ ] transformMode / 브라우저용과 SSR용 중 변환 방식을 고르는 옵션
- [ ] E2E Integration / Playwright·Cypress가 dev 서버를 그대로 띄워 쓰는 연동

---

# PART 5 · Deployment and Operations

## 15. Deployment

- [ ] Static Hosting / 빌드 산출물 dist 폴더를 그대로 올리는 배포 방식
- [ ] base Configuration / 루트가 아닌 하위 경로에 배포할 때 지정하는 값
- [ ] SPA History Fallback / 새로고침 시 모든 경로를 index.html로 돌리는 설정
- [ ] Cache Busting / 파일명에 해시를 붙여 캐시 갱신을 강제하는 방식
- [ ] CI Build / 빌드 전에 환경변수가 주입돼 있어야 하는 시점 문제

## 16. Troubleshooting

- [ ] Dev Works Build Fails / ESM과 CJS 상호운용 차이로 빌드에서만 터지는 문제
- [ ] Pre-bundling Cache Pollution / 오염된 프리번들 캐시가 오류를 일으키는 문제
- [ ] Node Built-in Import Error / 브라우저 번들에 Node 내장 모듈이 섞여 나는 오류
- [ ] Dev / Prod 동작 차이 원인 추적
- [ ] Build Profiling / --debug·--profile 플래그로 빌드 병목을 분석하는 방법

---

# 이 로드맵 밖

- 프론트엔드 전반 `software/role-based/frontend.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 설정 중심 대체 번들러 `software/skill-based/Build-Tools/webpack.md`
- 내부 트랜스파일 엔진 `software/skill-based/Build-Tools/esbuild.md`
- 프레임워크 `software/skill-based/Frameworks/react.md`, `vue.md`
- 테스트 러너 `software/skill-based/Testing/vitest.md`
