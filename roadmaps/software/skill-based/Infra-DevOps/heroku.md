# Heroku `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Heroku

## 1. What is Heroku?

### Overview

- [ ] PaaS Model / 인프라 관리를 플랫폼에 맡기는 모델
- [ ] Git Push Based Deployment / git push 한 번으로 배포하는 방식
- [ ] Dyno-Centric Execution Model / dyno를 실행 단위로 삼는 구조
- [ ] Add-on Ecosystem / 마켓에서 골라 붙이는 부가 기능 생태계

### Design Principles

- [ ] Twelve-Factor App / 무상태 앱을 전제하는 열두 원칙
- [ ] Stateless Process and Ephemeral Filesystem / 재시작마다 파일이 사라지는 무상태 구조
- [ ] Config in Environment / 설정을 코드가 아닌 환경변수로 두는 원칙
- [ ] Heroku vs Vercel vs Self-Managed Containers / 세 배포 방식의 관리 범위 차이

## 2. Getting Started

- [ ] Heroku CLI / heroku login으로 인증하는 명령줄 도구
- [ ] App Creation / heroku create로 앱을 생성하는 명령
- [ ] Region / 앱이 돌아갈 인프라 위치를 고르는 설정
- [ ] Procfile / 프로세스 종류를 선언하는 파일
- [ ] First Deploy / git push heroku main으로 하는 첫 배포
- [ ] heroku logs --tail / 로그를 실시간으로 스트리밍하는 명령
- [ ] heroku run / 일회성 dyno를 띄워 명령을 실행하는 기능

---

# PART 2 · Application Structure

## 3. Dynos

- [ ] Dyno Types / web·worker·one-off로 나뉘는 역할
- [ ] Dyno Type / Eco·Basic 등 성능별 요금제 등급
- [ ] Dyno Lifecycle / 재시작과 순환으로 도는 생명주기
- [ ] Sleeping Dyno / Eco 플랜에서 대기 중 잠드는 현상
- [ ] Boot Timeout / 기동과 SIGTERM 종료에 걸리는 시간제한
- [ ] Scaling / heroku ps:scale로 dyno 수를 조절하는 명령
- [ ] Process Concurrency / WEB_CONCURRENCY로 정하는 동시 처리 수
- [ ] $PORT Binding Rule / 라우터가 넘겨준 포트로 리슨해야 하는 규칙

## 4. Buildpacks and Slugs

- [ ] Build Process / 감지·컴파일·릴리스로 도는 빌드 단계
- [ ] Official Buildpack / Node.js 등 언어별 런타임 감지 도구
- [ ] Multiple Buildpacks / 순서대로 겹쳐 적용하는 빌드팩 조합
- [ ] Custom Buildpack / 공식 목록에 없는 빌드팩 직접 지정
- [ ] Slug / 용량 제한이 있는 빌드 결과물 압축본
- [ ] Container Registry / Dockerfile로 이미지를 직접 배포하는 방식 `선택`
- [ ] Stack / heroku-24 등 실행 환경의 베이스 이미지
- [ ] Build Cache / 다음 빌드를 앞당기는 의존성 캐시

## 5. Config and Add-ons

- [ ] Config Vars / heroku config:set으로 넣는 환경변수
- [ ] Per-Environment Separation / 스테이징과 프로덕션을 나누는 설정
- [ ] Add-on / 프로비저닝하고 플랜을 바꾸는 부가 기능
- [ ] Automatic Add-on Config Var Injection / 애드온 설치 시 자동으로 꽂히는 접속 정보
- [ ] Attached Resource / 여러 앱이 함께 붙여 쓰는 리소스
- [ ] Add-on Cost Structure / 사용 시간 단위로 매기는 과금 방식

---

# PART 3 · Deployment and Data

## 6. Deployment Workflow

- [ ] Release / 슬러그와 설정을 묶은 불변 배포 단위
- [ ] Rollback / heroku releases:rollback으로 되돌리는 명령
- [ ] Release Phase / 배포마다 마이그레이션을 실행하는 단계
- [ ] Pipeline / 리뷰·스테이징·프로덕션을 잇는 배포 흐름
- [ ] Review App / PR마다 자동으로 뜨는 임시 환경
- [ ] Promote / 같은 슬러그를 다음 단계로 승격하는 절차
- [ ] GitHub Integration / 브랜치 푸시로 자동 배포하는 연동
- [ ] Preboot / 새 dyno를 띄운 뒤 전환하는 무중단 배포
- [ ] Maintenance Mode / 요청을 막고 점검 화면을 띄우는 상태

## 7. Heroku Postgres

- [ ] Plan / Essential·Standard·Premium 요금제 등급
- [ ] DATABASE_URL / 연결 수 제한이 걸린 접속 환경변수
- [ ] Connection Pooling / PgBouncer로 연결을 묶는 기능
- [ ] Backup / 수동과 예약으로 뜨는 데이터베이스 백업
- [ ] Follower / 읽기 부하를 나누는 복제본
- [ ] Fork / 데이터를 통째로 복제해 새 DB를 만드는 기능
- [ ] Dataclip / 쿼리 결과를 공유하는 링크 `선택`
- [ ] Plan Upgrade / 다운타임을 최소화하며 등급을 올리는 절차

## 8. Other Data Services

- [ ] Heroku Key-Value Store / Redis와 호환되는 관리형 캐시
- [ ] Apache Kafka on Heroku / 관리형으로 붙이는 스트리밍 애드온 `선택`
- [ ] Connecting External Managed Databases / 외부 DB를 config var로 붙이는 방식
- [ ] File Storage / 휘발성이라 S3 등 외부에 둬야 하는 저장소

---

# PART 4 · Operations

## 9. Logging and Monitoring

- [ ] Logplex / 모든 로그를 한 스트림으로 모으는 라우터
- [ ] Log Drain / 로그를 외부 서비스로 흘려보내는 통로
- [ ] Router Log / 요청 상태와 지연을 담은 로그
- [ ] Metrics / 응답시간·처리량·메모리로 보는 지표
- [ ] R14 Memory Quota Exceeded and H12 Timeout / 메모리 초과와 30초 응답 지연 오류
- [ ] Threshold Alert / 지표가 기준을 넘으면 오는 알림
- [ ] APM Add-on / New Relic 등 성능 모니터링 확장

## 10. Networking and Domains

- [ ] Custom Domain / DNS를 heroku로 돌리는 설정
- [ ] Automated Certificate Management / TLS 인증서를 자동 발급·갱신하는 기능
- [ ] Router / 요청을 대기시키다 30초면 끊는 관문
- [ ] Static IP / 애드온으로 고정하는 발신 IP `선택`
- [ ] Private Space / VPC로 격리하는 전용 네트워크 `선택`

## 11. Security and Access

- [ ] Team / 역할을 나눠 협업자를 관리하는 조직 단위
- [ ] API Key / CLI·API 인증에 쓰는 OAuth 토큰
- [ ] Two-Factor Authentication / 로그인에 두 번째 인증을 요구하는 기능
- [ ] Shield Space / 규제 준수를 위한 강화된 전용 공간 `선택`
- [ ] Secret Management / config var 노출을 조심해야 하는 관리

## 12. Cost and Migration

- [ ] Billing Units / dyno 시간과 애드온으로 매기는 과금 단위
- [ ] Pricing After the Free Tier Ended / 2022년 무료 요금제가 사라진 이후 체계
- [ ] Cost Reduction / dyno 축소와 애드온 정리로 낮추는 비용
- [ ] Migration Decision / 컨테이너·클라우드로 옮길 시점 판단
- [ ] Lower Migration Cost from Twelve-Factor Compliance / 열두 원칙 준수 덕에 낮아지는 이전 비용

---

# 이 로드맵 밖

- Docker `software/skill-based/Infra-DevOps/docker.md`
- AWS `software/skill-based/Infra-DevOps/aws.md`
- Vercel `software/skill-based/Infra-DevOps/vercel.md`
- DigitalOcean `software/skill-based/Infra-DevOps/digitalocean.md`
- 백엔드 전반 `software/role-based/backend.md`
- 데브옵스 전반 `software/role-based/devops.md`
