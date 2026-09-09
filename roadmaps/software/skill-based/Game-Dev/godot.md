# Godot `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Godot

## 1. What is Godot?

### Overview of Godot / What is it?

- [ ] Open Source Engine / MIT 라이선스 무료 공개 엔진
- [ ] Node & Scene Architecture / 모든 것이 Node이고 쌓아 Scene을 구성
- [ ] 2D / 3D 별도 렌더러

### Godot vs Other Engines

- [ ] Godot vs Unity / Unreal 대비 씬 트리·시그널 중심 구조

### Getting Started

- [ ] Godot 4 vs Godot 3 Differences / 렌더러·GDScript 문법 등 주요 차이
- [ ] Standard vs .NET Build / C# 지원 여부로 빌드 방식 선택 `택 1`
- [ ] Project Manager / 프로젝트 생성

## 2. Godot Editor

### Editor Layout

- [ ] Scene Dock / Node Tree로 씬 구성을 보여주는 패널
- [ ] FileSystem Dock / 프로젝트 파일을 탐색하는 패널
- [ ] Inspector Dock / 선택한 Node의 속성을 편집하는 패널
- [ ] Viewport / 2D, 3D, Script, AssetLib 전환
- [ ] Output / 콘솔 로그와 디버거를 보여주는 창

### Navigation

- [ ] Transform Tool / 이동·회전·크기로 Node를 조작하는 도구
- [ ] Play Scene, Play Project, Remote Tree / 씬 단위 실행과 전체 실행 구분

### Configuration

- [ ] Project Settings / Input Map·Display·Rendering을 잡는 전역 설정
- [ ] Renderer Selection / Forward+·Mobile·Compatibility 중 선택

## 3. Node & Scene

### Node

- [ ] Node Hierarchy / 부모-자식으로 이어지는 Node 구조
- [ ] Node Type / Node2D·Node3D·Control 등 공간별 종류
- [ ] Node Lifecycle / _ready·_process 등 생명주기 콜백 순서
- [ ] Groups / 여러 Node를 묶어 한 번에 다루는 태그
- [ ] Node Path / get_node, $ 문법, Unique Name

### Scene

- [ ] Scene as a Reusable Node Tree / 재사용 가능한 Node 묶음 단위
- [ ] Instancing / Scene 중첩
- [ ] Scene Tree / SceneTree·Root Viewport로 보는 씬 계층
- [ ] Scene Transition / change_scene_to_file로 씬 전환
- [ ] Autoload (Singleton) / 모든 씬에서 접근 가능한 전역 Node

---

# PART 2 · Scripting

## 4. GDScript

### Language Basics

- [ ] Variables and Types / var·const로 하는 변수 선언과 타입 지정
- [ ] Functions / func, 기본 인자, 반환 타입
- [ ] Control Flow and Loops / match·for·while로 하는 분기와 반복
- [ ] Class / class_name·extends로 하는 클래스 정의와 상속

### Godot-Specific Syntax

- [ ] Export Variable / @export, @export_range로 Inspector에 노출
- [ ] @onready / 노드가 준비된 뒤 값을 초기화하는 시점
- [ ] await and Coroutine / 신호·타이머를 기다리는 비동기 처리

### Scripting Language `택 1`

- [ ] GDScript / Godot 전용 파이썬 스타일 스크립트 언어 `추천`
- [ ] C# (.NET) / .NET 빌드로 쓰는 C# 스크립트
- [ ] GDExtension / C++ 등 네이티브 코드로 엔진 확장

## 5. Signals & Communication

- [ ] Signal Concept / Observer Pattern 기반 발행-구독 알림
- [ ] Built-in Signal Connection / 에디터, 코드
- [ ] Custom Signal / signal 선언, emit_signal
- [ ] Callable / bind로 인자를 미리 묶어 값으로 넘기는 방법
- [ ] Group Call / call_group으로 그룹 전체에 메서드 호출
- [ ] Node Reference Strategy / 위로는 Signal, 아래로는 직접 호출

## 6. Input

- [ ] Input Map / Action 정의
- [ ] Input Polling / Input.is_action_pressed로 매 프레임 확인
- [ ] Input Event / _input, _unhandled_input, _gui_input 콜백 구분
- [ ] InputEvent Type / Key, MouseButton, JoypadMotion 등 입력 종류
- [ ] Event Consumption / set_input_as_handled로 전파 차단

---

# PART 3 · Building a Game

## 7. 2D Game Development

### 2D Basics

- [ ] Node2D / Transform·Z Index로 정하는 2D 좌표와 순서
- [ ] Sprite2D and AnimatedSprite2D / 이미지·프레임 애니메이션 출력 Node
- [ ] Texture Filter / Pixel Art 설정
- [ ] Camera2D / Limit·Smoothing으로 정하는 화면 시점 범위

### Level Design

- [ ] TileMapLayer and TileSet / 타일 배치 레이어와 타일 모음
- [ ] Terrain (Autotile) / 주변 타일에 맞춰 자동 연결되는 지형
- [ ] Physics Layer in TileSet / 타일별 충돌 속성 지정
- [ ] Parallax Background / 배경을 원근감 있게 다중 스크롤

## 8. 3D Game Development

- [ ] Node3D / Basis·Transform3D로 담는 위치·회전·크기
- [ ] MeshInstance3D / 메시 출력과 재질 덮어쓰기
- [ ] Camera3D / FOV·Projection으로 정하는 3D 시야
- [ ] Light3D / Directional·Omni·Spot 등 조명 종류
- [ ] WorldEnvironment / Sky·Tonemap·SSAO 등 환경 효과 설정
- [ ] GI / VoxelGI·SDFGI·LightmapGI 등 전역 조명 계산
- [ ] CSG Node / 레벨 프로토타이핑
- [ ] Import Workflow / glTF와 Import Dock으로 모델 가져오기

## 9. Physics

### Body

- [ ] CharacterBody2D/3D / move_and_slide로 이동하는 캐릭터 바디
- [ ] RigidBody2D/3D / 중력 등 물리 시뮬레이션을 받는 바디
- [ ] StaticBody and AnimatableBody / 움직이지 않는 충돌체와 코드로 움직이는 충돌체
- [ ] Area2D/3D / body_entered Signal로 겹침 감지하는 영역

### Shape & Layer

- [ ] CollisionShape and CollisionPolygon / 충돌 판정용 도형 정의
- [ ] Collision Layer vs Mask / 충돌 대상을 구분하는 레이어 체계
- [ ] Raycast / RayCast Node와 intersect_ray로 하는 충돌 검사
- [ ] Physics Material / Bounce·Friction 값으로 정하는 반발·마찰

## 10. Animation

- [ ] AnimationPlayer / Track·Keyframe으로 재생하는 애니메이션
- [ ] Call Method Track and Property Track / 메서드 호출·속성 변경 트랙
- [ ] AnimationTree / State Machine·BlendSpace로 하는 애니메이션 전환
- [ ] Skeleton, Bone, IK / 뼈대 구조와 역운동학
- [ ] Tween / create_tween과 Easing으로 값을 부드럽게 보간
- [ ] Path2D/3D and PathFollow / 경로를 따라 이동하는 Node

## 11. UI (Control Node)

- [ ] Control Node / Rect·Focus를 가진 UI 기본 Node
- [ ] Anchor & Offset / Layout Preset으로 정하는 UI 배치 기준
- [ ] Container / VBox·HBox·Grid로 자식 UI를 자동 정렬하는 Node
- [ ] Size Flags / Expand·Fill로 정하는 UI 크기 규칙
- [ ] Common Control / Button·Label·LineEdit 등 기본 UI 부품
- [ ] Theme / StyleBox·Theme Override로 UI 스타일 일괄 관리
- [ ] CanvasLayer / UI 분리
- [ ] Viewport Resolution Handling / Stretch Mode로 하는 해상도 대응

## 12. Audio & Particles

### Audio

- [ ] AudioStreamPlayer, 2D, 3D / 위치 유무에 따른 소리 재생 Node
- [ ] Audio Bus / 소리 채널별 이펙트 적용
- [ ] Import Settings / Loop·Compression으로 하는 오디오 설정

### Particle & Shader

- [ ] GPUParticles and CPUParticles / GPU·CPU 기반 파티클 처리 방식
- [ ] Particle Process Material / 파티클 생성·움직임 규칙 정의
- [ ] Shader / Godot 전용 셰이더 언어
- [ ] Visual Shader / 노드 연결로 짜는 셰이더
- [ ] Shader Type / canvas_item, spatial 등 적용 대상 구분

---

# PART 4 · Advanced Topics and Deployment

## 13. Resource & Project Architecture

### Resource

- [ ] Resource Concept / .tres·.res로 저장하는 직렬화 데이터
- [ ] Custom Resource / 데이터 정의
- [ ] ResourceLoader / preload·load의 로드 시점 차이

### Project Structure

- [ ] user:// vs res:// Paths / 사용자 저장 경로와 프로젝트 내부 경로
- [ ] Save, Load, ConfigFile, JSON, Binary / 데이터 저장 형식 선택지
- [ ] Editor Plugin / addons로 에디터 기능 확장

### Performance

- [ ] Profiler / Monitor Tab에서 보는 프레임·메모리 측정
- [ ] Object Pooling / Node 재사용
- [ ] Draw Call / MultiMesh로 메시를 한 번에 그려 호출 절감

## 14. Export & Deployment

### Export

- [ ] Export Template Installation / 플랫폼별 빌드에 필요한 템플릿 설치
- [ ] Export Preset / Feature Tag로 하는 플랫폼별 빌드 설정
- [ ] Platform / Windows·macOS·Android 등 지원 배포 대상
- [ ] Export Filter / PCK로 묶는 리소스 선별과 패키징

### Collaboration and Deployment

- [ ] Version Control / .gitignore, 텍스트 씬 포맷
- [ ] Headless Export / CI 자동화
- [ ] Multiplayer / MultiplayerSpawner, MultiplayerSynchronizer로 상태 동기화 `선택`

---

# 이 로드맵 밖

- 게임 개발 전반 · 수학 · 그래픽스 이론 `software/role-based/game-developer.md`
- 게임 서버 `software/role-based/server-side-game-developer.md`
- 다른 엔진 `software/skill-based/Game-Dev/unity.md`, `unreal-engine.md`
- C++ · Python `software/skill-based/Languages/cpp.md`, `python.md`
- 버전 관리 `software/skill-based/Infra-DevOps/git-github.md`
