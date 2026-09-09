# Hardhat `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Hardhat

## 1. What is Hardhat?

### Overview of Hardhat / What is it?

- [ ] Ethereum Development Environment / 이더리움 계약 개발에 특화된 통합 환경
- [ ] JavaScript · TypeScript Ecosystem / JS·TS 패키지와 툴체인을 그대로 쓰는 기반
- [ ] Task Runner + Plugin Architecture / 태스크와 플러그인으로 기능을 조립하는 구조
- [ ] Hardhat vs Truffle / 먼저 나온 프레임워크에서 갈아탄 이유
- [ ] Hardhat vs Foundry / JS 생태계냐 Rust 속도냐로 가르는 기준

### Prerequisites

- [ ] Node.js / 패키지 매니저로 툴체인을 받는 실행 환경
- [ ] Solidity Basic Syntax / 계약 작성 전 알아야 할 최소 문법

## 2. Project Setup

- [ ] npx hardhat init / 대화형으로 프로젝트 뼈대를 생성하는 명령
- [ ] Project Layout / 계약·테스트·스크립트를 정해진 폴더에 나누는 관례
- [ ] TypeScript Setup / 타입 안전하게 설정과 스크립트를 짜는 방식 `추천`
- [ ] hardhat.config.ts Structure / 컴파일러·네트워크·계정을 한 파일에 선언하는 구조
- [ ] Solidity Compiler Settings / 컴파일러 버전과 최적화를 설정에 못 박는 방법
- [ ] Multiple Compiler Versions / 파일별로 다른 버전을 override로 지정하는 방법
- [ ] paths Customization / sources·artifacts 등 폴더 위치를 바꾸는 설정
- [ ] Dependency Management / npm으로 OpenZeppelin 등 외부 계약을 받는 방법

## 3. Compilation

- [ ] npx hardhat compile / 소스를 ABI·바이트코드로 컴파일하는 명령
- [ ] Artifacts / 컴파일 결과인 ABI와 바이트코드 산출물
- [ ] Cache / 안 바뀐 파일은 다시 컴파일 안 하는 캐시
- [ ] Type Generation / TypeChain으로 계약 타입을 자동 생성하는 기능
- [ ] npx hardhat clean / 캐시와 아티팩트를 지우고 새로 빌드하는 명령
- [ ] Compilation Error · Warning Interpretation / 컴파일 에러·경고 메시지를 읽는 방법

---

# PART 2 · Local Network and Testing

## 4. Hardhat Network

- [ ] In-process EVM / 노드 프로세스 안에서 바로 도는 가상 EVM
- [ ] Auto-mining vs Interval Mining / 매 트랜잭션 채굴할지 간격 채굴할지 설정
- [ ] Solidity console.log / 계약 코드 안에서 값을 콘솔에 찍는 기능
- [ ] Stack Trace / 실패 지점을 Solidity 줄까지 짚어주는 표시
- [ ] Network Config / 체인ID·계정·초기 잔액을 정의하는 설정
- [ ] npx hardhat node / 독립 JSON-RPC 서버로 띄우는 명령
- [ ] hardhat_ RPC Methods / 잔액 설정·채굴·리셋 등 전용 RPC 확장

## 5. Network Forking

- [ ] Mainnet Forking / forking.url로 메인넷 상태를 복제하는 기능
- [ ] Pinning Block Number / 같은 블록에 고정해 결과를 재현하는 설정
- [ ] Impersonating Accounts / 서명 없이 남의 계정처럼 트랜잭션을 보내는 기능
- [ ] Interacting with Deployed Protocols / 포크한 메인넷의 실제 계약을 호출하는 방법
- [ ] Fork Request Caching / 포크 시 받은 RPC 응답을 재사용하는 캐시
- [ ] Fork Reset / 매 테스트 전 포크 상태를 초기화하는 방법

## 6. Testing

### Basic Structure

- [ ] Mocha · Chai / 테스트 실행기와 단언 라이브러리 조합
- [ ] describe and it / 테스트를 그룹과 개별 케이스로 나누는 문법
- [ ] npx hardhat test / --grep로 이름 필터링해 테스트를 실행하는 명령
- [ ] Deploying Contracts in Tests / 테스트마다 계약을 새로 배포하는 패턴
- [ ] Obtaining Signers / getSigners로 테스트용 계정을 받아오는 방법

### Hardhat Chai Matchers

- [ ] revertedWith and revertedWithCustomError / 리버트 메시지·커스텀 에러를 검사하는 매처
- [ ] emit and withArgs / 이벤트 발생과 인자 값을 함께 검사하는 매처
- [ ] changeEtherBalance and changeTokenBalance / 잔액 변화량을 검사하는 매처
- [ ] properAddress and properHex / 문자열이 주소·16진수 형식인지 검사하는 매처

### Network Helpers

- [ ] Time Travel / time.increase 등으로 블록 시간을 앞당기는 기능
- [ ] Block Control / mine·mineUpTo로 블록 생성을 직접 제어하는 방법
- [ ] State Setting / setBalance 등으로 체인 상태를 강제로 바꾸는 방법
- [ ] loadFixture / 스냅샷을 재사용해 테스트를 빠르게 하는 함수
- [ ] impersonateAccount / 서명 없이 계정 권한을 빌리는 헬퍼 함수

### Test Quality

- [ ] Gas Reporter / hardhat-gas-reporter로 함수별 가스 사용량을 뽑는 플러그인
- [ ] Coverage / solidity-coverage로 테스트가 지나간 코드 비율을 재는 도구
- [ ] Parallel Test Execution / 여러 테스트를 동시에 돌려 시간을 줄이는 방법

---

# PART 3 · Scripting and Deployment

## 7. Scripts and Tasks

- [ ] npx hardhat run / 스크립트 파일을 HRE 환경에서 실행하는 명령
- [ ] Hardhat Runtime Environment (HRE) / 스크립트·태스크에 주입되는 전역 객체
- [ ] Built-in Tasks / accounts·compile·test 등 기본 제공 명령
- [ ] Custom Task / task() 함수로 새 명령을 정의하는 방법
- [ ] Subtask · Task Override / 기존 태스크를 부르거나 덮어쓰는 방법
- [ ] Task Arguments / addParam·addFlag로 명령에 인자를 받는 방법
- [ ] Scripts vs Tasks / 반복 등록이냐 1회 실행이냐로 가르는 선택
- [ ] npx hardhat console / 환경을 바로 써보는 REPL 콘솔

## 8. Network Configuration

- [ ] networks Configuration / 접속할 네트워크 목록을 등록하는 설정
- [ ] RPC Provider / Alchemy·Infura 같은 외부 노드 접속 서비스
- [ ] Testnet Connection / Sepolia·Holesky 같은 테스트망에 붙는 설정
- [ ] Account Management / 개인키나 니모닉으로 서명 계정을 등록하는 방법
- [ ] Secret Management / dotenv나 hardhat-vars로 키를 코드 밖에 두는 방법
- [ ] Gas Settings / gasPrice·maxFeePerGas로 수수료를 지정하는 설정
- [ ] Custom Chains / L2나 사설망처럼 임의 체인을 등록하는 방법

## 9. Deployment

### Hardhat Ignition `추천`

- [ ] Ignition Module / buildModule로 배포 절차를 선언하는 단위
- [ ] m.contract and m.call / 계약을 배포하고 함수를 호출하는 API
- [ ] Module Parameters / 배포마다 값을 바꿔 넣는 모듈 입력값
- [ ] Deployment State / 실패한 배포를 이어서 재시도하는 상태 기록
- [ ] Deployment Artifacts / deployed_addresses.json에 남는 배포 결과
- [ ] Module Visualization / 배포 순서와 의존 관계를 그림으로 보는 기능

### Alternative Approaches `택 1`

- [ ] Hand-written Deploy Script / 배포 순서를 스크립트로 직접 짜는 방식
- [ ] hardhat-deploy Plugin / 태그·의존성으로 배포를 관리하는 서드파티 플러그인 `선택`

### Source Verification

- [ ] hardhat-verify / Etherscan에 소스를 검증 등록하는 플러그인
- [ ] Constructor Arguments Encoding / 검증 시 생성자 인자를 인코딩하는 과정
- [ ] Sourcify Verification / Etherscan 대신 Sourcify에 등록하는 방법

---

# PART 4 · Extensions and Operations

## 10. Plugin Ecosystem

- [ ] hardhat-toolbox / 자주 쓰는 플러그인을 한 번에 묶은 패키지
- [ ] hardhat-ethers vs hardhat-viem / 계약을 부를 클라이언트 스타일을 고르는 플러그인 `택 1`
- [ ] TypeChain Plugin / 컴파일 산출물로 타입 정의를 생성하는 플러그인
- [ ] hardhat-contract-sizer / 배포 전 계약 바이트코드 크기를 재는 플러그인
- [ ] hardhat-abi-exporter / ABI를 파일로 뽑아 저장하는 플러그인
- [ ] hardhat-tracer / 트랜잭션 호출 경로를 트리로 보여주는 플러그인
- [ ] hardhat-storage-layout / 계약 스토리지 슬롯 배치를 보는 플러그인

## 11. Upgradeable Contracts

- [ ] OpenZeppelin Upgrades Plugin / 프록시 업그레이드를 안전하게 돕는 플러그인
- [ ] deployProxy and upgradeProxy / 프록시를 배포하고 로직을 갱신하는 함수
- [ ] Transparent vs UUPS / 업그레이드 로직 위치로 가르는 프록시 방식
- [ ] Storage Layout Validation / validateUpgrade로 스토리지 충돌을 검사하는 절차
- [ ] ProxyAdmin / 프록시 소유권을 관리·이전하는 별도 계약
- [ ] Beacon Proxy / 여러 프록시가 로직 주소 하나를 공유하는 방식

## 12. Writing Plugins `선택`

- [ ] extendEnvironment / HRE에 커스텀 필드를 추가하는 훅
- [ ] extendConfig / 사용자 설정값에 기본값을 덧붙이는 훅
- [ ] Type Extensions / 선언 병합으로 HRE 타입에 필드를 추가하는 방법
- [ ] Publishing a Plugin / 만든 플러그인을 npm에 배포하는 방법

## 13. CI and Workflow

- [ ] GitHub Actions Pipeline / 커밋마다 컴파일·테스트를 자동 실행하는 설정
- [ ] Caching / node_modules·artifacts를 재사용해 빌드를 줄이는 방법
- [ ] Lint / solhint·prettier로 코드 스타일을 검사하는 도구
- [ ] Static Analysis in CI / Slither로 CI에서 취약점을 자동 스캔하는 방법
- [ ] Monorepo Setup / 여러 패키지를 workspace로 묶어 관리하는 구조
- [ ] Frontend Integration / ABI와 TypeChain 타입을 프론트와 공유하는 방법
- [ ] Hardhat 3 / EDR이라는 Rust 런타임으로 바뀐 신버전 `선택`

---

# 이 로드맵 밖

- 블록체인 전반 `software/role-based/blockchain.md`
- 스마트 컨트랙트 언어 `software/skill-based/Blockchain/solidity.md`
- 다른 프레임워크 `software/skill-based/Blockchain/foundry.md`
- 클라이언트 라이브러리 `software/skill-based/Blockchain/ethersjs.md`, `web3js.md`
- TypeScript · Node.js `software/skill-based/Languages/typescript.md`, `software/skill-based/Frameworks/nodejs.md`
- CI 파이프라인 `software/skill-based/Infra-DevOps/git-github.md`
