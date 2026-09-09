# LangChain `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to LangChain

## 1. What is LangChain?

### Overview of LangChain

- [ ] LLM Application Framework / 모델 호출을 코드로 감싸는 프레임워크 계열
- [ ] Composable Component Philosophy / 부품을 조합해 파이프라인을 짜는 설계 철학
- [ ] Provider Abstraction / 여러 모델 제공자를 같은 인터페이스로 교체
- [ ] LangChain vs Direct SDK Calls / 프레임워크 없이 직접 호출하는 것과의 차이

### Package Structure

- [ ] langchain-core / Runnable·프롬프트 등 핵심 추상화만 담은 패키지
- [ ] langchain / 체인·에이전트 조립 로직을 담은 메인 패키지
- [ ] Provider Packages / 제공자별로 따로 까는 openai·anthropic 패키지
- [ ] langchain-community / 커뮤니티가 유지하는 서드파티 통합 모음
- [ ] langgraph / 그래프 구조로 에이전트 흐름을 짜는 확장 라이브러리
- [ ] langsmith / 실행을 추적·평가하는 관측 플랫폼

### When to Use

- [ ] Multi-Step Pipeline / 여러 단계를 이어 붙여야 하는 상황
- [ ] Tool-Calling Agent / 모델이 도구를 스스로 골라 쓰는 상황
- [ ] Over-Engineering Boundary / 단순 한 번 호출은 SDK 직접 사용이 나은 경계

## 2. Getting Started

### Installation and Configuration

- [ ] pip Installation / 필요한 provider만
- [ ] API Key / 환경변수에 담아 코드에 노출 안 시키는 방식
- [ ] init_chat_model / 문자열 하나로 제공자·모델을 지정해 생성하는 함수
- [ ] First Invocation / invoke로 모델을 한 번 호출해보는 단계

### Python vs JavaScript `택 1`

- Python / 생태계가 가장 넓어 예제·통합이 앞서는 언어 `software/skill-based/Languages/python.md` `추천` `위임`
- [ ] LangChain.js / Node 환경에서 쓰는 자바스크립트 포팅판

## 3. Models and Messages

### Chat Model Interface

- [ ] invoke, batch, stream / 단건·배치·실시간 세 가지 호출 방식
- [ ] Async Variants / ainvoke·astream으로 같은 호출을 비동기로 돌리는 방법
- [ ] Invocation Parameters / temperature·max_tokens로 생성을 조절하는 인자
- [ ] Rate Limit and Retry / 호출 실패·과다 요청에 대응하는 설정

### Message Types

- [ ] SystemMessage / 모델의 역할·규칙을 지정하는 메시지
- [ ] HumanMessage / 사용자가 보낸 입력을 담는 메시지
- [ ] AIMessage / 모델이 생성한 응답을 담는 메시지
- [ ] ToolMessage / 도구 실행 결과를 모델에 돌려주는 메시지
- [ ] Message Content Blocks / 텍스트·이미지를 한 메시지에 섞는 구조

### Other Models

- [ ] Embedding Model Interface / 텍스트를 벡터로 바꾸는 모델의 공통 인터페이스
- [ ] Legacy LLM Interface / 문자열만 주고받는 구형 완성형 인터페이스

## 4. Prompts

- [ ] PromptTemplate / 변수를 채워 단일 문자열 프롬프트를 만드는 틀
- [ ] ChatPromptTemplate / 여러 역할의 메시지 목록을 템플릿으로 만드는 틀
- [ ] MessagesPlaceholder / 대화 기록을 템플릿 중간에 끼워 넣는 자리
- [ ] Few-shot Prompt Template / 예시 몇 개를 넣어 출력 형식을 유도하는 템플릿
- [ ] Example Selector / 상황에 맞는 few-shot 예시를 골라 넣는 로직
- [ ] Partial Variables / 일부 변수만 먼저 채워 템플릿을 재사용하는 방법
- [ ] LangChain Hub / 공개된 프롬프트를 가져와 쓰는 저장소 `선택`

---

# PART 2 · Building Chains

## 5. LCEL and Runnable

### Runnable Interface

- [ ] Pipe Operator / `|`로 컴포넌트를 이어 체인을 만드는 문법
- [ ] RunnableSequence / 여러 컴포넌트를 순서대로 실행하는 체인
- [ ] RunnableParallel / 같은 입력을 여러 갈래에 동시에 흘리는 체인
- [ ] RunnablePassthrough / 입력을 가공 없이 다음 단계로 넘기는 컴포넌트
- [ ] RunnableLambda / 임의의 파이썬 함수를 체인 부품으로 감싸는 방법

### Control Flow

- [ ] RunnableBranch / 조건에 따라 실행할 체인을 골라 분기하는 컴포넌트
- [ ] with_fallbacks / 첫 컴포넌트가 실패하면 대체 컴포넌트로 넘어가는 설정
- [ ] with_retry / 실패한 호출을 정해진 횟수만큼 재시도하는 설정
- [ ] bind / 호출 시마다 넘기던 인자를 미리 고정해두는 방법
- [ ] configurable_fields and configurable_alternatives / 실행 시점에 필드·컴포넌트를 바꿔 끼우는 설정

### Execution Options

- [ ] RunnableConfig / tags·metadata로 실행마다 부가정보를 붙이는 객체
- [ ] max_concurrency / 병렬 실행 개수를 제한하는 설정
- [ ] Streaming Propagation / astream_events로 하위 단계 이벤트까지 흘려보내는 방식

## 6. Structured Output

- [ ] with_structured_output / 스키마를 지정해 모델 출력을 객체로 강제하는 메서드 `추천`
- [ ] Pydantic Schema Definition / 필드 타입으로 출력 구조를 정의하는 방법
- [ ] JSON Mode / 모델이 유효한 JSON만 뱉도록 강제하는 옵션
- [ ] Output Parser / 문자열·JSON·Pydantic 객체로 응답을 변환하는 컴포넌트
- [ ] OutputFixingParser and RetryParser / 파싱 실패 시 모델에 재요청해 고치는 파서
- [ ] Parsing Failure Handling / 형식이 안 맞는 출력을 처리하는 방법

## 7. Tools

### Tool Definition

- [ ] @tool Decorator / 함수 하나를 도구로 등록하는 데코레이터
- [ ] StructuredTool / 여러 인자를 받는 도구를 클래스로 정의하는 방법
- [ ] Schema / 함수 시그니처와 docstring으로 인자 설명을 정의하는 법
- [ ] ToolException / 도구 실행 실패를 모델이 읽을 메시지로 돌려주는 예외

### Tool Calling

- [ ] bind_tools / 모델이 호출할 수 있는 도구 목록을 등록하는 메서드
- [ ] tool_calls Parsing / 응답에서 어떤 도구를 어떤 인자로 불렀는지 뽑아내는 과정
- [ ] ToolNode / 도구 호출을 받아 실제로 실행해 결과를 돌려주는 노드
- [ ] Parallel Tool Calls / 한 응답에서 여러 도구를 동시에 호출하는 방식

### Tool Integrations

- [ ] Search Tools / Tavily 같은 외부 검색 API를 도구로 붙이는 통합
- [ ] Python REPL / Shell `선택`
- [ ] Toolkit / 관련 도구 여러 개를 한 세트로 묶어 제공하는 단위
- [ ] MCP Integration / 외부 MCP 서버의 도구를 그대로 가져와 쓰는 연동 `별도`

## 8. Memory and Chat History

- [ ] Message History Concept / 이전 대화를 다음 호출에 이어 붙이는 개념
- [ ] RunnableWithMessageHistory / 체인에 대화 기록 저장·주입을 자동으로 붙이는 래퍼
- [ ] Session / thread_id로 대화 세션을 구분해 관리하는 방법
- [ ] Trimming / trim_messages로 오래된 메시지를 잘라내 토큰을 아끼는 방법
- [ ] Summarization Memory / 지난 대화를 요약해 축약된 형태로 보관하는 방식
- [ ] Persistent Store / Redis·Postgres 같은 외부 저장소에 기록을 영속화하는 방법
- [ ] Legacy Memory Class Migration / 구형 Memory 클래스를 새 방식으로 옮기는 작업

---

# PART 3 · Agents

## 9. Agents

- [ ] Agent Concept / 추론과 행동을 반복해 목표에 도달하는 루프
- [ ] create_agent / 미리 만들어진 에이전트를 한 줄로 생성하는 함수
- [ ] System Prompt Design / 에이전트의 역할·제약을 지시문으로 설계하는 작업
- [ ] Tool Selection Failure Handling / 엉뚱한 도구를 고르거나 실패했을 때 대응하는 설계
- [ ] Recursion Limit / 에이전트가 무한히 반복하지 않도록 거는 상한
- [ ] Legacy AgentExecutor Migration / 구형 AgentExecutor를 새 방식으로 옮기는 작업

## 10. LangGraph

### Graph Construction

- [ ] StateGraph / 노드와 엣지로 실행 흐름을 그래프로 정의하는 클래스
- [ ] Node and Edge / 작업 단위와 그 사이 연결을 나타내는 그래프 구성요소
- [ ] Conditional Edge / 상태값에 따라 다음 노드를 갈라 보내는 엣지
- [ ] State Schema and Reducer / 그래프가 공유하는 상태 구조와 병합 규칙

### Execution and Persistence

- [ ] Checkpointer / thread 단위로 그래프 상태를 저장·복원하는 컴포넌트
- [ ] Interrupt / 실행을 멈추고 사람 확인을 받는 지점
- [ ] Time Travel / 이전 체크포인트로 돌아가 실행을 다시 시작하는 기능
- [ ] Subgraph / 그래프 안에 다른 그래프를 노드처럼 끼워 넣는 구조
- [ ] Streaming Modes / values·updates·messages 중 무엇을 흘릴지 고르는 옵션

## 11. Multi-Agent Patterns

- [ ] Supervisor / 하위 에이전트에게 작업을 나눠주고 취합하는 관리 에이전트
- [ ] Handoff and Swarm / 에이전트끼리 대화 주도권을 넘기는 협업 패턴
- [ ] Hierarchical Teams / 팀 단위로 에이전트를 계층적으로 묶는 구조
- [ ] Command-Based Routing / 노드 반환값으로 다음 목적지를 지정하는 방식

---

# PART 4 · Data Integration

## 12. Retrieval Components

### Document Preparation

- [ ] Document Loader / PDF·웹·CSV 등 원본 형식을 읽어 문서로 바꾸는 컴포넌트
- [ ] Document Object / page_content·metadata로 텍스트와 부가정보를 담는 객체
- [ ] Text Splitter / 문서를 재귀·토큰·마크다운 기준으로 잘게 나누는 컴포넌트

### Storage and Retrieval

- [ ] VectorStore Interface / 임베딩을 저장하고 검색하는 공통 인터페이스
- [ ] similarity_search / 코사인 유사도 검색에 MMR 다양성 옵션을 더하는 메서드
- [ ] Retriever Interface / 질의를 받아 관련 문서를 돌려주는 공통 인터페이스
- [ ] Metadata Filtering / 벡터 유사도 외에 메타데이터 조건으로 좁히는 검색

### Retrieval Improvement

- [ ] MultiQueryRetriever / 질문을 여러 버전으로 바꿔 검색을 넓히는 리트리버
- [ ] ContextualCompressionRetriever / 검색 결과에서 관련 부분만 압축해 남기는 리트리버
- [ ] EnsembleRetriever / 키워드 검색과 벡터 검색을 섞어 채점하는 방식
- [ ] ParentDocumentRetriever / 작은 조각으로 검색하고 원본 큰 문서를 돌려주는 리트리버
- [ ] SelfQueryRetriever / 자연어 질의에서 메타데이터 필터를 스스로 뽑아내는 리트리버

## 13. RAG Chains

- [ ] Retrieval Chain Assembly / 검색과 생성을 하나의 체인으로 잇는 작업
- [ ] Stuff, Refine, Map-Reduce / 문서를 묶어 요약하는 세 가지 방식
- [ ] Citation / 답변에 근거 문서 출처를 함께 표시하는 방법
- [ ] Conversational RAG / 이전 대화를 반영해 질문을 다시 쓰는 검색 방식
- [ ] Agentic RAG / 검색 자체를 에이전트가 스스로 판단해 호출하는 방식

---

# PART 5 · Operations

## 14. Streaming and Callbacks

- [ ] Token Streaming / 토큰이 생성되는 대로 즉시 흘려보내는 방식
- [ ] Callback Handler / 실행 단계마다 걸리는 이벤트를 받아 처리하는 객체
- [ ] Custom Callback Implementation / 로깅·모니터링용으로 콜백 핸들러를 직접 만드는 작업
- [ ] astream_events Event Types / 체인 내부 단계별로 구분되는 이벤트 종류
- [ ] Server Streaming / SSE로 서버에서 클라이언트로 실시간 응답을 흘리는 연동

## 15. LangSmith

- [ ] Tracing Setup / 실행 기록을 LangSmith로 보내도록 연결하는 설정
- [ ] Run and Trace / 실행 한 건과 그 안 단계들을 묶은 트리를 읽는 법
- [ ] Dataset Construction / 평가에 쓸 입출력 예시 모음을 만드는 작업
- [ ] Evaluator / 모델 스스로 다른 모델 출력을 채점하게 하는 평가 방식
- [ ] Prompt Versioning / 프롬프트 변경 이력을 버전으로 관리하는 기능
- [ ] Feedback Collection / 사용자·평가자의 점수를 실행 기록에 붙이는 기능

## 16. Production Concerns

- [ ] LangServe / 체인을 REST API 엔드포인트로 바로 띄우는 도구
- [ ] Caching / 같은 요청의 응답을 저장해 재호출을 건너뛰는 방법
- [ ] Token Usage And Cost / 호출마다 소모 토큰과 비용을 집계하는 관리
- [ ] Timeout and Fallback Model / 응답 지연 시 끊고 대체 모델로 넘기는 설정
- [ ] Prompt Injection Defense / 입력에 섞인 악의적 지시를 걸러내는 방어
- [ ] Secret Management / API 키 등 민감정보를 코드 밖에서 관리하는 방법
- [ ] Version Upgrade / 폐기 예정 API를 새 버전으로 옮기는 대응

---

# 이 로드맵 밖

- LLM 앱 전반 · 임베딩 · 벡터 DB `software/role-based/ai-engineer.md`
- 에이전트 이론 · MCP `software/skill-based/AI/ai-agents.md`
- 프롬프트 작성법 `software/skill-based/AI/prompt-engineering.md`
- 인덱싱·검색 중심 대안 `software/skill-based/AI/llamaindex.md`
- Python `software/skill-based/Languages/python.md`
- 제품화 `software/skill-based/AI/ai-product-builder.md`
