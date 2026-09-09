# Jenkins `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Jenkins

## 1. What is Jenkins?

- [ ] Open-source Automation Server / 소스를 열어 무료로 쓰는 자동화 서버
- [ ] Build, Test, Deploy Automation / 빌드·테스트·배포를 하나로 잇는 자동화
- [ ] Plugin-based Architecture / 없는 기능을 플러그인으로 조립하는 구조
- [ ] Self-hosted and On-premise / 내가 서버를 직접 관리하는 배포 형태

### Use Cases

- [ ] CI/CD Pipeline / 커밋마다 빌드·테스트·배포를 잇는 흐름
- [ ] Scheduled and Batch Automation / 정해진 시각에 반복 실행하는 작업
- [ ] Legacy · Regulated Environment / 폐쇄망·규제망에서 쓰는 운용 방식

### Comparison with Other Tools

- [ ] Jenkins vs GitHub Actions / 서버 소유 대 SaaS 관리형의 차이
- [ ] Jenkins vs GitLab CI / 플러그인 조립 대 내장 기능의 차이
- [ ] When to choose Jenkins? / 통제권과 커스터마이징이 필요할 때

## 2. Installation and Setup

### Installation `택 1`

- Docker / 컨테이너로 띄워 격리해 운영하는 방법 `software/skill-based/Infra-DevOps/docker.md` `추천` `위임`
- [ ] WAR File and Servlet Container / 톰캣 같은 서블릿 컨테이너에 얹는 방법
- [ ] Package Manager / apt·yum으로 설치해 OS 서비스로 올리는 방법
- [ ] Kubernetes Helm Chart / 클러스터에 차트로 배포하는 방법

### Initial Configuration

- [ ] Unlock Jenkins / 파일에 찍힌 최초 관리자 비밀번호로 여는 절차
- [ ] Suggested Plugins / 설치 시 고르는 권장 플러그인 묶음
- [ ] JENKINS_HOME Layout / 설정·잡·빌드가 쌓이는 디렉터리 구조
- [ ] Java Version Requirement / 컨트롤러 구동에 맞춰야 할 JDK 버전
- [ ] Reverse Proxy and HTTPS / 앞단에 프록시를 둬 인증서를 붙이는 구성

## 3. Jenkins Basics

### UI Structure

- [ ] Dashboard and Views / 잡을 묶어 보여주는 목록 화면
- [ ] Job, Build, Console Output / 잡 실행 단위와 그 실시간 로그
- [ ] Build History and Workspace / 과거 실행 기록과 빌드용 작업 폴더

### Job Types

- [ ] Freestyle Project / UI 클릭으로 단계를 구성하는 잡
- [ ] Pipeline / Jenkinsfile로 단계를 코드로 정의하는 잡
- [ ] Multibranch Pipeline / 브랜치마다 잡을 자동 생성하는 방식
- [ ] Folder and Organization Folder / 잡을 계층으로 묶는 컨테이너

### Basic Concepts

- [ ] Controller and Agent Architecture / 중앙 서버와 실행 노드를 나눈 구조
- [ ] Executor and Build Queue / 노드의 동시 실행 슬롯과 대기열
- [ ] Manage Jenkins Menu / 서버 전역 설정을 모아둔 관리 화면

---

# PART 2 · Pipeline

## 4. Pipeline Fundamentals

### Syntax `택 1`

- [ ] Declarative Pipeline / 정해진 블록 구조로 쓰는 문법 `추천`
- [ ] Scripted Pipeline / Groovy로 자유롭게 짜는 문법

### Structure

- [ ] Pipeline Structure / pipeline·agent·stages·steps로 짜는 뼈대
- [ ] Jenkinsfile in SCM / 파이프라인 정의를 저장소에 함께 두는 방식
- [ ] Snippet Generator and Pipeline Syntax / 스텝 문법을 클릭으로 생성해주는 도구
- [ ] Replay and Restart from Stage / 코드 수정 없이 재실행하거나 중간부터 재개

## 5. Declarative Directives

- [ ] Agent Selection / any·label·docker로 실행 노드를 고르는 지시어
- [ ] Environment Block / 파이프라인 전역에 쓰는 환경변수 선언
- [ ] Parameters / string·choice로 실행 전 값을 받는 선언
- [ ] Options / timeout·retry로 실행 규칙을 거는 블록
- [ ] Triggers / cron·pollSCM으로 자동 시작을 거는 조건
- [ ] Tools / JDK·Maven을 자동 설치해 PATH에 걸어주는 지시어
- [ ] Post Conditions / success·failure 같은 결과별로 거는 후처리
- [ ] when Conditions / branch·changeset으로 스테이지를 건너뛰는 조건
- [ ] input and Manual Approval / 사람의 승인을 기다려 멈추는 단계

## 6. Steps and Scripting

- [ ] Common Steps / sh·bat·checkout 같은 기본 실행 단위
- [ ] script Block / 선언형 안에 Groovy 로직을 끼워 넣는 블록
- [ ] Error Handling / catchError로 실패를 잡아 빌드 상태를 정하는 법
- [ ] Parallel Stages / 여러 스테이지를 동시에 실행하는 구조
- [ ] Matrix Directive / axes로 조합을 펼쳐 병렬 실행하는 지시어
- [ ] Sequential Stages inside parallel / 병렬 가지 안에서 순서를 강제하는 중첩
- [ ] Timeouts and Retries / 단계별 제한 시간과 재시도 횟수 지정

## 7. Credentials in Pipeline

- [ ] Credentials Store / 자격증명을 범위와 도메인별로 나눠 담는 저장소
- [ ] Credential Types / 비밀번호·SSH 키·시크릿 파일로 나뉘는 저장 형식
- [ ] withCredentials Binding / 스텝 범위에서만 자격증명을 노출하는 바인딩
- [ ] credentials() Helper in environment / 환경변수 블록에서 자격증명을 끌어오는 함수
- [ ] Secret Masking in Logs / 콘솔 출력에서 비밀값을 가려주는 기능

---

# PART 3 · Extensions

## 8. Agents and Distributed Builds

- [ ] Agent Connection / SSH로 밀거나 JNLP로 붙게 하는 연결 방식
- [ ] Node Labels and Label Expression / 노드를 태그로 골라 잡을 배정하는 식
- [ ] Static vs Ephemeral Agents / 상시 대기 노드와 필요 시 생성되는 노드
- [ ] Docker Agent / 컨테이너를 에이전트로 즉석에서 띄우는 방식
- [ ] Kubernetes Plugin and Pod Templates / 파드를 에이전트 템플릿으로 정의하는 플러그인
- [ ] Cloud Agents / 클라우드 VM을 띄워 에이전트로 쓰는 구성
- [ ] Agent Sizing and Executor Count / 노드마다 동시 실행 슬롯 수를 정하는 일

## 9. Shared Libraries

- [ ] Library Structure / vars·src·resources로 정해진 폴더 구성
- [ ] Global vs Folder-level Library / 전역으로 쓸지 폴더 범위로 한정할지
- [ ] @Library Annotation and Versioning / 파이프라인에서 라이브러리 버전을 불러오는 표기
- [ ] Custom Steps and Global Variables / vars에 정의해 스텝처럼 쓰는 함수
- [ ] Groovy Classes in src / 로직을 클래스로 분리해 재사용하는 방식
- [ ] Testing / 공유 라이브러리를 단위 테스트로 검증하는 방법

## 10. Plugins

- [ ] Plugin Manager / 플러그인을 설치하고 버전을 갱신하는 화면
- [ ] Essential Plugins / 어느 구성에나 먼저 깔고 시작하는 플러그인 묶음
- [ ] Reporting Plugins / 테스트·정적분석 결과를 화면에 모아 주는 플러그인
- [ ] Notification Plugins / 빌드 결과를 슬랙·메일로 내보내는 플러그인
- [ ] Plugin Dependency and Compatibility Risk / 플러그인 간 의존과 버전 충돌 위험
- [ ] Plugin Security Advisories / 알려진 플러그인 취약점 공지

## 11. Configuration as Code

- [ ] JCasC / UI 설정을 YAML 한 장으로 되돌리는 플러그인
- [ ] casc.yaml Structure / JCasC가 읽어들이는 설정 파일 구조
- [ ] Job DSL Plugin / 잡 정의 자체를 코드로 생성하는 플러그인
- [ ] Seed Job Pattern / DSL 잡을 실행해 다른 잡을 만들어내는 패턴
- [ ] Immutable Jenkins Image / 설정을 이미지에 굳혀 매번 새로 띄우는 방식

---

# PART 4 · Deployment and Operations

## 12. Artifacts and Reporting

- [ ] archiveArtifacts / 빌드 산출물을 컨트롤러에 보관하는 스텝
- [ ] stash and unstash / 같은 빌드 안에서 파일을 스테이지 간 전달
- [ ] Test Report Publishing / 테스트 결과 XML을 모아 화면에 집계하는 스텝
- [ ] Code Coverage Report / 커버리지 결과를 빌드 화면에 표시
- [ ] Build Status Badge / 빌드 상태를 외부 화면에 보여주는 배지
- [ ] Artifact Repository / 산출물을 컨트롤러 밖 저장소에 넘겨 두는 곳

## 13. Deployment

- [ ] Deploy Stage Pattern / 배포를 파이프라인 마지막 단계로 두는 구성
- [ ] Environment Promotion / 같은 산출물을 dev에서 prod로 승격시키는 흐름
- [ ] Manual Approval Gate / 배포 직전 사람 승인을 강제하는 관문
- [ ] Container Build and Push / 이미지를 빌드해 레지스트리로 올리는 단계
- [ ] Kubernetes and Helm Deploy / 클러스터에 차트로 배포하는 단계
- [ ] Blue-Green and Canary Release / 무중단·점진 전환으로 배포하는 전략
- [ ] Rollback Handling / 배포 실패 시 이전 버전으로 되돌리는 처리

## 14. Administration

### Operations Management

- [ ] Backup / JENKINS_HOME을 통째로 떠 두는 대상과 주기
- [ ] Upgrade Strategy and LTS Line / 안정 버전 계열을 따라가는 업그레이드 방침
- [ ] Workspace Cleanup and Disk Usage / 쌓인 워크스페이스를 정리해 디스크 회수
- [ ] Build Retention Policy / 오래된 빌드 기록을 자동으로 지우는 정책
- [ ] Monitoring / 컨트롤러 지표를 프로메테우스로 노출하는 방법
- [ ] Logs / 시스템 로그와 지원 번들로 장애를 파고드는 자리

### Performance

- [ ] Controller JVM Tuning / 컨트롤러 자바 힙과 GC 옵션을 조정하는 일
- [ ] Reducing Controller Load / 무거운 작업을 에이전트로 넘겨 부하를 줄이는 법
- [ ] Queue Throttling and Concurrency / 동시 실행 수를 제한해 대기열을 조절

## 15. Security Hardening

- [ ] Authentication Realm / 로그인 검증을 LDAP·SSO에 위임하는 연동
- [ ] Authorization / 사용자·잡 단위로 권한을 나누는 전략
- [ ] CSRF Protection / 위조 요청을 막는 크럼(crumb) 검증
- [ ] Script Security / 승인 안 된 Groovy 실행을 막는 샌드박스
- [ ] Agent-to-Controller Access Control / 에이전트가 컨트롤러 자원에 접근하는 권한 제한
- [ ] Disabling Legacy Protocols / 취약한 옛 통신 프로토콜을 끄는 조치
- [ ] Secrets Rotation / 저장된 자격증명을 주기적으로 교체

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Git · GitHub Actions `software/skill-based/Infra-DevOps/git-github.md`
- 셸 스크립트 `software/skill-based/Languages/shell-bash.md`
- 서버 운영 `software/skill-based/Infra-DevOps/linux.md`
- 컨테이너 · 클러스터 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
- 파이프라인 보안 `software/role-based/devsecops.md`
