# Foundry `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Foundry

## 1. What is Foundry?

### Overview of Foundry / What is it?

- [ ] Rust-based Solidity Toolchain / Rust로 짠 스마트 컨트랙트 개발 도구
- [ ] Tests Written in Solidity / 테스트를 JS 아닌 Solidity로 쓰는 방식
- [ ] Toolchain Composition / 빌드·호출·로컬노드·REPL 네 명령으로 나뉜 구성
- [ ] Foundry vs Hardhat / Solidity 테스트냐 JS 설정이냐의 갈림
- [ ] foundryup / 툴체인을 설치·업데이트하는 명령

## 2. Project Structure

- [ ] forge init / 프로젝트 뼈대를 생성하는 명령
- [ ] Layout / 소스·테스트·스크립트·의존성을 나눠 두는 폴더 관례
- [ ] foundry.toml / 컴파일러·경로 등 설정을 담는 파일
- [ ] Profiles / 설정 묶음을 이름으로 갈아 끼우는 방법
- [ ] Remappings / import 경로를 실제 폴더로 잇는 매핑
- [ ] Dependency Management / npm 아닌 git 서브모듈로 받는 방식
- [ ] forge-std Library / 테스트에 필요한 유틸을 모은 표준 라이브러리
- [ ] forge update and forge remove / 의존성을 최신화·제거하는 명령
- [ ] Soldeer Package Manager / npm 스타일 별도 패키지 매니저 `선택`

## 3. Building

- [ ] forge build / 컨트랙트를 컴파일하는 명령
- [ ] Output Artifacts / 컴파일 결과가 쌓이는 out 폴더
- [ ] Compiler Settings / solc 버전·최적화 옵션을 정하는 설정
- [ ] forge clean / 빌드 산출물을 지우는 명령
- [ ] forge fmt / Solidity 코드를 정렬하는 포매터
- [ ] forge inspect / ABI·스토리지 배치 등을 조회하는 명령
- [ ] Contract Size / 컨트랙트 바이트코드 크기를 재는 명령

---

# PART 2 · Writing Tests in Solidity

## 4. Writing Tests in Solidity

### Test Contracts

- [ ] Test Base / Test 컨트랙트를 상속해 테스트를 짜는 기반
- [ ] setUp / 각 테스트 전에 초기 상태를 세팅하는 함수
- [ ] test_ Prefix Convention / 함수명 앞에 test_를 붙이는 인식 규칙
- [ ] Naming Convention / 실패·퍼즈 테스트를 구분하는 이름 규칙
- [ ] Assertions / 값을 비교해 통과·실패를 가르는 함수
- [ ] Console Logging / 테스트 중 값을 찍어 확인하는 방법

### Running

- [ ] forge test / 이름으로 테스트를 골라 돌리는 옵션
- [ ] Verbosity Levels / 트레이스 출력 수준을 조절하는 단계
- [ ] Trace Reading / 호출·실패 흐름을 트레이스로 읽는 방법
- [ ] Gas Report / 함수별 가스 소비를 표로 보는 옵션
- [ ] forge snapshot / 가스 사용량 변화를 비교하는 명령

## 5. Cheatcodes

### State Manipulation

- [ ] vm.prank and vm.startPrank / 다음 호출·이후 전체 호출자를 위장
- [ ] vm.deal / 주소의 ETH 잔액을 강제로 세팅하는 치트코드
- [ ] vm.warp and vm.roll / 블록 시간·번호를 조작하는 치트코드
- [ ] vm.store and vm.load / 스토리지 슬롯을 직접 읽고 쓰는 치트코드
- [ ] vm.etch / 주소에 임의 바이트코드를 심는 치트코드
- [ ] vm.mockCall / 특정 호출의 반환값을 가짜로 지정하는 치트코드

### Expectation Assertions

- [ ] vm.expectRevert / 다음 호출이 실패해야 통과하는 단언
- [ ] vm.expectEmit / 특정 이벤트 발생을 검증하는 단언
- [ ] vm.expectCall / 특정 호출이 일어났는지 검증하는 단언
- [ ] vm.label / 트레이스에 주소 대신 이름을 표시하는 치트코드

### Environment and External I/O

- [ ] Environment / .env 값을 타입별로 읽어오는 치트코드
- [ ] File IO · FFI / 파일을 읽거나 외부 프로그램을 실행하는 치트코드
- [ ] Snapshot / 상태를 저장했다 되돌리는 치트코드
- [ ] Signing / 개인키로 서명하고 주소를 구하는 치트코드

## 6. Fuzz Testing

- [ ] Property-based Testing / 무작위 입력으로 규칙 위반을 찾는 방식
- [ ] Fuzz Test Signature / 함수 인자에 랜덤값을 자동으로 채우는 방식
- [ ] Input Constraint / 유효하지 않은 입력을 걸러내는 방법
- [ ] Fuzz Config / 반복 횟수·난수 시드를 정하는 설정
- [ ] Counterexample Reproduction / 실패를 만든 입력값을 재현하는 방법
- [ ] Choosing Good Properties / 항상 참이어야 할 성질을 고르는 기준

## 7. Invariant Testing

- [ ] invariant_ Prefix / 함수명 앞에 invariant_를 붙이는 인식 규칙
- [ ] Handler Contract / 상태를 변화시키는 호출을 모아둔 컨트랙트
- [ ] targetContract, targetSelector, excludeContract / 퍼징 대상 컨트랙트·함수를 제한하는 설정
- [ ] Ghost Variables / 상태 추적용으로 테스트에만 두는 변수
- [ ] Bounded vs Open Testing / 입력 범위를 제한할지 열어둘지의 구분
- [ ] Config / 반복·호출 깊이·revert 처리 방식 설정
- [ ] Failing Sequence Replay / 실패로 이어진 호출 순서를 재현하는 방법

## 8. Fork and Coverage

- [ ] Fork Test / 실제 체인 상태를 가져와 테스트하는 방법
- [ ] Fork Block Pinning / 포크 상태를 특정 블록 번호로 고정하는 방법
- [ ] Multi-fork / 여러 체인 포크를 만들고 전환하는 치트코드
- [ ] RPC Cache / 포크에 쓸 RPC 주소를 등록하는 설정
- [ ] Differential Testing / FFI로 다른 구현과 결과를 대조하는 방법
- [ ] forge coverage / 테스트가 덮은 코드 비율을 재는 명령

---

# PART 3 · Scripting and CLI Tools

## 9. Forge Script

- [ ] Script Base / Script 컨트랙트를 상속해 배포 로직을 짜는 기반
- [ ] run Entry Point / 스크립트 실행이 시작되는 함수
- [ ] vm.startBroadcast and vm.stopBroadcast / 실제 전송 구간을 감싸는 치트코드
- [ ] Simulation vs Broadcast / 시뮬레이션만 할지 실제로 보낼지의 구분
- [ ] Broadcast Artifacts / 전송한 트랜잭션 기록이 쌓이는 폴더
- [ ] Deterministic Deploy / 같은 주소로 배포되게 하는 CREATE2 방식
- [ ] Verification / 배포한 컨트랙트 소스를 검증받는 옵션
- [ ] Key Handling / 개인키를 넘기는 여러 방법
- [ ] Hardware Wallet / 하드웨어 지갑으로 서명하는 옵션
- [ ] Resuming / 중단된 배포를 이어서 진행하는 옵션

## 10. Cast

- [ ] cast call and cast send / 읽기·쓰기 호출을 나눠 보내는 명령
- [ ] Chain State Query / 잔액·논스·코드 등을 조회하는 명령
- [ ] ABI Encoding / 함수 호출 데이터를 인코딩하는 명령
- [ ] Unit Conversion / 단위·진법을 서로 바꾸는 명령
- [ ] Signature Lookup / 함수 시그니처·셀렉터를 구하는 명령
- [ ] Transaction Lookup / 트랜잭션·영수증 정보를 조회하는 명령
- [ ] cast run / 과거 트랜잭션을 재실행해 디버깅하는 명령
- [ ] cast wallet / 지갑 생성·서명·주소 확인을 묶은 명령
- [ ] cast interface / ABI로부터 인터페이스 코드를 생성하는 명령

## 11. Anvil and Chisel

- [ ] Local EVM Node / 로컬에서 띄우는 테스트용 EVM 노드
- [ ] Prefunded Accounts / 니모닉으로 미리 잔액을 채운 테스트 계정
- [ ] Forking / 실제 체인 상태를 복제해 로컬에 띄우는 방법
- [ ] Mining Control / 블록 생성 주기·자동 채굴을 조절하는 옵션
- [ ] anvil_ RPC Methods / 노드 상태를 직접 조작하는 전용 RPC
- [ ] State Dump · Load / 노드 상태를 파일로 저장·복원하는 기능
- [ ] Chisel / Solidity 코드를 한 줄씩 실행해보는 REPL

---

# PART 4 · Advanced Topics and Operations

## 12. Gas and Optimization Workflow

- [ ] Gas Snapshot Diff / 가스 사용량 증가를 비교해 감시하는 방법
- [ ] Gas Report Interpretation / 가스 리포트에서 병목 함수를 읽는 방법
- [ ] Optimizer Runs Tuning / 배포 비용과 실행 비용의 균형을 맞추는 값
- [ ] via-ir Trade-off / 컴파일이 느려져도 최적화를 더 얻을지의 판단
- [ ] Assembly Optimization Validation / 인라인 어셈블리가 원본과 같은지 검증

## 13. Security Tooling Integration

- [ ] Slither Integration / 정적 분석 도구를 파이프라인에 붙이는 방법
- [ ] Echidna · Medusa / 별도 퍼저로 더 깊게 검증하는 도구 `선택`
- [ ] Halmos / 심볼릭 실행으로 모든 경로를 검증하는 도구 `선택`
- [ ] Invariant Suite as Audit Deliverable / 테스트 모음을 감사 자료로 제출하는 방식

## 14. CI and Workflow

- [ ] GitHub Actions / CI에서 Foundry를 설치하는 공식 액션
- [ ] forge fmt --check / 포맷 위반을 실패로 처리하는 CI 검사
- [ ] Test Matrix / 여러 solc 버전으로 동시에 테스트하는 구성
- [ ] RPC Secret Management / RPC 키를 CI 시크릿으로 감추는 방법
- [ ] Foundry + Hardhat Coexistence / 한 프로젝트에서 두 툴체인을 같이 쓰는 구성
- [ ] Library Publishing / 버전 태그로 라이브러리를 배포하는 방법

---

# 이 로드맵 밖

- 블록체인 전반 `software/role-based/blockchain.md`
- 스마트 컨트랙트 언어 `software/skill-based/Blockchain/solidity.md`
- 다른 프레임워크 `software/skill-based/Blockchain/hardhat.md`
- 클라이언트 라이브러리 `software/skill-based/Blockchain/ethersjs.md`, `web3js.md`
- Rust `software/skill-based/Languages/rust.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/git-github.md`
