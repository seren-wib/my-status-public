# ethers.js `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to ethers.js

## 1. What is ethers.js?

### Overview of ethers.js / What is it?

- [ ] Complete Ethereum Library / 지갑·컨트랙트·유틸까지 하나로 묶은 라이브러리
- [ ] Provider · Signer Separation / 읽기와 서명 권한을 객체로 분리하는 설계
- [ ] Immutable Object / 값을 바꾸지 않고 새로 반환하는 함수형 API
- [ ] v5 vs v6 / BigInt 전환, 이름 변경
- [ ] ethers.js vs web3.js / 콜백 대신 프라미스 중심으로 짠 설계

## 2. Setup

- [ ] npm install ethers
- [ ] Import Styles / 이름별 export를 ESM으로 가져오는 방식
- [ ] Sub-path Import / 필요한 하위 모듈만 골라 가져오는 방법
- [ ] TypeScript Support / 타입 정의가 내장돼 따로 설치 안 하는 지원

## 3. Providers

- [ ] Provider Concept / 서명 없이 체인 상태만 읽는 연결 객체
- [ ] JsonRpcProvider / RPC 노드 URL 하나로 붙는 기본 provider
- [ ] BrowserProvider / 지갑 확장이 주입한 표준 객체에 붙는 통로
- [ ] WebSocketProvider / 소켓을 유지해 이벤트를 실시간으로 받는 provider
- [ ] FallbackProvider / 여러 provider 응답을 정족수로 비교하는 방식
- [ ] getDefaultProvider / 여러 공개 노드를 자동으로 묶어 붙는 함수
- [ ] Network / 붙은 체인의 chainId를 확인하는 기능
- [ ] Query Methods / 잔액·블록·영수증을 provider로 조회하는 함수들

## 4. Signers

- [ ] Signer Concept / Provider와의 역할 분리
- [ ] Wallet / 개인키 하나로 서명 가능한 지갑을 만드는 방법
- [ ] HD Wallet / 니모닉 하나로 여러 계정을 파생하는 지갑
- [ ] JsonRpcSigner / 노드가 관리하는 계정을 signer로 감싸는 방식
- [ ] Encrypted JSON Wallet / 비밀번호로 지갑을 암호화해 파일로 저장하는 방식
- [ ] connect / 같은 지갑을 다른 provider에 다시 붙이는 함수
- [ ] signMessage / 임의 문자열에 EIP-191 규격으로 서명하는 함수
- [ ] signTypedData / 구조화된 데이터에 EIP-712 규격으로 서명하는 함수
- [ ] Signature Verification / 서명에서 서명자 주소를 역산해 검증하는 방법

---

# PART 2 · Working with Data

## 5. Utilities

- [ ] Unit Conversion / ether 단위와 최소 단위를 서로 변환하는 함수들
- [ ] BigInt Arithmetic / v6부터 금액을 네이티브 BigInt로 다루는 방식
- [ ] FixedNumber / 소수점을 그대로 보존하는 고정소수점 타입
- [ ] Byte Utilities / 16진 문자열과 바이트 배열을 다루는 함수들
- [ ] Hashing / 문자열·데이터를 keccak256으로 해시하는 함수들
- [ ] Address Utilities / 주소 형식을 검증하고 체크섬을 맞추는 함수들
- [ ] String Encoding / 문자열을 UTF-8 바이트로 주고받는 함수

## 6. ABI Coder and Interface

- [ ] Human-Readable ABI / 함수 시그니처를 문자열 배열로 적는 방식
- [ ] Interface Object / ABI를 인코딩·디코딩 단위로 감싼 객체
- [ ] encodeFunctionData and decodeFunctionResult / 함수 호출 데이터를 인코딩·디코딩하는 함수 쌍
- [ ] parseLog and parseTransaction / 로그와 트랜잭션을 ABI 기준으로 해석하는 함수
- [ ] AbiCoder / 함수 없이 타입 값만 직접 인코딩·디코딩하는 도구
- [ ] Fragment / ABI 조각을 함수·이벤트 단위로 표현한 객체
- [ ] Custom Error Decoding / 컨트랙트가 정의한 커스텀 revert 에러를 해석하는 기능

---

# PART 3 · Contracts

## 7. Contract Interaction

- [ ] new Contract(address, abi, runner) / 주소와 ABI를 묶어 호출 가능한 객체를 만드는 생성자
- [ ] Read Call / view 함수 직접 호출
- [ ] Write Transaction / 상태를 바꾸는 트랜잭션을 보내고 응답을 받는 호출
- [ ] tx.wait / 트랜잭션이 블록에 담겨 확정될 때까지 기다리는 함수
- [ ] Overrides / value·gasLimit·nonce 같은 호출 옵션을 덮어쓰는 값
- [ ] estimateGas and staticCall / 실제 전송 없이 가스·결과를 미리 확인하는 방법
- [ ] Ambiguous Method / 오버로드가 겹칠 때 전체 시그니처로 고르는 방법
- [ ] connect / 같은 컨트랙트를 다른 signer·provider로 바꿔 쓰는 함수
- [ ] getFunction / 이름이 겹칠 때 메서드를 동적으로 골라내는 함수

## 8. Contract Deployment

- [ ] ContractFactory / 배포에 필요한 bytecode와 ABI를 묶는 객체
- [ ] deploy / 생성자 인자를 넣어 배포 트랜잭션을 보내는 함수
- [ ] waitForDeployment and getAddress / 배포 확정을 기다린 뒤 주소를 얻는 절차
- [ ] Artifact Integration / abi, bytecode 공급

## 9. Events and Filters

- [ ] queryFilter / fromBlock·toBlock 범위로 지난 로그를 조회하는 함수
- [ ] contract.filters / 이벤트 필터 객체를 생성하는 헬퍼
- [ ] contract.on, off, once / 이벤트 리스너를 등록·해제·1회 등록하는 메서드
- [ ] Provider Event / 새 블록·펜딩 트랜잭션을 감지하는 이벤트
- [ ] Log Structure / 인덱싱된 topics와 나머지 data로 나뉜 로그 형식
- [ ] Polling vs WebSocket Subscription / 이벤트를 주기 조회할지 구독할지 고르는 방식
- [ ] Reorg Handling / confirmations 기준

---

# PART 4 · Transactions and Real-World Use

## 10. Transactions

- [ ] Transaction Object / to·value·data·nonce로 구성된 트랜잭션 필드
- [ ] EIP-1559 Fees / 기본료와 우선순위 팁으로 수수료를 나누는 방식
- [ ] getFeeData / 현재 네트워크의 권장 가스 수수료를 조회하는 함수
- [ ] populateTransaction / 서명 전 트랜잭션 필드를 자동으로 채우는 함수
- [ ] Serialization / 트랜잭션을 서명 가능한 문자열로 직렬화하는 방법
- [ ] Replacement Transaction / 같은 nonce로 다시 보내 대체하는 방법
- [ ] Error Interpretation / 실패 이유를 CALL_EXCEPTION 코드로 해석하는 방법

## 11. dApp Integration

- [ ] Wallet Connection / eth_requestAccounts로 지갑 연결을 요청하는 방법
- [ ] Chain Switching / 지갑에 네트워크 전환·추가를 요청하는 방법
- [ ] Wallet Event Handling / 계정·체인이 바뀌면 Provider를 다시 만드는 처리
- [ ] Read Provider vs Wallet Signer / 조회용과 서명용 연결을 분리하는 방식
- [ ] ENS / 사람이 읽는 이름과 주소를 서로 변환하는 기능
- [ ] Error Codes / 거부·잔액 부족 등 실패 원인을 표준 코드로 구분하는 방식

## 12. Advanced and Production

- [ ] Custom Network Registration / 지원 안 하는 체인을 직접 등록하는 방법
- [ ] Batch · Multicall Pattern / 여러 호출을 한 요청으로 묶어 보내는 방식
- [ ] Nonce Manager Pattern / 동시 전송 시 nonce를 직렬로 관리하는 방식
- [ ] Rate Limit · Retry Strategy / 요청 실패 시 재시도하는 전략
- [ ] Tree Shaking / 안 쓰는 모듈을 번들에서 제거해 크기를 줄이는 기법
- [ ] Migration from v5 to v6 / 이름 변경과 BigInt 전환을 반영해 옮기는 작업
- [ ] viem Comparison / 타입 안전성을 강조한 대안 라이브러리와 비교 `선택`

---

# 이 로드맵 밖

- 블록체인 전반 `software/role-based/blockchain.md`
- 스마트 컨트랙트 언어 `software/skill-based/Blockchain/solidity.md`
- 대안 라이브러리 `software/skill-based/Blockchain/web3js.md`
- 개발 프레임워크 `software/skill-based/Blockchain/hardhat.md`, `foundry.md`
- JavaScript · TypeScript `software/skill-based/Languages/javascript.md`, `typescript.md`
- 프런트엔드 연동 `software/skill-based/Frameworks/react.md`, `nextjs.md`
