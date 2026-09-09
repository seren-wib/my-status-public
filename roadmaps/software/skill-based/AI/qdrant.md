# Qdrant `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Qdrant

## 1. What is Qdrant?

### Vector Search Core Concepts

- [ ] Vector Embedding / 텍스트·이미지를 숫자 벡터로 바꾸는 표현 방식
- [ ] Distance / cosine·dot·euclid 중 하나로 벡터 유사도를 재는 기준
- [ ] ANN Index / HNSW 그래프를 타고 근사 최근접만 훑는 구조

### What Is Qdrant

- [ ] Rust-based Vector Search Engine / 러스트로 짜여 속도와 메모리 안전성을 노린 엔진
- [ ] Payload-Centric Filtering / 페이로드 필터를 HNSW 탐색에 직접 끼워 넣는 방식
- [ ] REST and gRPC API / 두 프로토콜로 같은 기능을 제공하는 API
- [ ] Open-source + Qdrant Cloud / 셀프호스팅과 관리형 클라우드 중 고르는 선택지

### Key Features

- [ ] Integrated Filtered Search / 필터를 걸어도 근사 탐색 정확도가 유지되는 검색
- [ ] Quantization Memory Savings / 양자화로 벡터 메모리 사용량을 줄이는 기법
- [ ] Horizontal Scaling / 샤드로 나누고 레플리카로 복제해 늘리는 방법

## 2. Getting Started

### Running `택 1`

- Docker / 컨테이너 하나로 바로 띄우는 방법 `software/skill-based/Infra-DevOps/docker.md` `추천` `위임`
- [ ] Binary and Source Build / 바이너리를 받거나 소스를 직접 빌드하는 방법
- [ ] Kubernetes Helm Chart / 헬름 차트로 쿠버네티스에 배포하는 방법
- [ ] Qdrant Cloud / 직접 운영 없이 쓰는 관리형 호스팅 옵션

### Clients

- [ ] Python Client / 파이썬 SDK로 컬렉션과 포인트를 다루는 클라이언트 `추천`
- [ ] JavaScript, Rust, Go, Java Client / 파이썬 외 언어에서 쓰는 공식 SDK
- [ ] REST vs gRPC Selection / 지연시간과 처리량 기준으로 프로토콜을 고르는 판단
- [ ] Web UI Dashboard / 브라우저에서 컬렉션·포인트를 확인하는 관리 화면

### First Exercise

- [ ] Collection Creation / 벡터 크기와 거리 함수를 정해 컬렉션을 만드는 과정
- [ ] Point Upsert / 포인트를 삽입하거나 갱신하는 첫 데이터 적재
- [ ] Query Execution / 저장한 포인트를 대상으로 검색을 실행하는 과정

---

# PART 2 · Data Model

## 3. Collection

- [ ] Collection Management / 컬렉션을 생성·조회·목록·삭제하는 관리 작업
- [ ] Vector Params / 벡터 차원 수와 거리 함수를 지정하는 설정
- [ ] Named Vectors / 한 포인트에 이름 붙인 벡터를 여러 개 두는 방식
- [ ] Sparse Vectors Configuration / 키워드 검색용 희소 벡터를 설정하는 항목
- [ ] Multivector / ColBERT처럼 포인트당 벡터 여러 개로 늦은 상호작용을 하는 방식
- [ ] Collection Alias / 이름을 안 바꾸고 별칭만 바꿔치기하는 전환 기법
- [ ] on_disk Vector Storage / 벡터를 램 대신 디스크에 두는 저장 옵션

## 4. Point

- [ ] Point Structure / id·벡터·페이로드로 이뤄진 데이터 단위
- [ ] ID Types / 부호 없는 정수 또는 UUID로 포인트를 식별하는 방식
- [ ] Point CRUD / 포인트를 삽입·조회·삭제하는 기본 연산
- [ ] Batch Upsert and wait Option / 여러 포인트를 한 번에 넣고 반영을 기다리는 옵션
- [ ] Scroll / 커서 기반으로 전체 포인트를 순회하는 페이지네이션
- [ ] Count and Conditional Delete / 조건에 맞는 포인트 수를 세거나 지우는 연산

## 5. Payload

- [ ] Payload Types / 문자열·숫자·불리언·geo 등 메타데이터 타입
- [ ] Nested Payload Structure / 페이로드 안에 객체를 중첩해 담는 구조
- [ ] Payload Update / 키를 추가·덮어쓰기·삭제하는 갱신 방식
- [ ] Payload Index Necessity / 필터링 속도를 위해 인덱스가 필요한 이유
- [ ] Payload Index Types / 필드 타입별로 고르는 페이로드 인덱스 종류
- [ ] Tenant Index / 멀티테넌시 필터를 빠르게 하는 전용 인덱스
- [ ] Payload on_disk Storage / 페이로드를 디스크에 두는 저장 옵션

---

# PART 3 · Search

## 6. Search

- [ ] Query API / query_points로 검색을 던지는 통합 엔드포인트
- [ ] Search by Vector and Point ID / 벡터값 또는 기존 포인트 id로 검색하는 방법
- [ ] limit and offset / 반환 개수와 건너뛸 개수를 정하는 파라미터
- [ ] Response Options / 응답에 페이로드·벡터를 포함할지 정하는 옵션
- [ ] score_threshold / 유사도 점수가 기준 미달이면 제외하는 옵션
- [ ] Batch Search / 여러 쿼리를 한 요청으로 묶어 보내는 검색
- [ ] Grouped Search / group_by로 그룹당 상위 결과만 뽑는 검색

## 7. Filtering

- [ ] Filter Structure / must·should·must_not으로 조건을 조합하는 구조
- [ ] Match Condition / 값 일치·포함·제외로 거는 필터 조건
- [ ] Range Condition / gt·gte·lt·lte로 숫자 범위를 거는 조건
- [ ] Geo Condition / 사각·반경·다각형으로 위치를 거르는 조건
- [ ] Values Count, Is Empty, Is Null / 배열 길이·공백·null 여부를 거는 조건
- [ ] Nested Object Filter / 중첩 객체 안쪽 필드를 걸러내는 필터
- [ ] Full-text Match / 텍스트 인덱스를 걸어야 쓸 수 있는 부분 일치 검색
- [ ] Filterable HNSW / 필터가 그래프 탐색에 통합되는 방식

## 8. Advanced Retrieval

- [ ] Recommendation API / 좋은 예·나쁜 예 포인트로 추천하는 API
- [ ] Discovery API / 맥락 쌍과 목표점으로 탐색 범위를 좁히는 API
- [ ] Hybrid Search / 밀집 벡터와 희소 벡터를 함께 쓰는 검색
- [ ] Fusion / RRF·DBSF로 여러 결과 순위를 합치는 방법
- [ ] Prefetch Multi-Stage Query / 1차로 후보를 뽑고 2차로 재검색하는 쿼리
- [ ] Reranking Stage Setup / 프리페치 결과를 다른 기준으로 재정렬하는 단계
- [ ] Facet Aggregation / 페이로드 값별 개수를 집계하는 기능

---

# PART 4 · Performance and Operations

## 9. Indexing & Storage

- [ ] Segment Structure / 컬렉션을 나눠 담는 내부 저장 단위
- [ ] HNSW Config / m·ef_construct로 그래프 정확도와 속도를 조절하는 설정
- [ ] Optimizer / 인덱싱·메모리맵 전환 시점을 정하는 백그라운드 작업
- [ ] Memmap Disk Storage / 램 대신 메모리맵으로 디스크를 읽는 방식
- [ ] WAL / 쓰기를 먼저 로그에 남겨 장애 시 복구하는 구조

## 10. Quantization

- [ ] Scalar Quantization / float를 int8로 줄여 메모리를 아끼는 양자화
- [ ] Binary Quantization / 벡터값을 1비트로 압축해 가장 빠른 양자화
- [ ] Product Quantization / 벡터를 조각내 코드북으로 압축하는 양자화
- [ ] Oversampling and Rescoring / 양자화 손실을 원본 벡터로 재채점해 메꾸는 기법
- [ ] always_ram Placement Strategy / 특정 데이터를 무조건 램에 고정하는 배치 전략
- [ ] Accuracy-Memory Tradeoff Measurement / 양자화 설정별 정확도와 메모리를 재는 측정

## 11. Distributed Deployment

- [ ] Cluster Setup / Raft 합의로 노드 간 상태를 맞추는 클러스터 구성
- [ ] Shard Number and Distribution / 샤드 개수와 노드별 배치를 정하는 설정
- [ ] Replication Factor / 복제본 수와 쓰기 성공 기준 노드 수 설정
- [ ] Shard Transfer and Rebalancing / 노드 추가·제거 시 샤드를 재배치하는 과정
- [ ] Custom Sharding / shard_key로 테넌트 단위 샤드를 직접 지정하는 방식
- [ ] Read Consistency Options / 읽을 때 복제본 간 일관성 수준을 고르는 옵션
- [ ] Multitenancy Pattern / 샤드 대신 페이로드 필터로 테넌트를 나누는 패턴

## 12. Operations

### Backup

- [ ] Snapshot Create and Restore / 특정 시점 상태를 저장하고 복원하는 기능
- [ ] Collection and Full Storage Snapshot / 컬렉션 단위 또는 전체 스토리지 단위 스냅샷
- [ ] S3 Snapshot Storage / 스냅샷을 S3 호환 오브젝트 스토리지에 두는 방식

### Security

- [ ] API Key and Read-only Key / 쓰기 가능 키와 읽기 전용 키를 나눠 발급하는 인증
- [ ] JWT-based Access Control / 토큰 클레임으로 세밀하게 권한을 제한하는 인증
- [ ] TLS Configuration / 노드 간·클라이언트 통신을 암호화하는 설정

### Monitoring

- [ ] Metrics Endpoint and Telemetry / 내부 지표를 노출하는 모니터링 엔드포인트
- [ ] Prometheus + Grafana / 지표를 수집하고 대시보드로 보는 모니터링 조합

## 13. Performance Tuning

- [ ] Accuracy-Speed Tradeoff / ef 값을 올리거나 exact 검색으로 정확도를 높이는 절충
- [ ] Memory-First vs Disk-First Config / 속도와 용량 중 뭘 우선할지 정하는 배치 설정
- [ ] Indexing Pause During Bulk Load / 대량 적재 시 인덱싱 일시 중단 후 재개
- [ ] Payload Index for Filter Speed / 필터 조건 컬럼에 인덱스를 걸어 속도를 높이는 방법
- [ ] Resource Estimation / 벡터 수 × 차원 × 4byte로 필요 메모리를 계산하는 공식

---

# 이 로드맵 밖

- AI 엔지니어 전반 `software/role-based/ai-engineer.md`
- AI 에이전트 · RAG 설계 `software/skill-based/AI/ai-agents.md`
- Rust `software/skill-based/Languages/rust.md`
- 다른 벡터DB `software/skill-based/AI/weaviate.md`, `pinecone.md`, `chroma.md`
- 컨테이너 · 오케스트레이션 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
- 관측 도구 `software/skill-based/Infra-DevOps/prometheus.md`, `grafana.md`
