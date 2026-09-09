# Weaviate `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Weaviate

## 1. What is Weaviate?

### Vector Search Core Concepts

- [ ] Vector Embedding / 텍스트·이미지를 숫자 벡터로 바꾼 표현
- [ ] Distance Metric / cosine·dot·l2 중 하나로 벡터 거리를 재는 기준
- [ ] ANN Index / HNSW 그래프로 근사 최근접을 빠르게 찾는 색인

### What Is Weaviate

- [ ] Open-source Vector Database / 스키마와 모듈을 갖춘 오픈소스 벡터 DB
- [ ] Schema-based Object Store / 컬렉션에 프로퍼티를 미리 선언해 저장하는 방식
- [ ] Built-in Vectorizer Module / DB 안에서 벡터 생성을 모듈에 맡기는 구조
- [ ] REST, GraphQL, gRPC API / 세 프로토콜로 같은 기능에 접근하는 방법

### Key Features

- [ ] Native Hybrid Search / BM25 키워드와 벡터 점수를 함께 쓰는 검색
- [ ] Cross-reference / 객체끼리 서로 참조를 거는 관계 필드
- [ ] Native Multi-tenancy / 테넌트별로 데이터를 격리해 관리하는 기능

## 2. Getting Started

### Running `택 1`

- [ ] Docker Compose / 로컬에 컨테이너로 Weaviate를 띄우는 방법 `추천`
- [ ] Kubernetes Helm Chart / 쿠버네티스에 차트로 배포하는 방법
- [ ] Weaviate Cloud (WCD) / Weaviate가 직접 운영하는 관리형 클라우드
- [ ] Embedded Weaviate / 서버 없이 클라이언트 프로세스 안에서 실행하는 방식 `선택`

### Clients

- [ ] Python Client v4 / 컬렉션 객체 기반으로 재설계된 파이썬 클라이언트 `추천`
- [ ] TypeScript, Java, Go Client / 다른 언어에서도 쓸 수 있는 공식 클라이언트
- [ ] Connection Helpers / 로컬·클라우드 접속을 한 줄로 여는 함수
- [ ] REST and gRPC Ports / REST와 gRPC가 각각 쓰는 통신 포트

### First Exercise

- [ ] Collection Creation / 컬렉션을 정의해 생성하는 첫 단계
- [ ] Object Insertion / 정의된 컬렉션에 객체를 넣는 단계
- [ ] near_text Search / 텍스트 쿼리로 벡터 검색을 실행하는 첫 예제

---

# PART 2 · Data Model

## 3. Schema / Collection

- [ ] Collection Definition / 이전 버전의 Class를 대체한 스키마 단위
- [ ] Property Types / 프로퍼티마다 text·int·date 같은 형을 선언하는 방법
- [ ] Nested Object Property / 객체 안에 객체를 중첩해 넣는 프로퍼티
- [ ] Auto-schema vs Explicit Schema / 스키마를 자동 추론할지 직접 선언할지 선택
- [ ] Property Options / 토큰화·필터·검색 인덱싱 여부를 프로퍼티별로 설정
- [ ] Collection Config Mutability / 생성 후 바꿀 수 있는 설정과 없는 설정의 구분

## 4. Object

- [ ] UUID / 같은 입력이면 같은 UUID가 나오게 만드는 방법
- [ ] Object CRUD / 객체를 넣고 읽고 고치고 지우는 기본 연산
- [ ] Batch Import / 배치 크기를 자동·고정으로 조절해 대량 삽입
- [ ] Batch Error Collection and Retry / 배치 실패 건만 모아 재시도하는 처리
- [ ] Manual Vector vs Vectorizer / 벡터를 직접 넣을지 모듈이 생성하게 할지 선택

## 5. Cross-references

- [ ] Reference Property Definition / 다른 컬렉션 객체를 가리키는 참조 필드 선언
- [ ] One-way vs Two-way Reference / 참조를 한쪽만 걸지 양쪽에 걸지 선택
- [ ] Reference Add and Delete / 이미 만든 객체에 참조를 추가·제거하는 방법
- [ ] Reference Retrieval in Query / 쿼리에서 참조된 객체를 같이 가져오는 방법
- [ ] Graph Modeling Cost and Limits / 참조를 깊게 걸수록 커지는 조회 비용과 한계

## 6. Vector Index

- [ ] HNSW Index / ef·efConstruction·maxConnections로 정확도와 속도를 조절
- [ ] Flat Index / 그래프 없이 전수 비교로 검색하는 소규모용 인덱스
- [ ] Dynamic Index / 객체 수에 따라 flat과 HNSW를 자동 전환하는 인덱스
- [ ] Vector Cache / 인덱스 탐색 속도를 위해 벡터를 메모리에 캐시
- [ ] Named Vectors / 하나의 객체에 다중 벡터 공간
- [ ] Quantization / PQ·BQ·SQ로 벡터를 압축해 메모리를 줄이는 방법

---

# PART 3 · Search

## 7. Modules & Vectorizer

- [ ] Module System Overview / 기능을 모듈 단위로 붙였다 뗐다 하는 구조
- [ ] text2vec-* / openai·cohere·huggingface 등 텍스트 임베딩 모듈
- [ ] multi2vec-* / clip·bind로 이미지까지 함께 임베딩하는 모듈
- [ ] generative-* / 검색 결과를 LLM에 넘겨 답을 생성하는 모듈
- [ ] reranker-* Modules / 1차 검색 결과 순위를 다시 매기는 모듈
- [ ] Module API Key Injection / 외부 API 키를 환경변수나 헤더로 넘기는 방법
- [ ] Weaviate Embeddings / Weaviate가 자체 제공하는 임베딩 서비스 `선택`

## 8. Search

### Search Types

- [ ] Vector Search / 벡터나 기존 객체를 기준으로 유사도를 찾는 검색
- [ ] Semantic Search / 텍스트 쿼리에 이동 벡터를 더해 방향을 조정하는 검색
- [ ] Keyword Search / BM25 점수로 키워드를 매칭하는 전통 검색
- [ ] Hybrid Search / alpha 비율과 융합 방식으로 벡터·키워드를 섞는 검색

### Common Options

- [ ] Limit and Offset / 결과 개수와 시작 위치를 지정하는 옵션
- [ ] autocut / 점수 격차가 큰 지점에서 결과를 자동으로 끊는 방법
- [ ] Distance and Certainty / 유사도 임계값을 두 방식 중 하나로 지정
- [ ] Returned Metadata / score·distance 같은 부가 정보를 함께 받는 방법

## 9. Filtering

- [ ] Filter Syntax / Filter.by_property로 조건을 짜는 문법
- [ ] Comparison Operators / equal·greater_than 같은 비교 연산자 목록
- [ ] Set Operators / 배열 값이 일부·전부 포함되는지 검사하는 연산자
- [ ] Logical Combination / and·or로 여러 필터를 하나로 묶는 방법
- [ ] Reference-based Filter / 참조로 연결된 객체 속성으로 필터링하는 방법
- [ ] ID and Timestamp / 객체 ID나 생성 시각으로 걸러내는 필터

## 10. Aggregation & GraphQL

- [ ] Aggregate Query / count·mean·topOccurrences로 집계하는 쿼리
- [ ] group_by / 집계나 검색 결과를 특정 필드로 묶는 방법
- [ ] GraphQL Query Structure / Get·Aggregate·Explore 세 루트 타입 구조
- [ ] GraphQL vs Client v4 Comparison / GraphQL과 클라이언트 v4 중 어느 쪽을 쓸지 비교

## 11. Generative Search (RAG)

- [ ] Single Prompt / 검색된 객체마다 따로 답을 생성하는 방식
- [ ] Grouped Task / 검색 결과 전체를 묶어 한 번에 답을 생성하는 방식
- [ ] Property Injection in Prompt / 객체 프로퍼티 값을 프롬프트 안에 끼워 넣는 방법
- [ ] Generative Model Config and Swap / 생성에 쓸 LLM 모델을 설정하고 바꾸는 방법

---

# PART 4 · Operations

## 12. Multi-tenancy

- [ ] Tenant Creation and Listing / 테넌트를 만들고 목록을 조회하는 방법
- [ ] Tenant Status / ACTIVE·INACTIVE·OFFLOADED로 관리하는 테넌트 상태
- [ ] Per-Tenant Data Isolation / 테넌트마다 데이터를 완전히 분리해 저장하는 방식
- [ ] Auto Tenant Creation / 새 테넌트 이름이 오면 자동으로 만들어주는 설정
- [ ] Large-Scale Tenant Operations / 테넌트 수가 많을 때의 운영·확장 고려사항

## 13. Cluster & Replication

- [ ] Sharding / 컬렉션 데이터를 여러 노드로 쪼개 분산하는 방법
- [ ] Replication Factor / 같은 데이터를 몇 개 노드에 복제할지 지정하는 값
- [ ] Consistency Level / ONE·QUORUM·ALL로 읽기·쓰기 일관성을 조절
- [ ] Raft-based Schema Consensus / Raft 합의로 스키마 변경을 클러스터 전체에 반영
- [ ] Node Addition and Rebalancing / 노드를 추가하고 샤드를 재분배하는 과정
- [ ] Async Replication / 복제를 비동기로 처리해 쓰기 지연을 줄이는 방식

## 14. Security

- [ ] Authentication / API 키나 OIDC로 사용자를 인증하는 방법
- [ ] Authorization / RBAC 역할 기반으로 권한을 나눠 부여하는 방식
- [ ] Anonymous Access Disabling / 인증 없는 익명 접근을 막는 설정
- [ ] TLS Configuration / 통신 구간을 TLS로 암호화하는 설정

## 15. Operations

- [ ] Backup Module / filesystem·s3·gcs 중 백업 저장 위치를 고르는 모듈
- [ ] Backup Create and Restore / 백업을 생성하고 필요할 때 복원하는 절차
- [ ] Monitoring / Prometheus로 지표를 모으고 Grafana로 보는 방법
- [ ] Resource Estimation / 벡터 개수로 필요한 메모리량을 가늠하는 방법
- [ ] Version Upgrade Procedure / 버전을 올릴 때 따르는 절차와 주의사항

---

# 이 로드맵 밖

- AI 엔지니어 전반 `software/role-based/ai-engineer.md`
- AI 에이전트 · RAG 설계 `software/skill-based/AI/ai-agents.md`
- GraphQL `software/skill-based/CS-Theory/graphql.md`
- 다른 벡터DB `software/skill-based/AI/qdrant.md`, `pinecone.md`, `chroma.md`
- 키워드 검색 엔진 `software/skill-based/Data-DB/elasticsearch.md`
- 컨테이너 · 오케스트레이션 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
