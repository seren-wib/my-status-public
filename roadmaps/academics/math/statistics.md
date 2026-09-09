# Statistics `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-25

# PART 1 · Descriptive Statistics

## 1. Data and Variables

- [ ] Variable Types / 범주형·순서형·연속형을 나누고 그에 맞게 다루기
- [ ] Sampling Methods / 표본추출 방식과 각 방식이 놓치는 것
- [ ] Sources of Bias / 선택편향·생존편향이 생기는 지점 사례로 찾기
- [ ] Handling Missing and Outliers / 결측·이상치 처리 기준을 정하고 근거 대기

## 2. Summarizing One Variable

- [ ] Measures of Center / 평균·중앙값·최빈값 중 뭐가 언제 왜곡되는지
- [ ] Measures of Spread / 분산·표준편차·IQR 계산과 해석
- [ ] Distribution Shape / 왜도·첨도로 분포 모양을 말로 설명
- [ ] Standardization / z점수로 척도가 다른 값을 비교
- [ ] Visual Summaries / 같은 데이터를 히스토그램·상자그림 두 방식으로 보기

## 3. Relationships Between Variables

- [ ] Covariance and Correlation / 상관계수 계산과 그것이 못 잡는 관계
- [ ] Correlation Is Not Causation / 허위상관 예시를 직접 하나 만들기
- [ ] Contingency Tables / 교차표에서 조건부 비율 읽기
- [ ] Simpson's Paradox / 심슨의 역설을 숫자로 재현

---

# PART 2 · Probability

## 4. Probability Foundations

- [ ] Sample Space and Events / 문제를 표본공간·사건으로 옮겨 적기
- [ ] Probability Axioms / 공리에서 기본 정리 유도
- [ ] Counting for Probability / 순열·조합으로 확률 세기
- [ ] Conditional Probability / 조건부확률 계산과 표기 정리
- [ ] Independence / 독립과 배반을 혼동하지 않게 판정
- [ ] Law of Total Probability / 전확률 공식으로 경우 나눠 계산
- [ ] Bayes' Theorem / 베이즈 정리로 진단검사 문제 풀고 직관 교정

## 5. Random Variables

- [ ] Random Variable as Function / 확률변수로 추상화하기
- [ ] PMF, PDF, CDF / 세 함수의 관계와 변환
- [ ] Expectation / 기댓값 계산과 선형성 활용
- [ ] Variance and Moments / 분산·적률의 계산
- [ ] Joint and Marginal Distributions / 결합분포에서 주변·조건부 뽑기
- [ ] Covariance of Random Variables / 확률변수 간 공분산과 상관
- [ ] Transformation of Variables / 변수 변환 후 분포 구하기

---

# PART 3 · Distributions

## 6. Discrete Distributions

- [ ] Bernoulli and Binomial / 이항분포를 쓸 상황 판정하고 계산
- [ ] Poisson / 포아송 근사와 그 적용 조건
- [ ] Geometric and Negative Binomial / 첫 성공까지의 분포들

## 7. Continuous Distributions

- [ ] Uniform and Exponential / 균등·지수분포와 무기억성 확인
- [ ] Normal Distribution / 정규분포 계산과 68-95-99.7 감각
- [ ] Sampling Distribution / 표본통계량의 분포를 시뮬레이션으로 만들어보기
- [ ] Central Limit Theorem / 중심극한정리가 성립하는 조건과 시뮬레이션 확인
- [ ] Law of Large Numbers / 대수의 법칙과 CLT를 구분해서 설명
- [ ] t, Chi-square, F / 추론에 쓰이는 세 분포가 어디서 나오는지

---

# PART 4 · Inference

## 8. Estimation

- [ ] Point Estimation / 추정량의 불편성·일치성 확인
- [ ] Maximum Likelihood / 최대우도추정을 직접 유도해서 풀기
- [ ] Standard Error / 표준오차와 표준편차를 구분해서 쓰기
- [ ] Confidence Interval / 신뢰구간을 구성하고 올바르게 해석
- [ ] Bootstrap / 붓스트랩으로 구간을 만들어 이론값과 비교

## 9. Hypothesis Testing

- [ ] Null and Alternative / 실제 질문을 가설 한 쌍으로 세우기
- [ ] p-value / p값의 정의와 흔한 오독 세 가지 지적
- [ ] Type I and II Errors / 두 오류와 유의수준의 관계
- [ ] Power and Sample Size / 검정력 계산과 필요한 표본크기 산출
- [ ] t-tests / 일표본·이표본·대응표본을 골라 쓰기
- [ ] ANOVA / 분산분석과 사후검정
- [ ] Chi-square Tests / 적합도·독립성 검정
- [ ] Nonparametric Tests / 가정이 깨질 때의 대안 검정
- [ ] Multiple Comparisons / 다중비교 보정과 p-해킹 인지
- [ ] Effect Size / 효과크기를 유의성과 함께 보고하기

## 10. Bayesian View

- [ ] Prior, Likelihood, Posterior / 세 요소로 믿음 갱신을 한 번 계산
- [ ] Conjugate Priors / 켤레사전분포로 계산이 닫히는 예
- [ ] Credible vs Confidence Interval / 두 구간의 해석 차이를 말로 구분

---

# PART 5 · Regression and Modeling

## 11. Linear Regression

- [ ] Simple Linear Regression / 단순회귀를 적합하고 계수를 해석
- [ ] Least Squares Derivation / 최소제곱 추정량 유도
- [ ] Model Assumptions / 선형성·독립성·등분산성·정규성 점검
- [ ] Residual Diagnostics / 잔차 그림으로 가정 위반 찾기
- [ ] Multiple Regression / 다중회귀에서 통제한다는 말의 뜻
- [ ] Multicollinearity / 다중공선성 진단과 대처
- [ ] R-squared and Model Fit / 결정계수의 쓸모와 함정
- [ ] Categorical Predictors and Interaction / 더미변수와 상호작용항 해석

## 12. Beyond Linear

- [ ] Logistic Regression / 로지스틱 회귀와 오즈비 해석
- [ ] Regularized Regression / 릿지·라쏘가 계수에 하는 일
- [ ] Overfitting / 과적합을 훈련·검증 점수 차이로 확인
- [ ] Cross-validation / 교차검증 절차를 직접 돌려보기

## 13. Study Design and Causality

- [ ] Experiment vs Observational / 실험과 관찰연구가 말할 수 있는 것의 차이
- [ ] Randomization and Control / 무작위 배정이 공짜로 주는 것
- [ ] Confounding / 교란변수 식별과 통제
- [ ] Causal Inference Basics / 인과 추론의 기본 도구 훑기

---

# 이 로드맵 밖

- 회귀·주성분의 행렬 계산 `academics/math/linear-algebra.md`
- 확률밀도의 적분과 우도 최적화 `academics/math/calculus.md`
- 경우의 수 세기와 이산확률 `academics/math/discrete-math.md`
- 확률 오독과 판단 편향 `academics/psychology/cognitive.md`
- 실험으로 검증한 비합리적 선택 `academics/economics/behavioral-economics.md`
