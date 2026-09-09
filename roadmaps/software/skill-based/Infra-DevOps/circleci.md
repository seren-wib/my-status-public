# CircleCI `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to CircleCI

## 1. What is CircleCI?

### CI/CD Basic Concepts

- [ ] Continuous Integration / 변경을 자주 합쳐 자동으로 검증하는 관행
- [ ] Continuous Delivery and Deployment / 배포 직전 혹은 배포까지 자동화하는 범위
- [ ] Build-Test-Deploy Pipeline / 빌드·테스트·배포를 잇는 표준 흐름
- [ ] Fail Fast and Feedback Loop / 실패를 빨리 드러내 기다림을 줄이는 원칙

### CircleCI Characteristics

- [ ] Cloud-hosted SaaS / 서버를 직접 두지 않고 쓰는 호스팅 방식
- [ ] Container-based Execution / 매 job을 컨테이너로 격리해 돌리는 방식
- [ ] Config as Code / 파이프라인 정의를 코드로 저장소에 커밋하는 방식

### Comparison with Other Tools

- [ ] CircleCI vs Jenkins / 서버를 직접 관리 않는 대신 자유도가 낮은 차이
- [ ] CircleCI vs GitHub Actions / 실행 환경 선택 폭과 과금 방식의 차이
- [ ] CircleCI vs GitLab CI / 저장소 결합도와 config 문법의 차이
- [ ] When to choose CircleCI? / 실행 환경 다양성과 비용을 저울질하는 기준

## 2. Getting Started

### Project Connection

- [ ] VCS Integration / 저장소를 연결해 커밋마다 파이프라인을 트리거하는 설정
- [ ] Organization and Project Setup / 조직과 프로젝트를 만들어 등록하는 단계
- [ ] First Pipeline Run / 연결 뒤 처음 자동으로 도는 파이프라인

### Interface

- [ ] Pipelines Dashboard / 실행 이력을 목록으로 모아 보는 화면
- [ ] Job and Step Output / 잡·스텝 단위로 나눠 보는 로그 화면
- [ ] Rerun and Rerun with SSH / 그대로 재실행하거나 SSH로 붙는 재실행

### CLI

- [ ] circleci CLI Install / 로컬에서 config를 다루는 명령줄 도구 설치
- [ ] config validate / 로컬에서 yml 문법 오류를 미리 잡는 검사
- [ ] local execute / job을 로컬 컨테이너에서 미리 실행하는 기능

## 3. Config File Basics

- [ ] YAML Syntax / 반복되는 값을 앵커·별칭으로 재사용하는 문법
- [ ] Config Structure / config.yml을 이루는 최상위 구성 요소
- [ ] Job, Steps, Commands / 잡 안에서 스텝과 커맨드가 겹치는 구조
- [ ] Built-in Steps / run·checkout처럼 미리 제공되는 스텝
- [ ] Working Directory / 커맨드가 실행되는 기준 경로
- [ ] Shell and Multi-line Commands / 여러 줄 스크립트를 한 스텝에 넣는 방법

---

# PART 2 · Runtime Environment and Workflows

## 4. Executors

### Runtime Environment `택 1`

- [ ] Docker Executor / 컨테이너 이미지 위에서 job을 돌리는 실행기 `추천`
- [ ] Machine Executor / 가상 머신 전체를 통째로 빌려 쓰는 실행기
- [ ] macOS Executor / 맥 빌드·서명이 필요할 때 쓰는 실행기
- [ ] Windows Executor / 윈도 전용 빌드에 쓰는 실행기
- [ ] Arm Executor / Arm 아키텍처 바이너리를 빌드하는 실행기

### Docker Execution Details

- [ ] Primary Container and Service Containers / 실행 컨테이너와 옆에 붙는 보조 컨테이너 구분
- [ ] Convenience Images / 언어별 의존성을 미리 깐 CircleCI 공식 이미지
- [ ] Custom Image and Registry Authentication / 사설 이미지를 쓸 때 레지스트리에 인증하는 절차
- [ ] Resource Class / job에 배정할 CPU·메모리 크기 등급

## 5. Workflows

- [ ] Workflow Definition / job들을 requires로 엮어 순서를 정의하는 층
- [ ] Sequential vs Parallel Jobs / job을 순서대로 돌리느냐 동시에 돌리느냐의 차이
- [ ] Fan-in and Fan-out / 여러 job이 하나로 모이거나 갈라지는 구조
- [ ] Job Filters / 브랜치·태그 조건으로 job 실행을 거르는 규칙
- [ ] Scheduled Pipelines / 정해진 시각에 자동으로 도는 파이프라인
- [ ] Manual Approval Job / 사람이 승인해야 다음으로 넘어가는 job
- [ ] Rerun from Failed Job / 실패한 job부터만 다시 돌리는 재실행

## 6. Contexts and Variables

- [ ] Built-in Environment Variables / 브랜치·커밋 정보를 담아 자동으로 주는 변수
- [ ] Project Environment Variables / 프로젝트 단위로 등록해 두는 비밀·설정값
- [ ] Contexts / 여러 프로젝트가 같이 쓰는 비밀값 묶음
- [ ] Context Restriction by Security Group / 특정 그룹만 context를 쓰게 막는 제한
- [ ] Secret Masking / 로그에 비밀값이 찍히면 자동으로 가리는 기능
- [ ] Parameters / 파이프라인·job 실행 시 값을 넘기는 매개변수

## 7. Caching and Workspaces

- [ ] Dependency Caching / 의존성을 저장했다 다음 job에서 되살리는 기능
- [ ] Cache Key Strategy / 체크섬으로 캐시가 유효한지 정하는 키 전략
- [ ] Partial Cache Restore / 정확히 안 맞아도 비슷한 캐시를 받아오는 방식
- [ ] Workspaces / 뒤 job에 파일을 넘기는 잡 사이 통로
- [ ] Artifacts / 빌드 결과물을 실행 뒤에도 내려받게 남기는 기능
- [ ] Cache vs Workspace vs Artifact / 재사용·전달·보관 목적이 갈리는 세 저장 방식

---

# PART 3 · Advanced

## 8. Test Optimization

- [ ] Test Splitting / 테스트를 여러 컨테이너에 나눠 돌리는 기능
- [ ] Split Strategy / 실행 시간·이름·크기 중 무엇으로 나눌지 정하는 기준
- [ ] Parallelism / 같은 job을 여러 컨테이너로 동시에 돌리는 수
- [ ] Test Results / 테스트 리포트를 모아 인사이트에 반영하는 기능
- [ ] Flaky Test Detection / 같은 코드인데 성공·실패가 오가는 테스트 검출
- [ ] Test Insights / 테스트 소요 시간과 성공률 추세를 보는 화면

## 9. Orbs

- [ ] What is an Orb? / 설정 조각을 패키지로 묶어 공유하는 단위
- [ ] Orb Registry / 공식·파트너·커뮤니티로 나뉘는 Orb 배포처
- [ ] Using Orbs / Orb가 주는 커맨드·job·실행기를 불러쓰는 법
- [ ] Common Orbs / 자주 쓰는 클라우드·언어·알림 Orb 예시
- [ ] Authoring an Orb / 재사용할 설정 조각을 직접 만드는 작업
- [ ] Orb Publishing and Semantic Versioning / 버전 규칙을 정해 Orb를 레지스트리에 올리는 절차
- [ ] Orb Development Kit / Orb를 로컬에서 검증·테스트하는 도구 모음

## 10. Dynamic Configuration

- [ ] Setup Workflow / 본 파이프라인 전에 설정만 만드는 예비 워크플로
- [ ] continuation Orb / 생성한 설정을 이어받아 실행하는 전용 Orb
- [ ] Path Filtering and Monorepo / 바뀐 경로만 보고 돌릴 job을 고르는 방식
- [ ] Generating Config at Runtime / 파이프라인 실행 중 config를 새로 만들어 내는 방식
- [ ] Pipeline Values / 파이프라인이 실행될 때 자동으로 채워지는 값

---

# PART 4 · Deployment and Operations

## 11. Deployment

- [ ] Deploy Job Pattern / 배포만 맡는 job을 워크플로 끝에 두는 구조
- [ ] Environment Separation / dev·staging·prod로 배포 대상을 나누는 구성
- [ ] Approval Gate before Production / 운영 배포 직전에 사람 승인을 두는 관문
- [ ] Deployment Strategies / 전환 위험을 줄이며 배포하는 여러 전략
- [ ] Container Registry Push / job 안에서 이미지를 빌드해 레지스트리로 올리는 단계
- [ ] Kubernetes Deploy / 빌드한 이미지를 클러스터에 반영하는 배포
- [ ] Serverless Deploy / 함수 코드를 서버리스 플랫폼에 올리는 배포
- [ ] Rollback Strategy / 배포 실패 시 이전 버전으로 되돌리는 전략

## 12. Security

- [ ] Secrets Management / API 키·비밀번호를 안전하게 보관·주입하는 체계
- [ ] OIDC Token / 고정 키 없이 클라우드에 인증하는 단기 토큰
- [ ] Restricted Contexts / 지정한 그룹만 쓸 수 있게 막은 context
- [ ] Forked PR Builds / 외부 포크의 PR도 검증할지 정하는 정책
- [ ] Third-party Orb Review / 남이 만든 Orb를 쓰기 전에 내용을 검토하는 절차
- [ ] Audit Logs / 조직 안 설정 변경 이력을 남기는 로그
- [ ] Dependency and Container Scanning / 의존성과 이미지의 취약점을 훑는 검사

## 13. Self-hosted Runners `선택`

- [ ] When to use Self-hosted Runners? / 관리형 실행기 대신 직접 둔 러너가 필요한 경우
- [ ] Container Runner / 컨테이너 단위로 job을 받는 자체 러너
- [ ] Machine Runner / VM 단위로 job을 받는 자체 러너
- [ ] Runner Namespace and Resource Class / 러너를 묶고 크기를 정해 job에 배정하는 단위
- [ ] Runner Scaling / 대기열 길이에 맞춰 러너 수를 늘리는 방식

## 14. Operations

### Troubleshooting

- [ ] Debug with SSH / 실패한 job에 SSH로 붙어 상태를 들여다보는 기능
- [ ] Common Failure / 캐시 불일치·자원 부족 등 자주 나는 실패 유형
- [ ] Step Timeout / 출력이 멈춘 스텝을 끊어내는 제한 시간
- [ ] Log Analysis / 빌드 로그에서 실패 원인을 찾아내는 작업

### Cost and Performance

- [ ] Credit Usage / 리소스 클래스별로 다르게 소모되는 크레딧 양
- [ ] Build Time Optimization / 캐시·병렬화로 빌드 소요 시간을 줄이는 작업
- [ ] Insights Dashboard / 소요 시간·성공률 추세를 모아 보는 화면
- [ ] Concurrency Limits / 플랜별로 동시에 돌릴 수 있는 job 상한
- [ ] Notifications / 빌드 결과를 Slack·메일 등으로 알리는 기능

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Git · GitHub Actions `software/skill-based/Infra-DevOps/git-github.md`
- 컨테이너 이미지 `software/skill-based/Infra-DevOps/docker.md`
- 배포 대상 클러스터 `software/skill-based/Infra-DevOps/kubernetes.md`
- 인프라 코드화 `software/skill-based/Infra-DevOps/terraform.md`
- 파이프라인 보안 `software/role-based/devsecops.md`
