# Caddy `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Caddy

## 1. What is Caddy?

### Overview

- [ ] Single Binary Web Server / 의존성 없이 실행 파일 하나로 도는 구조
- [ ] Automatic HTTPS / 인증서 발급과 갱신을 자동으로 처리하는 기능
- [ ] Caddyfile / 실제로는 JSON 설정으로 변환되는 사람용 문법
- [ ] Comparison with Nginx and Apache / 손잡이 대신 안전한 기본값을 미리 깐 설계

### Main Use Cases

- [ ] Static Site Hosting / 루트 지정만으로 끝나는 정적 파일 서빙
- [ ] Reverse Proxy / 백엔드 앞단에서 요청을 그대로 넘기는 용도
- [ ] Internal Service TLS Automation / 내부망 서비스도 자동 인증서로 묶는 용도
- [ ] Sidecar and Container Edge / 컨테이너 옆에 붙어 TLS·라우팅을 맡는 배치

## 2. Installation and Running

### Installation `택 1`

- [ ] Package Manager / 배포판 저장소로 설치하는 방법 `추천`
- [ ] Docker Image / 공식 이미지로 컨테이너에서 실행
- [ ] Static Binary / xcaddy로 플러그인 포함해 직접 빌드

### Running

- [ ] caddy run and caddy start / 포그라운드 실행과 데몬 실행의 차이
- [ ] Service Management / systemd 유닛으로 상시 구동시키는 방법
- [ ] Config Reload / 연결을 끊지 않고 설정을 다시 읽는 방법
- [ ] Config Validation / 적용 전 문법 오류를 미리 검사하는 명령
- [ ] Formatting / Caddyfile을 표준 형식으로 정렬하는 명령
- [ ] One-off Commands / 설정 파일 없이 즉석에서 띄우는 명령

## 3. Caddyfile Basics

- [ ] Caddyfile Structure / 사이트 주소와 지시어 블록으로 이뤄진 구성
- [ ] Site Address / 스킴·호스트·포트로 매칭 범위를 정하는 줄
- [ ] Global Options Block / 사이트 밖에서 서버 전역값을 설정하는 블록
- [ ] Directive Execution Order / 작성 순서와 무관하게 미리 정해진 순서로 실행
- [ ] Snippet / 반복되는 블록을 이름 붙여 import로 재사용
- [ ] Placeholder / 요청 정보를 변수처럼 꺼내 쓰는 표기
- [ ] Environment Variable Substitution / 설정값을 환경변수로 대체하는 기능

---

# PART 2 · Configuration and Routing

## 4. Matchers and Routing

- [ ] Matcher / 경로·호스트·헤더로 요청을 골라내는 조건
- [ ] Named Matcher / @기호로 조건을 이름 붙여 재사용
- [ ] Path Matching Rules / 와일드카드와 정확 일치를 구분하는 규칙
- [ ] route, handle, handle_path / 우선순위 처리 방식이 서로 다른 세 지시어
- [ ] redir and rewrite / 클라이언트를 보낼지 내부에서만 바꿀지의 차이
- [ ] error and handle_errors / 오류를 강제로 낼지 발생한 오류를 처리할지의 차이
- [ ] respond / 백엔드 없이 그 자리에서 바로 응답하는 지시어

## 5. Serving Content

- [ ] file_server / 디렉터리 목록·숨김 규칙을 갖는 정적 서빙
- [ ] root / 파일을 찾을 기준 디렉터리를 지정하는 지시어
- [ ] try_files / 파일이 없으면 대체 경로로 넘기는 지시어
- [ ] templates / 응답 본문에 템플릿 문법을 적용하는 기능 `선택`
- [ ] encode / gzip·zstd로 응답을 압축하는 지시어
- [ ] header / 응답 헤더를 추가·수정·삭제하는 지시어
- [ ] Cache-Control Configuration / 캐시 정책 헤더를 지정하는 설정
- [ ] php_fastcgi / PHP-FPM으로 요청을 넘기는 축약 지시어

## 6. Reverse Proxy

- [ ] reverse_proxy / 백엔드 주소로 요청을 그대로 넘기는 지시어
- [ ] Header Handling / 업스트림으로 오가는 헤더를 조작하는 방법
- [ ] Load Balancing Policy / 여러 업스트림에 요청을 분배하는 방식
- [ ] Health Check / 업스트림 생사를 능동·수동으로 확인하는 방식
- [ ] Timeout / 업스트림 연결·응답 대기 시간을 정하는 설정
- [ ] WebSocket / 별도 설정 없이 프로토콜 업그레이드를 처리
- [ ] Upstream TLS / 백엔드와의 연결도 TLS로 감싸는 설정
- [ ] gRPC Proxy / HTTP/2 기반 gRPC 트래픽을 프록시하는 기능 `선택`

---

# PART 3 · TLS Automation

## 7. Automatic HTTPS

- [ ] How Automatic HTTPS Works / 도메인만 적으면 인증서를 알아서 받아오는 원리
- [ ] Automatic HTTP to HTTPS Redirect / 별도 설정 없이 HTTP를 HTTPS로 넘기는 기본값
- [ ] ACME Challenge / 도메인 소유를 증명해 인증서를 받는 방식
- [ ] DNS Provider Plugin / DNS-01로 와일드카드 인증서를 받게 하는 확장
- [ ] Local HTTPS / 자체 CA로 내부망에도 인증서를 발급하는 기능
- [ ] Automatic Renewal / 만료 전 알아서 갱신하고 실패하면 재시도

## 8. TLS Configuration

- [ ] tls Directive / 자동 발급 대신 인증서를 직접 지정하는 지시어
- [ ] CA Selection / 인증서를 발급받을 CA를 바꾸는 설정
- [ ] Protocol and Cipher Tuning / TLS 버전과 암호 스위트를 제한하는 설정
- [ ] Client Authentication / 클라이언트 인증서로 상호 인증하는 기능
- [ ] On-Demand TLS / 목록에 없는 도메인도 요청 시점에 발급
- [ ] Certificate Storage / 인증서 저장소를 여러 인스턴스가 공유하는 설정

---

# PART 4 · Extension and Operations

## 9. JSON Config and API

- [ ] JSON Config Structure / apps 아래 http·servers·routes로 내려가는 구조
- [ ] Caddyfile to JSON Adaptation / Caddyfile을 실제 설정 JSON으로 변환하는 명령
- [ ] Admin API / 재시작 없이 설정을 조회·교체하는 API
- [ ] Config Persistence / API로 바뀐 설정을 디스크에 자동 저장
- [ ] Admin Endpoint Hardening / 관리 API 접근을 로컬로 제한하는 조치
- [ ] When to Use JSON / 정적 파일 대신 API로 동적 제어할 때 쓰는 방식

## 10. Plugins

- [ ] xcaddy / 원하는 모듈을 넣어 바이너리를 다시 빌드하는 도구
- [ ] Module Structure / 플러그인이 네임스페이스로 등록되는 구조
- [ ] Common Plugins / DNS 발급·보안·속도 제한 등 자주 쓰는 확장
- [ ] Plugin Maintenance Risk / 서드파티 모듈이라 업데이트가 끊길 위험

## 11. Security and Access Control

- [ ] basic_auth / 비밀번호 해시로 거는 기본 인증 지시어
- [ ] forward_auth / 인증 판단을 외부 서비스에 위임하는 지시어
- [ ] IP-Based Access Control / 출발지 IP로 접근을 허용·차단하는 방식
- [ ] Rate Limiting / 플러그인으로 요청 빈도를 제한하는 기능 `선택`
- [ ] Security Headers / HSTS·CSP 같은 보안 응답 헤더를 붙이는 설정
- [ ] request_body / 요청 본문 크기 상한을 거는 지시어

## 12. Operations

- [ ] log / 접근 로그 출력 대상과 형식을 지정하는 지시어
- [ ] Log Level / debug 모드로 로그 상세도를 올리는 설정
- [ ] Metrics / Prometheus가 긁어갈 지표 엔드포인트를 노출
- [ ] Container Deployment / Caddyfile 마운트와 인증서 볼륨 영속화
- [ ] Certificate Data Backup / 발급된 인증서가 쌓이는 디렉터리를 보존
- [ ] Common Problems / 인증서 발급 실패·포트 권한 등 흔한 장애
- [ ] Migration Mapping from Nginx / location을 matcher·handle로 옮기는 대응표

---

# 이 로드맵 밖

- Nginx `software/skill-based/Infra-DevOps/nginx.md`
- Apache HTTP Server `software/skill-based/Infra-DevOps/apache-httpd.md`
- Docker `software/skill-based/Infra-DevOps/docker.md`
- 리눅스 `software/skill-based/Infra-DevOps/linux.md`
- 데브옵스 전반 `software/role-based/devops.md`
