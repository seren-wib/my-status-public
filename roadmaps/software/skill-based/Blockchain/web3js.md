# web3.js `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to web3.js

## 1. What is web3.js?

### Overview of web3.js / What is it?

- [ ] Ethereum JavaScript API / 이더리움 노드와 통신하는 자바스크립트 라이브러리
- [ ] JSON-RPC Wrapper / RPC 호출을 함수 하나로 감싸는 방식
- [ ] Module-based Architecture / 기능마다 네임스페이스를 나눠 붙인 구조
- [ ] web3.js v4 / 타입스크립트로 다시 쓰고 모듈 방식을 바꾼 판
- [ ] web3.js vs ethers.js / 네임스페이스형과 분리형으로 갈리는 설계
- [ ] Sunset Status / 2025년 유지보수가 끝난 라이브러리
- [ ] Migration Path / ethers.js·viem으로 옮겨가는 경로
- [ ] Why Still Read It / 남아 있는 저장소를 읽어야 하는 자리

## 2. Setup and Connection

- [ ] npm install web3 / 패키지를 설치해 시작하는 방법
- [ ] Web3 Instance Creation / 프로바이더를 넣어 web3 객체를 만드는 방법
- [ ] Provider Types / 요청·구독·로컬 소켓 중 하나로 노드에 붙는 방식
- [ ] Injected Provider / 지갑 확장이 브라우저에 심어주는 프로바이더
- [ ] setProvider / 연결된 프로바이더를 나중에 바꾸는 메서드
- [ ] Node as a Service Connection / 직접 노드 없이 외부 업체 RPC에 붙는 방식
- [ ] Connection Check / 체인 ID·연결 상태를 확인하는 메서드

## 3. Utilities

- [ ] Unit Conversion / wei와 ether 단위를 서로 바꾸는 메서드
- [ ] Hex Conversion / 16진수·숫자·문자열을 서로 바꾸는 메서드
- [ ] Address Utilities / 주소 형식 검증·체크섬 변환 메서드
- [ ] Hashing / 값을 keccak256 방식으로 해시하는 메서드
- [ ] BigInt Handling / 큰 수를 v4부터 네이티브 BigInt로 다루는 방식
- [ ] Output Formatting / 반환값을 숫자·문자열 등으로 지정하는 옵션

---

# PART 2 · Reading and Writing the Chain

## 4. Reading Chain Data

- [ ] getBalance / 주소의 잔액을 조회하는 메서드
- [ ] getBlock and getBlockNumber / 블록 정보와 최신 블록 번호를 조회하는 메서드
- [ ] getTransaction and getTransactionReceipt / 트랜잭션 내용과 처리 결과를 조회하는 메서드
- [ ] getCode and getStorageAt / 컨트랙트 코드와 저장 슬롯 값을 조회하는 메서드
- [ ] getTransactionCount / 다음 트랜잭션에 쓸 nonce를 조회하는 메서드
- [ ] Fee Query / 현재 가스 가격과 과거 수수료 추이를 조회하는 메서드
- [ ] Block Tag / 조회 시점을 최신·대기·확정 중에서 고르는 값

## 5. Accounts and Signing

- [ ] web3.eth.accounts / 계정을 새로 만들거나 개인키에서 복원하는 모듈
- [ ] Wallet / 개인키를 추가해 로컬에서 서명하게 하는 모듈
- [ ] signTransaction and sendSignedTransaction / 서명한 뒤 서명된 트랜잭션을 전송하는 메서드
- [ ] Message Signing / 메시지에 서명하고 서명자를 복원하는 방법
- [ ] Typed Data Signing / 구조화된 데이터를 EIP-712 표준으로 서명하는 방식
- [ ] Keystore / 개인키를 암호화된 파일로 저장·복호화하는 방식

## 6. Transactions

- [ ] sendTransaction / 서명까지 노드에 위임해 트랜잭션을 보내는 메서드
- [ ] Transaction Object / 트랜잭션을 이루는 발신·수신·금액·데이터 필드
- [ ] Gas Estimation / 트랜잭션에 필요한 가스량을 미리 계산하는 메서드
- [ ] Legacy vs EIP-1559 Fields / gasPrice 방식과 maxFeePerGas 방식의 차이
- [ ] PromiEvent / 전송 단계별 이벤트를 순서대로 내는 프라미스
- [ ] Nonce Management / 대기 중 트랜잭션과 nonce가 겹치는 문제 관리
- [ ] Revert Reason Decoding / 실패한 트랜잭션의 되돌림 사유를 해석하는 메서드

---

# PART 3 · Contract Interaction

## 7. Contract Interface

- [ ] new web3.eth.Contract(abi, address) / ABI와 주소로 컨트랙트 인스턴스를 만드는 방법
- [ ] methods.foo().call() / 상태를 바꾸지 않고 값만 읽는 호출
- [ ] methods.foo().send() / 트랜잭션을 보내 상태를 바꾸는 호출
- [ ] Call Options / 호출 시 발신자·전송액·가스 한도를 지정하는 옵션
- [ ] encodeABI / Raw Calldata 생성
- [ ] Contract Deployment / 배포 트랜잭션을 만들어 전송하는 방법
- [ ] Return Value Decoding / 튜플·구조체 반환값을 해석하는 방식
- [ ] Contract Options / 기본 계정과 기본 블록을 미리 지정하는 옵션

## 8. Events and Subscriptions

- [ ] getPastEvents / 블록 범위를 지정해 지난 이벤트를 긁어오는 방법
- [ ] Event Filter / indexed 파라미터 값으로 로그를 걸러내는 방법
- [ ] contract.events.MyEvent / 계약 객체에서 바로 이벤트를 구독하는 통로
- [ ] web3.eth.subscribe / 새 블록·로그를 소켓으로 계속 받아보는 방법
- [ ] unsubscribe / 구독을 끊어 열린 소켓을 회수하는 방법
- [ ] WebSocket Reconnection / 연결이 끊겼을 때 구독까지 되살리는 처리
- [ ] decodeLog / 원시 로그를 ABI로 직접 풀어 읽는 방법

## 9. ABI Module

- [ ] encodeFunctionCall / 함수 이름과 인자를 호출용 데이터로 만드는 방법
- [ ] encodeParameters and decodeParameters / 인자 묶음을 ABI 규칙으로 감싸고 푸는 짝
- [ ] encodeFunctionSignature / 함수 시그니처를 4바이트 선택자로 줄이는 방법
- [ ] Custom Error ABI Decoding / 되돌림 데이터를 커스텀 에러로 되읽는 방법

---

# PART 4 · Extensions and Real-World Use

## 10. Plugins and Customization

- [ ] Plugin API / 외부 기능을 web3 객체에 얹어 확장하는 창구
- [ ] web3.extend / 표준에 없는 RPC 메서드를 직접 붙이는 방법
- [ ] Global Config / 기본 블록·폴링 주기를 인스턴스 전역에 거는 설정
- [ ] Custom Provider Implementation / 규약만 맞춰 전송 계층을 직접 만드는 방법

## 11. dApp Integration

- [ ] Wallet Connection Flow / 지갑에 계정 접근 권한을 요청하는 순서
- [ ] Chain Switching / 지갑이 보는 네트워크를 코드로 바꾸도록 요청
- [ ] Wallet Event Handling / 지갑이 던지는 계정·체인 변경 신호를 받는 처리
- [ ] Read Provider vs Wallet Provider / 조회는 노드로 서명은 지갑으로 나누는 구성
- [ ] React Integration Pattern / 인스턴스와 계정 상태를 훅으로 들고 있는 방식
- [ ] Error UX / 거절·잔액 부족을 사용자 말로 풀어 보여주는 처리

## 12. Production Concerns

- [ ] RPC Rate Limit / 호출을 한 요청에 묶어 노드 한도를 피하는 방법
- [ ] Fallback · Retry Strategy / 노드가 죽으면 다른 엔드포인트로 넘기는 전략
- [ ] Read Call Caching / 잘 안 바뀌는 조회 결과를 재사용하는 방법
- [ ] Multicall Pattern / 여러 조회를 계약 하나로 모아 한 번에 부르는 방법
- [ ] Bundle Size / 안 쓰는 네임스페이스를 털어 번들을 줄이는 방법
- [ ] Migration from v1 to v4 / 콜백·BN 의존을 걷어내며 옮겨오는 절차

---

# 이 로드맵 밖

- 블록체인 전반 `software/role-based/blockchain.md`
- 스마트 컨트랙트 언어 `software/skill-based/Blockchain/solidity.md`
- 대안 라이브러리 `software/skill-based/Blockchain/ethersjs.md`
- 개발 프레임워크 `software/skill-based/Blockchain/hardhat.md`, `foundry.md`
- JavaScript · TypeScript `software/skill-based/Languages/javascript.md`, `typescript.md`
- 프런트엔드 연동 `software/skill-based/Frameworks/react.md`
