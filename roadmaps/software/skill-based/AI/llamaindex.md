# LlamaIndex `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to LlamaIndex

## 1. What is LlamaIndex?

### Overview of LlamaIndex

- [ ] Data Framework for LLM / LLM에 데이터를 연결하는 용도로 특화된 프레임워크
- [ ] Indexing And Retrieval Focus / 체인 조립보다 색인·검색 자체에 집중하는 설계
- [ ] RAG Pipeline Skeleton / 읽기부터 답변까지 RAG 흐름을 갖춘 뼈대
- [ ] LlamaIndex vs LangChain Emphasis / 체인 조립 대신 데이터 파이프라인이 중심인 차이

### Five-Stage Flow

- [ ] Loading / 문서를 원본 소스에서 읽어들이는 첫 단계
- [ ] Indexing / 읽은 문서를 노드로 쪼개 색인에 넣는 단계
- [ ] Storing / 만든 인덱스를 디스크·DB에 보존하는 단계
- [ ] Querying / 저장된 인덱스에 질문을 던져 답을 얻는 단계
- [ ] Evaluating / 검색·응답 품질을 점수로 검증하는 단계

### Package Structure

- [ ] llama-index-core / 벤더 의존 없는 핵심 추상화만 담은 패키지
- [ ] Integration Packages / llms·embeddings·vector_stores별로 나뉜 연동 패키지
- [ ] LlamaHub / 리더·도구·팩을 모아둔 커뮤니티 레지스트리
- [ ] LlamaParse / 문서 파싱을 전담하는 별도 클라우드 패키지 `선택`

## 2. Getting Started

### Installation and Configuration

- [ ] pip Installation / core + 필요한 통합만
- [ ] API Key / OPENAI_API_KEY 등 환경변수로 주입하는 방법
- [ ] Global Settings / llm·chunk_size를 전역 기본값으로 한 번에 거는 방법
- [ ] Five-Line Starter / 폴더를 읽어 인덱스까지 다섯 줄로 만드는 최소 예제

### Model Connection

- [ ] LLM Interface / complete·chat 두 방식으로 모델을 부르는 공통 창구
- [ ] Embedding Model Swap / 임베딩 모델을 다른 것으로 갈아끼우는 방법
- [ ] Local Model / Ollama·HuggingFace로 로컬에서 모델을 돌리는 방식 `선택`
- [ ] Async and Streaming Calls / 기다리지 않고 비동기·스트림으로 받는 호출 방식

## 3. Core Abstractions

- [ ] Document / 원본 텍스트와 메타데이터를 담는 최상위 단위
- [ ] Node and TextNode / 문서를 쪼갠 뒤 다루는 최소 처리 단위
- [ ] Metadata / excluded_keys로 LLM에 안 보낼 필드를 지정하는 방법
- [ ] Relationships / prev·next·parent로 노드 순서를 잇는 구조
- [ ] NodeWithScore / 검색 결과에 유사도 점수를 붙인 노드
- [ ] QueryBundle / 질의 문자열과 임베딩을 함께 묶은 객체
- [ ] Response Object / source_nodes로 근거 노드까지 담는 응답 형태

---

# PART 2 · Ingestion and Indexing

## 4. Data Connectors

### Basic Loaders

- [ ] SimpleDirectoryReader / 폴더 안 파일을 통째로 읽어 문서로 만드는 리더
- [ ] File-Type Readers / PDF·DOCX·CSV 등 확장자별 전용 리더
- [ ] Manual Document Construction / Document 객체를 코드로 직접 만드는 방법

### External Sources

- [ ] Web and Sitemap Reader / 웹 페이지·사이트맵을 통째로 읽어오는 리더
- [ ] Notion, Slack, Google Drive / 협업 툴 데이터를 그대로 불러오는 커넥터
- [ ] Database Reader / SQL 쿼리 결과를 문서로 변환해 읽는 리더
- [ ] S3 / 클라우드 버킷의 파일을 그대로 인덱싱 대상으로 읽는 방법

### Parsing Quality

- [ ] LlamaParse / 표·레이아웃이 복잡한 PDF를 정확히 뽑아내는 방법
- [ ] Table And Image Extraction / 문서 속 표·이미지를 구조째로 뽑는 기능
- [ ] Metadata Injection Design / 검색에 쓸 메타데이터를 미리 설계해 넣는 방법

## 5. Node Parsing and Transformation

### Splitting Strategies

- [ ] SentenceSplitter / 문장 경계를 지켜 청크로 나누는 기본 분할기 `추천`
- [ ] TokenTextSplitter / 토큰 수 기준으로 균등하게 자르는 분할기
- [ ] SemanticSplitterNodeParser / 의미가 바뀌는 지점을 찾아 자르는 분할기
- [ ] Markdown, Code, JSON Parser / 문서 형식 구조를 살려서 자르는 전용 파서
- [ ] HierarchicalNodeParser / 큰 청크 밑에 작은 청크를 두는 계층 분할기

### Chunk Design

- [ ] chunk_size / chunk_overlap과 함께 크기·겹침을 정하는 트레이드오프값
- [ ] Metadata Extractor / 제목·요약·키워드·QA를 LLM으로 뽑아내는 추출기
- [ ] IngestionPipeline / 파싱부터 임베딩까지 변환 단계를 연결하는 파이프라인
- [ ] Docstore Deduplication / 같은 문서면 새로 안 만들고 upsert로 덮어쓰는 방식

## 6. Embeddings and Storage

### Embeddings

- [ ] Embedding Model Selection / 검색 품질을 좌우하는 임베딩 모델 선정
- [ ] Batch Size / 한 번에 임베딩할 텍스트 개수로 비용·속도 조절
- [ ] Dimension / 벡터 차원 수가 저장 용량·검색 속도를 좌우하는 값

### Vector Store `택 1`

- [ ] SimpleVectorStore / 별도 DB 없이 메모리·파일로 쓰는 방식 `추천`
- [ ] Chroma / 로컬 우선으로 쓰기 쉬운 오픈소스 벡터 DB
- [ ] Qdrant / 필터링 성능이 강한 러스트 기반 벡터 DB
- [ ] Pinecone / 직접 운영 없이 쓰는 완전관리형 벡터 DB
- [ ] pgvector / 기존 Postgres에 벡터 컬럼을 얹는 확장
- [ ] Elasticsearch and OpenSearch / 검색엔진에 벡터 인덱스를 얹어 쓰는 방식

### Storage Structure

- [ ] StorageContext / docstore·index_store·vector_store를 묶은 저장 설정
- [ ] Docstore, IndexStore, VectorStore / 원문·색인·벡터를 나눠 맡는 저장소 구성
- [ ] persist and load_index_from_storage / 인덱스를 저장하고 다시 불러오는 메서드 쌍
- [ ] Index Rebuild From Vector Store / 저장된 벡터만으로 인덱스를 재구성하는 방법

## 7. Index Types

- [ ] VectorStoreIndex / 임베딩 유사도로 검색하는 가장 기본 인덱스
- [ ] SummaryIndex / 순차 목록으로 저장해 전체를 훑는 인덱스
- [ ] DocumentSummaryIndex / 문서별 요약을 먼저 보고 골라 들어가는 인덱스
- [ ] KeywordTableIndex / 키워드와 노드를 매핑해 검색하는 인덱스
- [ ] PropertyGraphIndex / 엔티티와 관계를 그래프로 담는 인덱스
- [ ] ComposableGraph / 여러 인덱스를 계층으로 묶어 질의하는 구조
- [ ] insert, delete, refresh_ref_docs / 인덱스에 문서를 추가·삭제·갱신하는 메서드

---

# PART 3 · Retrieval and Response

## 8. Retrievers

- [ ] as_retriever / similarity_top_k로 반환 개수를 정해 리트리버로 변환
- [ ] VectorIndexRetriever / VectorStoreIndex 전용 유사도 검색기
- [ ] BM25Retriever / 임베딩 없이 단어 빈도로 찾는 키워드 검색기
- [ ] Hybrid / QueryFusionRetriever로 키워드·벡터 검색을 합치는 방식
- [ ] AutoMergingRetriever / 자식 노드가 몰리면 부모 노드로 합쳐 반환
- [ ] RecursiveRetriever / 참조를 따라 다른 인덱스까지 재귀로 탐색
- [ ] Metadata Filters / 메타데이터 조건을 걸어 검색 범위를 좁히는 필터
- [ ] Custom Retriever Implementation / 검색 로직을 직접 구현해 끼워 넣는 방법

## 9. Node Postprocessors

- [ ] SimilarityPostprocessor / cutoff 밑 유사도 노드를 걸러내는 후처리기
- [ ] Reranker / LLMRerank·SentenceTransformerRerank로 순위를 다시 매기는 방식
- [ ] Cohere / 별도 API로 상용 리랭크 모델을 불러쓰는 방식
- [ ] LongContextReorder / 중요한 노드를 앞뒤로 배치해 유실을 줄이는 재정렬
- [ ] MetadataReplacementPostProcessor / 요약 대신 원문 메타데이터로 되돌리는 후처리기
- [ ] SentenceWindow Retrieval Pattern / 문장 단위로 찾고 주변 문맥을 붙이는 패턴

## 10. Query Engines and Response Synthesis

### Query Engine

- [ ] as_query_engine / 인덱스를 질의 응답 엔진으로 바꾸는 메서드
- [ ] RetrieverQueryEngine / 리트리버와 합성기를 조합한 기본 질의 엔진
- [ ] SubQuestionQueryEngine / 질문을 하위 질문으로 쪼개 각각 답하는 엔진
- [ ] RouterQueryEngine / 질문에 맞는 엔진을 골라 보내는 라우터
- [ ] SQLTableQueryEngine / 자연어를 SQL로 바꿔 테이블에 질의하는 엔진
- [ ] PandasQueryEngine / 자연어를 판다스 코드로 바꿔 실행하는 엔진 `선택`

### Response Synthesis

- [ ] Response Mode / compact·refine·tree_summarize로 답을 합치는 방식
- [ ] Prompt Customization / text_qa·refine 템플릿을 직접 바꾸는 방법
- [ ] Streaming Response / 답을 토큰 단위로 흘려보내는 응답 방식
- [ ] Citation Query Engine / 답변 문장마다 근거 노드 출처를 붙이는 엔진
- [ ] Structured Output / output_cls로 응답을 정해진 스키마에 맞추는 방법

## 11. Advanced Retrieval

- [ ] Query Transformation / HyDE·Rewrite로 질의 자체를 바꿔 검색을 돕는 기법
- [ ] Query Decomposition / 복합 질문을 단순 질문들로 나누는 기법
- [ ] Multi-Document Agent Pattern / 문서마다 에이전트를 둬 비교·종합하는 패턴
- [ ] Small-to-Big Retrieval / 작은 단위로 찾고 큰 문맥으로 답을 만드는 방식
- [ ] Multi-Modal Index / 텍스트와 이미지를 함께 색인하는 방식 `선택`
- [ ] Text-to-Cypher / 자연어를 그래프 쿼리로 바꾸는 Graph RAG 기법

---

# PART 4 · Chat and Workflows

## 12. Chat Engines and Memory

- [ ] as_chat_engine / 인덱스를 대화형 챗 엔진으로 바꾸는 메서드
- [ ] Chat Mode / condense_question·context·best로 고르는 대화 처리 방식
- [ ] ChatMemoryBuffer / 최근 대화 기록을 순서대로 담아두는 버퍼
- [ ] Token Limit / 한도를 넘으면 오래된 대화를 요약해 압축
- [ ] Memory Persistence / 대화 기록을 세션 밖에 저장해 이어가는 방법

## 13. Agents and Tools

- [ ] FunctionAgent and ReActAgent / 함수 호출형과 추론-행동형 두 에이전트 유형
- [ ] QueryEngineTool / 질의 엔진을 에이전트가 부를 도구로 감싸는 래퍼
- [ ] FunctionTool / 파이썬 함수를 에이전트 도구로 등록하는 방법
- [ ] ToolSpec / LlamaHub에 등록된 외부 도구를 규격화한 래퍼
- [ ] AgentWorkflow / 여러 에이전트를 워크플로로 엮어 실행하는 구조
- [ ] Agent vs Query Engine Choice / 언제 Agent 대신 Query Engine으로 충분한가

## 14. Workflows

- [ ] Event-Driven Workflow Concept / 단계 대신 이벤트로 흐름을 잇는 설계
- [ ] @step / 함수를 워크플로 단계로 등록하는 데코레이터
- [ ] Context / 워크플로 단계 사이에서 상태를 주고받는 객체
- [ ] Streaming Event / 진행 상황을 이벤트로 실시간 전달하는 방식
- [ ] Human-in-the-Loop / 워크플로 중간에 사람 승인을 끼워 넣는 방식
- [ ] Checkpoint / 중단 지점부터 워크플로를 다시 잇는 기능

---

# PART 5 · Evaluation and Operations

## 15. Evaluation

### Response Evaluation

- [ ] Faithfulness / 답이 검색된 문맥에만 근거했는지 평가하는 지표
- [ ] Relevancy and Correctness / 질문과의 관련성·정답과의 일치도 평가
- [ ] Guideline Evaluator / 정해둔 기준 문장에 맞는지 LLM으로 채점

### Retrieval Evaluation

- [ ] Hit Rate and MRR / 정답을 찾았는지·몇 번째로 찾았는지 평가
- [ ] RetrieverEvaluator / Hit Rate·MRR 등을 계산해주는 평가 실행기
- [ ] Synthetic Question Generation / generate_question_context_pairs로 평가용 질문을 자동 생성
- [ ] BatchEvalRunner / 여러 평가자를 한꺼번에 돌리는 실행기

## 16. Observability and Deployment

- [ ] Callback and Instrumentation / 실행 과정에 훅을 걸어 관찰하는 두 체계
- [ ] Tracing Integration / Arize Phoenix·LangSmith로 호출 흐름을 추적하는 연동
- [ ] Token Counting / 호출마다 토큰 수를 세어 비용을 추적
- [ ] Caching / 동일 입력이면 재인덱싱 없이 캐시로 재사용
- [ ] Incremental Update Pipeline / 바뀐 문서만 골라 다시 색인하는 파이프라인
- [ ] create-llama / 명령 한 번으로 풀스택 앱 뼈대를 만드는 CLI `선택`
- [ ] API Server Exposure / 질의 엔진을 REST API로 띄워 외부 노출

---

# 이 로드맵 밖

- RAG 개념 · 벡터 DB 비교 `software/role-based/ai-engineer.md`
- 체인 · 에이전트 · 툴 중심 대안 `software/skill-based/AI/langchain.md`
- 에이전트 이론 `software/skill-based/AI/ai-agents.md`
- 프롬프트 작성법 `software/skill-based/AI/prompt-engineering.md`
- 검색 엔진 `software/skill-based/Data-DB/elasticsearch.md`
- Python `software/skill-based/Languages/python.md`
