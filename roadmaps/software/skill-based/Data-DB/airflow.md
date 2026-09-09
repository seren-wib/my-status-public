# Apache Airflow `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Airflow

## 1. What is Apache Airflow?

### Overview of Airflow / What is it?

- [ ] Workflow Orchestration Platform / 여러 작업의 실행 순서와 시점을 정하는 역할
- [ ] Workflows as Code / 파이프라인 정의를 Python 코드로 작성하는 방식
- [ ] DAG / 작업 순서를 순환 없이 그린 방향 그래프
- [ ] Scheduler + Executor Model / 언제 돌릴지 정하는 것과 실제로 돌리는 것을 분리한 구조

### Core Use Cases

- [ ] ETL / 추출→변환→적재 순서를 오케스트레이션하는 파이프라인
- [ ] ML Pipeline Orchestration / 학습·전처리 단계를 순서대로 실행하는 용도
- [ ] Batch Job Scheduling / 정해진 시각마다 배치 작업을 실행하는 용도
- [ ] Cross-system Dependency Management / 서로 다른 시스템 간 선후 관계를 조율

### Comparison with Other Tools

- [ ] Airflow vs Cron / 시간만 아는 cron과 상태·재시도까지 아는 차이
- [ ] Airflow vs Prefect and Dagster / 태스크 단위 스케줄링과 파이썬 네이티브 정의 차이
- [ ] Orchestration vs Data Processing Boundary / 순서만 정하고 처리는 위임하는 경계
- [ ] When to choose Airflow? / 태스크 수가 많고 재시도·의존성이 복잡할 때

## 2. Getting Started

### Installation `택 1`

- [ ] Docker Compose / 스케줄러·웹서버·DB를 컨테이너 여러 개로 함께 띄움 `추천`
- [ ] pip + Constraints File / 버전 충돌 막는 고정 의존성 파일로 설치
- [ ] Astro CLI / Astronomer가 만든 로컬 개발용 래퍼 도구
- [ ] Managed Service (MWAA, Cloud Composer) / 스케줄러·워커 운영을 클라우드에 맡기는 방식

### First Run

- [ ] airflow standalone / 스케줄러·웹서버·DB를 한 프로세스로 실행
- [ ] Web UI / Grid·Graph·Logs로 실행 상태를 확인하는 화면
- [ ] CLI / airflow dags·tasks·db로 상태를 조회하는 명령
- [ ] dags Folder / 이 폴더에 넣은 파일만 스캔해 DAG로 인식

## 3. Core Concepts

- [ ] DAG / 태스크와 의존관계를 하나로 묶은 정의 단위
- [ ] Task and Operator / 실행 단위와 그 단위를 만드는 템플릿
- [ ] Task Instance / 특정 DAG 실행에서 태스크가 도는 한 번
- [ ] DAG Run / 하나의 스케줄에 대해 DAG가 실행된 한 번
- [ ] Logical Date / 데이터 구간을 대표하는 시각, 실행 시각이 아님
- [ ] Data Interval / 이번 실행이 처리할 데이터의 시작~끝 구간
- [ ] Task State / queued·running·success 등 태스크가 거치는 상태
- [ ] Metadata Database / DAG·실행 이력·상태를 저장하는 DB

---

# PART 2 · Writing DAGs

## 4. DAG Authoring

### Definition Style `택 1`

- [ ] @dag Decorator / 함수 하나를 DAG 정의로 감싸는 방식 `추천`
- [ ] with DAG Context Manager / with 블록 안 태스크를 자동으로 묶는 방식
- [ ] DAG Constructor / DAG 객체를 직접 생성자로 만드는 방식

### DAG Parameters

- [ ] dag_id / DAG를 구분하는 고유 식별자 이름
- [ ] schedule / 얼마나 자주 DAG를 실행할지 정하는 값
- [ ] start_date / 시작 시각과 catchup 여부로 과거 실행을 채울지 결정
- [ ] default_args / 모든 태스크에 공통 적용할 기본 옵션 묶음
- [ ] max_active_runs / 동시에 도는 DAG 실행·태스크 수를 제한하는 값
- [ ] params / 실행할 때마다 값을 다르게 넣는 사용자 파라미터

## 5. Operators

### Core Operators

- [ ] PythonOperator / 파이썬 함수 하나를 태스크로 실행
- [ ] BashOperator / 셸 명령을 태스크로 실행
- [ ] EmptyOperator / 아무 일도 안 하는 자리표시용 태스크

### Data Operators

- [ ] SQL Operator / 쿼리 실행을 DB 커넥션에 떠넘기는 오퍼레이터
- [ ] Cloud Operator / S3·GCS·BigQuery 등 클라우드 작업을 떠넘김
- [ ] Container Operator / 컨테이너 실행을 Docker·K8s에 떠넘김

### Extensions

- [ ] Custom Operator / BaseOperator를 상속해 만드는 나만의 오퍼레이터
- [ ] Hook / 오퍼레이터가 쓰는 외부 시스템 접속 로직
- [ ] Provider Package Structure / 오퍼레이터·훅을 서비스별로 묶은 패키지

## 6. TaskFlow API

- [ ] @task Decorator / 파이썬 함수를 그대로 태스크로 바꾸는 문법
- [ ] Automatic XCom Return Value Passing / 함수 반환값을 자동으로 XCom에 저장
- [ ] Automatic Dependency Inference / 함수 호출 관계로 실행 순서를 자동 추론
- [ ] @task.virtualenv and @task.docker / 격리된 환경에서 태스크를 실행하는 데코레이터
- [ ] @task_group / 여러 태스크를 그래프에서 하나로 묶어 표시
- [ ] Mixing with Classic Operators / TaskFlow와 기존 오퍼레이터를 한 DAG에 혼용

## 7. Data Passing and Templating

- [ ] XCom / 태스크 간 작은 값을 주고받는 통로
- [ ] XCom Size Limit / 기본 저장 용량 제한과 이를 늘리는 커스텀 백엔드
- [ ] Jinja Templating / 실행 시점 값을 문자열에 채워 넣는 기능
- [ ] Template Variable / ds·ti·run_id 등 템플릿에서 쓰는 값
- [ ] template_fields / 오퍼레이터에서 템플릿 렌더링할 속성 지정
- [ ] Airflow Variable / 메타DB에 저장해 여러 DAG가 공유하는 값
- [ ] Intermediate Data in External Storage / 큰 데이터는 XCom 대신 외부에 저장

## 8. Dependencies and Control Flow

- [ ] Bitshift Operator / >>·<<로 태스크 실행 순서를 표시하는 문법
- [ ] chain / 여러 태스크를 순차 또는 교차로 연결하는 함수
- [ ] Task Group / 그래프 화면에서 태스크 묶음을 접어 표시
- [ ] Branching / 조건에 따라 다음 실행 경로를 고르는 방식
- [ ] Trigger Rule / 상류 태스크 상태별로 실행 여부를 정하는 규칙
- [ ] ShortCircuitOperator and LatestOnlyOperator / 조건 불충족·과거 실행이면 하류를 건너뜀
- [ ] Dynamic Task Mapping / 입력 개수만큼 태스크를 런타임에 늘림
- [ ] TriggerDagRunOperator / 다른 DAG의 실행을 시작시키는 오퍼레이터

---

# PART 3 · Scheduling and Architecture

## 9. Scheduling

- [ ] Cron Expression / 분·시·일 단위로 실행 시각을 지정하는 표기법
- [ ] Cron Preset / @daily·@hourly 등 자주 쓰는 표현 축약형
- [ ] timedelta Schedule / 고정 시각 대신 일정 간격으로 실행
- [ ] Custom Timetable / cron으로 못 그리는 특수 주기를 직접 정의
- [ ] Catchup and Backfill / 지난 스케줄을 놓쳤을 때 소급 실행하는 방법
- [ ] Execution Time vs Data Interval / 실행되는 시각과 처리 대상 구간의 차이
- [ ] Timezone Handling / 내부는 UTC로 저장하고 표시만 변환
- [ ] depends_on_past / 이전 실행 성공해야 이번 실행을 시작

## 10. Architecture

- [ ] Scheduler / DAG를 주기적으로 훑어 실행할 태스크를 큐에 넣음
- [ ] Webserver / Grid·Graph 등 UI를 제공하는 프로세스
- [ ] Worker / 큐에서 태스크를 꺼내 실제로 실행하는 프로세스
- [ ] Triggerer / 비동기로 대기하는 Deferrable 태스크를 관리
- [ ] Metadata DB / 상태 저장 DB, PostgreSQL을 권장
- [ ] DAG Parsing / dags 폴더 파일을 주기적으로 다시 읽는 과정
- [ ] DAG Serialization / 파싱한 DAG를 DB에 저장해 웹서버와 공유
- [ ] Scheduler HA / 스케줄러를 여러 대 띄워 장애를 대비

## 11. Executors `택 1`

- [ ] LocalExecutor / 한 머신 안에서 프로세스로 태스크를 실행 `추천`
- [ ] CeleryExecutor / 메시지 큐로 여러 워커에 태스크를 분산
- [ ] KubernetesExecutor / 태스크마다 파드를 새로 띄워 실행
- [ ] Executor Selection Criteria / 규모·격리 수준에 따라 executor를 선택

## 12. Sensors and Deferrable Tasks

- [ ] Sensor Concept / 조건이 될 때까지 기다리는 태스크
- [ ] Sensor Mode / 대기 중 슬롯을 계속 잡을지 반납할지
- [ ] Common Sensors / 파일·S3 객체·SQL 결과 등을 기다리는 센서
- [ ] ExternalTaskSensor / 다른 DAG의 특정 태스크 완료를 기다림
- [ ] Deferrable Operator / 대기 동안 워커 슬롯을 비워주는 방식
- [ ] Sensor Timeout / 무한 대기로 슬롯이 막히는 걸 방지

## 13. Connections and Datasets

### External Connections

- [ ] Connection / 외부 시스템 접속 정보를 저장하는 단위
- [ ] Secrets Backend / 접속 정보를 Vault 등 외부에서 가져옴
- [ ] Provider Installation and Version Management / 오퍼레이터 묶음을 패키지로 설치·관리

### Data-Aware Scheduling

- [ ] Dataset / 특정 데이터 산출물을 가리키는 스케줄링 단위
- [ ] Producer and Consumer DAG / Dataset을 갱신하는 쪽과 기다리는 쪽
- [ ] Combining Dataset Trigger with Schedule / Dataset 갱신과 시간 조건을 함께 검사

---

# PART 4 · Reliability and Resources

## 14. Reliability

- [ ] Retry / 실패 시 재시도 횟수·간격을 정하는 설정
- [ ] Timeout / 태스크·DAG 실행 전체에 거는 시간 제한
- [ ] SLA / 예상 완료 시각을 넘기면 감지하는 기준
- [ ] Callback / 성공·실패 시 실행할 후속 함수를 지정
- [ ] Alerting / 실패·SLA 미준수를 Slack·메일로 통보
- [ ] Idempotent Task Design / 재실행해도 같은 결과가 나오게 설계
- [ ] Clear and Rerun / 태스크 상태를 지워 다시 돌게 만드는 방법

## 15. Concurrency and Resources

- [ ] Pool / 동시 실행 수를 제한하는 슬롯 묶음
- [ ] Priority Weight / 같은 큐 안에서 실행 순서 우선도를 매김
- [ ] parallelism / 인스턴스 전체 동시 실행 태스크 수 상한
- [ ] Worker Concurrency / 워커 하나가 동시에 처리할 태스크 수
- [ ] Queue / 태스크를 특정 워커 그룹으로 보내는 경로

---

# PART 5 · Operations

## 16. Deployment

- [ ] DAG Deployment Methods / Git 동기화나 이미지 빌드로 DAG 파일을 배포
- [ ] Kubernetes / Helm Chart로 배포 구성을 관리하는 방식
- [ ] Environment Separation / dev·prod 등 환경별로 DAG를 분리 운영
- [ ] Dependency Management / 패키지 버전을 requirements나 이미지로 고정
- [ ] Major Version Upgrade Considerations / 메이저 버전 올릴 때 DAG 호환성 점검

## 17. Monitoring and Troubleshooting

- [ ] Remote Logging / 태스크 로그를 S3·GCS 등 외부에 저장
- [ ] Metrics / StatsD·OpenTelemetry로 지표를 외부에 전송
- [ ] Key Metrics / 스케줄러 지연·태스크 소요·대기 시간 등 지표
- [ ] Zombie / 워커가 죽었는데 상태만 running으로 남은 태스크
- [ ] DAG Import Error / 파싱 실패한 DAG 파일을 UI에서 알림
- [ ] Metadata DB Cleanup / 오래된 실행 이력을 지워 DB를 정리

## 18. Security and Best Practices

- [ ] RBAC / 역할별로 UI·API 권한을 나눠 부여
- [ ] Authentication / OAuth·LDAP 등 외부 인증 연동
- [ ] Avoiding Top-level Code / 파싱마다 실행되는 무거운 코드를 피함
- [ ] Keeping DAG Files Lightweight / DAG 파일엔 정의만 두고 로직은 분리
- [ ] Testing / DAG 임포트 검증과 태스크 단위 테스트
- [ ] CI/CD Pipeline / DAG 배포를 자동화하는 파이프라인

---

# 이 로드맵 밖

- 데이터 파이프라인 전반 `software/role-based/data-engineer.md`
- 분산 처리 엔진 `software/skill-based/Data-DB/spark.md`
- 변환 레이어 `software/skill-based/Data-DB/dbt.md`
- 이벤트 스트리밍 `software/skill-based/Data-DB/kafka.md`
- Python 기초 `software/skill-based/Languages/python.md`
- 실행 환경 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
