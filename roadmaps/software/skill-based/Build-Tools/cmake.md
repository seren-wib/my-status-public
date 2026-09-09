# CMake `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to CMake

## 1. What is CMake?

### Overview of CMake / What is it?

- [ ] Build System Generator / 실제 빌드 도구를 대신 만들어내는 상위 도구
- [ ] CMakeLists.txt Declaration / 프로젝트 구조를 선언하는 최상위 파일
- [ ] Cross-platform / 같은 스크립트로 OS마다 다른 빌드를 뽑는 구조
- [ ] Configure → Generate → Build Flow / 설정·생성·빌드 3단계로 진행되는 흐름

### Why It Is Needed

- [ ] Makefile / MSBuild 직접 관리의 한계
- [ ] Cross-Platform Compiler Abstraction / 컴파일러 차이를 감춰 통일된 명령으로 다루는 방식
- [ ] Dependency Find & Install Convention / 의존성 탐색·설치 방식을 표준화한 관례

### Comparison with Alternatives

- [ ] CMake vs Make / 생성기 유무로 갈리는 빌드 도구 위치
- [ ] CMake vs Meson and Bazel / 생성기 방식과 자체 실행 방식을 가르는 기준
- [ ] Modern CMake vs Legacy CMake / 타깃 중심이냐 전역 변수 중심이냐의 차이

## 2. Getting Started

- [ ] Installation / 패키지 매니저, 공식 바이너리
- [ ] Minimal Script / 최소 버전·프로젝트·실행 파일 세 줄로 시작하는 골격
- [ ] Out-of-source Build / 소스와 분리된 폴더에 빌드 결과를 두는 방식
- [ ] Configure / cmake -S . -B build 로 빌드 폴더를 준비하는 단계
- [ ] Build / cmake --build build 로 실제 컴파일을 실행하는 단계
- [ ] Generator Selection / Ninja·Make·VS 중 어떤 빌드 도구를 만들지 고르는 옵션

## 3. Language Basics

### Syntax

- [ ] Command / 함수처럼 명령어와 인자로 호출하는 문법 구조
- [ ] Variable / set·unset으로 값을 넣고 지우는 범위 단위
- [ ] Cache Variable / -D로 넘겨 재실행해도 값이 남는 저장소
- [ ] Variable Reference / ${}·$ENV{}로 변수값을 꺼내는 문법
- [ ] list() Operations / 리스트를 추가·삭제·정렬하는 함수 모음
- [ ] string() Operations / 문자열을 자르고 합치고 바꾸는 함수 모음

### Control Structures

- [ ] if, elseif, else / 조건에 따라 분기를 나누는 구문
- [ ] foreach and while / 목록·조건으로 반복하는 두 반복문
- [ ] function vs macro / 변수 범위를 갖는지 아닌지로 갈리는 차이
- [ ] include / 다른 cmake 파일 내용을 그대로 불러오는 명령
- [ ] message / STATUS·WARNING 등 레벨별로 로그를 찍는 명령

### Commonly Used Variables

- [ ] Path Variables / 소스·빌드·프로젝트 루트 경로를 담는 변수들
- [ ] CMAKE_BUILD_TYPE / Debug·Release 등 최적화 수준을 정하는 변수
- [ ] CMAKE_CXX_STANDARD / 프로젝트 전체 C++ 표준 버전을 지정하는 변수
- [ ] Search Path Variables / 모듈·패키지를 찾을 추가 경로를 지정하는 변수

---

# PART 2 · Target-Centric Design

## 4. Targets

- [ ] add_executable / 소스를 실행 파일로 빌드하는 타깃 선언
- [ ] add_library / 정적·동적·플러그인 라이브러리를 선언하는 명령
- [ ] OBJECT Library / 링크 없이 오브젝트 파일만 만드는 중간 타깃
- [ ] INTERFACE Library / 컴파일할 소스 없이 헤더만 전달하는 타깃
- [ ] ALIAS Target / 타깃에 네임스페이스 붙은 별칭을 만드는 방법
- [ ] add_custom_target and add_custom_command / 빌드 과정에 임의 명령을 끼워 넣는 방법

## 5. Target Properties

### Usage Requirements

- [ ] PUBLIC, PRIVATE, INTERFACE / 의존성을 상위 대상까지 전파할지 정하는 규칙
- [ ] target_include_directories / 타깃에 헤더 검색 경로를 붙이는 명령
- [ ] target_link_libraries / 타깃끼리 링크·속성 전파를 거는 핵심 명령
- [ ] target_compile_definitions / 타깃에 전처리기 매크로를 정의하는 명령
- [ ] target_compile_options / 타깃별 컴파일러 플래그를 추가하는 명령
- [ ] target_compile_features / cxx_std_20처럼 필요한 언어 기능을 요구하는 명령
- [ ] target_sources / FILE_SET으로 헤더까지 타깃에 등록하는 명령
- [ ] set_target_properties / 출력 이름·PIC 등 타깃 속성을 일괄 지정하는 명령

### Escaping Anti-Patterns

- [ ] Directory-Wide Commands / include_directories 등 디렉터리 전역 명령 회피
- [ ] Global Compile Flags / CMAKE_CXX_FLAGS 직접 조작 회피
- [ ] link_libraries and add_definitions / 타깃 구분 없이 전부에 걸리는 전역 명령 회피

## 6. Generator Expressions

- [ ] Evaluation Time / 빌드가 아닌 Generate 단계에서 평가되는 시점
- [ ] Config Branching / 빌드 타입별로 다른 값을 넣는 조건문
- [ ] Compiler Branching / 컴파일러 종류별로 다른 값을 넣는 조건문
- [ ] $<BUILD_INTERFACE> and $<INSTALL_INTERFACE> / 빌드 중과 설치 후 경로를 다르게 주는 표현
- [ ] Target Path Reference / 다른 타깃의 산출물 경로를 참조하는 표현

## 7. Project Structure

- [ ] add_subdirectory / 하위 폴더의 CMakeLists.txt를 포함하는 명령
- [ ] Directory Layout / include·src·tests로 나누는 폴더 관례
- [ ] option() / ON/OFF 캐시 변수로 기능을 켜고 끄는 명령
- [ ] Top-level Detection / 최상위 프로젝트인지 하위 포함인지 구분하는 변수

---

# PART 3 · Dependencies and Toolchains

## 8. Dependencies

### Finding System Dependencies

- [ ] find_package / Find모듈과 설치된 Config파일 두 탐색 방식
- [ ] Imported Target Usage / 찾은 패키지를 타깃처럼 링크하는 방법
- [ ] REQUIRED, COMPONENTS, QUIET / find_package 탐색 방식을 조정하는 옵션들
- [ ] Find Module Authoring / 자체 FindXxx.cmake를 직접 작성하는 방법
- [ ] pkg-config Integration / .pc 파일로 리눅스 의존성을 찾는 연동
- [ ] Search Path Hint / 패키지 탐색에 추가 경로를 알려주는 변수

### Source Integration `택 1`

- [ ] FetchContent / 빌드 시점에 외부 소스를 받아 포함하는 방법 `추천`
- [ ] ExternalProject_Add / 별도 빌드 단계로 외부 프로젝트를 통째로 빌드하는 방법
- [ ] Git Submodule + add_subdirectory / 서브모듈로 받은 소스를 직접 포함하는 방식
- [ ] External Package Manager / vcpkg·Conan으로 의존성을 미리 빌드해 오는 방식

## 9. Toolchain / Cross Compile

- [ ] Toolchain File / 크로스 컴파일 설정을 모아둔 스크립트 파일
- [ ] CMAKE_SYSTEM_NAME and CMAKE_SYSTEM_PROCESSOR / 타깃 OS와 CPU 아키텍처를 지정하는 변수
- [ ] Compiler and Sysroot / 크로스 컴파일용 컴파일러와 루트 경로를 지정하는 설정
- [ ] try_compile Behavior & Pitfalls / 짧은 코드를 미리 컴파일해 지원 여부를 보는 함정
- [ ] Target Platform / 모바일·임베디드 등 빌드 대상 플랫폼 종류

## 10. Feature Detection

- [ ] check_cxx_source_compiles and check_include_file / 코드·헤더가 컴파일되는지 확인하는 함수
- [ ] CheckSymbolExists and CheckCXXCompilerFlag / 심볼·컴파일러 플래그 지원 여부를 검사하는 모듈
- [ ] configure_file / 변수값을 채운 헤더·설정 파일을 만드는 명령
- [ ] Platform Macro Strategy / OS별 분기를 매크로로 처리하는 방식

---

# PART 4 · Testing · Installation · Deployment

## 11. Testing

- [ ] enable_testing and add_test / 테스트 기능을 켜고 케이스를 등록하는 명령
- [ ] CTest Execution / 실패 시 출력·이름 필터·병렬 실행 옵션
- [ ] Test Property / 제한 시간·라벨·실패 예상 등 테스트 속성
- [ ] GoogleTest Integration / 빌드 후 개별 테스트 케이스를 자동 등록하는 연동
- [ ] Catch2 and doctest / 헤더 하나로 붙는 경량 테스트 프레임워크 `선택`
- [ ] Sanitizer and Coverage / ASan·커버리지 계측 플래그를 켜는 설정

## 12. Install / Export

- [ ] install(TARGETS ... EXPORT) / 타깃을 설치하며 Export 셋에 등록하는 명령
- [ ] install(FILES) and install(DIRECTORY) / 개별 파일과 폴더 통째를 설치하는 명령
- [ ] GNUInstallDirs / bin·lib 등 표준 설치 경로 변수를 채우는 모듈
- [ ] install(EXPORT) / 다른 프로젝트가 find_package할 정보를 내보내는 명령
- [ ] Package Config File / 설치된 패키지를 찾게 해주는 배포용 스크립트
- [ ] CMakePackageConfigHelpers / Config 파일을 정형화해 생성해주는 모듈
- [ ] CMAKE_INSTALL_PREFIX and DESTDIR / 설치 기본 경로와 패키징용 임시 루트

## 13. Packaging

- [ ] CPack Basic Setup / 배포 패키지를 만들기 위한 최소 설정
- [ ] Generator / TGZ·DEB·RPM 등 패키지 형식을 고르는 옵션
- [ ] Component-Based Packaging / 기능 단위로 나눠 선택 설치되게 하는 방식
- [ ] Version and Metadata / 패키지 버전·설명 등 부가 정보를 설정하는 항목

---

# PART 5 · Operations and Optimization

## 14. Presets / Workflow

- [ ] CMakePresets.json / 설정·빌드·테스트 옵션을 미리 묶어두는 파일
- [ ] Preset Inheritance / 기존 프리셋 설정을 물려받아 재사용하는 방법
- [ ] CMakeUserPresets.json / 개인 로컬 환경용 프리셋을 얹는 파일
- [ ] IDE Integration / VS Code·CLion 등 에디터가 CMake를 인식하는 연동
- [ ] compile_commands.json / 코드 분석 도구용 컴파일 명령 목록 파일

## 15. Build Performance / CI

- [ ] Ninja Generator Adoption / Make보다 빠른 병렬 빌드 생성기 채택
- [ ] Compiler Cache / 재컴파일 결과를 캐시해 빌드를 앞당기는 도구
- [ ] Unity Build / 소스 여러 개를 묶어 컴파일 단위를 줄이는 기법
- [ ] Precompiled Header / 자주 쓰는 헤더를 미리 컴파일해 재사용하는 기법
- [ ] LTO / 링크 단계에서 파일 경계를 넘어 최적화하는 옵션
- [ ] Parallel Build / 여러 코어로 동시에 컴파일해 속도를 높이는 옵션
- [ ] CI Matrix / 여러 컴파일러·OS 조합으로 동시에 검증하는 구성

## 16. Troubleshooting

- [ ] --trace-expand and --debug-find / 변수 치환·패키지 탐색 과정을 추적하는 옵션
- [ ] Cache Pollution / 이전 설정이 남아 꼬인 CMakeCache.txt를 지우는 처리
- [ ] Policy / 버전 간 동작 변경을 CMP 번호로 관리하는 장치
- [ ] Deprecation Warning Handling / 폐지 예정 기능 경고를 처리하는 방법

---

# 이 로드맵 밖

- C `software/skill-based/Languages/c.md`
- C++ `software/skill-based/Languages/cpp.md`
- 게임 개발 `software/role-based/game-developer.md`
- 리눅스 · 툴체인 환경 `software/skill-based/Infra-DevOps/linux.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/circleci.md`
- 컨테이너 빌드 `software/skill-based/Infra-DevOps/docker.md`
