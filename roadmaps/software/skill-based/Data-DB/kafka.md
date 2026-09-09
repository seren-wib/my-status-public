# Kafka `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Kafka

## 1. What is Kafka?

### Overview of Kafka / What is it?

- [ ] Distributed Event Streaming Platform / 여러 브로커가 이벤트를 나눠 처리하는 플랫폼
- [ ] Pub/Sub Messaging System / 구독자에게 흘려보내되 지우지 않는 방식
- [ ] Distributed Commit Log / 기록 순서를 그대로 보존하는 로그
- [ ] Append-only, Immutable Log / 끝에만 추가하고 고치지 않는 구조

### Core Use Cases

- [ ] Event-Driven Architecture / 상태 변화를 이벤트로 전파하는 구조
- [ ] Log Aggregation / 여러 서버 로그를 한 곳에 모으는 용도
- [ ] Stream Processing / 흐르는 데이터를 실시간으로 처리하는 방식
- [ ] Metrics and Telemetry Collection / 지표와 원격 측정값을 모으는 용도
- [ ] Data Integration / CDC처럼 시스템 간 데이터를 잇는 용도

### Kafka vs Other Systems

- [ ] Kafka vs RabbitMQ / 지우지 않는 로그와 지우는 큐의 차이
- [ ] Kafka vs Traditional Message Queues / 보관 여부로 갈리는 메시징 방식
- [ ] When to choose Kafka? / 순서 보존과 재처리가 필요할 때 고르는 기준

## 2. Core Concepts

### Basic Units

- [ ] Record and Message / 큐가 아닌 로그에 쌓이는 데이터 한 건
- [ ] Key, Value, Headers, Timestamp / 레코드를 이루는 필드들
- [ ] Topic / 같은 종류 레코드를 묶는 이름
- [ ] Partition / 순서를 보장하는 단위로 나눈 조각
- [ ] Offset / 파티션 안에서 위치를 가리키는 번호

### Components

- [ ] Broker / 파티션을 저장하고 서비스하는 서버
- [ ] Cluster / 여러 브로커가 묶인 집합
- [ ] Producer / 로그 끝에 레코드를 이어붙이는 주체
- [ ] Consumer / 오프셋으로 읽은 위치를 기억하는 주체
- [ ] Consumer Group / 파티션을 나눠 맡는 컨슈머 묶음

## 3. Getting Started

### Installation `택 1`

- [ ] Docker and Docker Compose / 컨테이너로 브로커를 띄우는 방법 `추천`
- [ ] Binary Download / 바이너리를 받아 직접 실행하는 방법
- [ ] Managed Service (Confluent Cloud, MSK) / 클라우드가 운영을 대신하는 방식

### Cluster Metadata `택 1`

- [ ] KRaft Mode / 브로커끼리 합의로 메타데이터를 관리하는 방식 `추천`
- [ ] ZooKeeper Mode / 4.0에서 빠진 옛 메타데이터 방식

### CLI Basics

- [ ] kafka-topics / 토픽을 만들고 조회하는 명령
- [ ] kafka-console-producer / 콘솔에서 레코드를 보내는 명령
- [ ] kafka-console-consumer / 콘솔에서 레코드를 읽는 명령
- [ ] kafka-consumer-groups / 컨슈머 그룹과 오프셋을 조회하는 명령
- [ ] kafka-configs / 브로커·토픽 설정을 바꾸는 명령

---

# PART 2 · Producers and Consumers

## 4. Producer

### Send Methods

- [ ] Fire-and-forget / 응답을 기다리지 않고 보내는 방식
- [ ] Synchronous Send / 응답을 받을 때까지 기다리는 방식
- [ ] Asynchronous Send with Callback / 콜백으로 결과를 나중에 받는 방식

### Partitioning

- [ ] Default Partitioner / 키 유무로 파티션을 정하는 기본 규칙
- [ ] Key-based Partitioning / 같은 키를 같은 파티션에 몰아주는 방식
- [ ] Sticky Partitioner / 키 없을 때 배치를 한 파티션에 묶는 방식
- [ ] Custom Partitioner / 파티션 배정 규칙을 직접 정하는 방법

### Key Configuration

- [ ] Acknowledgements / acks 값으로 복제 확인 수준을 정하는 옵션
- [ ] Batching and Compression / batch.size·linger.ms로 묶어 압축하는 설정
- [ ] Retries and Timeouts / retries·delivery.timeout.ms로 재시도를 거는 설정

### Reliability

- [ ] Idempotent Producer / 같은 레코드가 중복 저장되지 않게 막는 기능
- [ ] Ordering Guarantees / max.in.flight.requests로 순서를 지키는 조건

## 5. Consumer

### Consumption Flow

- [ ] Poll Loop / 브로커에 반복해서 레코드를 당겨오는 루프
- [ ] Subscribe vs Assign / 그룹이 배정할지 직접 정할지의 차이
- [ ] Consumer Lag / 최신 오프셋과 커밋 오프셋 사이 지연

### Consumer Group / Rebalancing

- [ ] Group Coordinator / 그룹의 파티션 배정을 맡는 브로커
- [ ] Partition Assignment Strategies / 파티션을 컨슈머에 나누는 전략
- [ ] Eager vs Cooperative Rebalancing / 전원 멈출지 일부만 옮길지의 차이
- [ ] Static Group Membership / 재시작해도 같은 멤버로 취급하는 설정

### Offset Management

- [ ] Auto Commit / 일정 주기마다 오프셋을 자동 저장하는 방식
- [ ] Manual Commit / 동기·비동기로 오프셋을 직접 저장하는 방식
- [ ] Offset Reset Policy / auto.offset.reset으로 시작 위치를 정하는 정책
- [ ] seek / 오프셋을 되돌려 메시지를 다시 읽는 메서드

### Key Configuration

- [ ] Fetch Tuning / fetch.min.bytes·max.poll.records로 가져올 양을 정하는 설정
- [ ] Liveness Detection / session.timeout.ms·heartbeat.interval.ms로 생존을 판단하는 설정
- [ ] Processing Timeout / max.poll.interval.ms로 처리 지연 한도를 정하는 설정

## 6. Serialization

### Serialization Formats `택 1`

- [ ] Avro / 스키마를 붙여 이진으로 직렬화하는 포맷 `추천`
- [ ] Protobuf / 구글이 만든 이진 직렬화 포맷
- [ ] JSON / 사람이 읽기 쉬운 텍스트 직렬화 포맷

### Schema Registry

- [ ] Subject and Version / 스키마를 이름과 버전으로 구분하는 단위
- [ ] Schema Evolution / 스키마가 바뀌어도 호환을 유지하며 진화하는 것
- [ ] Compatibility Modes / 이전·이후 스키마와의 호환 범위를 정하는 설정

---

# PART 3 · Storage and Internals

## 7. Storage Internals

### Log Structure

- [ ] Log Segments / 로그를 일정 크기로 나눈 파일 단위
- [ ] Offset Index and Time Index / 오프셋·시간으로 위치를 빠르게 찾는 색인
- [ ] Page Cache / OS가 디스크 대신 메모리로 읽고 쓰는 캐시
- [ ] Zero-Copy Transfer / 커널 안에서 바로 네트워크로 보내는 전송

### Retention

- [ ] Time-based Retention / 정해진 기간이 지나면 지우는 보관 방식
- [ ] Size-based Retention / 정해진 용량을 넘으면 지우는 보관 방식
- [ ] Log Compaction / 키별 최신 값만 남기고 나머지를 지우는 방식
- [ ] Tombstone Records / 삭제를 표시하는 값 없는 레코드

## 8. Replication

- [ ] Leader and Follower Replica / 쓰기를 받는 복제본과 따라가는 복제본
- [ ] ISR (In-Sync Replicas) / 리더와 동기화된 복제본 집합
- [ ] Replication Factor / 파티션을 복제할 개수
- [ ] Minimum In-Sync Replicas / min.insync.replicas로 쓰기 성공 조건을 정하는 값
- [ ] Leader Election / ISR 안에서 새 리더를 뽑는 절차
- [ ] Unclean Leader Election / ISR 밖 복제본을 리더로 올려 데이터를 잃는 선택

## 9. Delivery Semantics

- [ ] At-most-once / 재전송 없이 놓칠 수 있는 전달 등급
- [ ] At-least-once / 중복은 감수하고 놓치지 않는 전달 등급
- [ ] Exactly-once / 중복도 손실도 없이 보장하는 전달 등급
- [ ] Transactional Producer / 여러 파티션 쓰기를 한 트랜잭션으로 묶는 프로듀서
- [ ] read_committed Isolation Level / 커밋된 트랜잭션 결과만 읽는 격리 수준
- [ ] Consume-Transform-Produce Pattern / 읽고 가공해 다시 쓰기를 트랜잭션으로 묶는 패턴

---

# PART 4 · Ecosystem

## 10. Kafka Connect

- [ ] Source Connector / 외부 시스템에서 토픽으로 가져오는 커넥터
- [ ] Sink Connector / 토픽에서 외부 시스템으로 내보내는 커넥터
- [ ] Standalone vs Distributed Mode / 단일 프로세스로 돌릴지 분산으로 돌릴지의 차이
- [ ] Converters / 레코드를 직렬화 포맷으로 바꾸는 구성요소
- [ ] Single Message Transforms (SMT) / 레코드 하나를 지나가며 가볍게 바꾸는 변환
- [ ] Error Handling / DLQ로 실패한 레코드를 따로 빼는 처리 방식

### Commonly Used Connectors

- [ ] JDBC Connector / 관계형 DB와 토픽을 잇는 커넥터
- [ ] S3 Sink Connector / 토픽 데이터를 S3로 내보내는 커넥터
- [ ] Debezium / DB 변경 로그를 읽어 CDC로 스트리밍하는 도구

## 11. Kafka Streams

### Abstractions

- [ ] KStream / 레코드 하나하나를 스트림으로 다루는 추상화
- [ ] KTable / 키별 최신 값을 테이블처럼 다루는 추상화
- [ ] GlobalKTable / 모든 파티션 데이터를 각 인스턴스에 복제하는 테이블

### Operators

- [ ] Stateless Operations / map·filter처럼 이전 상태 없이 처리하는 연산
- [ ] Aggregations / groupByKey로 묶어 count·reduce로 집계하는 연산
- [ ] Joins / 스트림끼리 또는 스트림과 테이블을 합치는 연산
- [ ] Windowing / 겹치거나 안 겹치는 시간 구간으로 나누는 방식

### State Storage

- [ ] State Stores / 집계·조인 상태를 로컬에 저장하는 저장소
- [ ] Changelog Topics / 상태 저장소 변경을 복구용으로 기록하는 토픽
- [ ] Interactive Queries / 애플리케이션 밖에서 상태 저장소를 조회하는 기능

## 12. ksqlDB `선택`

- [ ] Streams vs Tables / SQL에서 스트림과 테이블을 구분하는 개념
- [ ] Push Query and Pull Query / 계속 밀어줄지 요청 시점만 답할지의 차이
- [ ] Materialized Views / 집계 결과를 미리 구체화해 두는 뷰

---

# PART 5 · Operations

## 13. Cluster Operations

- [ ] Broker Configuration / 브로커 단위로 거는 설정값
- [ ] Topic Configuration / 토픽 단위로 거는 설정값
- [ ] Partition Reassignment / 파티션을 다른 브로커로 옮기는 작업
- [ ] Adding and Removing Brokers / 브로커를 넣거나 빼는 절차
- [ ] Rack Awareness / 랙 정보를 보고 복제본을 분산 배치하는 기능
- [ ] Quotas and Throttling / 클라이언트별 처리량 상한을 거는 기능

## 14. Monitoring

### Key Metrics

- [ ] Consumer Lag / 지연이 커지고 있는지 감시하는 지표
- [ ] Under-Replicated Partitions / ISR이 목표보다 적게 남은 파티션
- [ ] Request Latency / 요청 처리에 걸리는 시간 지표
- [ ] Broker Throughput / 브로커가 처리하는 처리량 지표
- [ ] JMX Metrics / JVM 표준 인터페이스로 노출하는 지표

### Tools

- [ ] Prometheus + Grafana / 지표를 모으고 그래프로 보는 도구 조합 `추천`
- [ ] CMAK and Kafka Manager / 파티션·토픽을 웹에서 관리하는 도구
- [ ] Conduktor / 클러스터를 GUI로 관리하는 상용 도구

## 15. Security

- [ ] SSL and TLS Encryption / 통신 구간을 암호화하는 설정
- [ ] SASL / PLAIN·SCRAM 등 인증 메커니즘을 고르는 설정
- [ ] ACLs / 누가 어떤 토픽에 접근할 수 있는지 정하는 권한 목록
- [ ] Encryption at Rest / 디스크에 저장된 데이터를 암호화하는 기능

## 16. Capacity Planning

- [ ] Choosing Partition Count / 처리량과 병렬성을 보고 파티션 수를 정하는 일
- [ ] Broker Sizing / 브로커 대수와 사양을 정하는 일
- [ ] Disk and Network Sizing / 디스크 용량과 네트워크 대역폭을 정하는 일
- [ ] Retention Sizing / 보관 기간에 필요한 디스크를 가늠하는 일

---

# 이 로드맵 밖

- 백엔드 전반 · 메시지 브로커 선택 `software/role-based/backend.md`
- 데이터 파이프라인 `software/role-based/data-engineer.md`
- 확장 설계 · 이벤트 기반 아키텍처 `software/skill-based/CS-Theory/system-design.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
- 검색 · 로그 저장소 `software/skill-based/Data-DB/elasticsearch.md`
- 관측 도구 `software/skill-based/Infra-DevOps/prometheus.md`, `grafana.md`
