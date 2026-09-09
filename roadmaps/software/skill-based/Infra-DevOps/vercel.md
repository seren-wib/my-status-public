# Vercel `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Vercel

## 1. What is Vercel?

### Overview

- [ ] Frontend Cloud / 빌드 산출물을 엣지망에 올려 서빙하는 개념
- [ ] Git-Integrated Deployment Model / git push가 곧 배포로 이어지는 구조
- [ ] Serverless Execution Model / 요청이 올 때만 함수가 깨어나는 모델
- [ ] Relationship Between Vercel and Next.js / 프레임워크 기능이 곧 플랫폼 기능인 관계

### When to Use

- [ ] Static Sites and SSG / 빌드 시 미리 만들어 두는 정적 페이지 배포
- [ ] SSR and ISR Applications / 요청마다 또는 주기적으로 다시 렌더링하는 방식
- [ ] Preview-Centric Collaboration / 커밋마다 미리보기로 리뷰하는 협업 방식
- [ ] Vercel vs Netlify vs Cloudflare Pages / 프레임워크 밀착도로 갈리는 경쟁 구도
- [ ] Limitations / 상태를 유지하는 장시간 서버를 못 돌리는 한계

## 2. Getting Started

### Project Connection `택 1`

- [ ] Git Integration / 저장소를 연결해 푸시마다 자동 배포 `추천`
- [ ] Vercel CLI / 터미널 명령으로 직접 배포하는 도구
- [ ] Deploy Hook / URL 호출만으로 배포를 트리거하는 방식

### First Deployment

- [ ] Automatic Framework Preset Detection / 저장소 구조를 보고 빌드 설정을 추정하는 기능
- [ ] Root Directory / 모노레포에서 빌드할 하위 폴더 지정
- [ ] Build Command / 빌드 실행 명령과 산출물 폴더 지정
- [ ] Install Command / 패키지 매니저를 감지해 설치 명령을 정하는 설정

---

# PART 2 · Deployment and Domains

## 3. Deployments

- [ ] Deployment Immutability / 커밋마다 고유 주소를 갖는 배포 성질
- [ ] Production vs Preview Deployment / 배포마다 정식·임시 상태를 가르는 구분
- [ ] Preview URL and Branch URL / 브랜치·커밋마다 자동 생성되는 임시 주소
- [ ] Instant Rollback and Promote / 과거 배포를 즉시 되돌리거나 정식으로 올리는 조작
- [ ] Deployment Protection / 비밀번호나 SSO로 배포 접근을 제한하는 기능
- [ ] Skew Protection / 배포 중 신구 버전이 섞여 요청이 꼬이는 문제 방지
- [ ] Build Cache / 이전 빌드 결과를 재사용해 시간을 줄이는 캐시
- [ ] Ignored Build Step / 조건에 따라 빌드를 건너뛰는 설정

## 4. Configuration

- [ ] vercel.json / 라우팅·헤더 등을 코드로 정의하는 설정 파일
- [ ] Routing / 경로를 다시 쓰거나 다른 주소로 넘기는 규칙
- [ ] Headers / 응답에 커스텀 헤더를 붙이는 설정
- [ ] Cleanpath / 확장자 없는 URL과 슬래시 형식을 다듬는 옵션
- [ ] Monorepo / Turborepo로 여러 앱을 한 저장소에서 관리하는 구조
- [ ] Node.js Version / 빌드에 쓸 Node 버전과 이미지를 고르는 설정

## 5. Domains and DNS

- [ ] Custom Domain Setup / 프로젝트에 내 도메인을 연결하는 절차
- [ ] DNS Record / 도메인을 연결하는 레코드 종류와 설정
- [ ] Apex Domain vs Subdomain / 루트 도메인과 하위 도메인의 연결 차이
- [ ] Automatic TLS / 인증서 발급과 갱신을 자동 처리하는 기능
- [ ] Domain Redirect / www 유무 등 주소를 한쪽으로 통일하는 설정
- [ ] Wildcard Domain / 서브도메인을 통째로 받는 멀티테넌트 설정

---

# PART 3 · Runtime and Performance

## 6. Functions

- [ ] Vercel Functions / 파일 하나가 API 엔드포인트가 되는 함수
- [ ] Runtime / 함수를 실행할 Node·Edge·Python 환경 선택
- [ ] Streaming Response / 함수가 응답을 조각내 실시간으로 보내는 방식
- [ ] Fluid Compute / 여러 요청이 함수 인스턴스를 함께 쓰는 모델
- [ ] Max Duration and Memory / 함수 실행 시간과 메모리 상한 설정
- [ ] Cron Jobs / 정해진 주기로 함수를 자동 실행하는 기능
- [ ] Cold Start Mitigation Strategy / 함수가 깨어날 때 지연을 줄이는 전략
- [ ] Function Limits / 요청 크기와 실행 시간의 상한선

## 7. Edge and Middleware

- [ ] Edge Network / 전 세계 접속점으로 요청을 분산하는 인프라
- [ ] Middleware / 요청이 엣지에 닿는 순간 가로채는 처리 층
- [ ] Middleware Use Cases / 인증·A/B 테스트·지역 분기에 쓰는 사례
- [ ] Edge Config / 엣지에서 초저지연으로 읽는 설정 저장소
- [ ] Geolocation / 요청 헤더에 담기는 접속 지역 정보

## 8. Caching

- [ ] CDN Cache / 헤더로 CDN에 캐시 유지 시간을 지정하는 방식
- [ ] stale-while-revalidate / 캐시를 먼저 주고 뒤에서 갱신하는 전략
- [ ] ISR and On-demand Revalidation / 주기 또는 요청으로 정적 페이지를 다시 굽는 방식
- [ ] Cache Tag and Purge / 태그로 묶어 캐시를 골라 지우는 기능
- [ ] Data Cache vs CDN Cache / 함수 안 데이터 캐시와 CDN 캐시의 차이
- [ ] Image Optimization / 요청 시 이미지를 변환해 최적화하는 기능

## 9. Storage and Integrations `선택`

- [ ] Vercel Blob / 파일을 올려두고 URL로 꺼내 쓰는 저장소
- [ ] Vercel Postgres · Redis / 마켓플레이스 제공자가 붙는 관리형 DB
- [ ] Marketplace Integration / 서드파티 서비스를 프로젝트에 붙이는 연동
- [ ] External DB Connection / 함수의 짧은 수명 탓에 커넥션 풀링이 필요한 이유

---

# PART 4 · Operations

## 10. Environment and Secrets

- [ ] Environment Variable / 배포 단계별로 값을 다르게 두는 변수
- [ ] Sensitive Variable / 값을 암호화해 저장하는 민감 변수
- [ ] System Environment Variable / 플랫폼이 자동으로 주입하는 내장 변수
- [ ] vercel env pull / 클라우드 환경 변수를 로컬로 내려받는 명령
- [ ] Custom Environment / 기본 3단계 외에 직접 만드는 배포 환경
- [ ] Secret Management Principles / 비밀 값이 브라우저로 새지 않게 다루는 원칙

## 11. Observability

- [ ] Build Log and Runtime Log / 빌드 과정과 함수 실행 중 남는 기록
- [ ] Log Drain / 로그를 외부 서비스로 실시간 전송하는 기능
- [ ] Web Analytics / 방문자 트래픽을 집계해 보여주는 기능
- [ ] Speed Insights / 실사용자 기준 코어 웹 바이탈을 측정하는 도구
- [ ] Observability Dashboard / 함수 호출량과 오류율을 모아 보는 화면
- [ ] Alert Configuration / 지표가 기준을 넘으면 알림을 보내는 설정

## 12. Security and Access

- [ ] Vercel Firewall / IP 차단과 요청 속도 제한을 거는 방화벽
- [ ] Attack Challenge Mode / 공격 트래픽에 인증 절차를 끼워 거르는 대응
- [ ] Team / 역할과 접근 그룹으로 팀원 권한을 나누는 기능
- [ ] Audit Log / 팀 안에서 일어난 변경 이력을 남기는 기록
- [ ] Secure Compute / 함수를 사설 네트워크 안에서 실행하는 기능 `선택`

## 13. Cost and Limits

- [ ] Plan / 사용 규모에 따라 나뉘는 요금제 등급
- [ ] Billing Units / 함수 호출·대역폭 등으로 매기는 과금 단위
- [ ] Spend Management / 예산 한도를 정해 초과를 알리는 기능
- [ ] Fair Use / 무료 등급의 상업적 사용을 제한하는 정책
- [ ] Cost Reduction / 캐시 적중률을 높여 비용을 낮추는 방법

---

# 이 로드맵 밖

- Next.js `software/skill-based/Frameworks/nextjs.md`
- 프런트엔드 전반 `software/role-based/frontend.md`
- 엣지 · CDN 플랫폼 `software/skill-based/Infra-DevOps/cloudflare.md`
- AWS `software/skill-based/Infra-DevOps/aws.md`
- Git · GitHub `software/skill-based/Infra-DevOps/git-github.md`
