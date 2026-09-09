# Flask `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Flask

## 1. What is Flask?

### Overview of Flask / What is it?

- [ ] Microframework Philosophy / 라우팅과 템플릿만 코어에 남긴 설계
- [ ] WSGI Application / 요청 하나를 함수 호출로 받는 동기 규약
- [ ] Werkzeug and Jinja2 / 요청 처리와 템플릿을 맡는 두 하위 라이브러리
- [ ] Batteries Not Included / DB·로그인을 확장으로 골라 붙이는 방침

### Flask vs Others

- [ ] Flask vs Django / 직접 조립과 정해진 규약의 차이
- [ ] Flask vs FastAPI / 동기 WSGI와 비동기 ASGI의 갈림
- [ ] When to choose Flask? / Flask를 고를 만한 프로젝트 조건

## 2. Getting Started

### Installation and Running

- [ ] Virtual Environment / venv·uv로 프로젝트마다 패키지를 가르는 방법
- [ ] pip install flask / 코어 패키지 하나만 받아 시작하는 설치
- [ ] Application Object / 모듈 이름을 넘겨 정적·템플릿 경로를 잡는 객체
- [ ] flask run / 환경변수로 앱 위치를 알려 띄우는 명령
- [ ] Development Server vs Production Server / 내장 서버를 실서비스에 쓰면 안 되는 이유

### Debug Mode

- [ ] Auto Reloader / 소스가 바뀌면 프로세스를 다시 띄우는 기능
- [ ] Werkzeug Debugger / PIN으로 잠가 두는 브라우저 예외 콘솔

---

# PART 2 · Requests and Responses

## 3. Routing

- [ ] Route Registration / 데코레이터와 add_url_rule 두 가지 등록 방법
- [ ] HTTP Methods / 한 URL이 받을 메서드를 목록으로 지정하는 인자
- [ ] Variable Rules / URL 조각을 int·path 같은 형으로 받는 규칙
- [ ] Custom URL Converter / 직접 만든 변환기를 URL 규칙에 등록하는 방법
- [ ] url_for / 엔드포인트 이름으로 URL을 거꾸로 만드는 방법
- [ ] Redirect & Trailing Slash Rules / 끝 슬래시 유무에 따라 넘겨 주는 규칙
- [ ] Static Route / static 폴더를 자동으로 열어 주는 기본 경로

## 4. Request & Response

### Request Object

- [ ] Request Context / 요청마다 다른 객체를 전역 이름으로 가리키는 구조
- [ ] Query String / 주소 뒤 물음표 값을 읽는 딕셔너리
- [ ] Form Data / 본문의 폼 필드를 읽는 딕셔너리
- [ ] JSON Body / 본문을 JSON으로 파싱해 받는 방법
- [ ] File Upload / 올라온 파일 객체를 받는 자리
- [ ] Headers & Cookies / 요청에 실려 온 헤더와 쿠키를 읽는 방법

### Response

- [ ] Return Types / 문자열·딕셔너리·튜플을 응답으로 바꾸는 규칙
- [ ] make_response / 상태 코드와 헤더를 손대려 응답을 감싸는 함수
- [ ] jsonify / 딕셔너리를 JSON 응답으로 바꿔 주는 함수
- [ ] redirect and abort / 다른 주소로 넘기거나 오류로 끊는 함수
- [ ] Cookie Configuration / 만료·경로·Secure를 정해 쿠키를 심는 방법
- [ ] File & Stream / 파일을 응답 본문으로 흘려보내는 함수

## 5. Templates

- [ ] render_template and render_template_string / 템플릿 파일과 문자열을 각각 그리는 함수
- [ ] Jinja2 Syntax / 이중 중괄호 표현식과 블록 제어 구문
- [ ] Template Inheritance / 부모 틀을 물려받아 블록만 갈아 끼우는 방법
- [ ] include and macro / 템플릿 조각을 재사용하는 두 수단
- [ ] Filters & Custom Filters / 파이프로 값을 가공하는 함수를 등록하는 방법
- [ ] Context Processors / 모든 템플릿에 변수를 자동으로 넣는 함수
- [ ] Autoescaping / HTML 태그가 그대로 나가지 못하게 막는 규칙

## 6. Forms & Validation

- [ ] HTML Form Handling / 폼 제출을 GET과 POST로 나눠 받는 방법
- [ ] Flask-WTF / WTForms를 Flask에 붙여 주는 확장 `추천`
- [ ] WTForms Validators / 입력값 조건을 필드마다 붙여 검사하는 규칙
- [ ] CSRF Protection / 남의 사이트에서 온 폼 제출을 토큰으로 막는 방법
- [ ] Upload Validation / 올라온 파일 이름을 안전한 형태로 바꾸는 방법

---

# PART 3 · Data and Authentication

## 7. Databases

### ORM Selection `택 1`

- [ ] Flask-SQLAlchemy / 세션 수명을 앱에 묶어 주는 SQLAlchemy 확장 `추천`
- [ ] SQLAlchemy Core / 확장 없이 세션을 직접 열고 닫는 방식
- [ ] Peewee / 모델 선언이 가벼운 소형 ORM
- [ ] Raw DB-API / ORM 없이 커서로 SQL을 직접 던지는 방식

### Models and Migrations

- [ ] Model Definition / 테이블을 파이썬 클래스로 선언하는 방법
- [ ] Relationship / 외래키를 객체 참조로 이어 주는 선언
- [ ] Flask-Migrate / Alembic으로 스키마 변경분을 파일로 남기는 확장
- [ ] Session Lifecycle / 세션을 요청 하나 동안만 살리는 수명 규칙

## 8. Sessions & Authentication

- [ ] Signed Cookie Session / 세션 값을 서버가 아닌 서명된 쿠키에 담는 방식
- [ ] Server-side Session / 세션 본문을 서버 저장소로 옮기는 확장 `선택`
- [ ] flash Messages / 다음 요청 한 번만 보여 줄 알림을 남기는 기능
- [ ] Password Hashing / 비밀번호를 해시로 저장하고 대조하는 함수
- [ ] Flask-Login / 로그인 상태와 접근 제한을 맡는 확장
- [ ] Token Auth / 쿠키 대신 서명 토큰으로 매 요청을 증명하는 방식 `선택`
- [ ] OAuth / 남의 계정으로 로그인시키는 위임 절차 `선택`

## 9. Building APIs

- [ ] JSON API Routing Patterns / 자원별 URL과 메서드를 짜는 배치 규칙
- [ ] MethodView / 메서드마다 클래스 함수를 나눠 붙이는 뷰
- [ ] Serialization / 모델 객체를 JSON 형태로 바꾸는 스키마
- [ ] Error Response Standardization / 오류 응답 본문 모양을 하나로 맞추는 방법
- [ ] CORS / 다른 출처 브라우저 요청을 허용하는 헤더 설정
- [ ] API Extension / 라우팅과 문서 생성을 묶어 주는 REST 확장 `선택`

---

# PART 4 · Application Structure

## 10. Application Structure

### Blueprints

- [ ] Blueprint Definition and Registration / 라우트 묶음을 따로 정의해 나중에 앱에 붙이는 단위
- [ ] url_prefix and subdomain / 블루프린트를 붙일 주소 위치를 정하는 인자
- [ ] Per-Blueprint Template and Static / 묶음마다 템플릿·정적 폴더를 따로 두는 방법

### Application Factory

- [ ] create_app Pattern / 앱을 함수 안에서 만들어 설정별로 찍어 내는 방식
- [ ] Extension Initialization / 확장을 먼저 만들고 앱에 나중에 묶는 순서
- [ ] Circular Import Avoidance / 모듈이 서로를 임포트해 막히는 것을 푸는 방법

## 11. Contexts & Hooks

- [ ] Application Context vs Request Context / 앱 단위 영역과 요청 단위 영역의 차이
- [ ] current_app and g / 현재 앱과 요청 임시 저장소를 가리키는 이름
- [ ] Context Local and Teardown / 영역이 끝날 때 붙은 자원을 정리하는 순서
- [ ] Request Hooks / 요청 앞뒤에 공통 처리를 끼우는 자리
- [ ] Signals / 정해진 시점에 알림을 받아 가는 구독 방식
- [ ] WSGI Middleware Insertion / Flask 밖 WSGI 층에 처리를 덧대는 방법

## 12. Configuration

- [ ] Config Object / 클래스나 파일에서 설정을 읽어 담는 자리
- [ ] Per-Environment Config Class / 개발·운영 설정을 클래스로 갈라 두는 방법
- [ ] .env Loading / 파일에 적은 값을 환경변수로 올리는 방법
- [ ] Secret Management / 키를 코드에 안 박고 밖에서 주입하는 방법
- [ ] Instance Folder / 저장소에 안 올리는 실행 환경 파일을 두는 폴더

---

# PART 5 · Quality and Deployment

## 13. Error Handling & Logging

- [ ] errorhandler / 상태 코드나 예외 종류별로 응답을 가로채는 등록
- [ ] Custom Error Page / 404·500에 직접 만든 화면을 붙이는 방법
- [ ] app.logger / 표준 logging 위에 얹힌 앱 전용 로거
- [ ] Error Reporting / 잡히지 않은 예외를 외부로 모아 보내는 연동 `선택`

## 14. Testing

- [ ] test_client / 서버를 안 띄우고 요청을 흉내 내는 객체
- [ ] pytest Fixture / 앱과 클라이언트를 테스트마다 새로 만드는 준비
- [ ] DB Isolation / 테스트마다 트랜잭션을 되돌려 DB를 비우는 방법
- [ ] CLI Command Testing / flask 명령으로 등록한 함수를 검증하는 방법

## 15. Performance & Background Work

- [ ] Caching / 계산 결과를 뷰 단위로 남겨 다시 쓰는 확장
- [ ] Background Task / 오래 걸리는 일을 별도 워커로 넘기는 방식
- [ ] Rate Limiting / IP·사용자별 요청 횟수를 제한하는 확장 `선택`
- [ ] async def View and Its Limits / 동기 WSGI 위에서 비동기 뷰가 못 하는 것

## 16. Deployment

### WSGI Server `택 1`

- [ ] Gunicorn / 프로세스를 여러 개 띄워 요청을 나누는 WSGI 서버 `추천`
- [ ] uWSGI / 설정 항목이 많고 오래된 WSGI 서버
- [ ] Waitress / 윈도우에서도 도는 순수 파이썬 WSGI 서버

### Operations

- [ ] Reverse Proxy / 정적 파일과 TLS를 앞단에서 처리하는 배치
- [ ] ProxyFix / 프록시가 붙인 헤더로 원래 주소를 되살리는 래퍼
- [ ] Worker Count and Concurrency Model / 워커와 스레드 수를 코어에 맞춰 잡는 기준
- [ ] Docker Image Build / 앱과 WSGI 서버를 한 이미지에 담는 방법
- [ ] Health Check & Graceful Shutdown / 배포 교체 때 요청이 끊기지 않게 하는 장치

---

# 이 로드맵 밖

- Python `software/skill-based/Languages/python.md`
- 백엔드 전반 `software/role-based/backend.md`
- Django `software/skill-based/Frameworks/django.md`
- FastAPI `software/skill-based/Frameworks/fastapi.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
- 테스트 · 배포 `software/skill-based/Testing/pytest.md`, `software/skill-based/Infra-DevOps/docker.md`
