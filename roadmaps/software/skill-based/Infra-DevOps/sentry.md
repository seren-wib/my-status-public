# Sentry `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Sentry

## 1. What is Sentry?

### Overview of Sentry / What is it?

- [ ] Error and Crash Reporting Platform / 예외와 크래시를 모아 보여주는 도구 범주
- [ ] Exception Aggregation / 같은 예외를 모아 하나로 보여주는 방식
- [ ] Release-Centric Regression Tracking / 릴리스 기준으로 회귀 여부를 판단하는 방식
- [ ] SaaS vs Self-hosted / 운영 주체에 따른 배포 형태 선택

### Comparison with Other Tools

- [ ] Sentry vs Log Aggregation / 로그 전체 저장과 에러 추적의 차이
- [ ] Sentry vs APM / 에러 중심과 성능 중심 도구의 차이
- [ ] When to Use Sentry / 에러 추적이 필요해지는 시점

### Core Concepts

- [ ] Event / 발생한 예외 하나를 담은 원시 기록
- [ ] Issue and Group / 같은 원인의 이벤트를 묶은 단위
- [ ] Fingerprint / 이벤트를 같은 Issue로 묶는 지문값
- [ ] Organization, Team, Project / 조직 아래 팀과 프로젝트로 나뉘는 위계
- [ ] DSN / SDK가 이벤트를 보낼 프로젝트 주소

## 2. Getting Started

### Installation `택 1`

- [ ] SaaS / 설치 없이 바로 쓰는 호스팅형 운영 `추천`
- [ ] Self-hosted / Docker Compose로 직접 띄워 운영하는 방식

### SDK Initialization

- [ ] SDK Installation / init 호출에 DSN을 넣어 연결하는 과정
- [ ] Environment and Release / 배포 환경과 버전을 태그로 구분하는 설정
- [ ] sample_rate / 에러 이벤트를 보낼 비율을 정하는 값
- [ ] Debug Mode / 연결 확인용 테스트 이벤트를 보내는 모드

### SDKs by Platform

- [ ] Browser JavaScript / 브라우저에서 발생하는 예외를 잡는 SDK
- [ ] Node.js / 서버 런타임 예외를 잡는 SDK
- [ ] Python / Django·Flask 프레임워크용 예외 수집 SDK
- [ ] Java / Spring 프레임워크용 예외 수집 SDK
- [ ] Mobile / Android·iOS·React Native용 SDK
- [ ] Go, PHP, Ruby, .NET / 그 외 언어별 공식 SDK 목록

---

# PART 2 · Error Tracking

## 3. Event / Context

### Event Structure

- [ ] Exception / 예외 종류와 스택트레이스를 담은 필드
- [ ] Message Event / captureMessage로 보내는 비예외 로그
- [ ] Level / fatal·error·warning·info 등 심각도 값
- [ ] Culprit / 원인으로 지목된 함수나 트랜잭션 이름
- [ ] Platform / 이벤트를 보낸 언어·SDK 정보

### Context

- [ ] Tags / 이벤트를 검색·필터링할 키값 쌍
- [ ] User Context / setUser로 넣는 겪은 사용자 정보
- [ ] Extra and Contexts / 구조화된 부가 디버깅 정보
- [ ] Breadcrumbs / 에러 전까지의 사용자 행동 발자국
- [ ] Attachments / 스크린샷 등 재현용 첨부 파일
- [ ] Scope / withScope로 태그·컨텍스트를 묶는 범위

## 4. Grouping

- [ ] Default Grouping / 스택트레이스와 예외 타입으로 자동 묶기
- [ ] Custom Fingerprint / fingerprint 배열로 묶음 기준을 직접 지정
- [ ] Server-side Fingerprint Rules / 서버에서 일괄 적용하는 묶음 규칙
- [ ] Stack Trace Rules / 내 코드 프레임만 골라 지문에 반영하는 규칙
- [ ] Merge and Unmerge Issues / 잘못 나뉘거나 뭉친 Issue를 재조정
- [ ] Diagnosing Over-Splitting and Over-Merging / 묶음이 과하게 쪼개지거나 뭉친 원인 진단

## 5. Issue Workflow

- [ ] Issue State / 미해결·해결·보관 등 처리 상태
- [ ] Resolve in Next Release / 다음 배포에서 고쳐질 예정으로 표시
- [ ] Assign / 소유 규칙에 따라 담당자를 자동 지정
- [ ] Issue Search Query / is:·assigned: 같은 검색 문법
- [ ] Saved Search / 자주 쓰는 검색 조건 저장
- [ ] Regression Detection / 해결 표시된 Issue가 재발했는지 판정
- [ ] Delete & Discard / Issue 삭제와 향후 유입 차단의 차이

## 6. Noise Control

- [ ] Inbound Filter / 브라우저 확장·구형 브라우저 잡음 차단
- [ ] ignoreErrors / 특정 에러 메시지를 전송 전에 제외
- [ ] beforeSend Hook / 전송 직전 이벤트를 가공·차단하는 콜백
- [ ] Rate Limiting / 급증한 이벤트를 자동으로 제한
- [ ] Client-side Sampling / SDK 단에서 미리 표본만 전송
- [ ] Quota / 플랜별 이벤트 전송 한도 관리

---

# PART 3 · Releases and Source Maps

## 7. Release

- [ ] Release Creation / sentry-cli로 새 릴리스 버전을 등록
- [ ] Commit Integration / 릴리스에 커밋 목록을 연결
- [ ] Suspect Commits / 에러를 들여온 것으로 지목된 커밋
- [ ] Deploy Tracking / environment별 배포 시점 기록
- [ ] Release Health / 크래시 없는 세션 비율과 채택률 지표
- [ ] Session Tracking / 릴리스 건강도 계산의 기반 데이터 수집
- [ ] First Seen and Last Seen Release / 처음·마지막으로 발생한 릴리스 버전

## 8. Source Maps / Symbolication

### JavaScript

- [ ] Source Map Upload / sentry-cli나 번들러 플러그인으로 업로드
- [ ] debug_id / 소스맵과 번들을 정확히 짝짓는 식별자
- [ ] Matching release and dist / 이벤트와 소스맵을 잇는 두 키값 일치
- [ ] Inline vs Hosted Source Map / 소스맵을 파일에 내장할지 따로 둘지
- [ ] Upload Verification / Source Map Wizard로 업로드 상태 점검

### Native / Mobile

- [ ] ProGuard / R8 난독화 매핑 파일 업로드
- [ ] dSYM Upload / iOS 네이티브 심볼 파일 업로드
- [ ] Debug Symbols / 네이티브 크래시를 코드 위치로 되돌리는 정보
- [ ] Diagnosing Symbolication Failure / 심볼릭 복원이 실패하는 원인 진단

## 9. CI/CD Integration

- [ ] sentry-cli / 릴리스·소스맵 작업을 자동화하는 CLI
- [ ] Bundler Plugin / Webpack·Vite·Rollup용 빌드 통합 플러그인
- [ ] GitHub Action / CI 파이프라인에 업로드 단계를 끼워 넣는 연동
- [ ] Auth Token / CI에서 쓰는 권한 범위 제한 토큰
- [ ] Automating Source Map Upload / 빌드마다 소스맵 업로드를 자동 실행
- [ ] Automatic Release Creation / 배포 시 릴리스 버전을 자동 생성

---

# PART 4 · Performance and Operations

## 10. Tracing / Performance

- [ ] Transaction and Span / 요청 전체와 그 안의 구간을 나타내는 단위
- [ ] Trace Propagation / sentry-trace 헤더로 트레이스를 이어 붙임
- [ ] tracePropagationTargets / 트레이스 헤더를 붙일 대상 URL 지정
- [ ] Web Vitals / 트레이싱에 곁들여 보는 프론트 성능 지표
- [ ] Performance Issue Detection / N+1 쿼리 등 느린 패턴 자동 탐지
- [ ] Trace Explorer / 느린 트랜잭션을 Issue처럼 묶어 보는 화면
- [ ] Frontend-Backend Trace Linking / 프론트 요청과 백엔드 처리를 한 트레이스로 연결
- [ ] OpenTelemetry Integration / OTel 계측 데이터를 그대로 받아들이는 연동

## 11. Additional Products `선택`

- [ ] Session Replay / 에러 발생 전후 화면을 영상처럼 재생
- [ ] Profiling / 코드 실행 시간을 함수 단위로 측정
- [ ] Cron Monitoring / 예약 작업이 정시에 실행됐는지 check-in으로 확인
- [ ] Uptime Monitoring / 서비스 응답 여부를 주기적으로 점검
- [ ] User Feedback Widget / 에러 화면에서 사용자 제보를 직접 수집
- [ ] Logs / 이벤트 옆에 남기는 구조화 로그 스트림
- [ ] AI Issue Fix / Issue 원인과 수정안을 AI가 제시하는 기능

## 12. Alerting and Integrations

- [ ] Issue Alert vs Metric Alert / 이슈 발생 기준과 지표 임계값 기준 알림
- [ ] Alert Condition Composition / 여러 조건을 조합한 알림 규칙 구성
- [ ] Notification Setting / 개인·팀 단위로 나눈 알림 수신 설정
- [ ] Integration / Slack·Jira·PagerDuty로 보내는 연동
- [ ] GitHub and GitLab Integration / 커밋·PR과 Issue를 잇는 연동
- [ ] Issue Owners / 코드 소유자 파일로 담당자를 자동 배정
- [ ] Internal Integration / 조직 내부용 커스텀 웹훅 연동

## 13. Organization Management

- [ ] Project Separation Strategy / 서비스·팀 기준으로 프로젝트를 나누는 전략
- [ ] Environment Separation / 운영·스테이징 환경을 태그로 구분
- [ ] Member Role / 팀 단위 권한을 정하는 구성원 역할
- [ ] SSO and SCIM / 조직 계정 인증과 프로비저닝 연동 `별도`
- [ ] Client-side Data Scrubbing / 개인정보를 SDK 단에서 먼저 지움
- [ ] Server-side Scrubbing Rule / 서버에 도달한 후 적용하는 마스킹 규칙
- [ ] Data Retention / 이벤트를 보관하는 기간 설정
- [ ] Sentry Web API / 데이터를 외부에서 조회·조작하는 API

---

# 이 로드맵 밖

- 프런트엔드 전반 `software/role-based/frontend.md`
- 백엔드 전반 `software/role-based/backend.md`
- 데브옵스 전반 `software/role-based/devops.md`
- 계측 표준 `software/skill-based/Infra-DevOps/opentelemetry.md`
- SaaS 관측 대안 `software/skill-based/Infra-DevOps/datadog.md`, `new-relic.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/gitlab-ci.md`, `git-github.md`
