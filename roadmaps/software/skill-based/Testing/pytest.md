# pytest `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to pytest

## 1. What is pytest?

### Overview / What is it?

- [ ] Testing Framework for Python / 함수 단위로 짜는 파이썬 테스트 도구
- [ ] unittest vs pytest / 클래스 상속 대신 함수로 테스트를 쓰는 차이
- [ ] Plain assert Based Design / 전용 API 없이 assert 하나로 검증하는 설계
- [ ] Fixture-Based Dependency Injection / 인자 이름으로 의존성을 주입받는 방식

### Testing Fundamentals

- [ ] Unit vs Integration vs E2E / 테스트 범위가 커지는 세 단계 구분
- [ ] Test Pyramid / 단위 테스트를 가장 많이 쌓는 비율 모델
- [ ] Arrange-Act-Assert / 준비·실행·검증 순서로 짜는 구조
- [ ] TDD Cycle / 테스트를 먼저 쓰고 통과시킨 뒤 다듬는 순서

## 2. Getting Started

### Installation

- [ ] pip and uv install / pip이나 uv로 패키지를 받는 설치 방법
- [ ] Virtual Environment / 프로젝트별로 패키지를 격리하는 환경
- [ ] Editable Install / src 배치에서 소스를 바로 참조하게 까는 방법

### Running

- [ ] pytest CLI / pytest 명령으로 테스트를 실행하는 도구
- [ ] Test Discovery Rules / test_*.py 파일명 규칙으로 자동 인식하는 방식
- [ ] Node ID / 파일::클래스::함수로 테스트 하나를 가리키는 표기
- [ ] Verbosity / -v로 자세히, -q로 간략히 출력하는 옵션
- [ ] Fail Fast / -x·--maxfail로 실패 즉시 중단하는 옵션
- [ ] Rerun Options / --lf로 실패한 것만, --ff로 실패부터 재실행

## 3. First Test

- [ ] Writing a Test Function / test_로 시작하는 평범한 함수 작성법
- [ ] tests/ Directory Layout / 테스트 코드를 모아두는 디렉터리 구조
- [ ] Role of conftest.py / 여러 파일이 공유할 fixture를 두는 곳
- [ ] Assertion Rewriting / assert 실패 시 값을 자동 분해해 보여주는 기능
- [ ] Naming Conventions / test_ 접두사로 파일과 함수를 맞추는 규칙

---

# PART 2 · Core Features

## 4. Assertions

- [ ] Plain assert / 별도 메서드 없이 assert 키워드만 쓰는 검증
- [ ] Exception Assertion / pytest.raises로 예외 발생과 메시지를 검증
- [ ] Warning Assertion / pytest.warns로 경고 발생 여부를 검증
- [ ] Float Comparison / pytest.approx로 부동소수점 오차를 허용 비교
- [ ] Custom Assertion Message / assert 뒤에 실패 메시지를 직접 붙이는 방법
- [ ] Designing Clear Failure Messages / 실패 원인을 바로 알 수 있게 쓰는 요령

## 5. Fixtures

### Basics

- [ ] @pytest.fixture / 함수를 재사용 가능한 준비 로직으로 등록
- [ ] Argument Injection / 테스트 함수 인자 이름으로 fixture를 받는 방식
- [ ] Setup and Teardown with yield / yield 앞뒤로 준비와 정리를 나누는 방법
- [ ] Fixture Scope / function·class·module·session으로 나누는 수명 범위

### Advanced

- [ ] conftest.py Hierarchy / 상위 디렉터리 conftest가 하위로 상속되는 구조
- [ ] autouse Fixture / 호출 안 해도 자동으로 실행되는 fixture
- [ ] Fixture Composition / fixture가 다른 fixture를 인자로 받아 조합
- [ ] Parametrized Fixture / params로 값을, ids로 이름을 지정하는 fixture
- [ ] request Object / request.param으로 현재 파라미터 값을 꺼내는 객체
- [ ] Factory as Fixture / 호출할 때마다 새 객체를 만드는 함수를 반환
- [ ] Built-in Fixtures / tmp_path·capsys 등 pytest가 기본 제공하는 fixture
- [ ] Finalization / addfinalizer로 정리 함수를 직접 등록하는 방법
- [ ] Inspecting Execution Order / --setup-show로 fixture 실행 순서 확인

## 6. Parametrize

- [ ] @pytest.mark.parametrize / 같은 테스트를 여러 입력값으로 반복 실행
- [ ] Multiple Arguments / 인자를 여러 개 나열하거나 데코레이터를 쌓아 조합
- [ ] Test ID Customization / ids 인자로 케이스별 표시 이름을 지정
- [ ] Indirect Parametrization / 값을 fixture에 넘겨 가공한 뒤 쓰는 방식
- [ ] pytest_generate_tests Hook / 생성 시점에 파라미터를 동적으로 넣는 훅

## 7. Markers / Selection

- [ ] Registering Custom Markers / 새 마커를 ini 파일에 등록하는 절차
- [ ] Marker Expression / -m 옵션으로 마커 조건에 맞는 테스트만 실행
- [ ] skip and skipif / 무조건 건너뛰거나 조건부로 건너뛰는 마커
- [ ] xfail / strict 옵션으로 예상 실패가 성공하면 오류 처리하는 마커
- [ ] Keyword Selection / -k 옵션으로 이름에 키워드가 맞는 테스트만 선택
- [ ] Random Order / pytest-randomly로 실행 순서를 무작위로 섞는 방법 `선택`

---

# PART 3 · Test Doubles and External Dependencies

## 8. Mocking

- [ ] Test Double Types / Dummy·Stub·Spy·Fake·Mock으로 나뉘는 대역 종류
- [ ] unittest.mock / Mock과 MagicMock을 제공하는 표준 라이브러리
- [ ] patch / patch.object로 특정 위치의 객체를 교체하는 방법
- [ ] return_value and side_effect / 고정값을 주거나 호출마다 동작을 바꾸는 설정
- [ ] Call Assertion / assert_called_with로 호출 인자를 검증하는 방법
- [ ] autospec / create_autospec 함수로 원본 시그니처를 강제하는 방법
- [ ] pytest-mock / mocker fixture로 자동 정리되는 mock을 제공하는 플러그인
- [ ] monkeypatch / setattr·setenv·chdir로 값을 임시로 바꾸는 fixture
- [ ] Mocking Overuse Warning / 과도한 mock이 실제 동작 검증을 놓치는 위험

## 9. External Systems

- [ ] HTTP Mocking / responses·respx 등으로 외부 API 호출을 대체
- [ ] Cassette-Based Replay / pytest-recording으로 응답을 녹화해 재생 `선택`
- [ ] Database / 트랜잭션 롤백이나 인메모리 SQLite로 격리하는 방법
- [ ] Testcontainers / 실제 DB를 컨테이너로 띄워 테스트하는 도구
- [ ] Filesystem / tmp_path나 pyfakefs로 파일 접근을 격리하는 방법
- [ ] Time Control / freezegun 등으로 현재 시각을 고정하는 방법
- [ ] Fixing the Random Seed / 난수를 고정해 결과를 재현 가능하게 만드는 방법

## 10. Async and Web Frameworks

- [ ] pytest-asyncio / async def 테스트를 이벤트 루프로 실행
- [ ] anyio Plugin / asyncio와 trio를 함께 지원하는 비동기 테스트 플러그인
- [ ] FastAPI / TestClient나 httpx로 엔드포인트를 호출해 검증
- [ ] Django / pytest-django의 db fixture로 DB 접근을 테스트
- [ ] Flask / Test Client와 App fixture로 요청을 시뮬레이션

---

# PART 4 · Extension and Advanced Topics

## 11. Plugin Usage

- [ ] Plugin Discovery / --trace-config로 로드된 플러그인을 확인
- [ ] pytest-cov / coverage.py를 pytest에 붙이는 플러그인
- [ ] pytest-xdist / -n auto로 CPU 코어 수만큼 병렬 실행
- [ ] pytest-timeout / 테스트별 실행 시간 제한을 거는 플러그인
- [ ] pytest-benchmark / 함수 실행 시간을 반복 측정하는 플러그인 `선택`
- [ ] pytest-html and pytest-sugar / 결과를 HTML로 남기거나 보기 좋게 꾸미는 플러그인 `선택`

## 12. Custom Plugin / Hooks

- [ ] Hook System / pluggy가 제공하는 플러그인 훅 등록 구조
- [ ] pytest_collection_modifyitems / 수집된 테스트 목록을 실행 전에 가공
- [ ] pytest_runtest_setup and pytest_runtest_makereport / 실행 전후에 개입하는 훅
- [ ] pytest_addoption / 커스텀 CLI 옵션을 새로 정의하는 훅
- [ ] Local Plugin vs Distributed Plugin / conftest에 두는지 패키지로 배포하는지 차이

## 13. Advanced Testing Techniques

- [ ] Property-based Testing / Hypothesis가 입력값을 자동 생성해 검증
- [ ] Snapshot Testing / syrupy로 이전 출력과 비교해 회귀를 잡는 방식
- [ ] Mutation Testing / 코드를 일부러 망가뜨려 테스트 품질을 측정
- [ ] API Schema Testing / schemathesis로 스키마 기반 입력을 자동 검증 `선택`
- [ ] Doctest Integration / --doctest-modules로 docstring 예제를 테스트로 실행
- [ ] Flaky Test Root Cause Analysis / 간헐적으로 실패하는 원인을 추적

---

# PART 5 · Configuration and Operations

## 14. Configuration

- [ ] pyproject.toml, pytest.ini, setup.cfg / 설정을 셋 중 한 파일에 모아두는 방법
- [ ] addopts and testpaths / 기본 옵션과 탐색 경로를 설정 파일에 고정
- [ ] Import Mode / importlib로 이름 충돌 없이 테스트를 임포트
- [ ] rootdir / 설정 파일 위치로 기준 디렉터리를 정하는 방식
- [ ] Logging and Warning Filter / 로그 캡처와 경고 필터링을 설정하는 옵션
- [ ] Matrix Execution / tox나 nox로 여러 파이썬 버전에서 실행 `선택`

## 15. Coverage

- [ ] How coverage.py Works / 실행된 코드 라인을 추적해 기록하는 원리
- [ ] Line vs Branch Coverage / 줄 실행 여부와 분기 경로까지 재는 차이
- [ ] Report / term-missing·HTML·XML로 결과를 출력하는 형식
- [ ] omit and exclude_lines / 특정 파일과 줄을 집계에서 제외하는 설정
- [ ] Coverage Target Trap / 수치만 높이려다 의미 없는 테스트를 채우는 함정

## 16. CI Integration

- [ ] GitHub Actions Matrix / 여러 파이썬 버전을 동시에 돌리는 CI 설정
- [ ] Marker-Based Split Execution / 마커로 나눠 여러 잡에서 분산 실행
- [ ] JUnit XML Report Collection / --junitxml로 CI가 읽는 결과 파일 생성
- [ ] Parallel / Sharding으로 테스트를 여러 워커에 나눠 실행하는 방식
- [ ] Retry Strategy / pytest-rerunfailures로 실패한 테스트를 자동 재시도
- [ ] Runtime Management / --durations로 느린 테스트 상위 목록을 확인

---

# 이 로드맵 밖

- QA 전반 `software/role-based/qa.md`
- Python `software/skill-based/Languages/python.md`
- Django `software/skill-based/Frameworks/django.md`
- 백엔드 전반 `software/role-based/backend.md`
- 데이터 분석 `software/skill-based/Data-DB/python-data-analysis.md`
- CI 파이프라인 `software/role-based/devops.md`
