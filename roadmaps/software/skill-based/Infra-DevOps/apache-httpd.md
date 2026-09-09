# Apache HTTP Server `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to httpd

## 1. What is Apache httpd?

### Overview

- [ ] Modular Web Server Architecture / 모듈을 얹고 빼 기능을 바꾸는 구조
- [ ] Module-Based Extension Philosophy / 핵심은 작게, 기능은 모듈로 얹는 설계
- [ ] .htaccess Distributed Configuration Model / 디렉터리마다 설정을 따로 얹는 방식
- [ ] httpd vs Nginx / 프로세스 기반과 이벤트 기반, 선택 기준

### Main Use Cases

- [ ] Static File Serving / 파일을 그대로 응답하는 가장 단순한 역할
- [ ] Application Hosting / mod_php·mod_wsgi로 언어 런타임을 얹는 방식
- [ ] Reverse Proxy and Load Balancer / 앞단에서 요청을 넘기고 분산하는 역할
- [ ] Legacy Operations and Migration / 오래된 서버를 그대로 옮겨 운영하는 일

## 2. Installation and Running

### Installation `택 1`

- [ ] Package Manager / OS 패키지로 설치해 버전 관리를 맡기는 방법 `추천`
- [ ] Docker Image / 컨테이너 이미지로 격리해 실행하는 방법
- [ ] Source Build / 소스를 직접 컴파일해 모듈을 고르는 방법

### Distribution Differences

- [ ] Debian Family / a2enmod·a2ensite로 모듈·사이트를 켜는 방식
- [ ] RHEL Family / conf.modules.d에 모듈 설정을 나눠 두는 방식
- [ ] Run User / 워커 프로세스가 파일에 접근할 때 쓰는 계정

### Process Control

- [ ] apachectl / start·graceful·configtest로 서버를 제어하는 명령
- [ ] Configuration Test / 반영 전 설정 문법을 미리 검사하는 명령
- [ ] Module and Config Inspection / 적재된 모듈과 가상호스트를 나열하는 명령

## 3. Configuration Structure

- [ ] File Layout / 메인 설정과 조각 설정 파일이 나뉜 구조
- [ ] Directive / 지시어 하나와 범위를 감싸는 컨테이너의 차이
- [ ] Container Directives / Directory·Files·Location처럼 범위를 감싸는 지시어
- [ ] Merge Order / 여러 컨테이너 설정이 겹칠 때 적용되는 우선순위
- [ ] Include and IncludeOptional / 파일이 없어도 되는지로 갈리는 include 지시어
- [ ] Conditional Configuration / 모듈 유무·정의값에 따라 설정을 가르는 문법
- [ ] ServerRoot, DocumentRoot, Listen / 서버·문서 기준 경로와 수신 주소를 정하는 지시어

---

# PART 2 · Request Handling

## 4. Virtual Hosts

- [ ] Name-based Virtual Host / 같은 IP·포트를 도메인 이름으로 나누는 방식
- [ ] IP-based Virtual Host / IP나 포트 자체를 사이트별로 다르게 쓰는 방식
- [ ] Default VirtualHost Precedence / 매칭되는 호스트가 없을 때 쓰는 우선순위
- [ ] ServerName and ServerAlias / 대표 도메인과 별칭 도메인을 지정하는 방식
- [ ] Per-Host Log and DocumentRoot Separation / 가상호스트마다 로그·문서 경로를 분리
- [ ] Port-Based Separation / 80·443처럼 포트로 사이트를 나누는 방식

## 5. Request Mapping

- [ ] Directory Directives / Options·AllowOverride로 디렉터리 권한을 제어
- [ ] Alias and ScriptAlias / URL 경로를 실제 파일·실행 경로로 매핑
- [ ] DirectoryIndex / 경로만 요청됐을 때 보여줄 기본 파일 지정
- [ ] Files and FilesMatch / 파일 이름·패턴 단위로 접근을 제어하는 블록
- [ ] .htaccess / 디렉터리마다 얹지만 요청마다 훑는 비용이 붙음
- [ ] MIME Type / AddType·AddEncoding으로 응답 타입을 지정
- [ ] ErrorDocument / 404·500 같은 오류에 보여줄 페이지 지정
- [ ] Content Negotiation / 언어·형식별 파일 중 하나를 골라 응답 `선택`

## 6. URL Rewriting

- [ ] mod_alias Redirect and RedirectMatch / 문자열·정규식으로 리다이렉트
- [ ] Enabling mod_rewrite / RewriteEngine 지시어로 재작성 기능을 켬
- [ ] RewriteRule, Flag, L, R, P, QSA / 규칙과 매치 후 동작을 정하는 플래그
- [ ] RewriteCond / RewriteRule 앞에 붙는 조건 검사 지시어
- [ ] RewriteBase / 상대 경로 재작성의 기준 디렉터리를 지정
- [ ] Rewrite Log Debugging / LogLevel rewrite:trace로 규칙 매칭을 추적
- [ ] Front Controller Pattern / 모든 요청을 진입점 파일 하나로 몰아주는 패턴

## 7. Logging

- [ ] Access Log / LogFormat·CustomLog로 접근 기록 형식을 정의
- [ ] Combined vs Common Format / 남기는 필드 개수로 갈리는 로그 형식
- [ ] Error Log / LogLevel로 남길 오류의 심각도를 조절
- [ ] Conditional Logging / SetEnvIf로 특정 요청만 골라 기록·제외
- [ ] Real IP Restoration / 프록시 뒤에서 원본 접속 IP를 복원
- [ ] Rotation / rotatelogs·logrotate로 로그 파일을 주기적으로 교체
- [ ] Status Code Based Troubleshooting / 응답 코드별로 원인을 좁혀가는 방법

---

# PART 3 · Execution Model and Applications

## 8. MPM and Process Model

- [ ] MPM Concept / prefork·worker·event로 갈아끼우는 처리 모델
- [ ] prefork / 요청마다 프로세스 하나를 물리는 MPM
- [ ] worker / 프로세스 안에 스레드를 섞어 쓰는 MPM
- [ ] event / 연결 유지를 별도 스레드로 넘겨 처리하는 MPM `추천`
- [ ] MPM Tuning / 동시 접속 규모에 맞춰 워커 수를 조절
- [ ] MaxConnectionsPerChild / 자식 프로세스를 주기적으로 재시작해 누수 방지
- [ ] KeepAlive and KeepAliveTimeout / 연결을 유지할지와 얼마나 유지할지 설정

## 9. Dynamic Content

- [ ] CGI / mod_cgi·mod_cgid로 외부 프로그램을 실행해 응답 생성

### PHP Integration `택 1`

- [ ] mod_php / PHP 런타임을 서버 프로세스 안에 얹는 방식
- [ ] PHP-FPM + mod_proxy_fcgi / PHP를 별도 프로세스로 떼어내 프록시로 연결 `추천`

### Other Runtimes

- [ ] mod_wsgi / Python 애플리케이션을 서버 프로세스에 얹는 모듈
- [ ] mod_passenger / Ruby 애플리케이션을 자동으로 띄우고 관리 `선택`
- [ ] Application Server Proxy Delegation / 실행을 서버 밖 애플리케이션 서버로 넘기는 방식

## 10. Proxy and Load Balancing

- [ ] mod_proxy / ProxyPass로 요청을 다른 서버로 넘기는 모듈
- [ ] Proxy Header Handling / 원본 호스트·클라이언트 정보를 헤더로 전달
- [ ] mod_proxy_balancer / 여러 백엔드를 묶어 분산 대상으로 등록
- [ ] Balancing Algorithms / 요청 수·트래픽량·부하로 분산 기준을 정함
- [ ] Sticky Session / 같은 클라이언트를 같은 백엔드로 계속 보내는 설정
- [ ] Health Check / 죽은 백엔드를 감지해 분산 대상에서 제외
- [ ] Balancer Manager UI / 분산 상태를 웹 화면에서 보고 조정하는 도구
- [ ] WebSocket / mod_proxy_wstunnel로 연결을 유지한 채 중계

## 11. Caching and Compression

- [ ] mod_cache / 응답을 저장해 재사용하는 캐시 모듈
- [ ] mod_cache_disk and mod_cache_socache / 캐시를 디스크·공유메모리 중 어디에 둘지
- [ ] Cache Invalidation / 오래되거나 틀린 캐시를 지우는 방법
- [ ] mod_deflate / 응답 본문을 gzip으로 압축해 전송량 절감
- [ ] mod_brotli / gzip보다 압축률 높은 방식으로 응답 압축 `선택`
- [ ] mod_expires / 브라우저 캐시 유효기간을 헤더로 지정
- [ ] mod_headers / 응답에 임의의 HTTP 헤더를 추가·수정·삭제

---

# PART 4 · Security

## 12. Authentication and Authorization

- [ ] Authentication Methods / 기본 인증과 다이제스트 인증 중 고르는 방식
- [ ] Provider / 계정 정보를 파일·DB·LDAP 중 어디서 조회할지
- [ ] htpasswd / 기본 인증용 계정·비밀번호 파일을 만드는 도구
- [ ] Require Directive / 사용자·그룹·IP 단위로 접근을 허용하는 조건
- [ ] RequireAll, RequireAny, RequireNone / 여러 Require 조건을 묶는 논리 연산
- [ ] Order and Allow Syntax Difference / 2.2의 옛 접근 제어 문법과의 차이

## 13. TLS

- [ ] Enabling mod_ssl / TLS 처리를 위한 모듈을 적재하는 절차
- [ ] Certificate Configuration / 인증서와 개인키 파일 경로를 지정
- [ ] Protocol and Cipher / 허용할 TLS 버전과 암호 스위트를 제한
- [ ] SNI / IP 하나로 도메인마다 다른 인증서를 제공
- [ ] HTTP to HTTPS Redirect / 평문 요청을 암호화 연결로 강제 전환
- [ ] HSTS Header / 브라우저에 항상 HTTPS로만 접속하라고 지시
- [ ] OCSP Stapling / 인증서 폐지 여부를 서버가 미리 첨부해 응답
- [ ] Let's Encrypt / certbot·mod_md로 인증서를 자동 발급·갱신
- [ ] Client Certificate / 클라이언트 인증서로 접속자를 확인하는 방식

## 14. Hardening

- [ ] Information Disclosure Reduction / 버전·서명 노출을 응답에서 숨김
- [ ] TRACE Blocking / TRACE 메서드를 막아 정보 유출 경로를 차단
- [ ] Options Minimization / 디렉터리 목록·심볼릭 링크 허용을 최소화
- [ ] Deny-by-Default Directory Policy / 기본은 막고 필요한 경로만 여는 정책
- [ ] Request Limits / 요청 본문 크기·필드 수 상한을 지정
- [ ] Timeout / 느린 요청을 끊어 연결 고갈 공격을 방지
- [ ] mod_evasive / 짧은 시간 과도한 요청을 감지해 차단 `선택`
- [ ] ModSecurity WAF / 규칙 기반으로 악성 요청을 걸러내는 방화벽 `선택`
- [ ] Security Headers / CSP·X-Frame-Options로 브라우저 방어를 지시

---

# PART 5 · Operations

## 15. Performance and Monitoring

- [ ] mod_status / 워커·연결 현황을 웹 페이지로 확인
- [ ] Scoreboard Interpretation / 워커별 상태 문자를 읽어 상황을 진단
- [ ] EnableSendfile and EnableMMAP / 파일 전송을 커널에 맡길지 정하는 설정
- [ ] HTTP/2 / mod_http2로 다중화·헤더 압축을 지원하는 프로토콜
- [ ] Resource Limits / 프로세스별 메모리·파일 디스크립터 상한 설정
- [ ] Metrics Collection / apache_exporter로 지표를 Prometheus에 노출
- [ ] Benchmarking / ab·wrk로 부하를 걸어 처리량을 측정

## 16. Operations and Migration

- [ ] Zero-Downtime Reload / 연결을 끊지 않고 설정만 다시 읽는 재시작
- [ ] Configuration Rollback / 설정을 이전 버전으로 되돌리는 절차
- [ ] Common Errors / 403·500과 권한·SELinux 컨텍스트 문제
- [ ] Debug Logging / LogLevel을 debug·trace로 올려 원인 추적
- [ ] Version Upgrade / 2.2에서 2.4로 갈 때 바뀐 설정 문법
- [ ] Nginx Frontend Placement / 앞단에 Nginx를 두고 httpd를 백엔드로 배치
- [ ] Container Deployment / 설정 파일을 컨테이너에 마운트해 배포

---

# 이 로드맵 밖

- Nginx `software/skill-based/Infra-DevOps/nginx.md`
- Caddy `software/skill-based/Infra-DevOps/caddy.md`
- 리눅스 `software/skill-based/Infra-DevOps/linux.md`
- PHP `software/skill-based/Languages/php.md`
- WordPress 호스팅 `software/skill-based/Frameworks/wordpress.md`
- 데브옵스 전반 `software/role-based/devops.md`
