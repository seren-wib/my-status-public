# TeamCity `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with TeamCity

## 1. What is TeamCity?

- [ ] JetBrains CI/CD Server / 코틀린 진영이 만든 상용 CI/CD 서버
- [ ] Server and Build Agent Architecture / 서버와 에이전트로 역할을 나누는 구조
- [ ] On-premise vs TeamCity Cloud / 직접 운영할지 클라우드에 맡길지 선택
- [ ] Build Chain Centric Model / 낱개 빌드보다 체인을 기본 단위로 보는 모델

### Key Features

- [ ] Out-of-the-box Build Runners / 언어·도구별 실행기를 기본 제공하는 기능
- [ ] IDE Integration / IDE 안에서 빌드를 확인·실행하는 연동
- [ ] Investigation and Build History Tracking / 실패 담당자 지정과 이력 추적 기능

### Comparison with Other Tools

- [ ] TeamCity vs Jenkins / 저장 설정 객체와 스크립트 파이프라인의 차이
- [ ] TeamCity vs GitLab CI / 별도 서버 도구와 내장 파이프라인의 차이
- [ ] Licensing Model / 에이전트 수로 과금하며 무료 등급도 있는 모델

## 2. Installation and Setup

### Installation `택 1`

- Docker / 컨테이너로 서버를 띄우는 설치 방식 `software/skill-based/Infra-DevOps/docker.md` `추천` `위임`
- [ ] Installer and Archive / 설치 프로그램이나 압축 파일로 배포하는 방식
- [ ] TeamCity Cloud / JetBrains가 호스팅하는 관리형 인스턴스 `선택`

### Initial Configuration

- [ ] Server Data Directory / 설정과 빌드 이력을 저장하는 디렉터리
- [ ] External Database / 운영용으로 PostgreSQL·MySQL을 붙이는 설정
- [ ] HTTPS and Reverse Proxy / 프록시 뒤에서 인증서를 붙이는 구성
- [ ] Agent Installation and Registration / 에이전트를 설치해 서버에 등록하는 절차
- [ ] Agent Authorization and Agent Pools / 등록된 에이전트를 승인해 풀로 묶는 관리

## 3. Core Concepts

- [ ] Project and Subproject Hierarchy / 프로젝트를 상하위로 중첩하는 구조
- [ ] Build Configuration / 빌드 절차를 통째로 담은 저장된 설정 객체
- [ ] Build Configuration Template / 여러 설정이 상속하는 공통 원본 틀
- [ ] Build and Build Queue / 실행 중인 빌드와 대기열 상태
- [ ] Build Agent and Agent Requirements / 빌드를 실행할 에이전트와 그 조건
- [ ] Parameter Inheritance / 템플릿·상위 설정에서 값을 물려받는 방식
- [ ] VCS Root / 저장소 접속 정보를 따로 떼어낸 객체

## 4. First Build Configuration

- [ ] Attach VCS Root and Auto-detect Settings / 저장소를 붙이면 빌드 방식을 자동 추정하는 기능
- [ ] Build Steps / 실행할 명령을 순서대로 쌓은 단계
- [ ] Common Runners / Maven·Gradle 등 도구별 실행기 목록
- [ ] Build Number Format / 빌드마다 붙는 번호의 형식 규칙
- [ ] Artifact Paths / 산출물 중 보관할 경로를 지정하는 값
- [ ] Running and Inspecting a Build / 빌드를 실행하고 로그·결과를 확인하는 절차

---

# PART 2 · Build Configuration

## 5. Triggers

- [ ] VCS Trigger / 커밋을 감지해 자동으로 여는 트리거
- [ ] Schedule Trigger / cron 식으로 정한 시각에 도는 트리거
- [ ] Finish Build Trigger / 지정한 설정의 빌드가 끝나면 도는 트리거
- [ ] Dependency Trigger / 의존 대상에 변경이 생기면 도는 트리거
- [ ] Retry Build Trigger / 직전 빌드가 실패하면 재시도하는 트리거
- [ ] Maven and NuGet Trigger / 패키지 저장소에 새 버전이 오르면 도는 트리거
- [ ] Trigger Rules / 특정 경로 변경만 걸러 반응하는 규칙

## 6. Parameters

- [ ] Parameter Kinds / 설정·시스템·환경 변수로 나뉜 종류
- [ ] Parameter Specification / 입력값의 타입과 표시 방식을 정하는 규격
- [ ] Value Reference / %이름% 문법으로 값을 참조하는 방법
- [ ] Secure Values / 비밀값을 암호화해 로그에 안 남기는 처리
- [ ] Predefined Parameters / 서버가 자동으로 채워주는 내장 변수
- [ ] Overriding Parameters in Dependencies / 의존 설정에 넘길 값을 상위에서 덮어쓰는 기능

## 7. Build Chains and Dependencies

- [ ] Snapshot Dependency / 같은 커밋 기준으로 설정들을 묶는 의존
- [ ] Artifact Dependency / 앞 설정이 만든 산출물을 받아오는 의존
- [ ] Build Chain Visualization / 체인 전체 진행을 그래프로 보는 화면
- [ ] Composite Build Configuration / 빌드 단계 없이 의존 상태만 합치는 설정
- [ ] Deployment Build Configuration / 체인 끝에 두는 배포 전용 설정
- [ ] Parallel Execution in a Chain / 체인 안 독립된 설정을 동시에 도는 실행
- [ ] Failure Propagation and Reusing Builds / 앞 단계 실패 전파와 성공 빌드 재사용 규칙

## 8. VCS and Branching

- [ ] VCS Root Configuration / 저장소 종류별 접속 정보 설정
- [ ] Branch Specification / 와일드카드로 감시할 브랜치를 지정하는 식
- [ ] Feature Branch Builds / 기본 브랜치 외 기능 브랜치도 자동 빌드하는 기능
- [ ] Pull Request Build Feature / PR을 감지해 따로 빌드하는 기능
- [ ] Commit Status Publisher / 빌드 결과를 커밋 상태로 되돌려 쓰는 기능
- [ ] Checkout Mode / 체크아웃을 에이전트나 서버 중 어디서 할지
- [ ] Checkout Rules / 체크아웃할 파일·경로를 제한하는 규칙

## 9. Build Features

- [ ] Failure Conditions / 지표나 로그 문구로 실패를 판정하는 조건
- [ ] Docker Support Feature / 빌드 안에서 이미지를 만들고 푸시하는 기능
- [ ] Free Disk Space Requirement / 에이전트 여유 공간 부족 시 막는 조건
- [ ] Agent Requirement Rules / 특정 에이전트 파라미터로 실행을 제한하는 규칙
- [ ] Investigation and Mute / 실패를 담당자에 배정하고 알림을 끄는 처리
- [ ] Notification Rules / 이메일·슬랙으로 결과를 알리는 규칙

---

# PART 3 · Advanced

## 10. Test and Quality

- [ ] Test Reporting / 테스트 프레임워크 결과를 자동 인식하는 기능
- [ ] Flaky Test Detection / 이력을 쌓아 들쭉날쭉한 테스트를 골라내는 기능
- [ ] Test Retry and Muted Tests / 실패 테스트를 재시도하거나 무시로 표시하는 처리
- [ ] Code Coverage / 도구별 커버리지 리포트를 수집하는 기능
- [ ] Code Inspection Runner / 정적 분석 경고를 빌드 결과에 모으는 실행기
- [ ] Duplicates Finder / 중복 코드 구간을 찾아 리포트하는 기능
- [ ] Service Messages / 빌드 스크립트가 서버에 상태를 알리는 프로토콜

## 11. Performance and Caching

- [ ] Dependency Cache / 라이브러리 다운로드를 재사용해 시간을 줄이는 캐시
- [ ] Agent-side Cache Directory / 에이전트에 남겨 다음 빌드가 쓰는 저장소
- [ ] Test Splitting and Parallel Tests / 테스트를 나눠 여러 에이전트가 동시에 도는 기능
- [ ] Agent Pool Sizing / 동시 처리량에 맞춰 에이전트 수를 조절하는 일
- [ ] Clean Checkout Policy / 매번 새로 받을지 기존 작업본을 쓸지 정하는 정책
- [ ] Build Time Analysis / 단계별 소요 시간을 서버가 축적한 통계

## 12. Kotlin DSL

- [ ] Versioned Settings / UI 설정을 저장소 코드로 동기화하는 기능
- [ ] DSL Structure / project·buildType 등으로 나뉜 코드 구조
- [ ] DSL Generation from UI / UI 폼으로 만든 설정을 코드로 내보내는 기능
- [ ] Portable vs Non-portable DSL / 버전 고정 여부로 갈리는 두 DSL 방식
- [ ] Reusable DSL Libraries / 여러 프로젝트가 같이 쓰는 DSL 공용 코드
- [ ] DSL Review Workflow / 코드로 바뀐 설정을 PR로 검토하는 절차

---

# PART 4 · Deployment and Operations

## 13. Deployment

- [ ] Deployment Build Configuration / 환경에 실제로 올리는 단계를 담은 설정
- [ ] Environment Promotion Chain / 스테이징을 거쳐 운영으로 올리는 순서
- [ ] Manual Run and Approval / 사람이 승인해야 실행되는 배포 단계
- [ ] Docker Registry Push / Docker 러너로 이미지를 레지스트리에 올리는 단계
- [ ] SSH Upload and Deploy Runner / SSH로 서버에 파일을 올리는 실행기
- [ ] Kubernetes Deploy / 클러스터에 매니페스트를 적용하는 배포 단계
- [ ] Deployment Dashboard / 환경별 배포 현황을 한눈에 보는 화면

## 14. Cloud Agents `선택`

- [ ] Cloud Profile / 클라우드에서 에이전트 띄울 방식을 정의하는 프로필
- [ ] AWS EC2 and Kubernetes Agent Cloud / 클라우드별 에이전트 자동 생성 연동
- [ ] Agent Image Preparation / 에이전트 이미지에 도구를 미리 심는 작업
- [ ] Autoscaling and Idle Timeout / 부하 따라 늘리고 유휴 시 줄이는 설정

## 15. Administration

### Server Operations

- [ ] Backup and Restore / 설정과 데이터를 백업·복구하는 절차
- [ ] Upgrade Path / 버전을 순서대로 올려야 하는 업그레이드 경로
- [ ] Clean-up Rules / 오래된 빌드·산출물을 지우는 보관 규칙
- [ ] Disk Usage Monitoring / 서버·에이전트 디스크 사용량을 감시하는 기능
- [ ] Server Health Report / 서버 상태 이상을 모아 보여주는 리포트
- [ ] Diagnostics / 스레드 덤프로 서버 문제를 진단하는 기능

### Access Control

- [ ] User and Group Management / 사용자를 그룹으로 묶어 관리하는 기능
- [ ] Roles and Permissions / 그룹에 부여할 권한 묶음을 정의하는 역할
- [ ] Authentication Modules / LDAP·OAuth 등 외부 인증 연동
- [ ] Audit Log / 누가 무엇을 바꿨는지 남기는 감사 로그
- [ ] Access Tokens / UI 로그인 없이 API를 쓰는 인증 토큰
- [ ] Secure Token Storage / 저장된 비밀값을 암호화해 보관하는 방식

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Git · GitHub Actions `software/skill-based/Infra-DevOps/git-github.md`
- Kotlin 문법 `software/skill-based/Languages/kotlin.md`
- 컨테이너 · 클러스터 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
- 서버 운영 `software/skill-based/Infra-DevOps/linux.md`
- 테스트 전략 `software/role-based/qa.md`
