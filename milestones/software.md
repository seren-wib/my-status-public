# 소프트웨어 마일스톤

> 로드맵이 아니다 — 학습 체크리스트에 섞지 않는 **성취 기록**.
> 2026-08-26, role 22개 파일 끝에 있던 `PART · 정상의 영역` 밴드를 해체해 옮긴 것.
> 로드맵 항목은 '배우는 것'(체크박스·진행률 있음)이고 여기 있는 것은 '이루는 것'이라 분모에 넣지 않는다.
> 지식 명사구 섹션에 성취 서술문을 섞으면 난이도 절벽이 생기고 섹션이 안 닫혀 진행이 막힌다.
> 파서(`tools/parse_roadmaps.py`)는 `roadmaps/` 만 훑으므로 이 파일은 stats·분모에 잡히지 않는다.
> 형식·json 변환은 큰 순서 ②(자격증 파일) 작성 시 통합 검토.

## 공통

원본 50줄이 6종의 변주였다. 한 줄로 합치면서 판정 불가 문구("널리 읽히기"·"다수에게 영향")에 기준을 박았다.

- Open Source Merge / 외부 오픈소스에 코드 기여 1건 머지 (오타·문서만 고친 것은 제외)
- Open Source Maintainer / 오픈소스 프로젝트의 메인테이너 권한 또는 핵심 기여자 지위 획득
- Library Release / 직접 만든 라이브러리를 패키지로 공개하고 외부 프로젝트 채택 1건 확인
- Public Talk / 사외 청중 앞 기술 발표 1회 (사내 세미나 제외)
- Technical Writing / 기술 글 공개 후 외부 유입·인용을 수치로 확인한 글 1편
- Engineer Mentoring / 주니어 1명을 독립 수행 가능 수준까지 성장시킨 사이클 완료
- Interview Panel / 채용 면접관으로 후보 평가 참여

## software/role-based/ai-engineer

- First AI Feature Live / AI 기능 하나를 실사용자에게 출시
- LLM Product Launch / LLM 기반 제품을 출시해 지속 사용자 확보
- Eval Suite Built / 제품 품질을 재는 평가 체계 구축해 배포 게이트로 정착
- Hallucination Reduction / 오답률을 측정 가능하게 줄여 전후 수치로 실증
- Cost Order-of-Magnitude / 토큰·추론 비용을 자릿수 단위로 절감
- Incident Playbook / 프롬프트 인젝션·오남용 대응 체계 만들어 실전 검증
- AI Feature Team Lead / AI 제품 기능 개발을 팀 단위로 리드
- Model Selection Authority / 모델·아키텍처 선정 기준을 조직 표준으로 만들기

## software/role-based/android

- Play Store Launch / 직접 만든 앱을 Play 스토어에 출시
- User Base / 출시 앱의 실사용자 수천 이상 확보
- Update Cadence / 정기 업데이트를 반년 이상 지속
- Crash-Free Proof / 크래시 프리 비율을 계측해 개선하고 전후 수치 기록
- Performance Profiling / 실기기 프로파일링으로 시작 시간·프레임 드랍 개선 실증
- Monetization Live / 광고·인앱 결제를 붙여 실수익 발생

## software/role-based/backend

- Production at Scale / 수천 이상 동시 사용자 서비스를 설계·운영해 실증
- Incident Command / 실서비스 장애 대응을 리드하고 포스트모템 작성
- Bottleneck Elimination / 실서비스 병목을 프로파일링으로 찾아 자릿수 단위 개선
- High Availability Proof / 다중화 구성으로 장애 주입에도 서비스 지속을 실증
- System Design Ownership / 신규 시스템 아키텍처를 설계하고 설계 문서로 합의 도출
- Legacy Decomposition / 운영 중인 모놀리스를 무중단으로 분리·이전
- Data Migration at Scale / 대용량 실데이터 마이그레이션을 무손실로 완수
- API Platform / 외부 개발자가 쓰는 공개 API를 설계·문서화해 운영

## software/role-based/bi-analyst

- Dashboard in Daily Use / 만든 대시보드가 팀의 매일 아침 화면으로 정착
- Executive Dashboard / 경영진이 의사결정에 직접 쓰는 대시보드 구축
- Report Retired / 수작업 반복 리포트를 자동화 대시보드로 대체해 공수 절감
- Data Story that Moved / 데이터 스토리텔링으로 전략 방향을 바꾼 발표
- Semantic Layer Owner / 지표 정의·시맨틱 레이어를 설계해 조직 단일 기준으로 정착
- Self-Serve BI Rollout / 현업이 직접 조회하는 셀프서브 BI 도입 주도
- Forecast Adopted / 내 예측·시계열 분석이 실제 사업 계획에 반영
- BI Migration Lead / BI 플랫폼 전환을 무사고로 완수
- BI Team Lead / BI 조직 리드로 지표·우선순위 책임

## software/role-based/blockchain

- Mainnet Deployment / 직접 작성한 컨트랙트를 메인넷에 배포
- Audit Pass / 외부 감사나 공개 리뷰를 통과한 컨트랙트 보유
- Upgrade in Production / 운영 중인 컨트랙트를 안전하게 업그레이드 완수
- dApp Live / 프론트까지 갖춘 dApp을 공개해 실사용자 확보
- Gas Optimization Proof / 가스 비용을 계측해 개선하고 전후 수치 기록
- Security Finding / 실제 취약점을 찾아 제보하고 버그 바운티·감사 리포트로 인정
- Deployment Pipeline / 테스트넷 검증에서 메인넷 배포까지 파이프라인을 구축해 반복 사용
- Standard Contribution / ERC·EIP 논의에 의견 제시나 제안으로 참여

## software/role-based/data-analyst

- Published Analysis / 의사결정을 바꾼 분석 보고서와 그 결과 복기
- Executive Briefing / 경영진 앞에서 분석 결과 발표해 실행 승인 받기
- Revenue Impact / 분석으로 찾은 개선안이 매출·비용 변화로 실증
- End-to-End Case Study / 원데이터→인사이트→권고까지 완결한 케이스 스터디 공개
- Competition Standing / 데이터 대회 입상 또는 상위권
- Self-Serve Dashboard / 내가 없어도 조직이 스스로 답을 찾는 대시보드 정착
- Metric Owner / 조직 핵심 지표의 정의·품질을 책임지는 오너 되기
- Analytics Playbook / 반복 분석을 표준 프로세스·템플릿으로 만들어 전파
- Analytics Team Lead / 분석 조직 리드로 우선순위·채용 책임

## software/role-based/data-engineer

- First Production Pipeline / 실무 데이터 파이프라인 구축해 무중단 운영
- Pipeline at Scale / 대용량 일배치·스트리밍 파이프라인 설계·운영
- Cost Structure Win / 저장·연산 비용을 구조 개선으로 크게 절감해 수치 실증
- Data Quality Gate / 품질 검증 자동화로 불량 데이터 사고 재발 방지
- Warehouse from Zero / 데이터 웨어하우스를 처음부터 설계해 조직에 정착
- Self-Serve Platform / 분석가가 엔지니어 없이 데이터 쓰는 셀프서브 환경 구축
- Migration Lead / 레거시에서 신규 데이터 스택 이전을 무사고로 완수
- Streaming Backbone / 실시간 스트리밍 기반 구축해 신규 제품 기능 뒷받침
- Data Platform Lead / 데이터 플랫폼 구축과 로드맵을 리드

## software/role-based/devops

- Internal Developer Platform / 셀프서비스 배포 플랫폼을 구축해 조직 전체가 사용
- Deploy Velocity Proof / 플랫폼 도입 전후 배포 빈도·리드타임 개선을 지표로 실증
- Zero-Downtime Migration / 무중단 인프라 이전을 설계·실행해 실증
- Multi-Region Architecture / 다중 리전 아키텍처를 설계해 리전 장애에도 서비스 유지
- Cost Optimization Win / 클라우드 비용 구조를 분석해 자릿수 단위 절감 실증
- Incident Command / 대형 장애 대응을 리드하고 포스트모템 주관
- SLO Culture / 조직에 SLO·에러버짓 체계를 도입해 운영 기준으로 정착
- Chaos Engineering Program / 카오스 실험을 정례화해 실제 약점을 사전 발견
- On-Call Redesign / 온콜 체계를 재설계해 알림 노이즈·번아웃 감소 실증
- Expert-Level Certification / CKA·클라우드 Professional급 최상위 자격 취득 `자격증 파일로 이관 예정`

## software/role-based/devsecops

- Pipeline Security Rollout / 조직 전 파이프라인에 보안 게이트를 도입해 정착
- Shift-Left Proof / 배포 전 취약점 검출 비율 상승을 지표로 실증
- Zero Trust Rollout / 제로 트러스트 아키텍처 전환을 설계·실행
- Compliance Audit Pass / SOC 2 또는 ISO 27001 심사 대응을 주도해 통과
- CVE or Bounty / 취약점 제보로 CVE 등재 또는 버그바운티 보상
- Red Team Exercise / 모의 침투 훈련을 설계·주관하고 방어 개선으로 연결
- Incident Command / 보안 사고 대응을 리드하고 포스트모템 주관
- Supply Chain Defense / 공급망 공격 시나리오를 방어하는 빌드 체계 구축 실증
- Top-Tier Certification / OSCP·CISSP급 최상위 자격 취득 `자격증 파일로 이관 예정`

## software/role-based/engineering-manager

- Team Built from Zero / 채용부터 온보딩까지 팀 하나를 처음부터 만들어 성과 궤도에 올림
- Retention Proven / 맡은 조직의 이직률을 낮게 유지하며 핵심 인재를 지켜냄
- Manager of Managers / 매니저를 육성해 매니저를 관리하는 층위로 올라섬
- Promotion Pipeline / 팀원 성장을 목표·피드백으로 이끌어 승진·성과로 실증
- Delivery Speed Turnaround / 정체된 조직의 전달 속도를 프로세스 개선으로 끌어올려 지표로 실증
- Crisis Led / 대형 장애·위기 상황의 지휘를 맡아 복구와 재발 방지까지 완결
- Reorg Executed / 조직 개편을 설계·실행해 이탈 없이 안착시킴
- Budget Owned / 조직의 연간 예산을 편성·집행하고 경영진에 결과로 보고
- Culture Survives You / 만든 문화·프로세스가 본인이 빠져도 굴러가는 상태 도달
- EM Mentoring / 시니어 엔지니어를 매니저로 전환시켜 독립적으로 팀을 맡게 함
- Executive Trust / 경영진 앞에서 기술 조직의 전략을 대변하는 창구가 됨

## software/role-based/frontend

- Production Launch / 실사용자가 쓰는 웹 서비스를 출시하고 운영
- Performance Turnaround / 실서비스의 Core Web Vitals를 계측해 개선하고 전후 수치 기록
- Accessibility Compliance / 운영 중인 서비스가 접근성 표준을 통과하도록 리드
- Zero-Downtime Migration / 운영 중인 서비스의 프레임워크·빌드 체계를 무중단 이전
- Design System Adoption / 디자인 시스템을 구축해 여러 화면·팀이 실제로 사용
- Component Library Release / 재사용 컴포넌트 라이브러리를 패키지로 공개해 외부 사용자 확보
- Frontend Tech Lead / 프론트엔드 기술 결정을 주도하고 코드 리뷰 문화 정착

## software/role-based/full-stack

- Solo Launch / 기획부터 배포까지 혼자 제품 하나를 출시
- Real Users / 출시한 제품에 외부 실사용자 확보
- First Revenue / 제품으로 첫 결제·수익 발생
- Full Ownership Ops / 배포·모니터링·백업·장애 대응을 혼자 감당하는 운영 체계 구축
- Iteration Loop / 사용자 피드백을 받아 개선 배포를 반복하는 주기 정착
- Cost Discipline / 인프라 비용을 계측해 수익 구조 안에서 유지
- Incident Recovery / 실서비스 장애를 스스로 복구하고 재발 방지 적용
- Second Product / 축적한 기반으로 두 번째 제품을 더 짧은 주기로 출시
- Build in Public / 제품 제작 과정을 공개 기록해 팔로워 확보

## software/role-based/game-developer

- Vertical Slice / 핵심 재미가 담긴 수직 슬라이스를 완성해 플레이테스트
- Playtest Pivot / 플레이테스트 피드백으로 핵심 루프를 갈아엎어 재미 개선 실증
- Game Jam Finisher / 게임잼에서 기한 내 완성작 제출
- Shipped Game / 게임을 스토어에 출시하고 사용자 피드백으로 업데이트
- Public Post-mortem / 출시작 포스트모템을 작성해 공개
- Monetization Live / 수익 모델(유료·IAP·광고)을 실제로 붙여 매출 발생
- Retention Update / 지표 기반 업데이트로 잔존율 개선 실증
- Engine Internals / 엔진 소스 수정이나 자체 엔진 기능 구현을 실제 게임에 투입
- Performance Rescue / 프레임 떨어진 게임을 프로파일링으로 목표 프레임까지 복구
- Project Lead / 게임 프로젝트 하나를 리드로 맡아 출시까지 완주

## software/role-based/ios

- App Store Launch / 직접 만든 앱을 App Store에 출시
- User Base / 출시 앱의 실사용자 수천 이상 확보
- Update Cadence / 정기 업데이트를 반년 이상 지속
- Crash-Free Proof / 크래시 프리 비율을 계측해 개선하고 전후 수치 기록
- Monetization Live / 구독·인앱 결제를 붙여 실수익 발생

## software/role-based/machine-learning

- Paper Reproduction / 논문 하나 골라 결과를 재현한 구현 공개
- Paper Improved / 재현한 기법을 개선해 원 결과 대비 향상 실증
- Model in Service / 직접 학습한 모델을 실사용자 서비스에 배포해 성과 실증
- Competition Medal / ML 대회 입상 또는 상위권
- Custom Architecture / 문제에 맞는 모델 구조를 직접 설계해 베이스라인 능가
- Training at Scale / 대규모 데이터·분산 환경에서 학습 파이프라인 완주
- Fine-tuned Foundation Model / 파운데이션 모델 미세조정으로 특화 성능 실증
- Publication or Preprint / 연구 결과를 논문·프리프린트로 공개
- ML Project Lead / 모델 개발을 문제 정의부터 배포까지 리드

## software/role-based/network-engineer

- Enterprise Network Build / 수백 대 규모 조직망을 설계·구축해 운영 이관
- Zero-Downtime Migration / 무중단 망 이전·장비 교체를 설계·실행해 실증
- Multi-Site WAN / 다중 사이트 WAN을 설계해 사이트 장애에도 연결 유지
- Network Automation Rollout / 망 구성 자동화를 도입해 수작업 설정 제거 실증
- Major Outage Command / 대형 네트워크 장애 대응을 리드하고 포스트모템 주관
- Capacity Planning Proof / 트래픽 증가를 예측한 증설 계획으로 병목 없이 통과
- Root Cause Hunt / 재현 어려운 간헐 장애를 패킷 수준 분석으로 규명
- DDoS Defense / 실제 DDoS 공격을 방어해 서비스 유지 실증
- Design Review Authority / 타 조직·팀의 망 설계를 검토하는 리뷰어 역할 수행
- Expert-Level Certification / CCIE급 최상위 자격 취득 `자격증 파일로 이관 예정`

## software/role-based/product-design

- End-to-End Ship / 리서치부터 출시까지 기능 하나의 디자인 전 과정을 소유해 완주
- Usability Metric Win / 디자인 개선이 전환·완료율 지표를 움직였음을 실증
- Design System Built / 디자인 시스템을 구축해 여러 제품·팀이 실사용
- Multi-platform Delivery / 한 제품을 웹·모바일 등 복수 플랫폼에 일관되게 출시
- Critique Culture / 디자인 크리틱 문화를 만들어 정기 운영으로 정착
- DesignOps Installed / 툴·핸드오프·리뷰 프로세스를 표준화해 조직에 안착
- Design Advocacy / 경영진을 설득해 디자인 주도 프로젝트를 승인·실행까지 이끎
- Portfolio Recognition / 작업물이 수상·피처링 등 외부 인정 획득

## software/role-based/product-manager

- Product Launched / 발굴부터 출시까지 제품·기능 하나의 전체 사이클을 소유해 완주
- Metric Moved / 출시한 기능이 핵심 지표를 움직였음을 데이터로 실증
- Kill Decision / 지표가 보여주는 실패를 인정하고 기능·제품을 접는 결정을 내림
- Pivot Led / 검증 결과를 근거로 방향 전환을 설득하고 실행까지 이끎
- Roadmap Defended / 세운 로드맵을 경영진·이해관계자 압박 속에서 근거로 지켜냄
- Cross-Team Alignment / 개발·디자인·마케팅을 한 목표로 정렬해 출시 완수
- Product-Market Fit / 만든 제품이 리텐션·성장 지표로 PMF 도달을 실증
- Revenue Impact / 제품 결정이 매출·전환에 미친 영향을 금액 단위로 증명

## software/role-based/qa

- Test Strategy Lead / 제품 하나의 테스트 전략을 설계해 릴리즈 품질 개선 실증
- Automation Pipeline / CI에 자동화 테스트 체계를 구축해 회귀 버그 조기 검출 실증
- Flaky Zero Campaign / 불안정 테스트를 추적·제거해 파이프라인 신뢰 회복
- Release Gate Owner / 릴리즈 승인 기준을 세워 게이트 운영
- Critical Catch / 출시 전 치명 결함을 잡아 사고를 막은 실증
- Quality Metrics Board / 결함·커버리지 지표 대시보드를 만들어 릴리즈 의사결정에 사용
- Performance Verdict / 부하 테스트로 병목을 찾아 성능 개선을 이끈 실증
- QA Team Build / QA 조직·프로세스를 처음부터 세워 운영

## software/role-based/server-side-game-developer

- Live Game Server / 실제 유저가 접속하는 게임 서버를 배포해 운영
- Concurrency Spike / 라이브 중 동접 스파이크를 무중단으로 받아낸 실증
- Zero-downtime Deploy / 라이브 중 무중단 패치·배포 체계 구축
- Incident Recovery / 라이브 장애를 복구하고 재발 방지 포스트모템 작성
- Live Data Migration / 라이브 DB 스키마·샤드 마이그레이션 무사고 수행
- Load Test Verdict / 부하 테스트로 서버 한계치를 측정하고 병목 제거 실증
- Horizontal Scale-out / 수평 확장 구조를 설계해 수만 단위 동접 처리
- Matchmaking System / 매치메이킹·세션 관리 시스템을 설계해 라이브 적용
- Realtime Sync Design / 실시간 상태 동기화 구조를 직접 설계해 출시 게임에 적용
- Anti-cheat Field / 실제 치팅·어뷰징을 서버 검증으로 차단한 실증
- Architecture Review Lead / 타 프로젝트 서버 설계 리뷰를 맡아 개선 주도

## software/role-based/software-architect

- Cross-Team Design Lead / 여러 팀에 걸친 시스템 설계를 처음부터 출시까지 주도
- Migration Delivered / 레거시 시스템을 무중단으로 새 구조로 이전 완수
- Scale Survived / 설계한 시스템이 트래픽 자릿수 단위 성장을 구조 변경 없이 버텨냄
- Standards Adopted / 세운 기술 표준·가이드가 조직 전체에 채택돼 굴러감
- Architecture Review Board / 조직의 설계 리뷰 체계를 만들거나 의장으로 운영
- Build vs Buy Call / 대규모 기술 도입·자체 구축 결정을 근거로 내리고 결과로 검증
- Tech Radar Owned / 조직의 기술 선택 지도(도입·보류·폐기)를 관리하는 사람이 됨
- Postmortem to Redesign / 대형 장애의 원인을 구조에서 찾아 재설계로 재발 차단

## software/role-based/technical-writer

- Docs System Adopted / 설계한 문서 체계가 팀·커뮤니티 표준으로 채택
- Docs from Zero / 문서가 없던 제품의 문서 사이트를 처음부터 구축해 공개
- Style Guide Owned / 작성한 스타일 가이드가 조직의 공식 규범이 됨
- Support Load Drop / 문서 개선으로 반복 문의가 줄었음을 수치로 실증
- Docs-as-Code Pipeline / 리뷰·버전 관리가 도는 문서 파이프라인을 구축해 운영
- Flagship Content / 쓴 글 하나가 검색 상위 노출·커뮤니티 회자로 대표작이 됨
- Paid Authority / 글·문서 작업으로 원고료·계약 등 외부 보상을 받음
