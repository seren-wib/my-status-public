# Unreal Engine `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Unreal Engine

## 1. What is Unreal Engine?

### Overview of Unreal Engine / What is it?

- [ ] AAA-grade Real-time Engine / 대작급 실시간 렌더링을 지원하는 상용 엔진
- [ ] C++ & Blueprint Dual Workflow / 코드와 비주얼 스크립팅을 함께 쓰는 이중 구조
- [ ] Royalty-based Licensing / 매출 기준으로 로열티를 내는 무료 라이선스

### Unreal vs Other Engines

- [ ] Unreal vs Unity / C++ 이중구조 vs C# 단일구조 비교

### Installation and Project Creation

- [ ] Engine Version / 배포판 설치냐 소스 직접 빌드냐 선택
- [ ] Project Template / 블루프린트냐 C++냐로 갈리는 시작 템플릿
- [ ] Project Directory Structure / Content·Config·Source로 나뉘는 폴더 구조

## 2. Unreal Editor

### Editor Layout

- [ ] Level Viewport / Navigation·View Mode로 씬을 보고 이동하는 화면
- [ ] Content Browser / 프로젝트 에셋을 찾고 관리하는 창
- [ ] Outliner / 레벨에 배치된 액터 목록 트리
- [ ] Details Panel / 선택한 액터의 속성을 편집하는 창
- [ ] Output Log / 로그 확인과 콘솔 명령 입력 창

### Navigation and Placement

- [ ] Transform Gizmo / World·Local로 갈리는 좌표 기준 조작 기즈모
- [ ] Play In Editor / Simulate·Standalone 등 에디터 내 실행 모드

### Configuration

- [ ] Project Settings and Editor Preferences / 프로젝트 전역 설정과 개인 에디터 설정
- [ ] Plugin Management / 부가 기능 모듈을 켜고 끄는 관리

## 3. Actor & Level

### Actor

- [ ] Actor / 월드에 배치되는 최소 단위 객체
- [ ] SceneComponent / 부모-자식으로 붙는 위치 계층 컴포넌트
- [ ] StaticMeshComponent and SkeletalMeshComponent / 고정 메시와 뼈대 있는 메시 컴포넌트
- [ ] Actor Lifecycle / BeginPlay·Tick·EndPlay로 이어지는 액터 생명주기
- [ ] Spawn and Destroy / 런타임에 액터를 만들고 없애기

### Level

- [ ] Level and Sublevel / 맵 하나와 그 안에 겹쳐 쓰는 하위 맵
- [ ] World Partition / 큰 맵을 구역별로 자동 스트리밍하는 기능
- [ ] Level Streaming / 필요한 구역만 불러오고 내리기

### Level Components

- [ ] Landscape / 지형을 조각하는 대규모 메시 툴

---

# PART 2 · Gameplay Programming

## 4. Gameplay Framework

### Core Classes

- [ ] GameInstance / 레벨 전환에도 안 죽는 전역 객체
- [ ] GameMode and GameState / 서버 전용 규칙과 복제되는 게임 상태
- [ ] PlayerController and PlayerState / 입력 처리 담당과 복제되는 플레이어 정보
- [ ] Pawn and Character / 조종 대상 액터와 이동 기능을 더한 확장판

### Input

- [ ] Enhanced Input / Input Action·Mapping Context로 키를 분리하는 체계
- [ ] Input Modifier and Trigger / 입력값 가공과 발동 조건 설정

### Movement and State

- [ ] Character Movement Component / 걷기·점프·중력을 맡는 이동 컴포넌트
- [ ] Save Game / 저장할 데이터를 담는 직렬화 객체

## 5. Blueprint Visual Scripting

### Blueprint Basics

- [ ] Blueprint Class vs Level Blueprint / 재사용 클래스 vs 레벨 전용 로직
- [ ] Event Graph / 실행 흐름과 값이 함께 흐르는 핀 그래프
- [ ] Variable / Category·Instance Editable 등 옵션을 가진 변수
- [ ] Function, Macro, Collapsed Graph / 그래프를 묶어 재사용하는 세 방법
- [ ] Construction Script / 에디터에서 배치할 때마다 실행되는 스크립트

### Communication

- [ ] Event Dispatcher / 여러 블루프린트에 알리는 이벤트 방송
- [ ] Blueprint Interface / 클래스 상관없이 공유하는 함수 규격

### Data and Extensions

- [ ] Data Asset, Data Table, Curve Table / 코드 없이 데이터를 담는 에셋들
- [ ] Blueprint Debugging / 그래프 실행을 멈추고 값 추적하기

## 6. C++ Programming

### Unreal C++ Basics

- [ ] Reflection Macro / UCLASS·UPROPERTY 등으로 C++ 요소를 노출하는 매크로
- [ ] UObject / 엔진이 자동 회수하는 기본 객체
- [ ] Module & Build.cs / 코드 묶음과 그 빌드 설정 파일
- [ ] Unreal Container / TArray·TMap·FString 등 언리얼 전용 자료형

### Memory Management

- [ ] TObjectPtr, TWeakObjectPtr, TSharedPtr / GC 관여 방식이 다른 스마트 포인터들

### Connecting C++ and Blueprint

- [ ] BlueprintCallable, BlueprintImplementableEvent, BlueprintNativeEvent / C++ 함수를 블루프린트에 여는 매크로들
- [ ] C++ Base Class Inheritance Structure / C++로 뼈대 잡고 블루프린트로 확장하는 구조 `추천`

### Developer Experience

- [ ] Live Coding and Hot Reload / 에디터 켠 채로 C++ 코드 바로 반영
- [ ] Delegate / Dynamic Multicast 등 함수를 값처럼 넘기는 콜백 바인딩
- [ ] Subsystem / GameInstanceSubsystem·WorldSubsystem 등 전역 시스템
- [ ] Gameplay Ability System / 스킬·버프를 데이터로 다루는 프레임워크 `선택`

## 7. Physics & Collision

### Collision

- [ ] Collision Preset / Object·Trace Channel을 묶어둔 프리셋
- [ ] Collision Response / Block·Overlap·Ignore 세 갈래 충돌 처리
- [ ] Overlap and Hit Event / 겹침과 물리 충돌이 각각 보내는 이벤트

### Physics

- [ ] Chaos Physics / 언리얼 기본 물리 시뮬레이션 엔진
- [ ] Simulate Physics / 물리 적용 액터의 질량·저항·구속 설정
- [ ] Physical Material / 마찰·반발 등 표면 물리 속성 정의
- [ ] Trace / LineTrace·SweepTrace 등으로 검사하는 레이캐스트

---

# PART 3 · Content Creation

## 8. Materials & Shading

### Material Editor

- [ ] Material Node Graph / 셰이더를 노드로 조립하는 편집 그래프
- [ ] Material Domain, Blend Mode, Shading Model / 머티리얼이 어디에 어떻게 렌더될지 설정
- [ ] PBR Input / Base Color·Metallic·Roughness 등 표면 입력값
- [ ] Texture Sample / 텍스처를 불러와 좌표를 가공하는 노드

### Reusable Structures

- [ ] Material Instance / 그래프 재컴파일 없이 값만 바꾸는 인스턴스
- [ ] Material Function / 노드 묶음을 재사용하는 함수화
- [ ] Dynamic Material Instance / 런타임에 파라미터를 바꾸는 인스턴스

## 9. Lighting & Rendering

### Light

- [ ] Light Type / Directional·Point·Spot 등 조명 종류
- [ ] Mobility / Static·Stationary·Movable 세 이동성 등급
- [ ] Sky Light, Sky Atmosphere, Volumetric Cloud / 하늘 전역광과 대기·구름 표현

### Global Illumination `택 1`

- [ ] Lumen / 사전 베이크 없는 동적 전역광 시스템 `추천`
- [ ] Baked Lightmap / 정적 조명을 미리 텍스처로 구워두기
- [ ] Ray Tracing / 광선 추적으로 반사·그림자 계산

### Rendering Features

- [ ] Nanite / 폴리곤 수 제한 없는 가상화 지오메트리
- [ ] Virtual Shadow Map / 고해상도 그림자를 가상 텍스처로 처리
- [ ] Post Process Volume / Exposure·Bloom 등 후처리 효과 구역

## 10. Animation

### Skeletal Animation

- [ ] Skeleton, Skeletal Mesh, Animation Sequence / 뼈대·스킨 메시·동작 클립 세 요소
- [ ] Animation Blueprint / Event Graph·AnimGraph 두 그래프로 구성
- [ ] State Machine / 동작 상태 전환을 규칙으로 관리
- [ ] Blend Space / 이동값에 따라 애니메이션을 섞는 공간
- [ ] Anim Notify and Notify State / 재생 중 특정 시점에 이벤트 발생

### Advanced

- [ ] Montage and Slot / 여러 애니메이션을 조합 재생하는 트랙
- [ ] IK and Control Rig / 발·손을 지형에 맞추는 역운동학 리그
- [ ] Retargeting and IK Rig / 다른 뼈대 구조에 애니메이션 재사용
- [ ] Root Motion / 루트 뼈로 실제 이동 거리를 구동

### Cinematics

- [ ] Sequencer / Track·Keyframe 등으로 편집하는 논리니어 타임라인 툴

## 11. UMG / UI

- [ ] Widget Blueprint / UI 배치 화면과 로직 그래프
- [ ] Canvas Panel, Anchor, Slot / 화면 비율 기준 UI 배치 컨테이너
- [ ] Layout Panel / Horizontal·Vertical·Grid 등 정렬 패널
- [ ] Common Widget / Button·Text·Image 등 기본 UI 요소
- [ ] Property Binding vs Event-driven Update / 매 프레임 갱신 vs 이벤트로만 갱신
- [ ] Widget Creation and Management / Add to Viewport·Widget Component로 UI 붙이기
- [ ] Input Mode / Game·UI·GameAndUI 중 입력 대상 설정

## 12. Niagara & Audio

### Niagara

- [ ] Niagara System, Emitter, Module / 파티클 효과의 상위 구조 3단계
- [ ] Particle Spawn / 파티클 생성과 매 프레임 갱신 단계
- [ ] CPU vs GPU Simulation / 연산 부담을 CPU와 GPU 중 어디서 질지

### Audio

- [ ] Sound Cue and Sound Wave / 재생 로직과 원본 오디오 파일
- [ ] MetaSounds / 노드 기반으로 절차적으로 만드는 사운드
- [ ] Attenuation and Spatialization / 거리에 따른 감쇠와 입체 음향 배치

---

# PART 4 · Advanced Systems

## 13. AI & Navigation

- [ ] AIController / 폰을 대신 조종하는 AI 두뇌 액터
- [ ] Navigation Mesh / Nav Modifier로 조정하는 AI 이동 가능 영역 메시
- [ ] Behavior Tree / Task·Decorator·Service 노드로 짜는 의사결정 트리
- [ ] Blackboard / 행동 트리가 참조하는 AI 공유 메모리
- [ ] AI Perception / 시각·청각으로 대상을 감지하는 기능
- [ ] EQS (Environment Query System) / 주변 환경을 점수로 평가해 위치 선택

## 14. Multiplayer & Replication

### Networking Model

- [ ] Client-Server Architecture / 서버 겸 클라이언트 vs 전용 서버 구조
- [ ] Network Authority / HasAuthority로 판정하는 서버만의 최종 권한

### Replication

- [ ] Property Replication / Replicated·ReplicatedUsing으로 값 자동 동기화
- [ ] RPC / Server·Client·Multicast로 갈리는 원격 호출
- [ ] Reliable vs Unreliable / 도착 보장 여부에 따른 복제 신뢰도
- [ ] Relevancy / Net Cull Distance로 먼 액터를 복제에서 제외

### Perceived Quality

- [ ] Client Prediction and Server Reconciliation / 클라이언트 선처리 후 서버 값으로 보정
- [ ] Online Subsystem / 세션 생성과 매치메이킹 연동 계층

## 15. Performance & Profiling

### Profiling Tools

- [ ] Stat Command / 콘솔에 치는 stat fps 등 실시간 성능 수치
- [ ] Unreal Insights / 프레임별 성능을 타임라인으로 분석하는 툴
- [ ] GPU Visualizer / GPU 렌더 패스별 소요 시간 시각화

### Optimization Techniques

- [ ] LOD and HLOD / 거리별 메시 단순화와 그 묶음 처리
- [ ] Instanced Static Mesh and Hierarchical ISM / 동일 메시를 한 드로우콜로 대량 배치
- [ ] Draw Call / Material Slot 줄이기
- [ ] Tick Optimization / Tick Interval, Tick 비활성화
- [ ] Texture Streaming / 화면에 필요한 해상도만 메모리에 로드

---

# PART 5 · Deployment and Collaboration

## 16. Packaging & Team Workflow

### Build & Packaging

- [ ] Build Configuration / Debug·Development·Shipping 세 단계 빌드 설정
- [ ] Cook and Package Project / 에셋을 플랫폼용으로 변환해 패키징
- [ ] Platform Target / Windows·Android·iOS 등 배포할 플랫폼별 빌드 타깃 선택 `별도`
- [ ] Pak File, Chunk, DLC / 패키징된 에셋 압축·분할 배포 단위
- [ ] Automation Tool / UAT 등 커맨드라인으로 자동화하는 빌드 도구

### Collaboration

- [ ] Version Control / Perforce·Git LFS 등 대용량 에셋 버전 관리
- [ ] Asset Lock / Binary Asset 충돌 관리
- [ ] Config File Hierarchy / DefaultEngine.ini 등 겹쳐 쓰는 설정 파일

---

# 이 로드맵 밖

- 게임 개발 전반 · 수학 · 그래픽스 이론 `software/role-based/game-developer.md`
- 게임 서버 `software/role-based/server-side-game-developer.md`
- 다른 엔진 `software/skill-based/Game-Dev/unity.md`, `godot.md`
- C++ 언어 `software/skill-based/Languages/cpp.md`
- 버전 관리 `software/skill-based/Infra-DevOps/git-github.md`
- 소프트웨어 설계 `software/skill-based/CS-Theory/software-design-architecture.md`
