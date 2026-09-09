# Neo4j `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Graph Databases

## 1. Graph Database Basics

### Property Graph Model

- [ ] Node and Relationship / 노드와 그 사이 연결을 각각 데이터로 저장하는 단위
- [ ] Label and Relationship Type / 노드 분류명과 관계 종류명을 정하는 이름표
- [ ] Property / 노드·관계에 키-값으로 붙는 속성 자리
- [ ] Direction and Traversal / 방향을 정해 훑을 범위를 좁히는 것
- [ ] Index-free Adjacency / 이웃을 포인터로 직접 붙들어 조인 없이 찾는 구조

### Comparison with Other Models

- [ ] Graph vs Relational / 조인 비용이 관계 저장 방식에서 사라지는 이유
- [ ] Graph vs Document and Key-Value / 문서·키밸류와 관계 저장 방식을 대조
- [ ] Property Graph vs RDF / 트리플이 아닌 속성 그래프로 관계를 담는 차이
- [ ] When to choose a Graph DB? / 연결을 따라가는 질의가 많을 때 고르는 기준

### Core Use Cases

- [ ] Recommendation Engine / 이웃 노드를 따라가 추천 후보를 찾는 용도
- [ ] Fraud Detection / 계좌·거래 사이 숨은 연결 고리를 찾는 용도
- [ ] Knowledge Graph / 개체와 관계를 노드·엣지로 엮어 저장하는 용도
- [ ] Network and IT Topology / 장비 간 연결 구조를 노드·엣지로 담는 용도
- [ ] Identity and Access Graph / 사용자·권한·자원의 접근 관계를 담는 용도

## 2. Getting Started

### Installation `택 1`

- [ ] Neo4j Desktop / 로컬에서 DB와 브라우저를 함께 띄우는 GUI 앱 `추천`
- Docker / 컨테이너로 서버만 격리해 띄우는 방법 `software/skill-based/Infra-DevOps/docker.md` `위임`
- [ ] Server Tarball / OS 패키지나 압축 파일로 직접 설치
- [ ] AuraDB / Neo4j가 직접 운영하는 완전관리형 클라우드

### Tools and Sample Data

- [ ] Editions / 무료 커뮤니티와 유료 엔터프라이즈의 기능 차이
- [ ] Neo4j Browser / 질의 결과를 표 대신 노드-엣지 그림으로 보여주는 도구
- [ ] cypher-shell / 터미널에서 Cypher를 바로 실행하는 CLI
- [ ] Neo4j Bloom / 코드 없이 그래프를 마우스로 탐색하는 도구 `선택`
- [ ] Sample Datasets / Movies·Northwind 등 예제로 익히는 데이터셋

## 3. Cypher Basics

- [ ] Pattern Syntax / 노드-관계 모양을 괄호와 화살표로 그리는 문법
- [ ] MATCH and OPTIONAL MATCH / 패턴이 없으면 건너뛸지 null로 채울지 정함
- [ ] WHERE / 매칭된 패턴을 조건으로 걸러내는 절
- [ ] RETURN, DISTINCT, ORDER BY, LIMIT / 결과를 고르고 정렬해 개수를 제한하는 절
- [ ] CREATE and MERGE / 새로 만들지 있으면 재사용할지 가르는 차이
- [ ] SET and REMOVE / 속성·라벨을 붙이고 떼는 짝
- [ ] DELETE and DETACH DELETE / 연결된 관계까지 함께 지울지 정함
- [ ] WITH / 중간 결과를 다음 절로 넘겨 이어붙이는 절
- [ ] UNWIND / 리스트를 행 단위로 풀어 펼치는 절
- [ ] Aggregation / count·collect·sum으로 값을 모으는 집계
- [ ] Parameters / 문자열을 새로 만들지 않고 값만 바꿔 넣는 자리

## 4. Advanced Cypher

- [ ] Variable-Length Path / 몇 단계를 거칠지 정하지 않고 훑는 경로
- [ ] Shortest Path / shortestPath·allShortestPaths로 최단 경로를 구함
- [ ] Path Variables and Functions / 훑은 경로를 변수로 담아 길이·노드를 뽑는 기능
- [ ] List and Map Comprehension / 리스트·맵을 반복문 없이 한 식으로 걸러 만드는 문법
- [ ] CASE Expression / 조건에 따라 값을 갈라 넣는 식
- [ ] Subqueries / CALL {}로 질의 안에 별도 질의를 묶는 것
- [ ] EXISTS and COUNT Subquery / 패턴 존재 여부와 개수만 따로 확인
- [ ] UNION / 서로 다른 질의 결과를 하나로 합치는 절
- [ ] Temporal and Spatial Values / 날짜·시간·좌표를 전용 타입으로 다루는 값
- [ ] GQL Standard Direction / Cypher가 국제 표준 GQL로 수렴하는 방향

---

# PART 2 · Modeling and Performance

## 5. Data Modeling

- [ ] Node vs Relationship Decision / 개체로 둘지 연결로 둘지 가르는 기준
- [ ] Property vs Relationship Decision / 값을 속성으로 넣을지 별도 관계로 뺄지 정하는 기준
- [ ] Label Design / 한 노드에 라벨 여러 개를 겹쳐 붙이는 설계
- [ ] Relationship Granularity / 관계 타입을 얼마나 세분화할지 정하는 것
- [ ] Intermediate Node / 관계에 속성이 많을 때 노드로 승격하는 기법
- [ ] Time Modeling / 연결 리스트·시간 트리로 시계열을 잇는 방법
- [ ] Supernode Problem / 한 노드에 관계가 몰려 순회가 느려지는 문제
- [ ] Graph Refactoring / 운영 중인 그래프의 모델을 안전하게 바꾸는 작업

## 6. Indexes and Constraints

- [ ] Range Index / 크기 비교로 값을 찾는 기본 인덱스
- [ ] Text Index / 문자열 값 찾기에 맞춰진 인덱스
- [ ] Point Index / 좌표값 검색에 맞춰진 인덱스
- [ ] Full-text Index / 문장 안 단어로 찾는 전문 인덱스
- [ ] Vector Index / 임베딩 유사도로 가까운 노드를 찾는 인덱스
- [ ] Composite Index / 여러 속성을 묶어 한 번에 거는 인덱스
- [ ] Token Lookup Index / 라벨·관계타입 자체로 찾는 내장 인덱스
- [ ] Uniqueness Constraint / 같은 값이 두 번 들어오지 못하게 막는 제약
- [ ] Existence Constraint / 속성이 반드시 있어야 하게 강제하는 제약
- [ ] Node Key Constraint / 여러 속성을 묶어 고유 식별자로 강제하는 제약

## 7. Query Tuning

- [ ] EXPLAIN vs PROFILE / 실행만 미리 볼지 실제 돌려 통계까지 볼지 차이
- [ ] Plan Operators / 인덱스 탐색·전체 스캔·관계 확장 같은 실행 단위
- [ ] DB Hits and Rows / 저장소 접근 횟수와 처리 행 수로 보는 비용
- [ ] Cardinality Estimation / 옵티마이저가 각 단계 결과 행 수를 어림잡는 것
- [ ] Planner Hints / USING INDEX·USING SCAN으로 실행 경로를 지정
- [ ] Anchor Node Selection / 순회를 시작할 노드를 먼저 좁혀 잡는 것
- [ ] Eager Operator Problem / 다음 단계 전에 전체를 모아 메모리를 잡아먹는 문제
- [ ] Query Cache / 파라미터화된 질의 계획을 재사용하는 캐시
- [ ] Large Writes / CALL IN TRANSACTIONS로 대량 쓰기를 나눠 커밋

## 8. Data Import

- [ ] LOAD CSV / CSV 행을 한 줄씩 읽어 노드·관계로 만드는 절
- [ ] Bulk Import / neo4j-admin으로 빈 DB에 대량 적재
- [ ] APOC Import / apoc.load.json·jdbc로 외부 소스를 읽어옴
- [ ] Idempotent Import with MERGE / 같은 데이터를 다시 넣어도 중복 안 생기게 함
- [ ] Pre-creating Constraints / 제약을 미리 걸어 가져오기를 빠르게 함
- [ ] ETL from Relational Source / 관계형 테이블을 노드·관계로 변환해 옮기는 작업

---

# PART 3 · Internals and Extensions

## 9. Storage and Transactions

- [ ] Native Graph Storage / 노드·관계를 고정 크기 레코드로 저장
- [ ] Page Cache / 디스크 레코드를 메모리에 올려두는 캐시
- [ ] Transaction Log / 커밋한 변경을 순서대로 남겨 복구에 쓰는 로그
- [ ] ACID Guarantees / 트랜잭션이 전부 반영되거나 안 되는 보장
- [ ] Isolation Level / 커밋된 값만 읽게 하는 격리 수준
- [ ] Locking / 노드·관계 단위로 잠가 동시 쓰기를 막는 것
- [ ] Deadlock Handling / 서로 물린 잠금을 감지해 한쪽을 되돌리는 처리
- [ ] Memory Configuration / 힙과 페이지 캐시에 메모리를 나눠 배정

## 10. Graph Algorithms

- [ ] Graph Data Science Library / 그래프 알고리즘을 모아 둔 별도 라이브러리
- [ ] Graph Projection / 계산에 쓸 부분만 원본에서 메모리로 복사하는 것
- [ ] Pathfinding / 다익스트라·A*·옌 알고리즘으로 경로를 찾음
- [ ] Centrality / 페이지랭크 등으로 노드 중요도를 매기는 것
- [ ] Community Detection / 촘촘히 연결된 노드 무리를 찾는 것
- [ ] Similarity / 이웃이 비슷한 노드끼리 묶는 것
- [ ] Node Embeddings / 노드를 벡터로 바꿔 유사도 계산에 씀
- [ ] Link Prediction Pipeline / 없는 관계가 생길 확률을 예측하는 파이프라인 `선택`

## 11. Extensions and Integration

- [ ] APOC Library / Cypher에 없는 기능을 함수로 더해주는 확장
- [ ] User-Defined Procedures and Functions / 직접 코드를 짜 Cypher에서 부르는 확장 `선택`
- [ ] Drivers / 각 언어에서 Bolt로 접속하는 클라이언트
- [ ] Bolt Protocol / Neo4j 전용 이진 통신 프로토콜
- [ ] Session and Transaction Functions / 실패한 트랜잭션을 자동 재시도
- [ ] Query API over HTTP / HTTP로 Cypher를 보내고 JSON으로 받는 API
- [ ] Spring Data Neo4j / 스프링 객체를 노드·관계에 매핑해주는 라이브러리 `선택`
- [ ] Vector Search / 임베딩 검색을 RAG 컨텍스트로 연결 `별도`

---

# PART 4 · Operations

## 12. Clustering and Scaling

- [ ] Cluster Architecture / 쓰기 담당과 읽기 복제 서버로 나눈 구성
- [ ] Raft Consensus / 여러 서버가 합의로 리더를 뽑고 로그를 맞추는 방식
- [ ] Read Scaling with Secondaries / 읽기를 보조 서버로 분산해 부하를 나누는 것
- [ ] Routing Driver / neo4j:// 로 요청을 알맞은 서버로 보냄
- [ ] Causal Consistency / 북마크로 내가 쓴 걸 바로 읽게 보장
- [ ] Multi-Database / 한 서버 안에 여러 DB를 나눠 두는 것
- [ ] Sharding Limitations / 그래프를 여러 서버로 쪼개기 어려운 이유

## 13. Operations and Security

- [ ] Configuration / neo4j.conf 파일로 서버 설정을 정함
- [ ] Backup / neo4j-admin으로 온라인 백업이나 덤프를 뜸
- [ ] Restore and Consistency Check / 백업을 복원하고 저장소 손상 여부를 검사
- [ ] Version Upgrade / 이전 버전 저장 형식을 새 버전으로 옮김
- [ ] Monitoring Metrics / 트랜잭션 수·캐시 적중률로 상태를 봄
- [ ] Logs / 느린 질의와 오류를 나눠 남기는 로그
- [ ] Authentication and RBAC / 노드·속성 단위까지 권한을 쪼갬
- [ ] TLS / 클라이언트와 서버 사이 통신을 암호화
- [ ] AuraDB Operational Differences / 직접 운영과 달리 관리형이라 못 건드리는 부분

---

# 이 로드맵 밖

- SQL 문법 `software/skill-based/Languages/sql.md`
- 문서 지향 NoSQL `software/skill-based/Data-DB/mongodb.md`
- 검색 엔진 `software/skill-based/Data-DB/elasticsearch.md`
- 알고리즘 기초 · 그래프 탐색 `software/skill-based/CS-Theory/datastructures-and-algorithms.md`
- RAG · 임베딩 `software/role-based/ai-engineer.md`
- 백엔드 전반 `software/role-based/backend.md`
