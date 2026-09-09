# Symfony `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to Symfony

## 1. What is Symfony?

### Overview

- [ ] PHP Component-based Framework / 필요한 부품만 골라 얹는 PHP 프레임워크
- [ ] Symfony Components / 프레임워크 없이 따로 떼어 쓰는 부품 묶음
- [ ] Full-stack vs Microframework Setup / 전체를 깔지 부품만 쓸지 고르는 기준
- [ ] Differences from Laravel / 관례로 감추지 않고 배선을 드러내는 차이

### Architecture

- [ ] HttpKernel / 요청 객체 하나를 응답 객체 하나로 바꾸는 계약
- [ ] Front Controller / 모든 요청을 파일 하나로 모으는 진입 방식
- [ ] Kernel · Bundle · Container Triad / 앱을 이루는 세 축의 역할 분담

## 2. Setup and Project Structure

### Installation `택 1`

- [ ] Symfony CLI / 생성·로컬 서버·인증서를 겸하는 전용 도구 `추천`
- [ ] Composer create-project / 스켈레톤 패키지를 내려받아 시작하는 방법
- [ ] Docker-based Development Environment / PHP와 DB를 컨테이너로 묶어 띄우는 방식

### Structure

- [ ] Directory Layout / 코드·설정·템플릿·캐시를 나눠 두는 규약
- [ ] Flex · Recipe / 패키지를 깔 때 설정 파일까지 함께 놓는 장치
- [ ] composer.json · symfony.lock / 적용된 레시피 버전을 고정하는 파일
- [ ] Webapp Skeleton vs Minimal Skeleton / 풀스택 묶음과 최소 묶음을 가르는 기준
- [ ] Running the Local Server / 개발용 HTTPS 서버를 띄우는 명령

## 3. Routing

- [ ] Route Definition Formats / 라우트를 어디에 적을지 고르는 세 형식
- [ ] Path Parameter / URL 조각을 컨트롤러 인자로 받는 방법
- [ ] Requirements / 파라미터가 받을 값을 정규식으로 좁히는 규칙
- [ ] Matching Conditions / 경로 말고 메서드·호스트로도 거르는 조건
- [ ] Route Name / 이름으로 URL을 거꾸로 만들어 내는 방법
- [ ] Route Prefix / 클래스 단위로 하위 경로를 한꺼번에 미는 설정
- [ ] debug:router / 등록된 라우트와 매칭 결과를 확인하는 명령

## 4. Controllers and HTTP

- [ ] AbstractController / render·json 같은 단축 메서드를 얻는 상속 지점
- [ ] Request Object / 요청의 값들을 종류별로 담아 넘기는 객체
- [ ] Response Types / 본문 형태에 따라 골라 쓰는 응답 클래스
- [ ] Argument Resolver / 인자 타입을 보고 값을 만들어 넣는 장치
- [ ] DTO Binding / 요청 본문을 객체로 바로 받는 어트리뷰트
- [ ] Session · Flash Message / 다음 요청 한 번만 살아남는 메시지 저장
- [ ] Exception → HTTP Status Mapping / 던진 예외를 상태 코드로 바꾸는 규칙

---

# PART 2 · Container and Configuration

## 5. Service Container and DI

- [ ] Service Definition / 서비스를 설정 파일에 선언해 두는 조립대
- [ ] Autowiring / 타입힌트만 보고 의존성을 찾아 넣는 기능
- [ ] Autoconfigure / 구현한 인터페이스로 태그를 자동으로 다는 기능
- [ ] Constructor Injection First Principle / 의존성을 생성자로만 받게 하는 원칙
- [ ] Service Alias / 인터페이스 이름에 구현 하나를 지정하는 방법
- [ ] Named Argument / 스칼라 인자를 이름으로 짚어 넣는 설정
- [ ] Service Tag / 같은 역할의 서비스에 표를 붙여 모으는 방법
- [ ] Tagged Iterator / 같은 태그의 서비스 전부를 목록으로 받는 주입
- [ ] Service Locator / 필요할 때만 꺼내 쓰게 미루는 주입 방식
- [ ] Public vs Private Service / 컨테이너에서 직접 꺼낼 수 있는지 가르는 구분
- [ ] Container Diagnostics / 배선이 실제로 어떻게 됐는지 들여다보는 명령

## 6. Configuration

- [ ] Configuration Formats / 설정을 적는 세 가지 표기
- [ ] Parameter / 여러 설정에서 참조할 값에 이름을 붙이는 방법
- [ ] Environment / 환경마다 설정을 통째로 갈아 끼우는 구분
- [ ] .env Files / 여러 .env 파일이 서로를 덮는 순서
- [ ] Env Var Processor / 환경 변수 문자열을 타입으로 바꿔 읽는 문법
- [ ] Secrets Vault / 비밀값을 암호화해 저장소에 함께 두는 방법

## 7. Bundles

- [ ] Bundle Concept / 서비스와 설정을 통째로 앱에 꽂는 확장 단위
- [ ] bundles.php Registration / 환경별로 켤 번들을 나열하는 파일
- [ ] Common Bundles / 거의 모든 프로젝트에 깔리는 표준 번들
- [ ] Bundle Configuration / 번들이 받을 설정 스키마를 정의하는 클래스
- [ ] Custom Bundle Authoring / 내 기능을 남이 쓸 번들로 포장하는 방법 `선택`
- [ ] Bundle vs Plain Service / 그냥 서비스로 둘지 번들로 뺄지 가르는 기준

## 8. Events and Kernel

- [ ] EventDispatcher / 흐름 중간에 끼어들 지점을 여는 장치
- [ ] Kernel Event / 커널이 요청을 처리하며 거치는 이벤트 순서
- [ ] EventSubscriber vs EventListener / 구독 지점을 클래스가 정할지 설정이 정할지 차이
- [ ] Priority / 같은 이벤트에 붙은 리스너들의 실행 순서
- [ ] Full Request Lifecycle Trace / 요청이 커널을 통과하는 전 구간의 순서

---

# PART 3 · Data

## 9. Doctrine ORM Basics

- [ ] Entity Mapping / 엔티티가 DB를 모르게 두고 밖에서 대응시키는 방식
- [ ] EntityManager / 바뀐 객체를 모았다 flush 한 번에 반영하는 구조
- [ ] Repository / 엔티티별 조회 메서드를 모아 두는 클래스
- [ ] Association / 엔티티 사이 관계를 매핑으로 적는 방법
- [ ] Cascade · Orphan Removal / 부모를 저장·삭제할 때 자식까지 따라가는 설정
- [ ] Fetch Mode / 연관 객체를 언제 읽어올지 정하는 설정
- [ ] Doctrine Event · Lifecycle Callback / 저장·삭제 시점에 끼워 넣는 콜백

## 10. Doctrine in Practice

- [ ] DQL · Query Builder / 테이블이 아니라 엔티티를 대상으로 짜는 질의
- [ ] DBAL / ORM을 걷어내고 SQL을 직접 던지는 계층 `선택`
- [ ] Pagination / 연관이 걸린 결과를 쪽으로 끊어 세는 도구
- [ ] Migration / 매핑과 실제 스키마의 차이를 파일로 남기는 절차
- [ ] Fixtures / 개발·테스트용 초기 데이터를 코드로 심는 방법
- [ ] Transaction / 여러 변경을 한 트랜잭션으로 묶는 방법
- [ ] Custom Type / 값 객체를 컬럼 하나로 넣고 빼는 변환기

## 11. Forms and Validation

- [ ] FormType Class / 폼의 필드 구성을 클래스 하나로 적는 방식
- [ ] Field Type · Option Configuration / 필드마다 종류와 옵션을 지정하는 방법
- [ ] Data Mapping / 폼 값을 어떤 객체에 담을지 정하는 설정
- [ ] Submission Handling / 제출된 요청을 폼에 먹여 검사하는 순서
- [ ] Form Theme / 폼이 그려지는 마크업을 갈아 끼우는 방법
- [ ] Collection Type / 같은 필드 묶음을 여러 개 넣고 빼는 타입
- [ ] CSRF Protection / 남의 사이트에서 온 제출을 토큰으로 걸러내는 방법
- [ ] Validator Constraint / 값이 지켜야 할 조건을 클래스에 붙이는 선언
- [ ] Validation Group / 상황에 따라 검사할 제약만 골라 쓰는 묶음
- [ ] Custom Constraint · Validator / 내 규칙을 제약 클래스로 직접 만드는 방법

---

# PART 4 · Presentation and Security

## 12. Twig

- [ ] Syntax / 출력과 제어문을 나눠 쓰는 두 괄호 표기
- [ ] Template Inheritance / 뼈대 템플릿의 구멍을 자식이 채우는 구조
- [ ] Partial Templates / 조각 템플릿을 불러 끼우는 방법
- [ ] Filter · Function / 값을 파이프로 변형하는 호출 형태
- [ ] Auto-escaping / 출력값을 기본으로 이스케이프하는 동작
- [ ] Global Variable / 모든 템플릿에서 요청·사용자를 꺼내는 변수
- [ ] Custom Extension / 내 필터·함수를 Twig에 등록하는 클래스
- [ ] Asset Function / 자산 경로를 버전 붙은 URL로 바꾸는 함수

## 13. Frontend Assets

- [ ] AssetMapper / 번들러 없이 파일을 그대로 내보내는 방식
- [ ] Importmap / 브라우저에 모듈 이름과 경로를 알려주는 대응표
- [ ] Webpack Encore / 웹팩 설정을 감싸 둔 빌드 도구 `선택`
- [ ] Symfony UX / 서버 렌더에 자바스크립트 동작을 얹는 묶음
- [ ] Asset Versioning and Build on Deploy / 배포 때 자산에 버전을 붙여 캐시를 끊는 방법

## 14. Security

- [ ] Firewall / 경로별로 인증 규칙을 나눠 거는 구획
- [ ] Authenticator / 자격 증명을 확인해 사용자를 세우는 지점
- [ ] User Provider / 사용자를 어디서 어떻게 불러올지 정하는 곳
- [ ] Password Hasher / 비밀번호를 복원 못 하는 형태로 저장하는 방법
- [ ] Access Control / 경로 패턴에 필요한 권한을 못 박는 설정
- [ ] Role Hierarchy / 상위 역할이 하위 역할을 자동으로 갖게 하는 규칙
- [ ] Voter / 대상 객체별 허용 여부를 코드로 판정하는 클래스
- [ ] IsGranted / 어트리뷰트로 실행 전에 권한을 거는 방법
- [ ] Remember Me · Logout / 세션이 끝나도 로그인을 이어 두는 방법
- [ ] JWT · API Token Authentication / 세션 없이 토큰으로 API 요청을 증명하는 방식

---

# PART 5 · Extensions and Operations

## 15. Console and Messenger

- [ ] Console Command Authoring / 클래스를 CLI 명령으로 등록하는 어트리뷰트
- [ ] Input · Output / 명령의 인자를 받고 결과를 찍는 방법
- [ ] MakerBundle / 엔티티·컨트롤러 뼈대를 만들어 주는 명령 묶음
- [ ] Messenger / 할 일을 메시지로 만들어 처리기에 넘기는 구조
- [ ] Transport / 메시지를 어디에 쌓아 둘지 고르는 설정
- [ ] Async Dispatch / 요청 밖 워커 프로세스로 처리를 미루는 방법
- [ ] Retry · Failure Transport / 실패한 메시지를 다시 걸고 따로 모으는 설정
- [ ] Mailer · Notifier / 메일과 알림을 같은 방식으로 보내는 컴포넌트

## 16. Testing and Operations

### Testing

- [ ] PHPUnit Bridge / 커널을 띄운 채 서비스를 시험하는 기반 클래스
- [ ] WebTestCase / 서버 없이 요청을 넣어 응답을 훑는 테스트
- [ ] Test Container / 테스트에서 private 서비스까지 꺼내는 통로
- [ ] Database Test / 테스트마다 DB를 원상태로 되돌리는 방법
- [ ] Test Environment Configuration Separation / test 환경 설정을 따로 두는 이유

### Operations

- [ ] Profiler · Web Debug Toolbar / 요청마다 질의·이벤트를 기록해 보여주는 도구
- [ ] Monolog / 로그를 채널로 나눠 다른 곳에 보내는 설정
- [ ] Cache Component / 캐시 저장소를 표준 인터페이스로 다루는 방법
- [ ] HTTP Cache / 응답 자체를 앞단에서 재사용하게 하는 헤더 규약
- [ ] prod Optimization / 컨테이너와 클래스를 미리 구워 두는 방법
- [ ] Deployment / 쓰기 권한과 캐시 디렉터리를 맞추는 절차
- [ ] Upgrade / deprecation 경고를 지우며 메이저를 올리는 순서

---

# 이 로드맵 밖

- PHP `software/skill-based/Languages/php.md`
- Laravel `software/skill-based/Frameworks/laravel.md`
- PHPUnit `software/skill-based/Testing/phpunit.md`
- 백엔드 전반 `software/role-based/backend.md`
- API 설계 `software/skill-based/CS-Theory/api-design.md`
- MySQL · PostgreSQL 운영 `software/skill-based/Data-DB/mysql.md`, `software/role-based/postgresql-dba.md`
