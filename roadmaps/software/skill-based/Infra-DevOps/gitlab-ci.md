# GitLab CI/CD `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with GitLab CI

## 1. What is GitLab CI/CD?

### Overview

- [ ] Built-in CI/CD of GitLab / 별도 설치 없이 저장소에 포함된 기능
- [ ] .gitlab-ci.yml / 파이프라인 전체를 정의하는 설정 파일
- [ ] Runner-based Execution / Runner가 실제 job을 실행하는 구조
- [ ] Single Application and DevOps Platform / 기획부터 배포까지 한 제품에서 처리

### Core Use Cases

- [ ] Build and Test Automation / 빌드와 테스트를 파이프라인으로 자동화
- [ ] Container Image Build / 이미지를 빌드해 레지스트리에 올리는 job
- [ ] Release Automation / 태그 push로 릴리스를 자동 생성하는 기능
- [ ] Auto DevOps / 설정 없이 빌드·테스트·배포를 자동 구성

### Comparison with Other Tools

- [ ] GitLab CI vs GitHub Actions / 저장소 내장형과 외부 연동형의 차이
- [ ] GitLab CI vs Jenkins / 관리형 플랫폼과 자체 구축형의 차이
- [ ] SaaS vs Self-managed GitLab / 호스팅 주체로 갈리는 배포 형태

## 2. Getting Started

- [ ] First Pipeline / 설정 파일을 커밋해 처음 돌리는 파이프라인
- [ ] Pipeline, Stage, Job / CI 실행을 나누는 세 단위
- [ ] Pipeline Graph and Job Log UI / job 순서와 실행 로그를 보는 화면
- [ ] Pipeline Editor and CI Lint / 웹에서 yml을 고치고 문법을 검사하는 도구
- [ ] Project CI/CD Settings / 프로젝트별 CI/CD 옵션을 관리하는 화면

## 3. Runners

### Runner Scope `택 1`

- [ ] Instance and Shared Runner / 모든 프로젝트가 공유하는 러너 `추천`
- [ ] Group Runner / 그룹 내 프로젝트가 공유하는 러너
- [ ] Project Runner / 프로젝트 하나에 전용으로 붙는 러너

### Executor `택 1`

- [ ] Docker Executor / 컨테이너 안에서 job을 실행하는 방식 `추천`
- [ ] Shell Executor / 호스트 셸에서 직접 job을 실행하는 방식
- [ ] Kubernetes Executor / 파드를 띄워 job을 실행하는 방식
- [ ] Autoscaling Executor / 부하에 맞춰 러너 수를 늘리고 줄이는 방식

### Registration and Operations

- [ ] Runner Registration and Authentication Token / 등록 토큰으로 러너를 프로젝트에 연결
- [ ] Tags and Job Routing / 태그로 job을 맞는 러너에 보내는 방식
- [ ] Concurrency and Limits / 러너가 동시에 처리할 job 수 제한
- [ ] Runner Cache Configuration / 러너에 캐시 저장 경로를 지정하는 설정

## 4. Config File Structure

- [ ] Job Definition / script·stage·image로 job을 정의하는 문법
- [ ] Global Keywords / 파이프라인 전체에 적용되는 공통 설정
- [ ] before_script and after_script / job 앞뒤에 공통 명령을 끼워 넣는 훅
- [ ] Stage Ordering / stage 순서대로 job을 차례로 실행
- [ ] variables Keyword / job에서 쓸 변수를 선언하는 키워드
- [ ] YAML Anchors and !reference / 설정 조각을 다른 곳에서 재사용하는 문법

---

# PART 2 · Writing Pipelines

## 5. Job Control

- [ ] rules / if·changes 조건으로 job 실행 여부를 정하는 문법
- [ ] rules vs only-except / 신형과 구형 조건 문법의 차이
- [ ] when / job이 실행되는 시점을 정하는 키워드
- [ ] allow_failure / job이 실패해도 파이프라인을 계속 진행
- [ ] needs / stage 순서를 건너뛰어 job을 잇는 키워드
- [ ] dependencies / 이전 job의 아티팩트를 받을 대상 지정
- [ ] interruptible / 새 커밋이 오면 이전 파이프라인을 자동 취소
- [ ] resource_group / 같은 자원 쓰는 job이 겹치지 않게 막는 설정

## 6. Variables and Secrets

- [ ] Predefined Variables / GitLab이 자동으로 채워 주는 변수
- [ ] Project, Group, Instance Variables / 범위별로 나눠 등록하는 변수
- [ ] Protected and Masked Variables / 보호 브랜치 전용·로그 은닉 변수
- [ ] File-type Variables / 값을 파일로 주입하는 변수
- [ ] Environment-scoped Variables / environment별로 값이 달라지는 변수
- [ ] CI/CD Job Token / job이 프로젝트 API를 호출하는 인증 토큰
- [ ] External Secrets / 외부 저장소에서 시크릿을 가져오는 연동

## 7. Artifacts and Cache

- [ ] artifacts / job 결과물을 보관하고 만료를 정하는 설정
- [ ] Artifact Reports / 테스트·커버리지 결과를 UI에 붙이는 형식
- [ ] cache / 의존성을 job 사이에 재사용하는 설정
- [ ] Cache vs Artifact / 재사용 목적과 산출물 보관 목적의 차이
- [ ] Distributed Cache / 캐시를 외부 저장소로 러너 간 공유
- [ ] Passing Data Between Jobs / artifact로 job 사이에 값을 넘기는 방법

## 8. Advanced Pipeline Structure

- [ ] parallel and parallel:matrix / job을 값 조합별로 나눠 병렬 실행
- [ ] Child Pipelines / trigger로 하위 파이프라인을 불러와 실행
- [ ] Multi-project Pipelines / 다른 프로젝트 파이프라인을 연쇄 실행
- [ ] strategy:depend / 부모가 자식 파이프라인 결과를 기다리게 함
- [ ] Merge Request Pipelines / MR에서만 도는 전용 파이프라인
- [ ] Merged Results and Merge Trains / 머지 전에 결과를 미리 검증하는 큐
- [ ] Scheduled Pipelines / 정해진 주기로 자동 실행되는 파이프라인
- [ ] Tag and Release Pipelines / 태그 push로 트리거되는 파이프라인

## 9. Reuse and Templates

- [ ] include / 다른 yml 파일을 불러와 합치는 키워드
- [ ] extends Keyword / job 설정을 다른 job에서 물려받는 키워드
- [ ] CI/CD Components / 카탈로그에서 재사용 가능한 설정 단위
- [ ] Template Repository Pattern / 공통 설정을 별도 저장소로 분리
- [ ] Compliance Pipelines / 그룹 전체에 강제로 끼워 넣는 파이프라인

---

# PART 3 · Deployment

## 10. Environments and Deployment

- [ ] environment Keyword / 배포 대상에 이름을 붙이는 키워드
- [ ] Deployment History / environment별로 쌓이는 배포 이력
- [ ] Review Apps / MR마다 임시로 띄우는 환경
- [ ] stop Job / 환경을 정지시키는 전용 job
- [ ] Protected Environments / 배포 전에 승인을 요구하는 환경
- [ ] Deployment Strategies / 트래픽을 점진적으로 옮기는 배포 방식
- [ ] Rollback / 이전 배포를 environment에서 다시 실행

## 11. Container and Registry

- [ ] GitLab Container Registry / 프로젝트에 딸린 이미지 저장소
- [ ] Docker-in-Docker / 컨테이너 안에서 이미지를 빌드하는 방식
- [ ] Rootless Build / 데몬 권한 없이 이미지를 빌드하는 도구
- [ ] Image Tagging Strategy / 이미지 태그를 커밋·브랜치에 맞춰 규칙화
- [ ] Dependency Proxy / 외부 이미지를 캐싱해 당겨오는 프록시
- [ ] Package Registry / 빌드 산출 패키지를 저장하는 저장소

## 12. Kubernetes Integration `선택`

- [ ] GitLab Agent for Kubernetes / 클러스터에 상주하며 배포를 받는 에이전트
- [ ] Pull-based GitOps Workflow / 클러스터가 저장소 상태를 당겨가는 배포
- [ ] Auto DevOps / 클러스터까지 자동으로 배포를 구성하는 템플릿
- [ ] Helm Deploy Job / Helm 차트로 클러스터에 배포하는 job

---

# PART 4 · Security and Operations

## 13. Security and Compliance

- [ ] SAST and DAST / 코드와 실행 중인 앱을 각각 스캔하는 검사
- [ ] Dependency Scanning / 라이브러리 취약점을 찾는 검사
- [ ] Container Scanning / 이미지 안 취약점을 찾는 검사
- [ ] Secret Detection / 커밋에 섞인 키·토큰을 찾는 검사
- [ ] License Compliance / 의존성 라이선스를 점검하는 검사
- [ ] Security Dashboard and MR Widget / 스캔 결과를 대시보드와 MR에 노출
- [ ] Protected Branches and Tags / 보호된 브랜치·태그에만 push 제한

## 14. Operations

### Performance Optimization

- [ ] Job Duration Analysis / job별 소요 시간을 비교해 병목 찾기
- [ ] Runner Sizing / 러너 사양과 동시 실행 수를 맞추는 일
- [ ] Cache Hit Optimization / 캐시 키를 다듬어 적중률을 높이는 일
- [ ] Fail Fast Ordering / 빨리 실패하는 job을 앞 stage로 배치

### Observability and Management

- [ ] Pipeline Analytics / 배포 빈도·리드타임 등을 측정하는 지표
- [ ] Job Log Retention and Artifact Cleanup / 오래된 로그와 아티팩트를 정리하는 정책
- [ ] Debugging / 변수로 job 실행을 상세히 추적하는 법
- [ ] Pipeline Notifications / 파이프라인 결과를 외부로 알리는 설정
- [ ] Compute Quota / 계정에 할당된 실행 시간 한도

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Git · GitHub Actions `software/skill-based/Infra-DevOps/git-github.md`
- 컨테이너 이미지 `software/skill-based/Infra-DevOps/docker.md`
- 배포 대상 클러스터 `software/skill-based/Infra-DevOps/kubernetes.md`
- 인프라 코드화 `software/skill-based/Infra-DevOps/terraform.md`
- 보안 파이프라인 `software/role-based/devsecops.md`
