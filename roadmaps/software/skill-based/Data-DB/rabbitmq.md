# RabbitMQ `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to RabbitMQ

## 1. What is RabbitMQ?

### Overview of RabbitMQ / What is it?

- [ ] Message Broker / 생산자와 소비자 사이에서 메시지를 중계하는 서버
- [ ] AMQP 0-9-1 Implementation / 익스체인지·큐·바인딩을 정의하는 메시징 프로토콜
- [ ] Smart Broker and Dumb Consumer / 라우팅 판단은 브로커가 하고 소비는 받기만 하는 모델
- [ ] Erlang / 프로세스 격리로 대량 연결을 가볍게 견디는 실행 기반

### Core Use Cases

- [ ] Asynchronous Task Queue / 무거운 작업을 큐에 넣고 나중에 처리하는 방식
- [ ] Service Decoupling / 서비스 간 직접 호출 없이 메시지로 연결하는 구조
- [ ] Work Distribution / 느린 워커에 맞춰 작업을 고르게 나누는 방법
- [ ] RPC over Messaging / 동기 호출을 메시지 왕복으로 흉내내는 방식

### Comparison with Other Systems

- [ ] RabbitMQ vs Kafka / 받으면 지우는 큐와 쌓아만 두는 로그의 차이
- [ ] RabbitMQ vs SQS / 자체 운영 브로커와 완전관리형 큐의 차이
- [ ] When to choose RabbitMQ? / 정교한 라우팅 규칙이 필요할 때 고르는 이유

## 2. Getting Started

### Installation `택 1`

- [ ] Docker and Docker Compose / management 이미지로 관리 UI까지 함께 올리는 방법 `추천`
- [ ] Package Manager / OS 패키지로 설치해 서비스로 등록하는 방법
- [ ] Managed Service (CloudAMQP, Amazon MQ) / 클러스터 운영을 대신 맡기는 호스팅 선택지

### First Run

- [ ] Management Plugin / 큐와 익스체인지 상태를 웹 화면으로 보는 플러그인
- [ ] rabbitmqctl / 노드와 큐 상태를 명령줄에서 다루는 도구
- [ ] rabbitmqadmin / HTTP API를 명령줄로 감싼 관리 도구
- [ ] Port / AMQP는 5672·관리 UI는 15672인 기본 포트
- [ ] Hello World Producer and Consumer / 최소 코드로 발행과 소비를 확인하는 예제

## 3. AMQP Core Concepts

### Components

- [ ] Producer and Consumer / 메시지를 보내는 쪽과 받아서 처리하는 쪽
- [ ] Exchange / 라우팅 규칙에 따라 큐로 메시지를 밀어 넣는 단위
- [ ] Queue / 소비될 때까지 메시지를 담아 두는 버퍼
- [ ] Binding / 익스체인지와 큐를 바인딩 키 조건으로 잇는 규칙
- [ ] Routing Key / 메시지에 붙여 바인딩 키와 매칭시키는 값
- [ ] Virtual Host / 하나의 브로커 안에서 자원을 논리적으로 나누는 단위

### Connection Layer

- [ ] Connection / 브로커와 맺는 하나의 TCP 연결
- [ ] Channel / 하나의 연결을 나눠 쓰는 가상 회선
- [ ] Channel Reuse Principles / 매 작업마다 채널을 새로 열지 않는 원칙
- [ ] Heartbeat / 끊어진 연결을 감지하는 주기 신호
- [ ] Client Library / pika·amqplib 같은 언어별 AMQP 구현체

---

# PART 2 · Messaging Model

## 4. Exchange

- [ ] Direct Exchange / 라우팅 키가 정확히 일치하는 큐로만 보내는 방식
- [ ] Fanout Exchange / 라우팅 키를 무시하고 바인딩된 모든 큐로 뿌리는 방식
- [ ] Topic Exchange / *·#로 라우팅 키 패턴을 매칭하는 방식
- [ ] Headers Exchange / 라우팅 키 대신 헤더 값으로 큐를 고르는 방식
- [ ] Default Exchange / 큐 이름을 라우팅 키 삼아 바로 연결되는 익스체인지
- [ ] Alternate Exchange / 어떤 큐에도 안 꽂힌 메시지를 대신 받는 익스체인지
- [ ] Exchange to Exchange Binding / 익스체인지끼리 연결해 라우팅을 중첩하는 구조

## 5. Queue

### Attributes

- [ ] Durable vs Transient / 브로커 재시작 후 큐 정의가 남는지 여부
- [ ] Exclusive Queue / 연결 하나만 쓰고 끊기면 사라지는 큐
- [ ] Auto-delete Queue / 마지막 소비자가 빠지면 자동으로 지워지는 큐
- [ ] Queue Argument / x-로 시작하는 큐별 세부 동작 옵션

### Lifetime and Limits

- [ ] Message TTL / 큐에 머문 메시지를 자동 만료시키는 시간
- [ ] Queue TTL / 오래 비어 있으면 큐 자체를 지우는 시간
- [ ] Max Length / 큐 길이를 제한하고 넘칠 때 처리를 정하는 값
- [ ] Priority Queue / 우선순위가 높은 메시지를 먼저 꺼내는 큐
- [ ] Lazy Queue vs Default Queue / 메모리 대신 디스크에 먼저 쌓아 메모리를 아끼는 방식

## 6. Message

- [ ] Payload / 메시지가 실어 나르는 실제 데이터 본문
- [ ] Properties / content-type 등 메시지에 붙는 메타데이터
- [ ] Persistent vs Transient Message / 브로커 재시작에도 메시지가 살아남는지 여부
- [ ] Correlation ID and Reply-To / 요청·응답 메시지를 짝짓고 돌려줄 큐를 알리는 값
- [ ] Per-message Expiration / 메시지 하나하나에 개별로 거는 만료 시간
- [ ] Serialization Choice / JSON·Protobuf 등 페이로드 직렬화 형식의 선택

## 7. Messaging Patterns

- [ ] Work Queue / 여러 워커가 큐 하나를 나눠 소비하는 패턴
- [ ] Publish and Subscribe / 하나의 발행을 여러 구독자가 함께 받는 패턴
- [ ] Routing / 조건에 맞는 큐만 골라 메시지를 보내는 패턴
- [ ] Topic-based Filtering / 라우팅 키 패턴으로 구독 범위를 좁히는 방식
- [ ] Request and Reply (RPC) / 응답을 기다리는 왕복형 메시지 교환 패턴
- [ ] Delayed Message / 플러그인으로 지정 시간 뒤에 도착시키는 메시지
- [ ] Outbox Pattern / DB 트랜잭션과 메시지 발행을 함께 보장하는 패턴
- [ ] Saga / 이벤트 체인으로 분산 트랜잭션을 엮는 패턴 `선택`

---

# PART 3 · Reliability

## 8. Publisher Reliability

- [ ] Publisher Confirm / 브로커가 받았음을 발행자에게 알려주는 응답
- [ ] Transaction (tx) / 발행을 묶어 커밋하되 속도를 크게 낮추는 방식
- [ ] Mandatory Flag / 라우팅 실패한 메시지를 발행자에게 돌려주는 옵션
- [ ] Publisher-side Retry / 확인을 못 받은 발행을 다시 시도하는 로직
- [ ] Automatic Connection Recovery / 끊긴 연결과 채널을 클라이언트가 자동 복구하는 기능

## 9. Consumer Reliability

- [ ] Manual Ack / 처리를 끝낸 뒤 직접 완료를 알리는 방식
- [ ] Risks of Auto Ack / 받자마자 확인 처리해 처리 전에 유실될 위험
- [ ] Nack, Reject, requeue / 처리에 실패한 메시지를 되돌리거나 버리는 방법
- [ ] Prefetch Count / 소비자가 동시에 들고 있을 미확인 메시지 수
- [ ] Consumer Cancel Notification / 큐나 노드가 사라져 소비가 끊길 때 오는 신호
- [ ] Idempotent Consumer / 같은 메시지를 여러 번 받아도 결과가 같게 하는 소비자
- [ ] Single Active Consumer / 여러 소비자 중 하나만 실제로 메시지를 받게 하는 설정

## 10. Error Handling

- [ ] Dead Letter Exchange (DLX) / 처리 못한 메시지를 대신 받는 익스체인지
- [ ] Dead Letter Routing Key / 죽은 편지를 보낼 때 새로 붙이는 라우팅 키
- [ ] Retry Queue / TTL로 지연시켰다 원래 큐로 돌려보내는 큐
- [ ] Poison Message / 계속 실패해 재시도만 반복시키는 메시지
- [ ] Delivery Limit / 재전달 횟수를 정해 무한 반복을 막는 값
- [ ] Message Ordering Guarantee Scope / 순서가 보장되는 범위가 큐 하나로 좁다는 사실

---

# PART 4 · Cluster and Scaling

## 11. Clustering

- [ ] Cluster Node / 메타데이터를 디스크에 둘지 메모리에 둘지의 구분
- [ ] Erlang Cookie / 노드끼리 클러스터로 묶일 때 맞춰야 하는 비밀값
- [ ] Peer Discovery Plugin / 새 노드가 기존 클러스터를 자동으로 찾는 방법
- [ ] Metadata Replication Scope / 큐 위치가 아닌 정의만 전 노드에 복제되는 범위
- [ ] Client Connection Distribution / 클라이언트 연결을 여러 노드로 고르게 붙이는 방법
- [ ] Network Partition / 클러스터가 갈라졌을 때 대응하는 정책

## 12. Queue Replication

- [ ] Classic Queue / 복제 없이 단일 노드에 남는 기본 큐
- [ ] Classic Mirrored Queue / 여러 노드에 큐 전체를 복사하던 폐기 방식
- [ ] Quorum Queue / 다수결 합의로 복제 안전성을 보장하는 큐 `추천`
- [ ] Raft Consensus / 리더를 뽑아 로그 복제를 합의하는 알고리즘
- [ ] Stream Queue / 메시지를 지우지 않고 반복해 읽을 수 있는 큐
- [ ] Queue Type Selection Criteria / 상황에 맞는 큐 타입을 고르는 기준

## 13. Multi-Cluster

- [ ] Federation Plugin / 독립된 두 브로커 사이에 메시지를 넘기는 연결
- [ ] Shovel Plugin / 한 큐에서 다른 브로커 큐로 메시지를 퍼 나르는 도구
- [ ] Federation vs Shovel / 익스체인지 단위로 묶을지 큐 단위로 옮길지의 차이
- [ ] Geo-distributed Topology / 지역이 다른 브로커들을 연결하는 구성

## 14. Protocols and Plugins `선택`

- [ ] MQTT Plugin / IoT 기기용 경량 프로토콜을 지원하는 플러그인
- [ ] STOMP and Web STOMP / 단순 텍스트 프로토콜과 그 웹소켓 버전
- [ ] AMQP 1.0 / 0-9-1과 호환되지 않는 별도 표준 프로토콜
- [ ] Plugin Management / 플러그인을 켜고 끄는 명령줄 도구

---

# PART 5 · Operations

## 15. Configuration

- [ ] rabbitmq.conf / 대부분의 설정값을 담는 기본 설정 파일
- [ ] Memory Watermark / 메모리 사용량이 넘으면 발행을 막는 한계선
- [ ] Disk Free Limit / 디스크 여유가 부족하면 발행을 막는 한계선
- [ ] Flow Control / 느린 소비에 맞춰 발행자를 늦추는 장치
- [ ] Resource Alarm / 메모리·디스크 한계에 걸리면 발동하는 경보
- [ ] Definitions Export and Import / 유저·큐·바인딩 설정을 통째로 옮기는 기능

## 16. Monitoring

- [ ] Key Metrics / 큐 쌓임·미확인 수·발행 속도 같은 핵심 지표
- [ ] Management HTTP API / 웹 UI가 내부적으로 쓰는 REST 인터페이스
- [ ] Prometheus Plugin / 지표를 수집해 외부로 노출하는 플러그인
- [ ] Log Configuration / 로그 수준과 출력 위치를 정하는 설정
- [ ] Setting Alerting Thresholds / 지표가 위험 수준을 넘으면 알리도록 정하는 기준

## 17. Security

- [ ] User, Permission, vhost / 사용자·권한·가상호스트로 접근 범위를 나누는 단위
- [ ] User Tag / 관리자·모니터링처럼 UI 접근 범위를 정하는 역할
- [ ] TLS Configuration / 연결 구간을 암호화하는 인증서 설정
- [ ] Authentication Backend / LDAP·OAuth로 인증을 외부에 위임하는 방식
- [ ] Network Isolation / 브로커 접근을 특정 네트워크로 제한하는 조치

## 18. Performance and Production

- [ ] Throughput Factors / 영속성·ack·prefetch가 좌우하는 처리량 요인
- [ ] Connection and Channel Churn / 연결과 채널을 함부로 새로 맺지 않는 운영 원칙
- [ ] Queue Count Design / 큐를 몇 개로 쪼갤지 정하는 설계
- [ ] Capacity Planning / 예상 트래픽에 맞춰 필요한 자원을 미리 잡는 계획
- [ ] Rolling Upgrade / 서비스를 멈추지 않고 노드를 순서대로 올리는 방식
- [ ] Backup / 정의와 데이터를 복구용으로 미리 내보내는 작업

---

# 이 로드맵 밖

- 백엔드 전반 · 비동기 처리 `software/role-based/backend.md`
- Kafka `software/skill-based/Data-DB/kafka.md`
- 이벤트 기반 아키텍처 `software/skill-based/CS-Theory/system-design.md`
- Redis Pub/Sub `software/skill-based/Data-DB/redis.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
