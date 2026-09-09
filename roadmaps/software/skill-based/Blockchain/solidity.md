# Solidity `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Solidity

## 1. What is Solidity?

### Overview of Solidity / What is it?

- [ ] Contract-Oriented Language / 상태와 동작을 계정 하나에 묶는 언어 모델
- [ ] Statically Typed / 컴파일 시점에 타입을 확정하는 방식
- [ ] Compiles to EVM Bytecode / EVM이 실행하는 바이트코드로 변환하는 과정

### Runtime Environment Prerequisites

- [ ] Account Types / 키로 서명하는 계정과 코드가 든 계정의 차이
- [ ] Transaction vs Message Call / 서명이 필요한 트랜잭션과 내부 호출의 차이
- [ ] Gas / 연산마다 값을 매겨 실행량을 제한하는 단위

### Toolchain First Steps

- [ ] solc Compiler / Solidity 소스를 바이트코드로 컴파일하는 도구
- [ ] Remix IDE / 브라우저에서 작성·배포·테스트하는 IDE `추천`
- [ ] pragma solidity / 컴파일러 버전 범위를 파일 첫 줄에 못 박는 선언
- [ ] SPDX License Identifier / 라이선스 정보를 주석으로 명시하는 규칙

## 2. First Contract

- [ ] Contract Declaration / contract 키워드로 계약 단위를 정의하는 선언
- [ ] State Variables / 블록체인에 영구 저장되는 계약의 변수
- [ ] Constructor / 배포 시 한 번만 실행되는 초기화 함수
- [ ] Function Declaration and Call / 함수를 정의하고 호출하는 방법
- [ ] Compile · Deploy · Interact in Remix / Remix에서 컴파일·배포·호출까지 해보는 실습

---

# PART 2 · Language Syntax

## 3. Types

### Value Types

- [ ] Boolean / bool로 참과 거짓만 표현하는 타입
- [ ] Integers / 부호 있는·없는 정수를 비트 크기별로 나누는 타입
- [ ] Address / 이더 주소를 나타내고 송금 가능 여부로 나뉘는 타입
- [ ] Fixed-size Byte Arrays / 크기가 고정된 바이트 배열을 선언하는 타입
- [ ] Enum / 이름 붙인 정수 상수 집합으로 상태를 표현하는 타입
- [ ] Literals / 주소·16진수·wei·ether 단위를 직접 쓰는 표기법

### Reference Types

- [ ] Arrays / 고정·동적 배열에 push·pop으로 원소를 다루는 구조
- [ ] bytes and string / 가변 길이 바이트열과 문자열을 다루는 타입
- [ ] Struct / 여러 타입을 묶어 하나의 커스텀 타입을 만드는 구조
- [ ] Mapping / 키로 값을 찾되 순회는 못 하는 해시 구조

### Conversion and Encoding

- [ ] Implicit vs Explicit Conversion / 자동 형변환과 명시적 형변환의 잘림·부호확장 차이
- [ ] ABI Encoding / 함수 호출 데이터를 이진 형식으로 인코딩하는 규칙

## 4. Data Location

- [ ] storage / 계약 상태로 영구 저장되는 가장 비싼 데이터 위치
- [ ] memory / 함수 실행 동안만 존재하는 임시 데이터 위치
- [ ] calldata / 외부 호출 인자를 읽기 전용으로 참조하는 위치
- [ ] Assignment Semantics / 대입 시 값이 복사되는지 참조되는지의 차이
- [ ] Storage Slot Layout / 변수를 32바이트 슬롯에 압축해 배치하는 규칙

## 5. Functions

### Declarations

- [ ] Parameters and Return Values / 매개변수·반환값에 이름을 붙여 명시하는 방법
- [ ] Visibility Modifiers / 함수·변수의 호출 가능 범위를 정하는 4단계
- [ ] State Mutability / 상태를 읽기만·안 건드리기·이더 수신 여부로 구분
- [ ] Function Modifiers / 함수 실행 전후에 공통 로직을 끼워 넣는 장치

### Special Functions

- [ ] receive / 데이터 없이 이더만 받을 때 실행되는 함수
- [ ] fallback / 일치하는 함수가 없을 때 대신 실행되는 함수
- [ ] Auto-generated Getter / public 상태 변수에 자동 생성되는 조회 함수

### Call Types

- [ ] Internal vs External Call / 내부 점프 호출과 메시지 콜의 비용 차이
- [ ] Function Types / 함수를 변수처럼 저장·전달하는 타입
- [ ] Low-level Calls / 주소에 저수준으로 호출을 거는 세 방식
- [ ] Sending Ether / 이더를 보내는 세 방법과 가스·에러 처리 차이

## 6. Control Flow and Error Handling

### Control Statements

- [ ] Conditionals / 조건에 따라 분기하는 if-else와 삼항 연산자
- [ ] Loops / 반복문 종류와 흐름을 제어하는 break·continue

### Error Handling

- [ ] require / 조건이 거짓이면 되돌리고 가스를 환불하는 검사
- [ ] revert / 실행을 취소하고 이유를 담아 되돌리는 명령
- [ ] assert / 절대 참이어야 할 내부 불변식을 검사하는 함수
- [ ] Custom Errors / 문자열 대신 가스를 아끼는 커스텀 에러 정의
- [ ] try and catch / 외부 호출 실패를 잡아 처리하는 예외 구문
- [ ] unchecked Arithmetic / 오버플로 검사를 생략해 가스를 아끼는 블록

## 7. Contract Composition

### Inheritance

- [ ] Inheritance / is 키워드로 다른 계약을 상속받는 방법
- [ ] virtual and override / 재정의 가능 함수와 실제 재정의를 표시하는 키워드
- [ ] super / 부모 계약의 함수를 명시적으로 호출하는 키워드
- [ ] Abstract Contract / 구현 없는 함수를 남겨 상속을 강제하는 계약
- [ ] Interface / 함수 시그니처만 정의하고 구현은 없는 규격
- [ ] Multiple Inheritance / 여러 부모를 상속할 때 순서를 정하는 규칙
- [ ] Constructor in Inheritance / 부모 생성자에 인자를 넘기는 방법

### Reusable Units

- [ ] Library / 상태 없이 재사용하는 함수 모음
- [ ] using ... for / 특정 타입에 라이브러리 함수를 메서드처럼 붙이는 구문
- [ ] Import Statements / 다른 파일의 코드를 선택적으로 가져오는 구문

## 8. Events and Logs

- [ ] event Declaration / 로그로 남길 데이터 구조를 정의하는 선언
- [ ] emit / 정의된 이벤트를 실제로 로그에 기록하는 명령
- [ ] indexed Parameters / 이벤트 파라미터를 검색 가능하게 표시하는 키워드
- [ ] Log Data Structure / 이벤트가 블록체인에 저장되는 로그 형식
- [ ] Events vs Storage / 이벤트 기록과 상태 저장 중 조회 비용을 따져 고르는 기준

## 9. Global Variables and Built-ins

- [ ] Message Context / 호출자·전송액·데이터를 담은 호출 컨텍스트
- [ ] Block Context / 현재 블록의 시간·번호·체인ID 정보
- [ ] tx.origin / 트랜잭션을 최초로 서명한 계정 주소
- [ ] Hash Functions / 데이터를 고정 길이로 해시하는 내장 함수
- [ ] ecrecover / 서명에서 서명자 주소를 복원하는 함수
- [ ] Address Members / 주소의 잔액·코드·코드해시를 조회하는 멤버

---

# PART 3 · Contract Design

## 10. Token Standards

- [ ] ERC-20 / 서로 교환 가능한 토큰을 정의하는 표준
- [ ] ERC-721 / 하나하나가 고유한 토큰을 정의하는 표준
- [ ] ERC-1155 / 대체·비대체 토큰을 한 계약에서 다루는 표준
- [ ] ERC-165 / 계약이 어떤 인터페이스를 지원하는지 확인하는 표준
- [ ] ERC-2612 / 서명만으로 승인을 처리해 가스를 아끼는 표준
- [ ] ERC-4626 / 예치 자산을 토큰화해 표준 인터페이스로 다루는 규격

## 11. OpenZeppelin Contracts

- [ ] Ownable and AccessControl / 소유자 하나 또는 역할 기반으로 권한을 제한하는 모듈
- [ ] SafeERC20 / 반환값이 불안정한 토큰 호출을 안전하게 감싸는 라이브러리
- [ ] ReentrancyGuard / 재진입 공격을 막는 잠금 모디파이어
- [ ] Pausable / 비상시 계약 기능을 정지시키는 모듈
- [ ] ERC20 · ERC721 Base Implementation / 표준 토큰 인터페이스의 검증된 기본 구현체
- [ ] Utils / 주소·문자열·머클 증명을 다루는 유틸 모음

## 12. Design Patterns

- [ ] Checks-Effects-Interactions / 검사→상태변경→외부호출 순서로 재진입을 막는 원칙
- [ ] Pull over Push Payment / 송금을 강제하지 않고 인출을 요청받는 패턴
- [ ] Factory Pattern / 계약이 다른 계약을 배포해 찍어내는 패턴
- [ ] Minimal Proxy / 로직 계약 하나를 값싸게 복제하는 최소 프록시
- [ ] Upgradeable Proxy / 로직을 교체 가능하게 분리하는 업그레이드 프록시
- [ ] Storage Gap / 업그레이드 시 스토리지 슬롯 충돌을 막는 예약 공간
- [ ] Circuit Breaker / 이상 감지 시 계약 전체를 멈추는 안전장치

---

# PART 4 · Security and Gas

## 13. Security Vulnerabilities

### External Calls

- [ ] Reentrancy / 외부 호출 도중 되불려 들어와 상태를 악용하는 취약점
- [ ] Unchecked Call Return Value / 저수준 호출 실패 여부를 확인하지 않는 취약점
- [ ] delegatecall to Untrusted Contract / 신뢰할 수 없는 코드에 저장소 권한을 넘기는 위험
- [ ] Force-fed Ether / selfdestruct로 강제 주입된 잔액을 가정하는 위험

### Arithmetic and Storage

- [ ] Integer Overflow and Underflow / 숫자 타입의 범위를 넘거나 밑도는 연산 오류
- [ ] Division Precision Loss / 정수 나눗셈에서 순서를 잘못 두어 정밀도가 깎이는 문제
- [ ] Storage Collision in Proxy / 프록시와 로직 계약의 슬롯이 겹쳐 값이 깨지는 문제
- [ ] Uninitialized Storage Pointer / 초기화 안 된 포인터가 다른 슬롯을 덮는 버그

### Access Control and Signatures

- [ ] Missing Access Control / 권한 검사를 빠뜨려 아무나 호출 가능한 취약점
- [ ] tx.origin Authentication / 피싱 계약을 거친 호출에 속는 인증 방식의 위험
- [ ] Uninitialized Implementation Contract / 초기화 안 된 로직 계약을 탈취당하는 취약점
- [ ] Signature Replay / 같은 서명을 재사용해 재실행시키는 공격
- [ ] Signature Malleability / 서명 값을 조작해 다른 서명처럼 위조하는 취약점

### External Dependencies

- [ ] Oracle Price Manipulation / 플래시론으로 가격을 왜곡해 오라클을 속이는 공격
- [ ] Front-running / 대기 중인 트랜잭션을 앞질러 이익을 채가는 공격
- [ ] Weak Randomness / 예측 가능한 블록 값을 난수로 쓰는 취약점
- [ ] Denial of Service / 무한정 커지는 반복문으로 실행을 막는 공격

### Verification Tools

- [ ] Static Analysis / 실행 없이 코드 패턴으로 취약점을 찾는 정적 분석
- [ ] Property-based Fuzzing / 불변식을 정의하고 무작위 입력으로 깨보는 기법
- [ ] Formal Verification / 수학적으로 계약 동작을 증명하는 검증 기법 `선택`
- [ ] Audit Process / 범위 설정·취약점 발견·수정까지의 감사 절차

## 14. Gas Optimization

- [ ] Storage vs Memory Access Cost / 스토리지 접근이 메모리보다 훨씬 비싼 가스 구조
- [ ] Variable Packing / 작은 변수를 한 슬롯에 몰아 가스를 아끼는 배치
- [ ] constant and immutable / 배포 후 못 바꾸는 값을 저장소 없이 두는 두 키워드
- [ ] Caching Storage Reads / 반복되는 스토리지 읽기를 메모리에 캐싱하는 최적화
- [ ] Custom Errors vs Revert Strings / 문자열 revert보다 가스를 아끼는 커스텀 에러 비교
- [ ] calldata over memory / 함수 인자를 복사 없이 calldata로 받는 최적화
- [ ] unchecked Blocks / 오버플로 검사를 생략해 루프 가스를 줄이는 블록
- [ ] Loop Optimization / 루프마다 배열 길이를 다시 읽지 않는 최적화

---

# PART 5 · Compilation and Advanced Topics

## 15. Compilation and ABI

- [ ] Compiler Optimizer / 바이트코드 크기와 실행 가스를 맞바꾸는 최적화 옵션
- [ ] via-IR Pipeline / Yul 중간표현을 거쳐 더 강하게 최적화하는 컴파일 경로
- [ ] ABI JSON / 계약의 함수·이벤트 인터페이스를 담은 JSON 명세
- [ ] Function Selector / 함수 시그니처 해시 앞 4바이트로 함수를 구분하는 값
- [ ] Contract Size Limit / 배포 가능한 계약 바이트코드 크기의 상한

## 16. Advanced Solidity

- [ ] Inline Assembly / EVM에 더 가깝게 저수준으로 로직을 짜는 문법
- [ ] Assembly Opcodes / 어셈블리에서 직접 쓰는 저장소·메모리 연산 코드
- [ ] Transient Storage / 트랜잭션 끝나면 사라지는 값싼 임시 저장소
- [ ] Solidity Version Differences / 버전 간 오버플로 검사 등 호환성이 깨지는 차이

---

# 이 로드맵 밖

- 블록체인 전반 · 합의 · 스케일링 `software/role-based/blockchain.md`
- 개발 프레임워크 `software/skill-based/Blockchain/hardhat.md`, `foundry.md`
- 클라이언트 라이브러리 `software/skill-based/Blockchain/ethersjs.md`, `web3js.md`
- 보안 전반 `software/role-based/cyber-security.md`
- 소프트웨어 설계 원칙 `software/skill-based/CS-Theory/software-design-architecture.md`
