# esbuild `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to esbuild

## 1. What is esbuild?

### Overview of esbuild / What is it?

- [ ] Go-Based Bundler and Transpiler / 묶는 일과 문법 변환을 한 바이너리가 맡는 구조
- [ ] Bundle, Transform, Serve / esbuild가 맡는 세 가지 역할
- [ ] Single-Pass Pipeline Design / 파싱부터 출력까지 한 번에 처리하는 구조

### Why It Is Fast and the Trade-offs

- [ ] Native Binary / JS 인터프리터 없이 기계어로 도는 방식
- [ ] Multicore Parallelism / 여러 코어에 파일 처리를 나눠 돌리는 방식
- [ ] Minimal Intermediate Representation / 파싱 결과를 가볍게 유지해 속도를 낸 구조
- [ ] Reduced Feature Scope Trade-off / 기능을 줄이는 대신 얻은 속도라는 대가

### Position in the Ecosystem

- [ ] Vite Pre-bundling Engine / Vite가 개발 서버 시작 전에 미리 쓰는 번들 엔진
- [ ] Webpack esbuild-loader / 변환·압축 단계를 빠르게 대체하는 방법
- [ ] Higher-Level Wrapper / 자주 쓰는 설정을 미리 묶어둔 상위 도구

## 2. Getting Started

- [ ] Installation / 플랫폼별 바이너리가 함께 오는 설치 방법
- [ ] CLI Execution / 커맨드 플래그로 옵션을 넘기는 실행 방식
- [ ] JS API / 코드에서 직접 빌드를 호출하는 방법
- [ ] Go and Deno API / 노드 밖 런타임에서 부르는 공식 바인딩 `선택`

---

# PART 2 · Build Options

## 3. Core Build Options

- [ ] entryPoints / 시작점 파일과 출력 경로를 지정하는 옵션
- [ ] bundle / 의존성을 한 파일로 합칠지 정하는 옵션
- [ ] format / 출력 모듈 형식을 고르는 옵션
- [ ] platform / 실행 환경에 맞춰 처리 방식을 바꾸는 옵션
- [ ] target / 문법을 어느 환경까지 낮출지 정하는 옵션
- [ ] write / 디스크 대신 메모리로 결과를 받는 옵션

## 4. Input Handling

- [ ] Loader / 확장자별로 처리 방식을 정하는 옵션
- [ ] Extension-to-Loader Mapping / 확장자마다 다른 Loader를 자동으로 매칭하는 규칙
- [ ] resolveExtensions / 확장자 생략 시 찾아볼 순서를 정하는 옵션
- [ ] alias / tsconfig의 경로 별칭을 그대로 쓰는 방법
- [ ] mainFields / 진입점 필드와 exports 조건을 함께 보는 옵션
- [ ] external / 번들에서 빼고 외부 참조로 남기는 옵션
- [ ] inject / 코드 수정 없이 전역 변수를 주입하는 옵션
- [ ] define / 빌드 시점에 상수 값으로 치환하는 옵션

## 5. Output Control

- [ ] minify / 공백·이름·구문을 줄이는 세 단계 옵션
- [ ] sourcemap / 소스맵을 어디에 담을지 정하는 옵션
- [ ] splitting / 공통 코드를 청크로 나누는 ESM 전용 옵션
- [ ] Naming Templates / 출력 파일 이름 패턴을 정하는 옵션
- [ ] metafile / 번들 구성을 분석용 JSON으로 뽑는 옵션
- [ ] banner and footer / 출력 파일 앞뒤에 문구를 넣는 옵션
- [ ] legalComments / 라이선스 주석 처리 방식을 정하는 옵션
- [ ] publicPath / 코드 안에서 자산을 참조할 기준 경로

## 6. Language Features

- [ ] TypeScript Transpile / 타입은 안 보고 문법만 변환하는 방식
- [ ] tsconfig.json Support Scope / 일부 컴파일러 옵션만 읽는 범위
- [ ] JSX Configuration / JSX를 어떤 함수로 변환할지 정하는 옵션
- [ ] Decorator Support Limits / 최신 데코레이터 제안만 일부 지원하는 한계
- [ ] Syntax Lowering Scope / 신규 문법을 구버전으로 낮추는 범위와 한계
- [ ] CSS Bundling / @import·url() 경로를 함께 묶는 기능

---

# PART 3 · Development Workflow

## 7. Watch / Serve / Rebuild

- [ ] context API / 재사용 가능한 빌드 컨텍스트를 만드는 방법
- [ ] Watch Mode / 파일 변경을 감지해 자동으로 다시 빌드하는 모드
- [ ] Serve Mode / 정적 파일 서버에 프록시를 얹는 개발 모드
- [ ] Incremental Rebuild / 이전 빌드 결과를 재사용해 다시 빌드하는 방식
- [ ] dispose / 컨텍스트가 쓰던 리소스를 정리하는 메서드

## 8. Plugin API

- [ ] Plugin Shape / 이름과 setup 함수로 이뤄진 플러그인 구조
- [ ] onResolve / 경로 해석 단계에 개입하는 훅
- [ ] onLoad / 파일 내용을 가로채 직접 채우는 훅
- [ ] onStart and onEnd / 빌드 시작과 끝에 실행되는 훅
- [ ] Virtual Module Implementation / 실제 파일 없이 onLoad로 모듈을 만드는 방법
- [ ] onDispose / 빌드 컨텍스트가 정리될 때 실행되는 훅
- [ ] JS Callback Overhead / 네이티브 코드가 JS 콜백을 부를 때 드는 비용

---

# PART 4 · Limitations and Real-World Use

## 9. Limitations and Workarounds

- [ ] No Type Checking / 타입 검사는 tsc를 따로 돌려 채우는 한계
- [ ] No ES5 Downlevel / 구형 브라우저용 ES5까지는 못 낮추는 한계
- [ ] Legacy Decorator / 리플렉션용 메타데이터를 못 만드는 한계
- [ ] Tree Shaking Precision Limits / 부작용 판단이 정확하지 않아 남는 죽은 코드
- [ ] Plugin Ecosystem Size / webpack·rollup보다 적은 서드파티 플러그인 수
- [ ] Rollup Hybrid Strategy / dev는 esbuild, build는 Rollup을 쓰는 조합

## 10. Real-World Usage

- [ ] Node Library Build / CJS·ESM 둘 다 빌드해서 배포하는 방식
- [ ] CLI Tool Bundling / #!로 시작하는 실행 파일로 묶는 방법
- [ ] Lambda and Serverless / 콜드 스타트를 줄이려 최소 크기로 묶는 배포 방식
- [ ] Test Transform Integration / 테스트 러너 안에서 TS·JSX를 변환해주는 용도
- [ ] CI Build Time Reduction / CI 파이프라인의 빌드 대기 시간을 줄이는 용도
- [ ] metafile Size Regression Watch / metafile로 번들 용량 증가를 추적하는 방법

---

# 이 로드맵 밖

- JavaScript `software/skill-based/Languages/javascript.md`
- TypeScript `software/skill-based/Languages/typescript.md`
- 상위 번들러 `software/skill-based/Build-Tools/vite.md`
- Loader 연동 `software/skill-based/Build-Tools/webpack.md`
- Node.js 런타임 `software/skill-based/Frameworks/nodejs.md`
