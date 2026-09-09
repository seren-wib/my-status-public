# FastAPI `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to FastAPI

## 1. What is FastAPI?

### Overview of FastAPI / What is it?

- [ ] ASGI Framework / 요청을 비동기로 받는 파이썬 서버 규격
- [ ] Starlette + Pydantic Composition / 웹 계층과 검증 계층을 붙여 만든 구성
- [ ] Type Hint Based Validation / 함수 인자에 적은 타입으로 입력을 검사하는 방식
- [ ] Automatic OpenAPI Documentation Generation / 타입에서 뽑아낸 명세로 문서가 저절로 생기는 기능

### FastAPI vs Others

- [ ] FastAPI vs Flask / WSGI 동기 처리와 ASGI 비동기 처리의 차이
- [ ] FastAPI vs Django REST Framework / 다 갖춘 틀과 필요한 것만 고르는 틀의 차이
- [ ] When to choose FastAPI? / 다른 프레임워크 대신 이걸 고를 기준

## 2. Getting Started

- [ ] pip install fastapi and uvicorn / 프레임워크와 실행 서버를 따로 설치하는 이유
- [ ] FastAPI Instance Creation / 앱 객체를 만들어 라우트를 매다는 시작점
- [ ] fastapi dev and uvicorn --reload / 코드를 고치면 서버가 다시 뜨는 개발 실행
- [ ] First Path Operation / 데코레이터 하나로 경로와 함수를 잇는 방법
- [ ] Auto Documentation Check / 서버를 띄우면 /docs·/redoc에 문서가 붙는 확인

---

# PART 2 · Request and Response Contracts

## 3. Routing & Path Operations

- [ ] Path Operation Decorators / @app.get·post·put·delete로 메서드를 정하는 선언
- [ ] Path Matching Order Priority / 먼저 선언한 경로가 먼저 잡히는 규칙
- [ ] APIRouter / 라우트 묶음에 공통 prefix와 tags를 다는 도구
- [ ] include_router / 나눠 짠 라우터를 앱에 붙이는 호출
- [ ] Status Code Specification / status_code로 성공 응답 코드를 정하는 방법
- [ ] Route Metadata / summary·deprecated로 문서에 실릴 설명을 다는 방법

## 4. Parameters & Request Body

- [ ] Path Parameters / 주소 조각을 선언한 타입으로 바꿔 받는 방법
- [ ] Query Parameters / 물음표 뒤 값에 기본값과 선택 여부를 주는 방법
- [ ] Request Body / 본문 JSON을 모델 객체로 받아내는 방법
- [ ] Validation Metadata / Query·Path·Field로 길이·범위 조건을 다는 방법
- [ ] Header & Cookie Parameters / 헤더와 쿠키 값을 함수 인자로 받는 선언
- [ ] Form Data / 폼 전송을 받으려 python-multipart를 까는 방법
- [ ] File Upload / 올린 파일을 메모리 대신 임시 파일로 받는 방법
- [ ] Annotated Style / 기본값 자리를 비우고 타입 쪽에 조건을 붙이는 문법 `추천`

## 5. Pydantic Models

- [ ] BaseModel / 타입만 적으면 검증과 변환을 대신해 주는 기반 클래스
- [ ] Nested Model & Collection / 모델 안에 모델·리스트를 겹쳐 넣는 구조
- [ ] Validator / 타입만으로 안 되는 조건을 함수로 검사하는 방법
- [ ] Model Config / 바깥 JSON 키 이름을 필드에 따로 맞추는 설정
- [ ] Pydantic v1 vs v2 Differences / 검증기 문법과 속도가 갈라진 지점
- [ ] Environment Configuration With pydantic-settings / 환경변수를 모델로 읽어 검증까지 하는 방법

## 6. Response

- [ ] response_model / 응답에 나갈 필드를 입력과 따로 정하는 선언
- [ ] Response Field Control / 안 채운 필드를 응답에서 빼는 옵션
- [ ] Response Class / JSON 말고 HTML·평문으로 돌려주는 응답 종류
- [ ] Streaming & File / 큰 파일을 통째로 안 올리고 흘려보내는 응답
- [ ] jsonable_encoder / 모델·날짜를 JSON에 넣을 형태로 바꾸는 함수
- [ ] Direct Status Code and Header Control / 응답 객체를 받아 코드와 헤더를 직접 쓰는 방법

## 7. Error Handling

- [ ] HTTPException / 오류 응답을 예외 던지기로 만드는 방법
- [ ] RequestValidationError / 검증 실패를 422 본문으로 자동 내보내는 형식
- [ ] Exception Handler Registration / 예외 종류마다 응답 만드는 함수를 거는 방법
- [ ] Custom Error Schema Unification / 오류 응답 모양을 앱 전체에서 하나로 맞추는 방법

---

# PART 3 · Dependencies and Data

## 8. Dependency Injection

- [ ] Depends Basics / 함수가 필요한 것을 인자로 선언해 받는 구조
- [ ] Sub-Dependencies Chain / 의존성이 또 다른 의존성을 부르는 사슬
- [ ] yield Dependency / 응답을 보낸 뒤 뒷정리를 돌리는 방식
- [ ] Class as Dependency / 클래스 자체를 의존성으로 걸어 상태를 담는 방법
- [ ] Router · App Level dependencies= / 라우터나 앱 전체에 공통 의존성을 거는 방법
- [ ] Dependency Caching / 같은 요청 안에서 결과를 한 번만 푸는 규칙
- [ ] dependency_overrides / 테스트에서 의존성을 가짜로 바꿔 끼우는 방법

## 9. Databases

### ORM / Driver `택 1`

- [ ] SQLAlchemy 2.0 / 동기와 비동기 세션을 다 지원하는 파이썬 ORM `추천`
- [ ] SQLModel / 모델 하나로 테이블과 검증을 겸하는 라이브러리
- [ ] Tortoise ORM / 처음부터 비동기로 만들어진 장고식 ORM
- [ ] Motor and Beanie / 몽고DB에 비동기로 붙는 드라이버와 문서 매퍼 `선택`

### Integration Patterns

- [ ] Session Dependency Pattern / DB 세션을 요청마다 열고 닫는 의존성 구성
- [ ] Sync ORM Threadpool Delegation vs Async Driver / 동기 ORM을 스레드로 넘길지 비동기 드라이버를 쓸지 선택
- [ ] Alembic Migration / 모델 변경을 스키마 변경 스크립트로 남기는 도구
- [ ] ORM Model and Pydantic Schema Separation / 테이블 모델과 응답 모델을 따로 두는 이유

## 10. Authentication & Security

- [ ] Security Dependency / 인증을 의존성으로 걸어 문서에도 드러내는 방법
- [ ] OAuth2PasswordBearer / 아이디·비밀번호를 토큰으로 바꿔 주는 흐름
- [ ] JWT Issuance and Verification / 서명한 토큰을 발급하고 만료를 확인하는 방법
- [ ] Password Hashing / 비밀번호를 되돌릴 수 없게 저장하는 방법
- [ ] API Key & Bearer / 헤더에 담긴 키를 읽어 인증하는 방식
- [ ] Scope-Based Permissions / 토큰에 적힌 권한 목록으로 접근을 나누는 방법
- [ ] CORS Middleware / 다른 도메인 브라우저 요청을 허용하는 설정

---

# PART 4 · Async and Structure

## 11. Async Concurrency

- [ ] async def vs def Path Operation / 하나는 이벤트 루프에서 하나는 스레드에서 도는 차이
- [ ] Threadpool Delegation Rules / 동기 함수를 별도 스레드로 넘기는 기준
- [ ] Blocking I/O Avoidance / 블로킹 호출 하나가 전체 요청을 멈추는 이유
- [ ] Async Client / requests 대신 비동기로 바깥을 부르는 도구
- [ ] Concurrency Control / 여러 호출을 동시에 띄우되 개수를 묶는 방법

## 12. Background Work & Realtime

- [ ] BackgroundTasks / 응답을 보낸 뒤 같은 프로세스에서 마저 도는 일
- [ ] External Task Queue / 오래 걸리는 일을 다른 프로세스로 넘기는 구조
- [ ] WebSocket / 연결을 열어 둔 채 양쪽이 주고받는 통신
- [ ] Server-Sent Events / 서버가 한 방향으로 계속 밀어 보내는 방식
- [ ] Lifespan Event / 앱이 뜨고 질 때 한 번씩 도는 자리

## 13. Application Structure & Middleware

- [ ] Bigger Applications / 라우터·모델·의존성을 패키지로 쪼개는 배치
- [ ] Router Separation by Domain / 업무 단위로 라우터 파일을 나누는 기준
- [ ] Settings Injection / 설정 객체를 한 번만 만들어 돌려쓰는 방법
- [ ] HTTP Middleware Implementation / 모든 요청 앞뒤에 공통 처리를 끼우는 방법
- [ ] ASGI Middleware / 응답 압축·호스트 검사를 붙이는 기성 미들웨어
- [ ] Sub Application Mount / 다른 앱을 하위 경로에 통째로 매다는 방법

---

# PART 5 · Quality and Deployment

## 14. Testing

- [ ] TestClient / 서버를 안 띄우고 앱을 직접 호출하는 도구
- [ ] pytest Fixture Setup / 테스트마다 앱과 DB를 새로 세우는 준비
- [ ] Async Test / 비동기 함수를 테스트에서 돌리는 방법
- [ ] DB Isolation via Dependency Override / 의존성을 갈아 끼워 테스트 DB로 돌리는 방법

## 15. OpenAPI & Documentation

- [ ] Auto-Generated Schema / 라우트 선언에서 뽑혀 나오는 API 명세 파일
- [ ] App Metadata / 문서 제목·버전·태그 묶음을 정하는 설정
- [ ] Example & Schema Customization / 문서에 실릴 예시 값과 스키마를 손보는 방법
- [ ] Docs Exposure Control in Production / 운영에서 문서 주소를 닫거나 가리는 설정
- [ ] Client SDK Generation / 명세에서 호출 코드를 뽑아내는 방법 `선택`

## 16. Deployment & Operations

### ASGI Server `택 1`

- [ ] Uvicorn / uvloop로 도는 가장 흔한 ASGI 서버 `추천`
- [ ] Hypercorn / HTTP/2와 여러 워커 방식을 지원하는 ASGI 서버
- [ ] Granian / 러스트로 만들어 속도를 노린 ASGI 서버

### Operations

- [ ] Worker Scaling / 프로세스를 여러 개 띄워 CPU 코어를 다 쓰는 방법
- [ ] Reverse Proxy / 프록시 뒤에서 원래 주소와 프로토콜을 되찾는 설정
- [ ] Docker Image Build / 파이썬 런타임과 앱을 한 이미지로 묶는 방법
- [ ] Structured Logging / 로그를 JSON 한 줄로 남겨 검색하게 만드는 방법
- [ ] Health Check & Graceful Shutdown / 살아있음을 알리고 남은 요청을 마치고 끄는 방법
- [ ] Load Testing and Profiling / 초당 요청 수와 느린 구간을 재는 방법

---

# 이 로드맵 밖

- Python `software/skill-based/Languages/python.md`
- 백엔드 전반 `software/role-based/backend.md`
- Flask `software/skill-based/Frameworks/flask.md`
- Django `software/skill-based/Frameworks/django.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
- 테스트 · 배포 `software/skill-based/Testing/pytest.md`, `software/skill-based/Infra-DevOps/docker.md`
