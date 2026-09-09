# Apache CouchDB `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to CouchDB

## 1. What is CouchDB?

### Overview of CouchDB / What is it?

- [ ] Document-Oriented NoSQL Database / 행 대신 문서 하나를 저장 단위로 삼는 구조
- [ ] JSON Document Store / 필드 구성을 JSON 그대로 디스크에 저장하는 방식
- [ ] HTTP and REST as the Native API / URL과 HTTP 메서드 자체가 API 규격인 구조
- [ ] Schema-free Data Model / 문서마다 필드 구성이 달라도 되는 구조

### Design Philosophy

- [ ] Eventual Consistency / 복제가 끝나야 노드 간 값이 같아지는 모델
- [ ] Crash-only Design and Append-only Storage / 파일에 계속 이어 써서 죽어도 복구되는 구조
- [ ] Replication as a First-class Feature / 노드끼리 문서를 주고받는 복제를 DB가 직접 담당
- [ ] Offline-First Applications / 끊긴 클라이언트가 로컬에 쓰고 나중에 합치는 모델

### CouchDB vs Other Databases

- [ ] CouchDB vs MongoDB / HTTP API와 리비전 방식이 쿼리 언어형과 갈리는 지점
- [ ] CouchDB vs Couchbase / 복제 중심 설계와 메모리 성능 중심 설계의 차이
- [ ] When to choose CouchDB? / 오프라인 동기화가 핵심일 때 고르는 기준

## 2. Getting Started

### Installation `택 1`

- [ ] Docker Image / 이미지 하나로 컨테이너에서 바로 띄우는 방법 `추천`
- [ ] Package Manager / OS 패키지로 직접 설치하는 방법
- [ ] Managed Service / IBM Cloudant처럼 호스팅형으로 운영을 맡기는 방식

### First Run

- [ ] Single Node Setup vs Cluster Setup / 단일 노드로 뗄지 클러스터로 뗄지 정하는 선택
- [ ] Fauxton Web UI / 내장된 웹 관리 콘솔
- [ ] Admin Party and Admin Setup / 인증 없이 열린 초기 상태와 관리자 계정 설정

---

# PART 2 · Documents and Data Model

## 3. Document Model

### Document Structure

- [ ] Document / _id와 _rev로 식별되는 저장 단위
- [ ] Revision Tree / 문서를 고칠 때마다 옛 리비전을 가지처럼 남기는 구조
- [ ] Revision Numbering / 세대 번호와 내용 해시로 만드는 리비전 값
- [ ] Tombstone / 지운 문서를 흔적으로 남겨두는 빈 리비전

### Data Modeling

- [ ] Denormalization and Embedding / 조인 대신 관련 데이터를 문서 안에 넣는 방식
- [ ] Document Type Field Pattern / 문서 안에 종류를 적어 구분하는 관행
- [ ] One Database per User Pattern / 사용자마다 별도 DB를 둬 격리하는 설계
- [ ] Choosing Meaningful _id / _id에 의미 있는 값을 넣어 조회를 돕는 설계
- [ ] Avoiding Large Documents / 문서 크기를 키워 성능을 깎지 않는 원칙

## 4. CRUD via HTTP API

### Database Level

- [ ] Database Operations / PUT·DELETE·GET /_all_dbs로 DB 자체를 다루는 요청

### Document Level

- [ ] Create / POST나 _id 지정 PUT으로 문서를 만드는 방법
- [ ] Read / GET에 rev를 넘겨 특정 리비전을 읽는 방법
- [ ] Update / 보낸 rev가 최신인지 대조해 막는 충돌 검사
- [ ] Delete / 최신 rev를 실어 보내야 지워지는 요청
- [ ] Conditional Requests / ETag와 If-Match로 버전을 대조하는 요청

### Reading/Querying

- [ ] _all_docs / include_docs를 켜면 본문까지 같이 오는 목록 조회
- [ ] Key Range Query / startkey와 endkey로 구간을 지정하는 조회
- [ ] Pagination / limit·skip·bookmark로 나눠 받는 방법

## 5. Bulk Operations and Attachments

- [ ] Bulk Insert / _bulk_docs로 여러 문서를 한 요청에 넣는 방법
- [ ] Bulk Fetch / _bulk_get으로 여러 문서를 한 요청에 읽는 방법
- [ ] all_or_nothing vs Per-document Errors / 벌크 실패를 통째로 볼지 건별로 볼지
- [ ] Attachments / Base64로 문서에 넣거나 별도로 저장하는 방식
- [ ] Attachment Stubs / 본문 조회 때 첨부 내용은 빼고 메타만 주는 것
- [ ] Attachments vs External Object Storage / 파일을 문서에 둘지 밖에 둘지 정하는 기준

---

# PART 3 · Queries and Indexes

## 6. MapReduce Views

### Design Document

- [ ] Design Document / _design으로 시작하는 id에 뷰·함수를 담는 문서
- [ ] View Definition / map과 reduce 함수로 뷰를 정의하는 방법

### Map Function

- [ ] emit(key, value) / map 함수 안에서 뷰에 넣을 키·값을 내보내는 호출
- [ ] View Collation Order / 키를 정렬해 저장하는 고유 순서 규칙
- [ ] Complex Keys / 배열을 키로 써서 복합 조건을 만드는 방법
- [ ] View Query Params / key·startkey·descending·group_level로 거르는 옵션

### Reduce Function

- [ ] Built-in Reducers / _count·_sum·_stats처럼 미리 마련된 집계 함수
- [ ] Rereduce / 리듀스 결과를 다시 리듀스해 트리를 좁히는 단계
- [ ] Custom Reduce Pitfalls / 출력이 커지면 느려지는 리듀스 함정

### Index Behavior

- [ ] Incremental View Build / 바뀐 문서만 다시 계산해 뷰를 갱신하는 방식
- [ ] Stale Views / update=lazy로 갱신을 미루고 옛 결과부터 주는 옵션
- [ ] View Compaction / 쌓인 옛 인덱스 파일을 정리해 줄이는 작업

## 7. Mango Query

- [ ] _find Endpoint / 조건으로 문서를 검색하는 HTTP 진입점
- [ ] Selector Syntax / $eq·$gt·$in·$regex로 조건을 쓰는 문법
- [ ] Logical Operators / $and·$or·$not으로 조건을 묶는 연산자
- [ ] Sorting and Fields Projection / 정렬 기준과 돌려받을 필드를 고르는 옵션
- [ ] Index Creation / _index로 검색용 색인을 미리 만드는 방법
- [ ] Partial Index / 조건에 맞는 문서만 골라 색인하는 방법
- [ ] Explain Plan / _explain으로 색인 사용 여부를 확인하는 방법
- [ ] Mango vs MapReduce Tradeoffs / 즉석 조건 검색과 미리 계산된 뷰의 차이

## 8. Design Document Functions `선택`

- [ ] Full-Text Search / Nouveau나 Lucene 엔진으로 텍스트를 검색하는 기능
- [ ] Update Handlers / 서버에서 문서를 변형해 저장하는 함수
- [ ] Show and List Functions / 문서·뷰 결과를 다른 형식으로 바꿔 주는 함수
- [ ] Validate Document Update Function / 저장 전에 문서를 검사해 막는 함수
- [ ] Partitioned Databases / 파티션 키로 문서를 묶어 조회 범위를 좁히는 기능

---

# PART 4 · Replication and Conflicts

## 9. Replication

- [ ] Replication Protocol Overview / 두 DB가 변경분을 비교해 주고받는 절차
- [ ] One-shot vs Continuous Replication / 한 번만 맞출지 계속 따라갈지 정하는 방식
- [ ] Push, Pull, Bidirectional / 복제가 흐르는 방향을 정하는 설정
- [ ] _replicate vs _replicator Database / 요청으로 돌릴지 문서로 등록해 돌릴지
- [ ] Filtered Replication / 필터 함수나 doc_ids로 복제 범위를 줄이는 방법
- [ ] Checkpointing and Resume / 끊긴 지점을 기억해 이어서 복제하는 기능
- [ ] Replication Monitoring / _scheduler로 진행 중인 복제를 확인하는 방법

## 10. Conflict Handling

- [ ] Conflict Detection / _conflicts 필드로 충돌 리비전을 확인하는 방법
- [ ] Winning Revision Selection / 결정적 규칙으로 대표 리비전을 고르는 방식
- [ ] Application-level Conflict Resolution / 진 리비전을 앱이 읽어 직접 병합하는 처리
- [ ] Conflict-avoiding Data Design / 문서를 잘게 쪼개 충돌 확률을 줄이는 설계

## 11. Change Feed and Offline-First

- [ ] Changes Feed / _changes로 문서 변경을 순서대로 받는 기능
- [ ] Feed Modes / normal·longpoll·continuous·eventsource로 받는 방식
- [ ] Sequence Number and since / 어디까지 받았는지 표시해 이어 받는 값
- [ ] PouchDB / 브라우저 안에서 CouchDB와 동기화하는 자바스크립트 라이브러리

---

# PART 5 · Operations

## 12. Clustering

- [ ] Cluster Setup / _cluster_setup API로 노드를 묶는 절차
- [ ] Sharding / q 값으로 DB를 몇 조각으로 나눌지 정하는 것
- [ ] Replicas / n 값으로 조각마다 복사본 수를 정하는 것
- [ ] Quorum / r과 w 값으로 읽기·쓰기 응답 기준 노드 수를 정하는 것
- [ ] Shard Placement and Rebalancing / 조각을 노드에 배치하고 옮기는 작업
- [ ] Node Membership / _membership으로 클러스터 소속 노드를 확인하는 방법

## 13. Configuration and Operations

- [ ] Configuration / local.ini 파일이나 _node/_config API로 바꾸는 설정
- [ ] Compaction / DB 파일과 뷰 인덱스 각각에 거는 정리 작업
- [ ] Storage Growth and Disk Planning / 리비전이 쌓여 느는 용량을 가늠하는 계획
- [ ] Backup Strategies / 파일 복사나 복제로 백업을 뜨는 방법
- [ ] Monitoring Endpoints / _stats와 _active_tasks로 상태를 확인하는 API
- [ ] Version Upgrade / 리비전 형식 호환을 살펴 올리는 절차

## 14. Security

- [ ] Admin vs Member Roles / DB 권한을 관리자와 구성원으로 나누는 등급
- [ ] Database Security Object / _security 문서에 담는 DB별 권한 목록
- [ ] Users Database / _users에 계정을 문서로 저장하는 특수 DB
- [ ] Authentication / Basic·Cookie·JWT·Proxy로 신원을 확인하는 방식
- [ ] TLS / 앞단 리버스 프록시에서 암호화를 끝내는 방식
- [ ] CORS Configuration / 다른 출처의 브라우저 요청을 허용하는 설정

---

# 이 로드맵 밖

- MongoDB `software/skill-based/Data-DB/mongodb.md`
- SQL 문법 `software/skill-based/Languages/sql.md`
- 백엔드 전반 · REST API 설계 `software/role-based/backend.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
- 분산 시스템 · 일관성 모델 `software/skill-based/CS-Theory/system-design.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`
