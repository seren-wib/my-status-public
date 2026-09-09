# Chroma `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Chroma

## 1. What is Chroma?

### Vector Search Core Concepts

- [ ] Embedding / 텍스트·이미지를 실수 벡터로 바꾼 표현
- [ ] Distance Function / l2·cosine·ip 중 하나로 유사도를 재는 기준
- [ ] ANN Index / HNSW 그래프로 근사 최근접 이웃을 빠르게 찾는 구조

### What Is Chroma

- [ ] Open-source Embedding Database / 소스가 공개된 임베딩 전용 DB
- [ ] Local-first / 서버 없이 로컬 프로세스 안에서 바로 도는 방식
- [ ] Python-Native API / 파이썬 객체로 바로 쓰는 클라이언트 인터페이스
- [ ] Prototype-Scale RAG Focus / 대규모보다 빠른 RAG 프로토타이핑에 초점

### Selection Criteria

- [ ] When To Use Chroma / 프로토타입, 단일 노드, 로컬 개발
- [ ] Limitations / 분산 미지원, 대규모 부적합
- [ ] Chroma vs Managed And Distributed Alternatives / pinecone·qdrant 같은 대안과 갈리는 지점

## 2. Run Modes `택 1`

- [ ] EphemeralClient / 메모리에만 떠서 종료하면 사라지는 방식 `추천`
- [ ] PersistentClient / 로컬 디스크 경로에 저장해 재시작해도 남는 방식
- [ ] HttpClient / 별도로 뜬 Chroma 서버에 접속해 쓰는 방식
- [ ] AsyncHttpClient / HttpClient를 비동기로 쓰는 방식
- [ ] Chroma Cloud / 매니지드로 호스팅되는 Chroma 서비스 `선택`

## 3. Getting Started

- [ ] Installation / pip install chromadb 한 줄로 끝나는 설치 방법
- [ ] Client Instantiation / 코드에서 Client 객체를 만들어 연결하는 단계
- [ ] First Collection And Add / 컬렉션을 만들고 데이터를 처음 넣는 흐름
- [ ] First Query / 넣은 데이터를 검색해 결과를 확인하는 단계
- [ ] Persistence Path Layout / SQLite 파일, 인덱스 디렉터리

---

# PART 2 · Data Model

## 4. Collection

- [ ] Collection Management / 생성·조회·목록·삭제로 컬렉션을 다루는 함수들
- [ ] Collection Metadata / 컬렉션 단위로 붙이는 설정·태그 정보
- [ ] Distance Configuration / hnsw:space로 거리 함수를 지정하는 설정
- [ ] Collection Naming Rules / 길이·문자 제한 등 이름 짓는 규칙
- [ ] Collection Inspection / count·peek로 내용을 미리 훑는 방법
- [ ] Collection Partitioning Strategy / 데이터를 여러 컬렉션으로 나누는 기준

## 5. Record Structure

- [ ] Record Composition / id·문서·임베딩·메타데이터로 이뤄진 레코드 구조
- [ ] Document / 검색 결과로 그대로 돌려줄 원문 텍스트
- [ ] Metadata Value Types / 문자열·정수·실수·불리언만 허용하는 제약
- [ ] URIs / 문서 대신 외부 리소스 위치를 저장하는 필드 `선택`
- [ ] ID Design / 중복 방지와 멱등 재적재

## 6. Embedding Function

- [ ] Default Embedding Model / all-MiniLM-L6-v2(ONNX)가 기본으로 도는 모델
- [ ] SentenceTransformer Embedding Function / 다른 ST 모델로 바꿔 끼우는 방법
- [ ] API-Based Embedding Function / OpenAI·Cohere 등 외부 API로 임베딩하는 방식
- [ ] Custom Embedding Function Implementation / 인터페이스를 구현해 직접 만드는 방법
- [ ] Precomputed Embedding Passthrough / 미리 계산한 벡터를 그대로 넣는 방식
- [ ] Embedding Function Consistency / 넣을 때와 검색할 때 같은 함수를 써야 하는 이유

---

# PART 3 · Ingestion and Search

## 7. Data Ingestion

- [ ] Record CRUD / 추가·조회·수정·upsert·삭제하는 기본 연산
- [ ] Batch Ingestion And max_batch_size / 한 번에 넣을 수 있는 최대 건수 제한
- [ ] ID and Filter Query / get(ids), get(where)로 조건에 맞는 항목만 꺼내는 방법
- [ ] Document Chunking Strategy / 긴 문서를 검색 단위로 잘게 나누는 기준
- [ ] Document Re-Ingestion Pattern / 같은 문서를 다시 넣을 때 중복을 막는 방식

## 8. Query

- [ ] query_texts and query_embeddings / 텍스트로 넣을지 벡터로 직접 넣을지 정하는 방식
- [ ] n_results / 검색 결과를 몇 개 돌려줄지 정하는 개수
- [ ] include Option / 결과에 어떤 필드를 포함할지 고르는 옵션
- [ ] Concurrent Multi-Query / 한 번의 호출에 여러 쿼리를 동시에 넣는 방법
- [ ] Distance Interpretation / 값이 작을수록 더 유사하다는 반대 방향 해석
- [ ] Result Post-Processing / 거리 임계값으로 결과를 한 번 더 거르는 처리

## 9. Filtering

- [ ] Metadata Filter / where 인자로 메타데이터 조건을 거는 방법
- [ ] Comparison And Set Operators / 같다·크다·포함 등을 표현하는 비교 연산자
- [ ] Logical Operators / 조건 여러 개를 and·or로 묶는 연산자
- [ ] Document Filter / 문서 본문에 특정 문자열이 있는지 거르는 필터
- [ ] Filter And n_results Interaction / 필터링 후 남은 것 중에서 상위 n개를 뽑는 순서
- [ ] Pre-Filter Mechanics And Performance / 검색 전에 걸러 후보를 줄이는 방식과 비용

---

# PART 4 · Integration and Operations

## 10. Integration

- [ ] LangChain Chroma VectorStore / LangChain에서 Chroma를 벡터 저장소로 쓰는 연동
- [ ] LlamaIndex ChromaVectorStore / LlamaIndex에서 Chroma를 붙여 쓰는 연동
- [ ] RAG Assembly / 청킹 → 임베딩 → 검색 → 프롬프트
- [ ] Jupyter / Streamlit 프로토타입 워크플로

## 11. Server Operations

- [ ] chroma run / 호스트·포트·경로를 지정해 서버로 띄우는 명령
- [ ] Environment Variables / CHROMA_SERVER_* 접두사로 서버 설정을 넣는 방법
- [ ] Docker and Docker Compose / 컨테이너로 Chroma 서버를 배포하는 방법
- [ ] Authentication / 토큰이나 기본 인증으로 접근을 제한하는 방법
- [ ] Tenant And Database / 하나의 서버 안에서 논리적으로 데이터를 나누는 단위
- [ ] CORS Configuration / 브라우저에서 다른 출처의 요청을 허용하는 설정

## 12. Persistence & Migration

- [ ] SQLite Metadata Store / 컬렉션·메타데이터를 담는 SQLite 파일
- [ ] HNSW Index File Layout / 벡터 인덱스가 디스크에 저장되는 구조
- [ ] Backup And Restore / 영속화 디렉터리를 통째로 복사해 옮기는 방법
- [ ] Version Upgrade Migration / Chroma 버전을 올릴 때 데이터를 옮기는 절차
- [ ] Collection Rebuild / 임베딩 모델을 바꾸면 인덱스를 재생성해야 하는 이유

## 13. Performance & Limits

- [ ] HNSW Parameters / M·construction_ef·search_ef로 정밀도와 속도를 조절
- [ ] Memory Footprint Estimation / 벡터 수×차원으로 메모리 사용량을 어림잡는 방법
- [ ] Single-Node Scaling Limit / 노드 하나로 감당 가능한 데이터량의 한계
- [ ] Batch Insert Tuning / 배치 크기를 조절해 삽입 속도를 높이는 방법
- [ ] Migration Target Evaluation / 규모가 커지면 어떤 DB로 옮길지 판단하는 기준

---

# 이 로드맵 밖

- AI 엔지니어 전반 `software/role-based/ai-engineer.md`
- AI 에이전트 · RAG 설계 `software/skill-based/AI/ai-agents.md`
- Python `software/skill-based/Languages/python.md`
- 관리형 대안 `software/skill-based/AI/pinecone.md`
- 확장 시 이전 대상 `software/skill-based/AI/qdrant.md`, `weaviate.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
