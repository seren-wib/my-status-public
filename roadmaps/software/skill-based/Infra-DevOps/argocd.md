# Argo CD `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to GitOps and Argo CD

## 1. GitOps Fundamentals

- [ ] Declarative Infrastructure / 원하는 결과 상태만 선언해 정의하는 방식
- [ ] Git as Single Source of Truth / 배포할 상태의 유일한 기준을 Git으로 두는 원칙
- [ ] Pull-based vs Push-based Deployment / 클러스터가 당겨오는지 외부가 밀어넣는지 구분
- [ ] Continuous Reconciliation / 목표 상태와 실제 상태를 끊임없이 맞추는 루프
- [ ] Drift Detection / Git과 클러스터 실물이 어긋난 걸 잡아내는 기능

### Separation of CI and CD

- [ ] CI Builds Image and CD Syncs Manifest / 이미지 빌드와 배포 반영을 역할로 분리하는 구조
- [ ] App Repo vs Config Repo / 앱 코드와 배포 매니페스트를 저장소로 분리하는 구조
- [ ] Image Update Automation / 새 이미지 태그를 Git에 자동으로 커밋하는 기능

## 2. What is Argo CD?

- [ ] Kubernetes-native CD Controller / 쿠버네티스 컨트롤러로 동작하는 배포 방식
- [ ] Declarative Application Delivery / 앱 배포 자체를 선언형 리소스로 다루는 방식
- [ ] Sync and Health Status Model / 동기화 여부와 헬스 상태를 별도 축으로 보는 모델
- [ ] Web UI · CLI · API / 같은 기능을 세 통로로 제공하는 구조

### Comparison with Other Tools

- [ ] Argo CD vs Flux / UI와 멀티테넌시 모델이 갈리는 GitOps 비교
- [ ] Argo CD vs Push-based CD / 당겨오는 방식과 밀어넣는 방식의 근본 차이
- [ ] When to choose Argo CD? / 조정 루프가 맞는 상황을 가리는 판단 기준

## 3. Getting Started

### Installation `택 1`

- [ ] Manifest Install / 공식 매니페스트를 그대로 적용하는 설치법 `추천`
- [ ] Helm Chart / 차트 값으로 설정을 조정하며 설치하는 방법
- [ ] Argo CD Operator / 오퍼레이터가 설치·업그레이드를 대신 관리하는 방식
- [ ] HA Install / 컴포넌트를 다중화해 장애에 대비하는 설치 구성

### Access

- [ ] argocd CLI Login / CLI에서 API 서버로 인증하는 절차
- [ ] Initial Admin Password / 최초 admin 비밀번호가 저장되는 시크릿 위치
- [ ] UI Access / 포트포워딩이나 Ingress로 접속하는 경로
- [ ] First Application Creation / 첫 Application 등록으로 배포를 시작하는 절차

## 4. Architecture

- [ ] API Server / CLI·UI 요청을 받아 처리하는 관문 컴포넌트
- [ ] Repo Server / Git에서 매니페스트를 내려받아 렌더링하는 컴포넌트
- [ ] Application Controller / 목표 상태와 실제 상태를 비교하는 핵심 컨트롤러
- [ ] Redis Cache / 클러스터 상태를 캐싱해 API 부하를 줄이는 컴포넌트
- [ ] ApplicationSet Controller / 여러 Application을 자동 생성하는 컴포넌트
- [ ] Dex / 외부 인증을 연동해 SSO를 처리하는 컴포넌트
- [ ] Reconciliation Loop / 목표 상태와 실제 상태를 맞추는 핵심 제어 루프

---

# PART 2 · Application Management

## 5. Application CRD

- [ ] Application Spec / 소스·대상·프로젝트를 정의하는 스펙
- [ ] Target Revision / 추적할 브랜치·태그·커밋 지정 값
- [ ] Source Path / 저장소 안 매니페스트가 있는 하위 경로
- [ ] Destination Cluster / 배포될 클러스터와 네임스페이스 지정 값
- [ ] App of Apps Pattern / 상위 Application으로 여러 앱을 묶어 관리하는 구조
- [ ] Declarative vs UI-created App / YAML로 선언했는지 UI로 만들었는지 차이

## 6. Manifest Sources

### Rendering Method `택 1`

- [ ] Kustomize / 오버레이로 원본 수정 없이 값만 바꾸는 방식 `추천`
- [ ] Helm / 템플릿과 값 파일을 조합해 렌더링하는 방식
- [ ] Plain YAML Directory / 가공 없이 YAML 파일을 그대로 적용하는 방식
- [ ] Jsonnet / 코드처럼 매니페스트를 생성하는 프로그래밍형 방식

### Source Configuration

- [ ] Helm Values / values 파일이나 파라미터로 주입하는 값
- [ ] Kustomize Overlays / 이미지 태그 등을 환경별로 덮어쓰는 값
- [ ] Multiple Sources / 한 Application에 소스 여러 개를 합치는 기능
- [ ] Config Management Plugin / 표준 렌더링 밖 로직을 스크립트로 붙이는 확장 `선택`

## 7. Sync

- [ ] Manual vs Automated Sync / 사람이 누르는지 컨트롤러가 자동으로 맞추는지 차이
- [ ] Sync Policy / 지우기·되돌리기 자동 실행 여부 설정
- [ ] Sync Options / 네임스페이스 생성 등 동기화 세부 옵션
- [ ] Sync Waves / 리소스를 순서대로 나눠 동기화하는 단계
- [ ] Sync Phases / 동기화 전후로 나뉘는 실행 구간
- [ ] Resource Hooks / 특정 Phase에 잡을 끼워 실행하는 훅 리소스
- [ ] Sync Windows / 동기화를 허용하거나 막는 시간대 설정
- [ ] Diff Customization / 특정 필드 차이를 무시하는 설정

## 8. Health and Status

- [ ] Sync Status / Git과 클러스터 일치 여부 판정
- [ ] Health Status / 리소스가 실제로 정상 동작하는지 판정
- [ ] Built-in Health Checks / 리소스 종류별로 내장된 정상 판정 로직
- [ ] Custom Health Check / Lua 스크립트로 짜는 판정 로직
- [ ] Resource Tree View / 배포된 리소스 관계를 트리로 보여주는 화면
- [ ] Application Events and Pod Logs / 문제 원인을 UI에서 바로 확인하는 기능

---

# PART 3 · Multi-Environment and Scaling

## 9. Projects and Multi-tenancy

- [ ] AppProject CRD / 여러 팀의 Application 권한을 나누는 경계 단위
- [ ] Source Repository Whitelist / 프로젝트가 쓸 수 있는 Git 저장소를 제한하는 목록
- [ ] Destination Restriction / 배포 가능한 클러스터와 네임스페이스 제한
- [ ] Cluster and Namespace Resource Whitelist / 허용할 리소스 종류를 제한하는 목록
- [ ] Project Roles / JWT 토큰으로 발급하는 프로젝트 권한
- [ ] Orphaned Resource Monitoring / Git에 없는데 클러스터에 남은 리소스 탐지

## 10. ApplicationSet

- [ ] Generator Overview / 여러 Application을 자동 생성하는 소스 종류 개관
- [ ] List and Cluster Generator / 고정 목록이나 등록된 클러스터로 찍어내는 방식
- [ ] Git Generator / 저장소 디렉터리·파일 목록으로 찍어내는 방식
- [ ] Matrix and Merge Generator / 여러 생성기 결과를 조합하는 방식
- [ ] Pull Request Generator / 열린 PR 목록으로 Application을 만드는 생성기
- [ ] SCM Provider Generator / 조직의 저장소 목록으로 자동 생성하는 방식
- [ ] Template / goTemplate 문법으로 값을 채우는 틀
- [ ] Progressive Sync / 클러스터군에 단계별로 순차 배포하는 전략 `선택`

## 11. Multi-cluster

- [ ] Cluster Registration / 외부 클러스터를 관리 대상으로 등록
- [ ] In-cluster vs External Cluster / Argo CD가 도는 클러스터와 배포 대상 구분
- [ ] Cluster Credential Secret / 대상 클러스터 접속 정보를 담은 시크릿
- [ ] Hub-Spoke Topology / 중앙 하나가 여러 클러스터를 관리하는 구조
- [ ] Environment Promotion Strategy / 같은 변경을 단계별 환경에 순차 반영하는 전략

## 12. Secrets Management `택 1`

- [ ] External Secrets Operator / 외부 저장소 시크릿을 동기화해 오는 방식 `추천`
- [ ] Sealed Secrets / 시크릿을 암호화한 채 Git에 커밋하는 방식
- [ ] SOPS and KSOPS / 파일 일부만 암호화해 저장하는 방식
- [ ] Vault Plugin / Vault에서 시크릿을 실시간으로 가져오는 플러그인
- [ ] No Plaintext Secrets in Git / 원문 시크릿을 저장소에 남기지 않는 원칙

---

# PART 4 · Operations

## 13. Access Control

- [ ] Local Accounts / argocd-cm에 직접 등록하는 자체 계정 방식
- [ ] SSO / OIDC 연동으로 외부 계정을 로그인시키는 방식
- [ ] RBAC Policy / policy.csv로 정의하는 권한 규칙
- [ ] Role and Group Mapping / SSO 그룹을 RBAC 역할에 연결하는 매핑
- [ ] API Tokens / 사람 계정 없이 자동화가 쓰는 인증 토큰
- [ ] Disabling Admin Account / 기본 admin 계정을 잠가 위험을 줄이는 조치

## 14. Progressive Delivery `선택`

- [ ] Argo Rollouts Overview / 카나리아·블루그린을 다루는 별도 컨트롤러 개관
- [ ] Canary and Blue-Green Strategy / 트래픽을 점진적으로 혹은 한 번에 전환하는 전략
- [ ] Analysis Template / 지표로 배포 성공 여부를 자동 판단
- [ ] Traffic Management / Ingress나 메시로 트래픽 비율 조정

## 15. Operations

### Configuration and Extension

- [ ] argocd-cm and argocd-cmd-params-cm / Argo CD 동작을 바꾸는 두 핵심 설정 맵
- [ ] Resource Inclusion and Exclusion / 특정 리소스 종류를 감시 대상에서 빼는 설정
- [ ] Repository Credentials / 저장소 접근 인증 방식 등록
- [ ] Webhook Configuration / Git push를 폴링 대신 즉시 알리는 설정

### Monitoring and Troubleshooting

- [ ] Prometheus Metrics / Sync·Health 지표를 외부로 노출하는 기능
- [ ] Notifications Controller / 상태 변화를 Slack 등으로 알리는 컨트롤러
- [ ] Common Issues / 계속 어긋나거나 멈춘 동기화 장애 패턴
- [ ] Performance Tuning / 샤딩과 점검 주기로 부하 조절
- [ ] Disaster Recovery / 전체 상태를 내보내고 복원하는 절차
- [ ] Upgrade Strategy / 버전을 올릴 때 순서와 호환성을 챙기는 전략

---

# 이 로드맵 밖

- 쿠버네티스 기초 `software/skill-based/Infra-DevOps/kubernetes.md`
- 컨테이너 이미지 `software/skill-based/Infra-DevOps/docker.md`
- 데브옵스 전반 `software/role-based/devops.md`
- Git 브랜치 전략 `software/skill-based/Infra-DevOps/git-github.md`
- 인프라 코드화 `software/skill-based/Infra-DevOps/terraform.md`
- 배포 보안 `software/role-based/devsecops.md`
