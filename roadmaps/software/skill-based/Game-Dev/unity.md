# Unity `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Unity

## 1. What is Unity?

### Overview of Unity / What is it?

- [ ] Real-time 2D / 실시간으로 화면을 그리는 2D·3D 게임 엔진
- [ ] Component-based Architecture / GameObject에 기능 조각을 붙여 조립하는 설계
- [ ] C# Scripting Runtime / 게임 로직을 실행하는 C# 실행 환경
- [ ] Cross-platform Deployment / 하나의 프로젝트를 여러 플랫폼용으로 빌드

### Unity vs Other Engines

- [ ] Unity vs Unreal Engine / 컴포넌트 조립형과 C++ 이중 구조의 차이
- [ ] Licensing / 매출 규모에 따라 갈리는 요금제 등급

### Installation and Version Selection

- [ ] Unity Hub / 여러 버전·프로젝트를 관리하는 런처
- [ ] LTS vs Tech Stream / 장기 지원판과 최신 기능판 중 선택
- [ ] Render Pipeline Selection / 프로젝트 시작 시 렌더링 방식을 고르는 단계 `택 1`

## 2. Unity Editor

### Editor Layout

- [ ] Scene View / 오브젝트를 배치하고 편집하는 3D 작업 공간
- [ ] Game View / 카메라가 실제로 찍는 최종 화면 미리보기
- [ ] Hierarchy Window / 씬에 있는 GameObject 목록과 부모-자식 구조
- [ ] Project Window / 프로젝트에 포함된 에셋 파일 탐색기
- [ ] Inspector Window / 선택한 GameObject의 컴포넌트와 값 편집
- [ ] Console Window / 로그·경고·에러 메시지 출력창

### Scene Navigation

- [ ] Transform Tools / 오브젝트를 이동·회전·크기조절하는 도구
- [ ] Snapping / 격자·정점 단위로 배치를 맞추는 기능

### Editor Environment

- [ ] Play Mode vs Edit Mode / 실행 중 상태와 편집 중 상태의 구분
- [ ] Project Settings / 프로젝트 전역 설정과 에디터 개인 설정
- [ ] Package Manager / 엔진 기능·라이브러리를 추가 설치하는 창

## 3. GameObject & Scene

### GameObject

- [ ] GameObject / Component를 담는 빈 그릇
- [ ] Transform / 위치·회전·크기와 부모-자식 계층을 갖는 컴포넌트
- [ ] Tag / 오브젝트를 식별하는 이름표와 그룹 분류 체계
- [ ] Active vs Enabled / GameObject 활성과 컴포넌트 활성의 구분

### Scene

- [ ] Scene Asset / 게임의 한 장면을 저장한 파일
- [ ] Scene Loading / 씬을 코드로 불러오고 겹쳐 로드하는 방법

### Camera & Light

- [ ] Camera / 원근·평행 투영 중 화면을 그리는 방식을 정하는 컴포넌트
- [ ] Light Type / 빛이 퍼지는 형태에 따른 네 가지 조명 종류

---

# PART 2 · C# Scripting

## 4. Scripting Fundamentals

### MonoBehaviour

- [ ] MonoBehaviour Lifecycle / 스크립트가 자동 호출되는 순서와 시점
- [ ] Coroutine / 여러 프레임에 걸쳐 나눠 실행하는 함수
- [ ] Inspector Serialization / 필드 값을 인스펙터에 노출해 편집
- [ ] Script Execution Order / 여러 스크립트의 실행 순서를 강제 지정

### Component References

- [ ] GetComponent / 붙어있는 컴포넌트를 찾아 참조로 가져오는 함수
- [ ] Cost of Find APIs / 이름·타입으로 찾는 함수의 느린 성능
- [ ] Inspector Injection / 코드에서 찾지 않고 인스펙터로 참조를 미리 연결 `추천`

### Time and Math

- [ ] Time.deltaTime, fixedDeltaTime, timeScale / 프레임 간격과 시간 흐름을 다루는 값들
- [ ] Vector3 / 좌표·회전을 다루는 수학 구조체와 함수
- [ ] Mathf / 보간·범위제한 등 게임 수학 함수 모음

### Data and Debugging

- [ ] ScriptableObject / 씬에 안 묶이고 재사용하는 데이터 컨테이너

## 5. Input & Character Movement

### Input System `택 1`

- [ ] Input System Package / 새 방식의 입력 처리 패키지 `추천`
- [ ] Input Manager (Legacy) / 구버전부터 있던 축 기반 입력 설정

### Input System

- [ ] Input Actions Asset / 입력 동작을 모아 정의한 에셋 파일
- [ ] Action Map / 상황별 입력 묶음과 키·버튼 연결
- [ ] PlayerInput Component / 입력 이벤트를 스크립트로 전달하는 컴포넌트
- [ ] Control Scheme / 키보드·게임패드 등 장치 전환 대응

### Movement Approaches

- [ ] Character Controller / 캡슐 충돌로 걷는 이동을 처리하는 컴포넌트
- [ ] Rigidbody-based Movement / 물리 힘으로 밀어서 움직이는 방식

## 6. Physics

### Rigidbody

- [ ] Rigidbody / 질량·저항으로 물리 반응을 갖게 하는 컴포넌트
- [ ] Kinematic vs Dynamic / 물리 영향을 받을지 코드로만 움직일지 구분
- [ ] Force Mode / 힘을 가하는 방식(지속·순간·속도변경)의 구분

### Collider

- [ ] Collider Shape / 충돌 판정 영역의 모양 종류
- [ ] Trigger vs Collision / 통과 감지와 물리 충돌 반응의 구분
- [ ] Collision Callback / 충돌·감지 발생 시 자동 호출되는 함수
- [ ] Physics Material / 마찰·탄성을 정의하는 물리 재질 에셋

### Queries and Configuration

- [ ] Raycast / 직선·구 모양으로 충돌체를 감지하는 질의
- [ ] Layer Collision Matrix / 레이어끼리 충돌 여부를 정하는 표
- [ ] Fixed Timestep / 물리 연산 주기와 화면 보간 처리
- [ ] Physics2D Differences / 2D 전용으로 따로 있는 물리 컴포넌트

---

# PART 3 · Content Creation

## 7. Assets & Prefabs

### Asset Pipeline

- [ ] Import Settings / 에셋을 가져올 때 적용되는 처리 옵션
- [ ] Texture Import / 압축·밉맵·스프라이트 방식을 정하는 설정
- [ ] Model Import / 3D 모델 파일을 가져올 때의 리깅·재질 설정
- [ ] .meta File / 에셋을 고유 ID로 추적하는 숨김 파일

### Prefab

- [ ] Prefab Asset vs Instance / 원본 자산과 씬에 배치된 사본의 구분
- [ ] Prefab Variant / 원본을 상속해 일부만 바꾼 파생 프리팹
- [ ] Override / 인스턴스에서 바꾼 값을 원본에 반영·되돌리기
- [ ] Instantiate / 프리팹을 복제 생성하고 제거하는 함수
- [ ] Object Pooling / 생성·삭제 대신 오브젝트를 재활용하는 기법

## 8. Rendering & Materials

### Render Pipeline `택 1`

- [ ] Universal Render Pipeline (URP) / 성능과 품질 균형을 맞춘 표준 파이프라인 `추천`
- [ ] Built-in Render Pipeline / 예전부터 있던 기본 렌더링 방식
- [ ] High Definition Render Pipeline (HDRP) / 고사양 그래픽 전용 파이프라인

### Material & Shader

- [ ] Material / Shader 관계
- [ ] PBR Workflow / 실제 재질감을 표현하는 물리 기반 렌더링 방식
- [ ] Shader Graph / 코드 대신 그래프로 셰이더를 만드는 도구

### Lighting

- [ ] Realtime vs Baked Lighting / 즉시 계산할지 미리 구워둘지 조명 방식 선택
- [ ] Lightmapping / 조명 계산 결과를 텍스처로 미리 구워두기
- [ ] Light Probe / 움직이는 오브젝트에 주변 조명 정보를 전달

### Post-Processing

- [ ] Post Processing Volume / 화면 전체에 색·빛 보정 효과를 씌우는 영역

## 9. Animation & Cinematics

### Animation Clip

- [ ] Animation Window / 키프레임을 찍어 애니메이션을 편집하는 창
- [ ] Animation Event / 애니메이션 재생 중 특정 시점에 함수 호출

### Animator

- [ ] Animator Controller / 애니메이션 상태 전환을 관리하는 컴포넌트
- [ ] Transition / 조건 값에 따라 다른 동작으로 넘어가는 연결
- [ ] Blend Tree / 여러 동작을 파라미터 값으로 부드럽게 섞기
- [ ] Root Motion / 애니메이션 자체의 이동을 캐릭터 위치에 반영

### Rig & Staging

- [ ] Humanoid vs Generic Rig / 표준 골격 재사용 여부에 따른 리그 구분
- [ ] Timeline / 컷신 연출과 Cinemachine 카메라 전환을 다루는 도구

## 10. UI

### UI System `택 1`

- [ ] uGUI (Canvas) / 화면에 UI를 그리는 캔버스 기반 시스템 `추천`
- [ ] UI Toolkit / 웹처럼 마크업으로 UI를 만드는 최신 시스템

### uGUI

- [ ] Canvas / UI를 담는 최상위 컨테이너 컴포넌트
- [ ] RectTransform / UI 요소의 위치·크기를 정하는 사각형 좌표계
- [ ] Canvas Scaler / 해상도 대응
- [ ] Layout Group / 자식 UI를 자동 정렬·배치하는 컴포넌트
- [ ] UI Component / 버튼·슬라이더 등 미리 만들어진 UI 부품
- [ ] TextMeshPro / 선명하게 렌더링되는 고급 텍스트 컴포넌트

### UI Toolkit

- [ ] UXML, USS, UI Builder / UI Toolkit이 쓰는 구조·스타일·편집 도구

## 11. Audio

- [ ] Audio Source / 소리를 재생하고 듣는 위치를 정하는 컴포넌트
- [ ] Spatial Blend / 소리를 평면적으로 들을지 입체적으로 들을지 비율
- [ ] Audio Mixer / 여러 소리를 그룹으로 묶어 조절하는 믹서
- [ ] Load Type / 오디오 파일을 메모리에 올리는 방식 설정
- [ ] Particle System / 불꽃·연기 같은 입자 효과를 만드는 컴포넌트

---

# PART 4 · Advanced Topics and Optimization

## 12. Performance Optimization

### Profiling

- [ ] Profiler / CPU·GPU·메모리 사용량을 실시간 측정하는 도구
- [ ] Frame Debugger / 한 프레임의 렌더링 과정을 단계별로 확인

### Rendering Cost

- [ ] Draw Call, Batching, SRP Batcher / 렌더링 호출 횟수를 줄이는 방법들
- [ ] GPU Instancing / 같은 메시를 한 번에 대량으로 그리는 기법
- [ ] LOD Group / 멀리 있으면 저사양으로 바꾸고 안 보이면 생략

### Script Cost

- [ ] Reducing GC Allocation / 가비지 컬렉션으로 인한 끊김을 줄이기
- [ ] Minimizing Update Calls / 매 프레임 도는 코드 수를 줄이는 최적화
- [ ] Asynchronous Loading / 멈춤 없이 백그라운드에서 리소스 불러오기

## 13. Advanced Systems

### Large Project Structure

- [ ] Assembly Definition (asmdef) / 스크립트를 묶어 컴파일 단위를 나누는 파일
- [ ] Addressables / 주소로 에셋을 비동기 로드·관리하는 시스템
- [ ] AssetBundle / 에셋을 따로 묶어 배포하는 구버전 패키징 방식

### Runtime Performance Scaling

- [ ] Job System / 작업을 여러 코어에 나눠 병렬 처리하는 시스템
- [ ] DOTS / 컴포넌트를 데이터 배열로 다뤄 성능을 높이는 구조 `선택`

### Networking `선택`

- [ ] Netcode for GameObjects / GameObject를 네트워크로 동기화하는 공식 패키지
- [ ] Client-Server Model / 호스트·전용 서버 중 구조를 정하는 방식
- [ ] Server Authority / 판정을 서버가 맡고 클라이언트는 미리 예측

---

# PART 5 · Deployment and Collaboration

## 14. Build & Deployment

### Build Settings

- [ ] Build Target / 빌드할 플랫폼을 고르고 전환하는 설정
- [ ] Scripting Backend / C# 코드를 실행 파일로 변환하는 방식
- [ ] Player Settings / 아이콘·화면방향 등 빌드별 세부 설정

### Platform-Specific Deployment

- [ ] Mobile / 안드로이드·iOS로 내보내는 빌드
- [ ] Desktop / 윈도우·맥 실행 파일로 빌드
- [ ] WebGL / 브라우저에서 바로 실행되는 빌드
- [ ] Console / 콘솔 빌드에 필요한 제조사 라이선스 `별도`

### Automation

- [ ] Command Line Build / 에디터 없이 명령줄로 빌드 자동화
- [ ] Unity Cloud Build / 클라우드에서 자동으로 빌드해주는 서비스

## 15. Project Workflow

### Collaboration

- [ ] Version Control / 대용량 에셋까지 다루는 형상관리 설정
- [ ] Asset Serialization Mode / 에셋을 사람이 읽을 텍스트로 저장하는 설정
- [ ] Smart Merge (UnityYAMLMerge) / 씬·프리팹 충돌을 자동 병합하는 도구
- [ ] Folder Convention / 팀이 공유하는 폴더·이름 규칙

### Quality Management

- [ ] Editor Scripting / 인스펙터 화면 자체를 커스텀 제작
- [ ] Unity Test Framework / 편집·실행 모드에서 자동 테스트하는 프레임워크

---

# 이 로드맵 밖

- 게임 개발 전반 · 수학 · 그래픽스 이론 `software/role-based/game-developer.md`
- 게임 서버 `software/role-based/server-side-game-developer.md`
- 다른 엔진 `software/skill-based/Game-Dev/unreal-engine.md`, `godot.md`
- 모바일 배포 `software/role-based/android.md`, `software/role-based/ios.md`
- 버전 관리 `software/skill-based/Infra-DevOps/git-github.md`
- 테스트 전략 `software/role-based/qa.md`
