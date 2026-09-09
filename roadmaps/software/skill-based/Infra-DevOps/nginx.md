# Nginx `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Nginx

## 1. What is Nginx?

### Overview

- [ ] Web Server, Reverse Proxy, Load Balancer / 세 역할을 한 바이너리로 겸하는 소프트웨어
- [ ] Event-driven Architecture / 워커가 이벤트 루프로 다수 연결을 동시 처리하는 구조
- [ ] Nginx vs Apache httpd / 연결마다 프로세스 대신 워커로 처리하는 차이
- [ ] Nginx Open Source vs Nginx Plus / 액티브 헬스체크 등 상용 전용 기능 유무

### Primary Use Cases

- [ ] Static File Serving / sendfile로 커널이 직접 응답하는 처리
- [ ] Application Reverse Proxy / 런타임을 뒤로 넘겨 요청을 위임하는 역할
- [ ] TLS Termination / 암호화를 여기서 풀고 뒤로는 평문 전달
- [ ] API Gateway and Edge Cache / 라우팅과 캐시를 앞단에서 겸하는 역할

## 2. Installation and Running

### Installation `택 1`

- [ ] Package Manager / 배포판 저장소로 설치해 갱신을 맡기는 방식 `추천`
- [ ] Docker Image / 컨테이너로 격리해 배포하는 방식
- [ ] Source Build / configure 옵션으로 기능을 골라 컴파일하는 방식

### Process Control

- [ ] Service Management / systemctl로 서비스 단위를 제어하는 방식
- [ ] Signal / nginx -s로 프로세스에 명령을 보내는 방식
- [ ] Configuration Test / 적용 전 문법 오류를 미리 잡는 검사
- [ ] Graceful Reload Internals / 새 워커를 띄우고 기존 연결은 끝낸 뒤 종료
- [ ] Version and Module Inspection / 빌드에 포함된 모듈을 확인하는 방법

## 3. Configuration Structure

- [ ] Directory Layout / 배포판별로 설정 파일을 나누는 관례
- [ ] Context Hierarchy / 설정 블록이 중첩되며 범위를 좁히는 구조
- [ ] Directive / 한 줄로 끝나거나 블록으로 감싸는 두 형태
- [ ] Inheritance and Override Rules / 하위 컨텍스트가 상위 값을 물려받고 덮는 규칙
- [ ] include / 여러 파일로 쪼갠 설정을 하나로 모으는 지시어
- [ ] Variable / 요청 정보를 담아 지시어 안에서 쓰는 값
- [ ] Global Directives / worker_processes·worker_connections처럼 전역에 거는 설정

---

# PART 2 · Request Handling

## 4. Server Blocks

- [ ] Virtual Host / 하나의 IP·포트에 여러 도메인을 얹는 단위
- [ ] Default Server / 매칭되는 이름이 없을 때 받는 블록
- [ ] Name-based vs IP-based / Host 헤더로 가를지 주소로 가를지의 차이
- [ ] Port and IP Binding / listen에 주소·포트·옵션을 함께 지정하는 방식
- [ ] Server Name Matching Precedence / 정확 일치·와일드카드·정규식 순으로 고르는 우선순위

## 5. Location and Request Routing

- [ ] Location Modifier / =·^~·~ 등으로 매칭 방식을 지정하는 기호
- [ ] Location Matching Precedence / 정확·접두사·정규식 순으로 location을 고르는 순서
- [ ] Path Mapping / root는 이어붙이고 alias는 통째로 바꾸는 차이
- [ ] Internal Redirect / 파일이 없으면 다음 후보로 넘어가는 순서
- [ ] Rewrite / URL을 바꿔 다시 매칭시키는 지시어
- [ ] Error Page / 상태 코드별로 보여줄 응답을 지정하는 지시어
- [ ] Named Location / 직접 매칭되지 않고 내부에서만 불리는 위치

## 6. Static Content

- [ ] MIME Type / 확장자로 Content-Type을 정하는 표
- [ ] Directory Listing / 인덱스 파일이 없을 때 목록을 보여주는 기능
- [ ] Byte Range, Sendfile, sendfile, tcp_nopush / 파일 일부만 응답하고 커널로 직접 전송하는 최적화
- [ ] Compression / 응답을 압축해 전송량을 줄이는 기능
- [ ] Brotli / gzip보다 압축률 높은 대체 알고리즘 `선택`
- [ ] Client Cache Headers / 브라우저에 캐시 기간을 알리는 헤더
- [ ] Upload Size Limit / client_max_body_size로 업로드 용량을 막는 값

## 7. Logging

- [ ] Access Log / 요청마다 형식을 정해 남기는 로그
- [ ] Error Log / 심각도별로 걸러 남기는 오류 로그
- [ ] JSON Log Format / 로그 수집기가 파싱하기 쉬운 구조화 형식
- [ ] Real IP Restoration / 프록시 뒤에서 진짜 클라이언트 IP를 복원하는 설정
- [ ] Log Rotation / 로그 파일을 순환시키고 새 파일로 다시 여는 절차
- [ ] Log Shipping Integration / 외부 수집기로 로그를 실시간 전달하는 연동

---

# PART 3 · Proxying and Load Balancing

## 8. Reverse Proxy

- [ ] Basic Proxying / 요청을 다른 서버로 넘기며 URI를 치환하는 규칙
- [ ] Header Forwarding / 원 요청 정보를 백엔드에 헤더로 전달하는 설정
- [ ] Proxy Timeouts / 백엔드 연결·응답 대기 시간의 상한
- [ ] Buffering / 백엔드 응답을 메모리에 모았다 클라이언트로 보내는 방식
- [ ] WebSocket Proxy / 연결을 유지한 채 프로토콜을 전환해 넘기는 방식
- [ ] HTTP Version / 백엔드와의 연결에 쓸 HTTP 버전과 재사용 여부
- [ ] Upstream Error Handling / 백엔드 오류 시 다른 서버로 재시도하는 규칙

## 9. Load Balancing

- [ ] Upstream Block / 분산 대상 서버들을 묶어 이름 붙이는 블록
- [ ] Balancing Algorithms / 요청을 서버들에 나눠 보내는 방식
- [ ] Server Weights / 서버마다 받는 비중과 대기·제외 상태를 정하는 값
- [ ] Passive Health Check / 실패 횟수를 세어 자동으로 빼는 방식
- [ ] Connection Pool / 백엔드와의 연결을 재사용해 두는 풀
- [ ] Session Persistence / 같은 클라이언트를 매번 같은 서버로 보내는 방식 `선택`
- [ ] Active Health Check / 별도 요청을 주기적으로 보내 상태를 확인하는 기능 `별도`

## 10. Caching

- [ ] Proxy Cache / 백엔드 응답을 디스크에 저장해 재사용하는 층
- [ ] Cache Key / 캐시를 구분해 저장할 기준을 정하는 값
- [ ] Cache Validity / 상태 코드별로 캐시를 유지할 기간을 정하는 설정
- [ ] Stale Response / 갱신 중에도 오래된 캐시를 우선 내보내는 방식
- [ ] Cache Lock / 캐시 미스 요청을 하나만 통과시켜 몰림을 막는 잠금
- [ ] Cache Bypass Conditions / proxy_cache_bypass·proxy_no_cache로 캐시를 건너뛰는 조건
- [ ] Purge Strategy / 캐시를 강제로 지우는 방법

## 11. Application Gateways

- [ ] FastCGI / PHP 등 별도 프로세스로 요청을 넘기는 프로토콜
- [ ] uWSGI and SCGI / 파이썬 등 다른 언어 런타임과 통신하는 프로토콜
- [ ] gRPC Proxy / HTTP/2 기반 gRPC 요청을 넘기는 설정
- [ ] Stream Module / L7이 아닌 L4에서 TCP·UDP를 그대로 넘기는 모듈
- [ ] Mail Proxy / SMTP·IMAP·POP3 인증을 대신 처리하는 기능 `선택`

---

# PART 4 · Security and Performance

## 12. TLS and HTTPS

- [ ] Certificate Configuration / 인증서와 개인키 경로를 지정하는 설정
- [ ] Protocol · Cipher / 허용할 TLS 버전과 암호화 방식을 제한하는 설정
- [ ] Session Reuse / TLS 핸드셰이크를 캐시해 재접속을 빠르게 하는 설정
- [ ] HTTP to HTTPS Redirect / 평문 요청을 암호화 접속으로 돌리는 처리
- [ ] HSTS / 브라우저에 HTTPS만 쓰라고 강제하는 헤더
- [ ] SNI / 한 IP에서 도메인별로 다른 인증서를 고르는 확장
- [ ] OCSP Stapling / 인증서 폐지 여부를 서버가 미리 첨부해 응답하는 방식
- [ ] Let's Encrypt / 무료 인증서를 자동 발급·갱신하는 서비스
- [ ] mTLS / 클라이언트에도 인증서를 요구하는 상호 인증
- [ ] Enabling HTTP/2 and HTTP/3 / 새 프로토콜 버전을 리스너에 켜는 설정

## 13. Access Control and Limits

- [ ] IP Access Control / 주소 대역별로 접근을 허용·차단하는 규칙
- [ ] Basic Auth / 아이디·비밀번호로 접근을 막는 간단 인증
- [ ] Subrequest Authentication / 내부 요청으로 인증 서버에 물어보고 통과시키는 방식
- [ ] Rate Limiting / 초당 요청 수를 제한하고 초과분을 다루는 설정
- [ ] Connection Limiting / 동시 연결 수 자체를 제한하는 설정
- [ ] Bandwidth Limiting / 전송 속도 상한을 거는 설정
- [ ] Method Restriction / 지정한 HTTP 메서드만 예외 없이 허용하는 제한
- [ ] Security Headers / 클릭재킹·XSS 등을 막는 응답 헤더 모음
- [ ] Information Disclosure Reduction / 오류 응답에서 서버 버전을 숨기는 설정
- [ ] CORS Handling / 다른 출처 요청을 허용할지 헤더로 알려주는 처리

## 14. Performance Tuning

- [ ] Worker Tuning / 워커 개수와 파일 디스크립터 상한을 맞추는 설정
- [ ] Connection Processing / 워커가 커널 이벤트로 연결을 받아들이는 방식
- [ ] Keepalive / 한 연결에서 몇 요청까지·얼마나 유지할지 정하는 설정
- [ ] Open File Cache / 자주 여는 파일의 디스크립터를 캐시해 두는 기능
- [ ] Buffer Sizing / 요청 본문·헤더를 담을 버퍼 크기를 조정하는 설정
- [ ] OS Tuning / 커널의 연결 대기열·파일 디스크립터 상한을 올리는 조정
- [ ] Benchmarking / 부하를 걸어 처리량과 지연을 재는 도구

---

# PART 5 · Extensions and Operations

## 15. Modules and Extensions

- [ ] Static vs Dynamic Module / 빌드에 넣을지 나중에 불러올지의 차이
- [ ] Map and Geo Modules / 조건이나 주소에 따라 변수 값을 만드는 모듈
- [ ] Sub Filter / 응답 본문의 문자열을 바꿔 내보내는 필터
- [ ] Lua / OpenResty 배포판으로 스크립트를 끼워 넣는 확장 `선택`
- [ ] njs / 설정 안에서 자바스크립트로 로직을 짜는 확장 `선택`
- [ ] ModSecurity WAF / 요청을 룰셋으로 걸러내는 방화벽 모듈 `선택`
- [ ] Nginx Ingress Controller / 쿠버네티스 안에서 라우팅을 맡는 컨트롤러 `별도`

## 16. Operations and Troubleshooting

- [ ] Zero-Downtime Config Rollout / 서비스 중단 없이 설정을 바꿔 반영하는 절차
- [ ] Binary Upgrade / 무중단으로 실행 파일 자체를 교체하는 절차
- [ ] Status Endpoint / 연결·요청 통계를 노출하는 내장 엔드포인트
- [ ] Metrics Collection / 상태 값을 프로메테우스 형식으로 변환해 수집하는 도구
- [ ] Common Errors / 502·504·413·499 같은 코드별 원인을 구분하는 방법
- [ ] Debug Log / 요청 처리 과정을 상세히 남기는 로그 레벨
- [ ] Configuration Management / 설정을 템플릿화해 버전으로 관리하는 방식
- [ ] Container Deployment / 컨테이너에 설정을 마운트하고 갱신하는 전략

---

# 이 로드맵 밖

- Apache HTTP Server `software/skill-based/Infra-DevOps/apache-httpd.md`
- Caddy `software/skill-based/Infra-DevOps/caddy.md`
- 리눅스 `software/skill-based/Infra-DevOps/linux.md`
- Kubernetes Ingress `software/skill-based/Infra-DevOps/kubernetes.md`
- 확장 설계 · 캐시 전략 `software/skill-based/CS-Theory/system-design.md`
- 데브옵스 전반 `software/role-based/devops.md`
