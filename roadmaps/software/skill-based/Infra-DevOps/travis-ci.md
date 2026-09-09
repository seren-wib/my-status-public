# Travis CI `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Getting Started with Travis CI

## 1. What is Travis CI?

- [ ] Hosted CI Service / 서버 없이 빌드 환경을 대신 돌려주는 서비스
- [ ] .travis.yml Based Configuration / 저장소 루트 파일 하나로 빌드를 정의하는 방식
- [ ] travis-ci.com and Legacy .org / 요금제 통합 후 갈린 현재·과거 도메인
- [ ] Position in the OSS Ecosystem / 여러 언어 버전을 동시에 검증하던 자리

### Current Status

- [ ] Credit-based Pricing / 빌드 실행 시간을 크레딧으로 차감하는 과금
- [ ] Migration Trend Toward GitHub Actions / 무료 크레딧 폐지 뒤 옮겨간 흐름
- [ ] When to still use Travis CI? / 기존 저장소 유지보수에만 남는 이유

## 2. Getting Started

- [ ] Repository Activation / GitHub·Bitbucket 저장소에 빌드 훅을 연결하는 절차
- [ ] .travis.yml at Repo Root / 커밋 시 자동으로 읽히는 설정 파일 위치
- [ ] First Build and Build Log UI / 첫 빌드를 로그 화면에서 확인하는 흐름
- [ ] Travis CLI / travis lint로 로컬에서 설정을 검증하는 도구
- [ ] Build Status Badge / 최신 빌드 성패를 README에 보여주는 배지

## 3. Config Structure

- [ ] language Key / 언어 한 줄로 기본 빌드 순서를 정하는 설정
- [ ] Build Lifecycle / install·script·deploy로 이어지는 정해진 순서
- [ ] Lifecycle Hooks / 정해진 순서 사이에 끼워 넣는 훅 지점
- [ ] os, dist, arch / OS·배포판·아키텍처를 지정하는 키
- [ ] Build vs Job vs Stage / 실행 단위를 나누는 세 단계 계층
- [ ] YAML Anchors / 반복되는 설정 블록을 재사용하는 문법

---

# PART 2 · Writing Builds

## 4. Language and Environment

- [ ] Language Runtimes / 언어별로 정해진 빌드·테스트 기본값
- [ ] Runtime Version Selection / 매트릭스에 넣을 언어 버전을 고르는 설정
- [ ] Default install and script per Language / 언어별로 이미 정해진 기본 실행 단계
- [ ] Custom Script Override / 기본 순서 대신 직접 명령을 쓰는 설정
- [ ] services / 빌드 중 띄워 쓰는 백그라운드 서비스
- [ ] addons / apt 패키지·브라우저 등을 미리 설치하는 설정

## 5. Build Matrix

- [ ] Matrix Expansion / 버전·환경변수 조합을 곱해 늘리는 방식
- [ ] jobs.include and jobs.exclude / 매트릭스에 칸을 더하고 빼는 설정
- [ ] allow_failures / 특정 칸이 실패해도 전체를 통과시키는 설정
- [ ] fast_finish / 필수 칸이 끝나면 나머지를 안 기다리는 설정
- [ ] Job Naming / 매트릭스 칸마다 구분용 이름을 붙이는 설정

## 6. Environment Variables

- [ ] env Global vs Matrix / 전역과 매트릭스별 환경변수의 범위 차이
- [ ] Repository Settings Variables / 저장소 웹 UI에서 등록하는 비밀 값
- [ ] Encrypted Variables / travis encrypt로 만든 암호문을 커밋하는 방식
- [ ] Encrypted Files / 키 파일 자체를 암호화해 커밋하는 방식
- [ ] Built-in Variables / 빌드 정보를 자동으로 주입하는 값
- [ ] Fork PR Secret Restrictions / 포크 PR에서 암호화 값을 숨기는 보안 규칙

## 7. Caching and Artifacts

- [ ] cache Directive / 언어별 의존성 폴더를 재사용하는 설정
- [ ] Custom Cache Directories / 기본값 밖의 폴더를 직접 지정해 캐싱하는 법
- [ ] Cache Invalidation / 오염된 캐시를 지우고 새로 받게 하는 절차
- [ ] Artifact Upload / 빌드 결과물을 S3 등에 올리는 절차

---

# PART 3 · Deployment and Operations

## 8. Build Stages

- [ ] stages Definition / 잡들을 순서대로 묶는 단계를 선언하는 설정
- [ ] Sequential Stage Execution / 앞 단계가 끝나야 다음 단계가 도는 순서
- [ ] Conditional Stage / if 조건에 따라 단계를 건너뛰는 설정
- [ ] Manual Approval Stage / 사람이 승인해야 다음 단계로 넘어가는 단계

## 9. Deployment

- [ ] deploy Provider Overview / 배포 대상마다 정해진 provider 키 구조
- [ ] Common Providers / 패키지 저장소·플랫폼 등 자주 쓰는 배포 대상
- [ ] Deploy Conditions / 특정 브랜치·태그일 때만 배포하는 조건
- [ ] skip_cleanup / 배포 전 빌드 산출물을 안 지우는 설정
- [ ] Custom Deploy Script / 기본 provider 대신 직접 짜는 배포 명령
- [ ] Environment-based Deploy / 스테이징·프로덕션을 나눠 배포하는 방식

## 10. Conditions and Triggers

- [ ] Conditional Builds / if 문으로 실행 여부를 거르는 문법
- [ ] Branch Filtering / 특정 브랜치만 빌드에 넣거나 빼는 설정
- [ ] Tag Builds / 태그 푸시를 릴리스 빌드 트리거로 쓰는 법
- [ ] Cron / 정해진 주기로 저절로 도는 예약 빌드
- [ ] API-triggered Build / API 호출로 외부에서 빌드를 거는 방식
- [ ] Skipping CI / 커밋 메시지에 적어 빌드를 건너뛰는 표시

## 11. Operations

### Troubleshooting

- [ ] Debug Build over SSH / 실패한 빌드 환경에 직접 접속해 보는 기능
- [ ] Build Timeout / 출력 없이 길어지면 죽는 기본 제한 시간
- [ ] Log Truncation / 로그가 길어지면 일부가 잘려나가는 현상
- [ ] Common Failures / 캐시·의존성 문제로 자주 나는 실패 유형

### Operations

- [ ] Concurrency / 동시 실행 수만큼 크레딧을 함께 소모하는 구조
- [ ] Notifications / 빌드 결과를 메일·슬랙 등으로 알리는 설정
- [ ] Travis CI Enterprise / 사내 서버에 직접 설치해 쓰는 버전 `선택`
- [ ] Migration to Other CI / 매트릭스 개념을 다른 CI로 옮겨 쓰는 작업

---

# 이 로드맵 밖

- 데브옵스 전반 `software/role-based/devops.md`
- Git · GitHub Actions `software/skill-based/Infra-DevOps/git-github.md`
- 셸 스크립트 `software/skill-based/Languages/shell-bash.md`
- 컨테이너 이미지 `software/skill-based/Infra-DevOps/docker.md`
- 배포 대상 클라우드 `software/skill-based/Infra-DevOps/aws.md`
