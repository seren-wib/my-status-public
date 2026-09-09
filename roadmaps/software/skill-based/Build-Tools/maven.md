# Maven `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Maven

## 1. What is Maven?

### Overview of Maven / What is it?

- [ ] Build Automation Tool / 빌드·테스트·배포를 자동으로 처리하는 도구
- [ ] Project Object Model (POM) / 프로젝트 정보를 XML로 선언하는 모델
- [ ] Convention over Configuration / 설정보다 관례를 앞세우는 설계 원칙
- [ ] Declarative Dependency Management / 좌표만 적으면 해결되는 의존성 선언 방식

### Core Use Cases

- [ ] Compile, Test, Package / 소스를 빌드해 산출물로 묶는 흐름
- [ ] Dependency Resolution / 선언한 좌표로 라이브러리를 내려받는 과정
- [ ] Artifact Publishing / 빌드 결과물을 저장소에 올리는 작업
- [ ] Multi-module Project Management / 여러 모듈을 부모 POM 하나로 묶는 방법

### Maven vs Other Build Tools

- [ ] Maven vs Ant / 선언형 POM과 절차형 스크립트의 차이
- [ ] Maven vs Gradle / XML 선언 방식과 코드형 빌드의 차이
- [ ] When to choose Maven? / 표준 관례를 그대로 따를 때 유리한 이유

## 2. Getting Started

### Installation `택 1`

- [ ] SDKMAN and Homebrew / 버전 관리형 패키지 매니저로 설치하는 방법 `추천`
- [ ] Binary Download + PATH / 압축을 풀고 경로를 직접 등록하는 방법
- [ ] Maven Wrapper / mvnw로 팀 전체가 같은 버전을 쓰게 고정하는 방법 `추천`

### Environment Verification

- [ ] mvn -v / 설치된 버전과 JDK 경로를 확인하는 명령
- [ ] JAVA_HOME and MAVEN_HOME / JDK와 설치 경로를 잡는 환경 변수
- [ ] Local Repository / 받은 아티팩트를 홈 디렉터리에 쌓아두는 캐시

### First Project

- [ ] Archetype / 정해진 뼈대에서 새 프로젝트를 찍어내는 방법
- [ ] Standard Directory Layout / 소스·테스트·리소스를 정해진 위치에 두는 구조
- [ ] mvn compile, test, package / 단계별로 빌드를 실행하는 명령들

## 3. POM Basics

### Coordinate System

- [ ] GAV / 조직·아티팩트·버전으로 좌표를 식별하는 체계
- [ ] Packaging / jar·war·pom 중 산출물 형식을 정하는 값
- [ ] SNAPSHOT vs Release Version / 개발 중 버전과 고정 배포 버전의 구분

### POM Structure

- [ ] Project Metadata / 이름·설명·라이선스를 적는 항목
- [ ] Properties / 버전·경로 값을 변수로 빼두는 영역
- [ ] Build Section / 빌드에 쓸 플러그인을 선언하는 영역
- [ ] Effective POM / 상속·기본값까지 합쳐진 최종 POM을 보는 명령

### Inheritance and Aggregation

- [ ] Super POM / 모든 POM이 기본으로 상속하는 최상위 정의
- [ ] Parent POM / relativePath로 위치를 잡는 부모 POM
- [ ] Aggregation / 여러 하위 모듈을 한 빌드로 묶는 방법
- [ ] Inheritance vs Aggregation Distinction / 설정 상속과 모듈 묶음의 차이

---

# PART 2 · Dependency Management

## 4. Dependencies

### Declaration

- [ ] dependencies and dependency / 의존성 목록과 개별 항목을 적는 태그
- [ ] Optional Dependency / 전이되지 않게 표시하는 선택적 의존성
- [ ] Type and Classifier / 같은 좌표에서 변형 산출물을 구분하는 값

### Dependency Scope

- [ ] compile / 컴파일·실행 모두에 포함되는 기본 스코프
- [ ] provided / 컴파일엔 필요하나 실행 땐 컨테이너가 제공하는 스코프
- [ ] runtime / 컴파일엔 불필요하고 실행 시에만 필요한 스코프
- [ ] test / 테스트 컴파일·실행에만 포함되는 스코프
- [ ] system / 로컬 경로의 jar를 직접 지정하는 스코프
- [ ] import / BOM의 dependencyManagement를 상속하는 스코프

### Resolution Rules

- [ ] Transitive Dependency / 의존성이 딸려오는 그 의존성의 의존성
- [ ] Nearest-Wins Mediation / 트리에서 더 가까운 버전을 고르는 규칙
- [ ] Exclusions / 특정 전이 의존성을 빼는 설정
- [ ] dependencyManagement / 버전을 한 곳에서 통일해 선언하는 영역
- [ ] BOM / 여러 라이브러리 버전을 한 세트로 묶어 관리하는 목록

### Diagnostics

- [ ] mvn dependency:tree / 의존성 관계를 트리로 보여주는 명령
- [ ] mvn dependency:analyze / 쓰지 않거나 누락된 의존성을 찾는 명령
- [ ] Version Conflict Strategy / 버전 충돌을 해결하는 전략
- [ ] Maven Enforcer Plugin / 버전 수렴·환경 조건을 강제하는 플러그인

## 5. Repositories

### Repository System

- [ ] Local Repository / 저장소 계층에서 가장 먼저 찾는 캐시 위치
- [ ] Central Repository / 메이븐이 기본으로 참조하는 공개 저장소
- [ ] Remote and Custom Repository / 사내망 등에 직접 지정하는 저장소
- [ ] Mirrors / 저장소 요청을 다른 곳으로 대신 받는 설정
- [ ] Update Policy / SNAPSHOT 갱신 주기

### settings.xml

- [ ] servers and Credentials / 저장소 인증 정보를 저장하는 설정
- [ ] profiles and activeProfiles / 환경별 설정을 정의하고 활성화하는 태그
- [ ] Password Encryption / 저장소 비밀번호를 암호화해 저장하는 방법
- [ ] Offline Mode / 원격 저장소 없이 로컬 캐시만 쓰는 옵션

### Repository Manager `선택`

- [ ] Nexus / 사내에 아티팩트를 호스팅하는 저장소 도구
- [ ] Artifactory / 여러 저장소 유형을 통합 관리하는 도구
- [ ] Proxy, Hosted, Group Repository / 역할별로 나뉜 저장소 유형 세 가지

---

# PART 3 · Build Lifecycle and Plugins

## 6. Build Lifecycle

### The Three Lifecycles

- [ ] default / 빌드·테스트·배포를 처리하는 기본 라이프사이클
- [ ] clean / 이전 빌드 산출물을 지우는 라이프사이클
- [ ] site / 프로젝트 문서 사이트를 만드는 라이프사이클

### Default Phase Order

- [ ] validate / 프로젝트 구조가 올바른지 확인하는 단계
- [ ] compile / 소스 코드를 컴파일하는 단계
- [ ] test / 테스트 코드를 실행하는 단계
- [ ] package / 컴파일 결과를 jar·war로 묶는 단계
- [ ] verify / 패키징 결과가 유효한지 검증하는 단계
- [ ] install / 산출물을 로컬 저장소에 등록하는 단계
- [ ] deploy / 산출물을 원격 저장소에 올리는 단계

### Execution Model

- [ ] Phase vs Goal / 생명주기 단계와 실제 실행 작업의 구분
- [ ] Goal Binding / 플러그인 목표를 특정 단계에 연결하는 설정
- [ ] Packaging Default Bindings / 패키징 타입마다 정해진 기본 목표 연결

## 7. Core Plugins

- [ ] maven-compiler-plugin / 자바 버전을 지정해 컴파일하는 플러그인
- [ ] maven-surefire-plugin / test 단계에서 단위 테스트를 돌리는 플러그인
- [ ] maven-failsafe-plugin / verify 단계에서 통합 테스트를 돌리는 플러그인
- [ ] maven-resources-plugin / 리소스 파일의 변수를 값으로 치환하는 플러그인
- [ ] maven-jar-plugin / jar 매니페스트에 실행 클래스를 지정하는 플러그인
- [ ] maven-shade-plugin / 의존성을 한 jar에 합치고 패키지를 재배치하는 플러그인
- [ ] maven-assembly-plugin / 원하는 형태로 배포 묶음을 구성하는 플러그인
- [ ] maven-install-plugin and maven-deploy-plugin / 로컬·원격 저장소에 등록하는 플러그인

## 8. Profiles

- [ ] profiles / 조건에 따라 켜지는 설정 묶음을 정의하는 태그
- [ ] Activation / 속성·JDK·OS·파일 조건으로 프로파일을 켜는 방법
- [ ] activeByDefault Pitfall / 다른 프로파일이 켜지면 무시되는 함정
- [ ] Profile Activation / -P 옵션으로 프로파일을 직접 켜는 방법
- [ ] Per-Environment Config Split / 환경별로 설정을 나눠 관리하는 방법

## 9. Custom Plugin `선택`

- [ ] Mojo and AbstractMojo / 플러그인 목표 하나를 구현하는 클래스 단위
- [ ] Annotation / 목표 이름과 파라미터를 선언하는 방법
- [ ] maven-plugin-api and maven-plugin-annotations / 커스텀 플러그인 개발에 쓰는 라이브러리
- [ ] Plugin Descriptor Generation / 플러그인 메타데이터를 자동 생성하는 과정

---

# PART 4 · Multi-Module and Release

## 10. Multi-module Project

- [ ] Reactor / 여러 모듈의 빌드 순서를 계산하는 엔진
- [ ] Module Build Order / 모듈 간 의존관계로 정해지는 빌드 순서
- [ ] Inter-module Dependency / 한 모듈이 다른 모듈을 참조하는 관계
- [ ] Partial Build / 특정 모듈과 그 의존 모듈만 빌드하는 옵션
- [ ] Parallel Build / 여러 모듈을 스레드로 동시에 빌드하는 옵션

## 11. Testing / Quality

- [ ] Test Execution Control / 테스트 실행이나 컴파일 자체를 건너뛰는 옵션
- [ ] JaCoCo / 테스트가 코드를 얼마나 실행했는지 재는 도구
- [ ] Checkstyle, PMD, SpotBugs / 코드 스타일·품질·버그 패턴을 검사하는 도구들
- [ ] SonarQube Integration / 정적 분석 결과를 대시보드로 모으는 연동

## 12. Release / Publishing

- [ ] Versioning Strategy / 의미 있는 규칙으로 버전을 올리는 방식
- [ ] distributionManagement / 배포·스냅샷 저장소 주소를 지정하는 태그
- [ ] maven-release-plugin / 버전 태깅과 배포를 자동화하는 플러그인
- [ ] Maven Central Publishing / 서명·소스·문서까지 갖춰 올리는 절차
- [ ] versions-maven-plugin / 여러 모듈의 버전을 한 번에 갱신하는 플러그인

---

# PART 5 · Real-World Operations

## 13. CI Integration

- [ ] Wrapper Version Pinning / mvnw로 팀 전체의 메이븐 버전을 고정하는 방법
- [ ] Batch Mode / 대화형 출력을 없애 로그를 줄이는 옵션
- [ ] Local Repository Caching / CI 실행 사이에 .m2 캐시를 재사용하는 방법
- [ ] Reproducible Builds / 빌드 시각을 고정해 항상 같은 산출물을 만드는 설정
- [ ] Docker Multi-stage Build / 빌드 단계와 실행 단계를 이미지로 분리하는 방법

## 14. Build Performance

- [ ] Parallel Build Tuning / 스레드 수를 조절해 빌드 속도를 맞추는 작업
- [ ] Incremental Compile Limits / 메이븐이 변경분만 다시 빌드하지 못하는 한계
- [ ] Maven Daemon / mvnd 데몬을 띄워 재시작 비용을 없애는 도구
- [ ] Dependency Prefetch / 오프라인 빌드 전에 의존성을 미리 받는 명령

## 15. Troubleshooting

- [ ] Debug Output / 상세 로그와 스택 트레이스를 보는 옵션
- [ ] Forced SNAPSHOT Update / 캐시를 무시하고 스냅샷을 새로 받는 옵션
- [ ] Corrupted Repository Recovery / 손상된 로컬 저장소를 지우고 복구하는 방법
- [ ] Unpinned Plugin Version Drift / 버전을 안 고정해 빌드 결과가 흔들리는 문제
- [ ] Classpath Order Diagnosis / 클래스패스 순서로 생기는 충돌을 진단하는 방법

## 16. Ecosystem `선택`

- [ ] Spring Boot Maven Plugin / 실행 가능한 jar로 다시 묶는 목표
- [ ] Jib / 도커 데몬 없이 컨테이너 이미지를 만드는 플러그인
- [ ] Flatten Plugin / 상속·변수를 걷어내 배포용 POM을 단순화하는 플러그인
- [ ] Maven Toolchains / 프로젝트마다 다른 JDK 버전을 지정하는 방법

---

# 이 로드맵 밖

- Java `software/skill-based/Languages/java.md`
- Gradle `software/skill-based/Build-Tools/gradle.md`
- Spring Boot 빌드 연동 `software/skill-based/Frameworks/spring-boot.md`
- 단위 테스트 `software/skill-based/Testing/junit.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/jenkins.md`, `gitlab-ci.md`
- 컨테이너 이미지 빌드 `software/skill-based/Infra-DevOps/docker.md`
