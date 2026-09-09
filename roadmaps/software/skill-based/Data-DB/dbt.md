# dbt `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to dbt

## 1. What is dbt?

### Overview of dbt / What is it?

- [ ] SQL-based Transformation Tool / 적재 후 SQL만으로 변형을 수행하는 도구
- [ ] The T in ELT / 적재까지 끝난 데이터를 SQL로 변형하는 단계
- [ ] Analytics Engineering / SQL로 데이터를 만드는 소프트웨어 엔지니어링 방식
- [ ] One SELECT Statement Equals One Model / SQL 파일 하나가 모델 하나가 되는 규칙

### Core Use Cases

- [ ] Data Warehouse Modeling / 원천 테이블을 분석용 구조로 다시 짜는 일
- [ ] Reusable Transformation Logic / 변형 로직을 모델로 나눠 재사용하는 방식
- [ ] Data Quality Test / 결과 테이블의 값 조건을 자동으로 검사
- [ ] Lineage / 모델 간 참조로 계보와 문서를 자동 생성

### Positioning

- [ ] dbt vs Airflow / 실행 순서가 아니라 모델 참조로 의존성을 정함
- [ ] dbt vs Stored Procedure / SQL 로직을 DB 밖 파일로 버전 관리하는 차이

### Execution Method `택 1`

- [ ] dbt Core / 명령줄로 로컬에서 돌리는 무료 실행 방식 `추천`
- [ ] dbt Cloud / 웹 IDE와 스케줄러를 얹은 관리형 실행 방식

## 2. Getting Started

### Prerequisites

- [ ] SQL / CTE·윈도우 함수를 다루는 사전 지식
- [ ] Data Warehouse Concepts / 팩트·차원 테이블 같은 웨어하우스 기본 개념
- [ ] Git Basics / 모델 파일을 버전 관리하는 데 필요한 최소 지식

### Installation and Initialization

- [ ] dbt Core Installation / pip·uv로 dbt Core를 설치하는 두 방법
- [ ] Adapter Installation / 웨어하우스별 어댑터를 따로 설치하는 방식
- [ ] dbt init / 프로젝트 뼈대를 자동으로 생성하는 명령
- [ ] profiles.yml / 접속 정보를 프로젝트 밖 파일에 따로 두는 설정
- [ ] dbt debug / 연결과 설정이 맞는지 점검하는 명령
- [ ] First dbt run / 설치가 끝났는지 확인하는 첫 실행

## 3. Project Structure

- [ ] dbt_project.yml / 프로젝트 전역 설정을 모아두는 파일
- [ ] models Directory / 모델 SQL 파일을 담는 표준 폴더
- [ ] Layer Structure / staging·intermediate·marts로 나누는 단계 구조
- [ ] Naming Convention / 접두사로 모델 종류를 구분하는 규칙
- [ ] target Directory / 컴파일된 SQL과 실행 결과가 쌓이는 폴더
- [ ] .yml File Placement Rules / 소스·테스트 정의 yml을 두는 위치 규칙

---

# PART 2 · Modeling

## 4. Models

- [ ] Model = One File = One SELECT / SQL 파일 하나가 곧 모델 하나라는 원칙
- [ ] ref() / 다른 모델을 참조해 실행 순서를 자동 결정
- [ ] source() / 원천 테이블을 모델 계보 안으로 끌어들이는 함수
- [ ] Automatic DAG Generation / ref로 맺어진 참조에서 순서를 뽑아내는 기능
- [ ] Model Config / 머티리얼라이제이션 등을 모델별로 지정하는 설정
- [ ] Schema and Database / 모델이 저장될 위치를 지정하는 설정
- [ ] Model Contract / 출력 컬럼의 이름과 타입을 미리 고정하는 계약
- [ ] Model Versioning / 모델을 버전별로 나눠 병행 운영하는 기능 `선택`

## 5. Materializations

### Types

- [ ] view / 매번 쿼리로 재계산하는 가벼운 머티리얼라이제이션
- [ ] table / 쿼리 시점에 결과를 통째로 저장하는 방식
- [ ] incremental / 새 데이터만 골라 기존 테이블에 추가하는 방식
- [ ] ephemeral / 테이블로 남기지 않고 CTE로 접혀 들어가는 방식
- [ ] materialized_view / 웨어하우스가 백그라운드로 갱신을 유지하는 뷰
- [ ] Selection Criteria / 비용·신선도·크기로 머티리얼라이제이션을 고르는 기준

### Incremental Model

- [ ] is_incremental() Conditional Block / 증분 실행일 때만 SQL을 다르게 타는 분기
- [ ] unique_key / 기존 행과 새 행을 매칭하는 기준 컬럼
- [ ] Incremental Strategy / append·merge 등 증분 반영 방식을 고르는 옵션
- [ ] on_schema_change / 원천 컬럼이 바뀌었을 때 처리 방식을 정하는 옵션
- [ ] Full Refresh / 증분 테이블을 통째로 다시 쌓는 재실행
- [ ] Late-arriving Data Handling / 늦게 도착한 데이터를 증분 로직에 반영하는 처리

## 6. Sources, Seeds, Snapshots

### Sources

- [ ] sources.yml Definition / 원천 테이블 목록과 이름을 선언하는 파일
- [ ] Source Freshness / 원천 데이터가 얼마나 최신인지 재는 기준 컬럼
- [ ] dbt source freshness / 선언된 원천의 최신성을 검사하는 명령

### Seeds

- [ ] CSV Seed / 고정 CSV를 테이블로 올리는 명령
- [ ] Appropriate Scope for Seeds / 코드 값처럼 작고 안 바뀌는 데이터로 한정하는 범위

### Snapshots

- [ ] SCD Type 2 Concept / 값이 바뀐 이력을 행으로 남기는 방식
- [ ] Snapshot Strategy / 타임스탬프나 값 비교로 변경을 감지하는 방식
- [ ] dbt snapshot / 정의된 전략대로 이력 테이블을 갱신하는 명령
- [ ] invalidate_hard_deletes / 원천에서 사라진 행을 이력상 종료 처리하는 옵션

## 7. Jinja and Macros

- [ ] Jinja Basics / 변수·조건·반복으로 SQL을 대신 생성하는 문법
- [ ] Inspecting Compiled Output / Jinja가 풀린 실제 SQL을 확인하는 방법
- [ ] Macro Definition and Invocation / 반복되는 SQL 조각을 함수처럼 묶어 재사용
- [ ] var() / 실행 시점에 값을 프로젝트 밖에서 주입하는 함수
- [ ] env_var() / 환경변수 값을 SQL 안으로 끌어오는 함수
- [ ] Hooks / 실행 전후에 추가 SQL을 끼워 넣는 지점
- [ ] Custom Schema and Alias Macro / 스키마·별칭 생성 규칙을 매크로로 덮어쓰기

---

# PART 3 · Quality and Collaboration

## 8. Tests

- [ ] Generic Test / unique·not_null 같은 재사용 가능한 검사 규칙
- [ ] Singular Test / 특정 조건을 직접 SQL로 짜는 1회성 검사
- [ ] Custom Generic Test / 직접 만들어 여러 모델에 재사용하는 검사
- [ ] Test Severity / 실패 시 빌드를 막을지 경고만 할지 정하는 수준
- [ ] Test Config / 검사 범위와 실패 행 저장 여부를 지정하는 설정
- [ ] Unit Test / 가짜 입력값으로 모델 로직만 따로 검증
- [ ] dbt-expectations / 통계·분포 기반 검사를 더해주는 확장 패키지

## 9. Documentation and Lineage

- [ ] Model and Column Description / 모델·컬럼에 설명을 붙이는 문서화
- [ ] docs Block / doc()로 불러 쓰는 재사용 설명 블록
- [ ] dbt docs generate / 문서와 계보 그래프를 만들고 웹으로 여는 명령
- [ ] Lineage Graph / ref로 이어진 모델 관계를 그림으로 보여주는 화면
- [ ] Exposure / 대시보드 등 모델을 소비하는 곳을 선언하는 개념
- [ ] Semantic Layer and Metrics / 지표 정의를 한 곳에 모아 재사용하는 계층 `선택`

## 10. Packages

- [ ] packages.yml / dbt deps로 설치할 외부 패키지 목록 선언
- [ ] dbt_utils / 날짜·서로게이트 키 등 범용 매크로 모음 패키지
- [ ] codegen / 소스·모델 yml 뼈대를 자동 생성하는 패키지
- [ ] audit_helper / 리팩터링 전후 결과를 비교해주는 패키지
- [ ] Private Package / 사내 저장소를 Git 경로로 불러오는 패키지 등록

---

# PART 4 · Running and Operations

## 11. Commands and Node Selection

- [ ] dbt run, test, compile / 모델 실행·검사·SQL 컴파일을 나누는 기본 명령
- [ ] Why dbt build Is the Default / run·test·seed·snapshot을 한 번에 묶어 도는 이유
- [ ] Node Selection / 특정 모델만 골라 돌리거나 빼는 옵션
- [ ] Graph Operator / 상류·하류 모델까지 같이 골라내는 기호
- [ ] Selector Method / 태그·경로·상태로 모델을 고르는 기준
- [ ] defer / 없는 모델은 이전 실행 결과를 빌려 쓰는 옵션
- [ ] Slim CI / 이전 상태와 비교해 바뀐 모델만 돌리는 방식
- [ ] --full-refresh / 증분을 통째로 다시 쌓거나 즉시 멈추는 옵션

## 12. Environments and Deployment

- [ ] Target / dev·prod 등 연결 대상을 profiles에서 전환
- [ ] Custom Schema Strategy / 환경별로 스키마 이름을 다르게 붙이는 전략
- [ ] Orchestration / dbt 실행을 외부 스케줄러가 언제 돌릴지 트리거
- [ ] CI Pipeline / PR마다 바뀐 모델만 자동으로 빌드·검사
- [ ] Artifacts / 실행마다 남는 그래프·결과 메타데이터 파일
- [ ] Logging / 실행 중 로그가 쌓이는 파일

## 13. Performance and Cost

- [ ] Warehouse-specific Optimization Points / 대상 창고별로 dbt가 건드리는 최적화 지점
- [ ] Deciding When to Go Incremental / 테이블이 커질 때 증분으로 바꿀지 판단하는 기준
- [ ] Clustering and Partitioning Config / 모델 config로 정렬·분할 방식을 지정
- [ ] threads / 모델을 동시에 몇 개 돌릴지 정하는 병렬도
- [ ] Unused Model Cleanup / 더 안 쓰는 모델을 찾아 정리하는 작업
- [ ] Cost Monitoring / 실행이 창고 비용에 얼마나 드는지 추적

---

# 이 로드맵 밖

- 데이터 파이프라인 전반 `software/role-based/data-engineer.md`
- SQL 기초 `software/skill-based/Languages/sql.md`
- 오케스트레이션 `software/skill-based/Data-DB/airflow.md`
- 대상 웨어하우스 `software/skill-based/Data-DB/snowflake.md`, `bigquery.md`, `databricks.md`
- 분석 지표 활용 `software/role-based/bi-analyst.md`
