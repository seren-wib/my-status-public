# DigitalOcean `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with DigitalOcean

## 1. Introduction

### Overview

- [ ] Developer-Centric Cloud / 개발자 편의를 우선하는 단순한 포지션
- [ ] Region / 데이터센터 위치를 가리키는 코드
- [ ] Positioning vs AWS and GCP / 서비스 폭 대신 단순함을 택한 자리
- [ ] Suitable Workloads / 소규모 서비스와 사이드 프로젝트에 적합

### Accounts and Organizations

- [ ] Team and Project / 계정을 나누는 조직 구성 단위
- [ ] Billing / 시간 과금이 월 상한에서 멈추는 방식

## 2. Getting Started

### Interfaces `택 1`

- [ ] Control Panel / 브라우저에서 리소스를 클릭으로 다루는 화면
- [ ] doctl CLI / 터미널에서 리소스를 다루는 공식 CLI `추천`
- [ ] API and Client Libraries / 코드에서 직접 호출해 붙이는 방식

### First Exercise

- [ ] SSH Key Registration / 접속용 공개키를 계정에 등록하는 절차
- [ ] Droplet Creation and Access / 서버를 만들고 SSH로 접속하는 순서
- [ ] Basic Firewall Setup / 포트를 열고 닫는 최소한의 방화벽 설정

---

# PART 2 · Core Infrastructure

## 3. Droplets

- [ ] Droplet Plan / CPU와 메모리 비중으로 나뉜 사양 등급
- [ ] Shared vs Dedicated vCPU / vCPU를 나눠 쓰는지 독점하는지 구분
- [ ] Image / 배포판·마켓플레이스·커스텀 중에서 고르는 원본
- [ ] Cloud-init / 첫 부팅 때 실행할 설정을 스크립트로 주입
- [ ] Snapshot vs Backup / 수동 캡처와 자동 주기 저장의 차이
- [ ] Resize / 플랜을 올려 수직으로만 늘리는 확장
- [ ] Metadata Service / Droplet 내부에서 자기 정보를 조회하는 API
- [ ] Droplet Console and Recovery Mode / SSH가 막혔을 때 쓰는 웹 콘솔 진입

## 4. Networking

- [ ] VPC / 사설 IP 대역으로 Droplet을 묶는 네트워크
- [ ] Reserved IP / 장애 시 다른 Droplet에 옮겨 붙는 고정 IP
- [ ] Cloud Firewall / 인바운드·아웃바운드 규칙을 거는 방화벽
- [ ] Load Balancer / 헬스체크와 세션 고정을 지원하는 분산기
- [ ] Load Balancer TLS / 로드밸런서에 인증서를 붙이는 설정
- [ ] DNS / 도메인과 레코드를 직접 관리하는 기능
- [ ] IPv6 / 사설 네트워크에서도 쓸 수 있는 주소 체계
- [ ] Bandwidth Pool / 포함 대역폭을 넘으면 과금되는 한도

## 5. Storage

- [ ] Volumes / Droplet에 붙여 늘릴 수 있는 블록 스토리지
- [ ] Spaces / 파일을 키로 넣고 꺼내는 S3 호환 저장소
- [ ] Spaces CDN / Spaces 파일을 엣지에 캐싱해 배포
- [ ] Spaces Access Key / Spaces에 접근할 키와 시크릿 발급
- [ ] Backup Policy / 스냅샷을 주기적으로 자동 생성하는 정책

---

# PART 3 · Managed Platform

## 6. Managed Databases

- [ ] Supported Engines / 관리형으로 제공되는 DB 엔진 목록
- [ ] Cluster / 주 노드와 대기 노드로 구성된 단위
- [ ] Connection Pool / PgBouncer로 연결 수를 줄이는 풀링
- [ ] Read Replica / 읽기 부하를 나눠 받는 복제본
- [ ] Trusted Source / 지정한 소스만 DB에 접근하게 제한
- [ ] Backup / 특정 시점으로 되돌리는 PITR 지원
- [ ] Migration / 기존 DB를 관리형으로 옮기는 절차

## 7. App Platform

- [ ] PaaS Model / 저장소에 push하면 자동 배포되는 모델
- [ ] Component Type / 앱을 구성하는 역할별 단위
- [ ] App Spec / 앱 구성을 통째로 적는 YAML 파일
- [ ] Build / Buildpack이나 Dockerfile로 이미지 생성
- [ ] Environment Variable / 값을 암호화해 저장하는 Secret 옵션
- [ ] Autoscaling / 인스턴스 크기와 개수를 자동 조절
- [ ] Custom Domain / 연결하면 TLS를 자동 발급하는 기능
- [ ] Droplet vs App Platform Decision Criteria / 둘 중 무엇을 쓸지 가르는 기준

## 8. Kubernetes and Containers

- [ ] DOKS / 컨트롤 플레인을 대신 관리해주는 쿠버네티스
- [ ] Node Pool / 노드 그룹 단위로 자동 확장하는 설정
- [ ] Container Registry / 이미지를 저장하는 DOCR 사설 저장소
- [ ] CSI Driver / 쿠버네티스에서 Volumes를 붙이는 드라이버
- [ ] Load Balancer Integration / 어노테이션으로 로드밸런서를 연동
- [ ] 1-Click App / Ingress·Cert-manager를 원클릭 설치
- [ ] Cluster Upgrade / 새 노드를 먼저 띄워 무중단 전환

## 9. Functions and Serverless `선택`

- [ ] DigitalOcean Functions / 네임스페이스와 트리거로 묶는 서버리스
- [ ] Execution Limits / 실행 시간과 메모리에 걸린 상한

---

# PART 4 · Operations

## 10. Automation

- [ ] doctl Scripting / doctl 명령을 스크립트로 자동화
- [ ] Terraform digitalocean Provider / 리소스를 코드로 선언해 관리 `추천`
- [ ] API Token / 권한 범위와 만료 기한을 가진 토큰
- [ ] Ansible / 서버 설정을 코드로 맞추는 도구 `선택`
- [ ] CI/CD Integration / GitHub Actions에서 배포까지 연결

## 11. Monitoring

- [ ] Monitoring Agent / Droplet에 심어 지표를 수집하는 에이전트
- [ ] Metric / CPU·메모리·디스크·대역폭 등 수집 지표
- [ ] Alert Policy / 임계치를 넘으면 알림을 보내는 규칙
- [ ] Uptime Check / 외부에서 주기적으로 접속을 확인
- [ ] Log Collection / 로그를 외부 도구로 내보내 모으기

## 12. Security

- [ ] SSH Hardening / 비밀번호 로그인을 막고 키만 허용
- [ ] Deny-by-Default Firewall Policy / 허용한 것 외엔 전부 막는 원칙
- [ ] Private Networking First / 외부 노출 대신 사설망을 우선 사용
- [ ] Team Permissions / 팀원에게 역할별로 권한을 부여
- [ ] TLS Certificates / Let's Encrypt로 인증서를 자동 갱신

## 13. Cost and Scaling

- [ ] Pricing Structure / 시간 과금이 월 상한에서 멈추는 구조
- [ ] Snapshot and Volume Retention Cost / 보관 용량만큼 쌓이는 비용
- [ ] Bandwidth Overage Cost / 포함량 초과분에 붙는 비용
- [ ] Vertical vs Horizontal Scaling Decision / 사양을 올릴지 대수를 늘릴지 선택
- [ ] Scaling Ceiling / 규모 커지면 대형 클라우드로 갈아탈 시점

---

# 이 로드맵 밖

- AWS `software/skill-based/Infra-DevOps/aws.md`
- Kubernetes `software/skill-based/Infra-DevOps/kubernetes.md`
- 리눅스 `software/skill-based/Infra-DevOps/linux.md`
- IaC `software/skill-based/Infra-DevOps/terraform.md`
- Nginx `software/skill-based/Infra-DevOps/nginx.md`
- 데브옵스 전반 `software/role-based/devops.md`
