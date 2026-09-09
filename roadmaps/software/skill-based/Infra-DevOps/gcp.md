# Google Cloud Platform `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Cloud and GCP Basics

## 1. Introduction to GCP

### Cloud Basics

- [ ] Cloud Computing / IaaS·PaaS·SaaS로 나뉜 위탁 정도 단계
- [ ] Shared Responsibility Model / 보안 책임을 인프라와 사용자로 나눈 경계
- [ ] Google Cloud Architecture Framework / 안정성·보안 등 설계 원칙 5축

### Infrastructure Structure

- [ ] Global Infrastructure / 리전·존·엣지로 나뉜 물리 배치 단위
- [ ] Global vs Regional vs Zonal Resources / 리소스가 걸치는 지리 범위 구분
- [ ] Service Mapping to AWS and Azure / 타 클라우드 대응 서비스 대조표

### Access Methods `택 1`

- [ ] Cloud Console / 브라우저로 리소스를 조작하는 콘솔
- [ ] gcloud CLI / 터미널에서 GCP를 조작하는 명령줄 도구 `추천`
- [ ] Cloud Shell / 브라우저에 딸린 임시 리눅스 셸
- [ ] Client Libraries / REST API를 언어별로 감싼 SDK

### First Exercise

- [ ] Free Tier / 무료 한도와 신규 가입 크레딧
- [ ] gcloud init / 로컬 gcloud에 프로젝트를 연결하는 초기화
- [ ] Enabling APIs / 서비스별로 따로 켜야 쓰이는 구조

## 2. Resource Hierarchy and Billing

- [ ] Resource Hierarchy / 조직-폴더-프로젝트로 뻗는 상속 트리
- [ ] Project ID vs Project Number / 사람용 문자열과 시스템용 숫자 식별자
- [ ] Billing Account / 여러 프로젝트가 매달리는 결제 단위
- [ ] Labels / 리소스에 붙여 비용을 나누는 키-값 태그
- [ ] Quotas / 프로젝트별 리소스 사용 상한
- [ ] Organization Policy / 조직 전체에 거는 제약 규칙

---

# PART 2 · IAM and Networking

## 3. IAM

### Components

- [ ] Principal / 권한을 받는 사용자·그룹·도메인 대상
- [ ] Role / 기본·사전정의·커스텀 세 등급의 권한 묶음
- [ ] Allow Policy / 프로젝트 계층을 타고 내려가는 허용 규칙
- [ ] Deny Policy / Allow보다 먼저 걸리는 명시적 거부 규칙

### Service Account

- [ ] Service Account / 워크로드가 갖는 비인간용 신원
- [ ] Attached Service Account / 인스턴스에 붙어 자동 인증하는 기본 신원
- [ ] Workload Identity Federation / 키 없이 외부 신원을 교환하는 인증
- [ ] Service Account Impersonation / 키 없이 잠깐 남의 신원을 빌리는 방법

### Operating Principles

- [ ] Least Privilege Principle / 과다 권한을 찾아 좁히는 분석 도구
- [ ] Audit Log / 관리 조작과 데이터 접근을 남기는 감사 기록

## 4. VPC Networking

### Basic Structure

- [ ] VPC / 리전을 넘어 서브넷이 이어지는 전역 네트워크
- [ ] Subnet / 리전 단위로 쪼갠 IP 대역
- [ ] Firewall Rule / 태그·서비스 계정 기준으로 거는 방화벽 규칙
- [ ] Route / 고정 또는 동적으로 정해지는 경로

### Connectivity

- [ ] Shared VPC / 여러 프로젝트가 한 네트워크를 나눠 쓰는 구조
- [ ] VPC Network Peering / 서로 다른 VPC를 사설 IP로 잇는 연결
- [ ] Cloud NAT and Cloud Router / 사설 인스턴스가 외부로 나가는 길을 내는 두 서비스
- [ ] Cloud VPN and Cloud Interconnect / 온프레미스와 잇는 두 전용 연결 방식 `선택`

### Private Access

- [ ] Private Google Access / 외부 IP 없이 구글 API에 닿는 접근
- [ ] Private Service Connect / 내부 IP로 타사 서비스를 붙이는 연결
- [ ] VPC Service Controls / 데이터 반출을 막는 서비스 경계

## 5. Load Balancing and Edge

- [ ] Cloud Load Balancing / 애니캐스트 IP 하나로 전 세계를 받는 분산
- [ ] Backend Service / LB가 트래픽을 보낼 대상 묶음
- [ ] Cloud CDN / LB 앞단에 붙는 엣지 캐시
- [ ] Cloud DNS / 공개·내부 존을 관리하는 이름 해석
- [ ] Cloud Armor / LB 앞에서 막는 웹 방화벽
- [ ] Certificate Manager / 구글이 자동 갱신하는 인증서 관리

---

# PART 3 · Compute and Storage

## 6. Compute Engine

- [ ] Machine Family / 용도별로 나뉜 VM 계열
- [ ] Custom Machine Type / vCPU·메모리를 직접 정하는 VM 사양
- [ ] Image / VM을 만드는 원본 디스크 스냅샷
- [ ] Disk / 영속성과 속도가 다른 VM 디스크 종류
- [ ] Metadata / 부팅 시 실행되는 스크립트를 심는 곳
- [ ] Instance Template / MIG가 복제할 VM 설정 원본
- [ ] Autoscaling and Autohealing / 부하로 늘리고 헬스체크로 교체하는 자동화
- [ ] Spot VM and Preemptible / 남는 용량을 싸게 쓰다 회수당하는 VM
- [ ] Discounts / 오래 켜둘수록 자동 깎이는 지속 사용 할인

## 7. Serverless and App Platform

- [ ] Cloud Run Resource Model / 서비스가 리비전으로 쌓이는 배포 단위
- [ ] Cloud Run Cold Start / 최소 인스턴스로 초기 지연을 줄이는 설정
- [ ] Cloud Run Jobs / 끝나면 종료되는 배치 실행 단위
- [ ] Cloud Functions / 이벤트 하나에 붙는 단일 함수
- [ ] App Engine / 서버 없이 배포하는 초기 서버리스 플랫폼 `선택`
- [ ] Eventarc / 이벤트를 서비스 간에 연결하는 라우터
- [ ] Cloud Scheduler and Cloud Tasks / 정기 실행과 비동기 큐 작업
- [ ] Selection Criteria / 제어냐 자동화냐로 고르는 컴퓨트 선택

## 8. GKE

- [ ] Cluster Mode / 노드를 직접 관리할지 맡길지 구분
- [ ] Node Pool / 속성이 같은 노드끼리 묶은 그룹
- [ ] Networking / Pod가 VPC IP를 직접 받는 방식
- [ ] Workload Identity / Pod에 서비스 계정을 직접 매는 인증
- [ ] Autoscaling / 노드·Pod·리소스 세 층의 자동 조정
- [ ] Release Channel / 버전 안정성 따라 고르는 업그레이드 궤도
- [ ] Artifact Registry / 컨테이너 이미지를 담는 저장소
- [ ] Binary Authorization / 서명된 이미지만 배포하게 막는 검증 `선택`

## 9. Storage

- [ ] Cloud Storage / 키로 넣고 꺼내는 버킷 객체 저장소
- [ ] Storage Class / 접근 빈도로 나뉜 요금 등급
- [ ] Object Lifecycle Management / 조건 맞으면 등급을 자동으로 낮추는 규칙
- [ ] Versioning / 덮어써도 이전 객체를 남기는 기능
- [ ] Access Control / 버킷 단위 권한과 임시 서명 URL
- [ ] Static Website Hosting / 버킷을 그대로 웹 호스팅으로 쓰는 기능
- [ ] Filestore / 여러 VM이 같이 마운트하는 NFS 파일 서버
- [ ] Data Transfer / 대량 데이터를 옮기는 전송 도구

---

# PART 4 · Data and Analytics

## 10. Databases

- [ ] Cloud SQL / 오픈소스 엔진을 그대로 돌리는 관리형 RDB
- [ ] Cloud SQL Operations / 이중화·복제본·시점 복구 운영
- [ ] AlloyDB / PostgreSQL 호환에 분석까지 빠른 고성능 DB
- [ ] Cloud Spanner / 리전 넘어도 강한 일관성을 지키는 RDB
- [ ] Firestore / 실시간 동기화되는 문서형 DB
- [ ] Bigtable / 로우 키 설계가 성능을 가르는 와이드 컬럼 DB
- [ ] Memorystore / Redis·Memcached를 관리형으로 돌리는 캐시
- [ ] Database Selection Criteria / 데이터 모양으로 고르는 DB 선택

## 11. Data and Analytics

- [ ] BigQuery / 저장과 질의를 분리한 서버리스 분석 엔진
- [ ] BigQuery Optimization / 스캔량을 줄이는 분할과 정렬
- [ ] Pub/Sub / 발행과 구독을 떼어놓는 전역 메시지 큐
- [ ] Dataflow / 배치와 스트림을 한 모델로 처리하는 엔진
- [ ] Dataproc / Spark·Hadoop을 관리형 클러스터로 돌리는 서비스 `선택`
- [ ] Cloud Composer / Airflow를 관리형으로 돌리는 워크플로 오케스트레이션 `선택`
- [ ] Dataplex / 흩어진 데이터를 한 카탈로그로 묶는 거버넌스 `선택`

## 12. AI and ML `선택`

- [ ] Vertex AI / 학습부터 서빙까지 묶은 ML 플랫폼
- [ ] Model Garden / 기반 모델을 꺼내 쓰는 카탈로그
- [ ] Vector Search / 임베딩을 가까운 순서로 찾는 검색

---

# PART 5 · Automation and Operations

## 13. Infrastructure as Code and CI/CD

- [ ] Terraform google Provider / GCP 리소스를 코드로 선언하는 연결 지점 `추천`
- [ ] Config Connector / GCP 리소스를 쿠버네티스 오브젝트로 다루는 방식
- [ ] Cloud Build / 커밋을 계기로 도는 관리형 빌드
- [ ] Cloud Deploy / 환경 단계를 타고 승격되는 배포 파이프라인
- [ ] GitHub Actions / 키 없이 GCP에 인증하는 외부 CI 연동
- [ ] Artifact Registry / 환경별로 이미지를 승격시키는 저장소

## 14. Observability

- [ ] Cloud Monitoring / 지표를 모아 대시보드로 보는 관측
- [ ] Cloud Logging / 전 서비스 로그를 한곳에 모으는 수집
- [ ] Log Sink / 로그를 다른 저장소로 흘려보내는 경로
- [ ] Log-based Metric / 로그 패턴을 세어 만드는 지표
- [ ] Alerting Policy / 조건 충족 시 알림을 보내는 규칙
- [ ] Cloud Trace and Profiler / 요청 지연과 코드 실행 비용 추적
- [ ] Error Reporting / 예외를 자동으로 묶어 보여주는 집계
- [ ] SLO / 허용 가능한 실패 총량을 정하는 목표

## 15. Security

- [ ] Secret Manager / 버전을 매겨 회전시키는 비밀 저장소
- [ ] Cloud KMS / 암호화 키를 관리하는 키 관리 서비스
- [ ] Security Command Center / 취약점과 위협을 한데 모으는 콘솔
- [ ] Identity-Aware Proxy / VPN 없이 신원으로 앱 접근을 거르는 프록시
- [ ] reCAPTCHA Enterprise / 봇 트래픽을 점수로 걸러내는 방어 `선택`
- [ ] Assured Workloads / 규제 준수 경계를 두르는 격리 환경 `선택`

## 16. Cost Management

- [ ] Pricing Calculator / 구성 전에 비용을 미리 계산하는 도구
- [ ] Budget / 지출 한도를 정하고 알림 받는 설정
- [ ] Billing Export to BigQuery / 청구 데이터를 질의로 뜯어보는 내보내기
- [ ] Committed Use Discount / 사용량을 약정해 깎는 할인
- [ ] Recommender / 놀고 있는 리소스를 찾아주는 추천
- [ ] Quota Requests / 한도를 늘리려 올리는 신청

---

# 이 로드맵 밖

- AWS `software/skill-based/Infra-DevOps/aws.md`
- Azure `software/skill-based/Infra-DevOps/azure.md`
- Kubernetes `software/skill-based/Infra-DevOps/kubernetes.md`
- IaC `software/skill-based/Infra-DevOps/terraform.md`
- BigQuery 상세 `software/skill-based/Data-DB/bigquery.md`
- 데브옵스 전반 `software/role-based/devops.md`
