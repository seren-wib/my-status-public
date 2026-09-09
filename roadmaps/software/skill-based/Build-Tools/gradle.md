# Gradle `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Gradle

## 1. What is Gradle?

### Overview of Gradle / What is it?

- [ ] Build Automation Tool / 컴파일·테스트·배포를 자동 수행하는 도구
- [ ] Task Graph (DAG) Execution Model / 태스크를 방향성 그래프로 엮어 실행하는 모델
- [ ] Declarative DSL + Imperative Extension / 선언적 DSL에 명령형 코드를 얹는 방식
- [ ] JVM, Android, Native / Gradle이 빌드할 수 있는 대상 종류

### Core Use Cases

- [ ] JVM Application Build / 자바·코틀린 앱을 빌드하는 기본 용도
- [ ] Android Build / AGP로 APK·AAB를 빌드하는 용도
- [ ] Multi-language Monorepo / 여러 언어 모듈을 한 저장소에서 빌드하는 구조
- [ ] Custom Automation Task / 빌드 외 임의 작업을 자동화하는 용도

### Gradle vs Maven

- [ ] Fixed Lifecycle vs Task Graph / 정해진 단계 대 태스크 그래프의 차이
- [ ] XML vs DSL / XML 선언 대 코드형 DSL의 차이
- [ ] Incremental Build and Build Cache / 변경분만 다시 빌드해 시간을 아끼는 방식
- [ ] When to choose Gradle? / 태스크 그래프가 필요해지는 선택 기준

## 2. Getting Started

### Execution Methods `택 1`

- [ ] Gradle Wrapper / gradlew 스크립트로 팀의 버전을 고정하는 방식 `추천`
- [ ] SDKMAN and Homebrew / 버전 관리자로 배포판을 골라 설치하는 방법
- [ ] Binary Download / 설치 없이 압축 파일을 받아 쓰는 방법

### Wrapper

- [ ] gradle wrapper --gradle-version / 원하는 버전으로 래퍼를 생성하는 명령
- [ ] gradle-wrapper.properties / 래퍼가 받을 배포판 URL을 적는 파일
- [ ] distributionSha256Sum / 배포판 해시를 검증해 위조를 막는 설정

### First Build

- [ ] gradle init / 대화형으로 새 프로젝트 뼈대를 만드는 명령
- [ ] Project Layout / 소스와 테스트를 정해진 경로에 두는 관례
- [ ] gradle build, test, clean / 빌드·테스트·정리를 실행하는 기본 명령
- [ ] gradle tasks, projects, help --task / 태스크와 프로젝트 구조를 확인하는 명령

## 3. Build Script Basics

### DSL Choice `택 1`

- [ ] Kotlin DSL / build.gradle.kts에 코틀린 문법으로 타입 안전하게 적는 방식 `추천`
- [ ] Groovy DSL / build.gradle에 그루비 문법으로 빌드를 적는 방식

### File Layout

- [ ] settings.gradle(.kts) / rootProject.name과 include로 구조를 선언하는 파일
- [ ] build.gradle(.kts) / 플러그인·의존성·태스크를 선언하는 빌드 스크립트
- [ ] gradle.properties / JVM 옵션 등 빌드 전역 설정을 두는 파일
- [ ] gradle/libs.versions.toml / 버전 카탈로그를 정의하는 파일

### Script Structure

- [ ] plugins Block / 플러그인을 적용하는 선언 블록
- [ ] repositories Block / 의존성을 받아올 저장소를 선언하는 블록
- [ ] dependencies Block / 모듈별 의존성을 선언하는 블록
- [ ] Extension Configuration / java·application 등 플러그인 확장을 설정하는 블록
- [ ] Project / 태스크 API에 접근하는 진입점이 되는 객체

---

# PART 2 · Dependency Management

## 4. Dependencies

### Configuration

- [ ] implementation / 컴파일·런타임엔 쓰되 API로 안 드러내는 범위
- [ ] api / 의존한 모듈의 의존성까지 밖으로 노출하는 범위
- [ ] compileOnly / 컴파일 때만 필요하고 런타임엔 안 넣는 범위
- [ ] runtimeOnly / 런타임에만 필요하고 컴파일엔 안 쓰는 범위
- [ ] testImplementation / 테스트 소스에서만 쓰는 의존성 범위
- [ ] annotationProcessor / 컴파일 시 코드를 생성하는 처리기 전용 범위

### api vs implementation

- [ ] ABI Exposure Scope / 공개 API 표면에 노출할지 정하는 범위
- [ ] Compile Classpath Reduction / 컴파일 classpath를 줄이는 효과
- [ ] java-library Plugin / api·implementation 구분을 가능케 하는 플러그인

### Declaration Syntax

- [ ] Module Dependency / group:name:version 좌표로 지정하는 방식
- [ ] Project Dependency / project(":module")로 같은 빌드 내 모듈을 참조하는 방식
- [ ] File Dependency / 저장소 없이 로컬 jar 파일을 직접 의존하는 방식
- [ ] platform(), enforcedPlatform(), BOM / 여러 모듈의 버전을 한 곳에서 맞추는 방식

### Version Catalog

- [ ] libs.versions.toml / versions·libraries·bundles·plugins로 구성되는 파일
- [ ] Type-safe Accessor / libs.foo처럼 자동완성되는 참조 방식
- [ ] Bundle / 여러 라이브러리를 묶어 한 번에 추가하는 단위

## 5. Dependency Resolution

- [ ] Transitive Resolution / 의존성의 의존성까지 자동으로 끌어오는 방식
- [ ] Highest-Wins Conflict Resolution / 충돌 시 가장 높은 버전을 택하는 기본 전략
- [ ] Dependency Constraints / 직접 의존 안 해도 버전 범위를 강제하는 선언
- [ ] Exclude Rules / 전이 의존성 중 특정 모듈을 빼는 규칙
- [ ] Dynamic Version and Version Range / 버전이 빌드마다 바뀌어 재현성이 깨지는 위험
- [ ] Resolution Strategy / force·failOnVersionConflict로 해석을 강제하는 방식
- [ ] Dependency Locking / 해석된 버전 조합을 파일로 고정하는 기능
- [ ] Diagnostics / dependencies·dependencyInsight로 의존 트리를 보는 명령

## 6. Repositories

- [ ] mavenCentral, google, gradlePluginPortal / 자주 쓰는 공개 저장소 세 곳
- [ ] mavenLocal Caveats / 로컬 캐시를 참조해 재현성이 깨지는 함정
- [ ] Custom Maven Repository / credentials로 인증하는 사설 저장소 등록
- [ ] Repository Content Filtering / 저장소별로 받을 그룹·모듈을 제한하는 설정
- [ ] Dependency Verification / checksum·signature로 위변조를 검증하는 기능

---

# PART 3 · Tasks and Plugins

## 7. Task

### Basics

- [ ] Task Registration / tasks.register로 태스크를 지연 등록하는 방식
- [ ] Task Action / doFirst·doLast로 실행 전후 동작을 넣는 방식
- [ ] Task Ordering / dependsOn·finalizedBy·mustRunAfter로 순서를 정하는 방식
- [ ] Built-in Task Type / Copy·Zip·Exec·JavaExec 등 기본 제공 태스크 종류

### Input / Output

- [ ] Annotation / @Input·@InputFiles·@OutputFile로 입출력을 선언하는 방식
- [ ] Up-to-date Check / 입출력이 안 바뀌면 태스크를 건너뛰는 검사
- [ ] Incremental Task / InputChanges로 바뀐 파일만 처리하는 방식
- [ ] Task Skipping / onlyIf·enabled로 조건부 실행을 막는 방식

## 8. Build Lifecycle

- [ ] Initialization, Configuration, Execution / 설정 읽기·그래프 구성·실행으로 이어지는 세 단계
- [ ] Configuration Avoidance / register와 create 중 즉시 생성을 피하는 방식
- [ ] Lazy API / Provider·Property로 값 평가를 미루는 방식
- [ ] Task Graph Inspection / --dry-run으로 실행 없이 계획만 보는 방법

## 9. Plugins

### Applying Plugins

- [ ] plugins DSL vs apply / 선언형 블록과 명령형 호출의 차이
- [ ] Core Plugin / java·java-library·application·war 등 내장 플러그인
- [ ] Community Plugin / Plugin Portal에서 받아오는 외부 플러그인

### Commonly Used Plugins

- [ ] Spring Boot Plugin / bootJar·bootRun 태스크를 추가하는 플러그인
- [ ] Kotlin JVM Plugin / 코틀린 코드를 컴파일하게 해주는 플러그인
- [ ] Android Gradle Plugin / APK·AAB 빌드 태스크를 추가하는 플러그인
- [ ] Shadow Plugin / 의존성을 합쳐 Fat JAR로 묶는 플러그인
- [ ] Static Analysis / JaCoCo·Checkstyle·SpotBugs로 코드를 검사하는 플러그인

### Custom Plugin

- [ ] Script Plugin / 별도 스크립트 파일로 작성해 적용하는 플러그인
- [ ] Precompiled Script Plugin / buildSrc에 미리 컴파일해 두는 플러그인
- [ ] Binary Plugin / Plugin<Project>를 구현한 코드형 플러그인
- [ ] Extension Object Design / 플러그인 설정을 DSL로 받게 하는 객체 설계
- [ ] Composite Build / includeBuild로 별도 빌드를 참여시키는 방식

---

# PART 4 · Performance and Multi-Project Builds

## 10. Multi-project Build

- [ ] settings include / 하위 프로젝트를 계층 구조로 등록하는 선언
- [ ] Root vs Subproject Responsibility / 공통 설정과 빌드 로직의 역할 분담
- [ ] subprojects / allprojects와 함께 설정을 즉시 평가시키는 안티패턴
- [ ] Convention Plugin Extraction / 공통 빌드 로직을 플러그인으로 뽑아내는 방식
- [ ] Cross-project Configuration Avoidance / 다른 프로젝트 설정을 직접 안 건드리는 원칙

## 11. Performance

- [ ] Gradle Daemon / JVM을 상주시켜 기동 시간을 아끼는 프로세스
- [ ] Incremental Build / 태스크 입출력이 그대로면 재실행을 생략하는 방식
- [ ] Build Cache / Local·Remote 캐시로 결과물을 재사용하는 방식
- [ ] Configuration Cache / 설정 단계 결과를 직렬화해 재사용하는 캐시
- [ ] Parallel Execution / org.gradle.parallel로 태스크를 동시 실행하는 옵션
- [ ] File System Watching / 파일 변경을 감시해 다음 빌드를 빠르게 하는 기능
- [ ] Build Scan / --scan으로 빌드 상세 리포트를 만드는 기능
- [ ] JVM Tuning / org.gradle.jvmargs로 데몬 힙 크기를 조정하는 설정

## 12. Testing

- [ ] Test Task Configuration / useJUnitPlatform으로 테스트 엔진을 지정하는 설정
- [ ] Test Filtering / --tests로 특정 테스트만 골라 실행하는 옵션
- [ ] Parallel Test / maxParallelForks로 테스트를 병렬 실행하는 설정
- [ ] Test Fixtures / java-test-fixtures로 테스트 코드를 다른 모듈과 공유하는 기능
- [ ] Report / HTML 리포트와 JaCoCo 커버리지를 연동한 결과물

---

# PART 5 · Deployment and Operations

## 13. Publishing

- [ ] maven-publish Plugin / 생성물을 메이븐 형식으로 배포하는 플러그인
- [ ] publications / MavenPublication으로 배포물을 정의하는 블록
- [ ] POM Metadata Customization / POM의 이름·설명·라이선스를 채우는 작업
- [ ] Gradle Module Metadata / 변형·의존성 정보를 담는 그레이들 전용 메타데이터
- [ ] Signing Plugin / GPG로 배포물에 서명하는 플러그인
- [ ] Maven Central and Internal Repository / 공개·사내 저장소 중 배포 대상을 고르는 문제

## 14. CI Integration

- [ ] Wrapper Version Pinning / CI에서도 같은 버전을 쓰게 고정하는 방법
- [ ] Daemon Policy / CI에서 --no-daemon 사용 여부를 정하는 기준
- [ ] Remote Build Cache Setup / 팀·CI가 캐시를 공유하도록 서버를 두는 설정
- [ ] Dependency Cache Reuse / CI 실행 간 의존성 다운로드를 재사용하는 방법
- [ ] Build Scan Sharing / 스캔 링크를 팀과 공유해 문제를 진단하는 방법

## 15. Troubleshooting

- [ ] Log Level / -i·-d·-s로 로그 상세도를 조절하는 옵션
- [ ] Configuration Cache Diagnosis / 설정 캐시 무효화 원인을 찾는 진단 작업
- [ ] Daemon Failure / --stop으로 문제 있는 데몬을 종료하는 방법
- [ ] Compatibility Matrix / Gradle·JDK·AGP 버전 궁합을 맞추는 표
- [ ] Deprecation Handling / --warning-mode all로 폐기 경고를 전부 보는 옵션

## 16. Advanced `선택`

- [ ] Init Script / 모든 프로젝트에 적용되는 전역 초기화 스크립트
- [ ] Artifact Transform / 의존성을 소비 전에 변환하는 캐시 가능한 처리
- [ ] Attribute / Variant-aware Matching으로 맞는 변형을 고르는 값
- [ ] Java Toolchain / 설치 JDK와 무관하게 빌드용 JDK를 지정하는 기능
- [ ] Develocity / 빌드 성능을 조직 차원에서 분석하는 엔터프라이즈 도구

---

# 이 로드맵 밖

- Java `software/skill-based/Languages/java.md`
- Kotlin `software/skill-based/Languages/kotlin.md`
- Maven `software/skill-based/Build-Tools/maven.md`
- 안드로이드 전반 `software/role-based/android.md`
- 단위 테스트 `software/skill-based/Testing/junit.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/jenkins.md`, `gitlab-ci.md`
