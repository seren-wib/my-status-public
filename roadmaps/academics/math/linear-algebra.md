# Linear Algebra `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-25

# PART 1 · Vectors and Space

## 1. Vectors

- [ ] Vector as Arrow and List / 화살표와 수의 나열, 두 관점을 오가며 같은 문제 보기
- [ ] Vector Addition and Scaling / 덧셈·스칼라배를 좌표와 그림 양쪽으로 확인
- [ ] Linear Combination / 선형결합으로 만들어지는 것과 안 되는 것
- [ ] Span / 벡터 두세 개가 펼치는 공간을 직접 그려보기
- [ ] Linear Independence / 독립·종속 판정과 그것이 뜻하는 낭비

## 2. Inner Product and Geometry

- [ ] Dot Product / 내적의 대수 정의와 사영 해석 연결하기
- [ ] Norm and Distance / 길이와 거리, L1·L2가 다르게 재는 지점
- [ ] Angle and Orthogonality / 각도 계산과 직교 판정
- [ ] Projection onto a Vector / 한 벡터 위로의 사영을 유도해서 계산
- [ ] Cross Product / 외적으로 법선벡터와 평행사변형 넓이 구하기

---

# PART 2 · Matrices and Linear Transformations

## 3. Matrices as Data and Operators

- [ ] Matrix Notation and Basic Ops / 덧셈·스칼라배·전치를 손으로 각 3개
- [ ] Matrix-Vector Product / 열벡터의 선형결합으로 읽는 습관 들이기
- [ ] Matrix Multiplication / 변환의 합성으로서의 곱, 비가환성 직접 확인
- [ ] Special Matrices / 항등·대각·대칭·직교행렬이 각각 뭘 보장하는지

## 4. Linear Transformations

- [ ] Transformation as Matrix / 선형사상과 행렬이 일대일로 대응하는 이유
- [ ] Standard Transformations / 회전·반사·스케일·전단 행렬을 직접 유도
- [ ] Composition of Transformations / 합성 순서를 바꿔서 결과가 달라지는 예 만들기
- [ ] Homogeneous Coordinates / 평행이동까지 행렬 하나로 처리하기

## 5. Solving Linear Systems

- [ ] Linear System as Matrix Equation / 연립방정식을 Ax=b로 옮겨 적기
- [ ] Gaussian Elimination / 소거법으로 3×3 이상을 손으로 풀기
- [ ] Row Echelon and Pivots / 계단형에서 피벗과 자유변수 읽기
- [ ] Solution Sets / 유일해·무수히 많은 해·해 없음을 기하로 구분
- [ ] LU Decomposition / LU 분해와 같은 A를 반복해 풀 때의 이득

## 6. Inverse and Determinant

- [ ] Matrix Inverse / 역행렬 계산과 존재 조건
- [ ] Determinant / 행렬식을 부피 배율로 해석하기
- [ ] Determinant Properties / 곱·전치·행연산에 대한 성질로 계산 줄이기
- [ ] Singularity / 특이행렬이 공간을 어떻게 뭉개는지

---

# PART 3 · The Structure of Spaces

## 7. Subspaces and Basis

- [ ] Subspace / 부분공간인지 아닌지 세 조건으로 판정
- [ ] Basis and Dimension / 주어진 공간의 기저와 차원 구하기
- [ ] Four Fundamental Subspaces / 열·영·행·좌영공간의 차원 관계 정리
- [ ] Rank and Nullity / 랭크-널리티 정리를 실제 행렬에 적용
- [ ] Change of Basis / 기저변환 행렬을 세우고 좌표를 옮기기

## 8. Orthogonality

- [ ] Orthogonal Complement / 직교여공간을 구하고 분해에 쓰기
- [ ] Gram-Schmidt / 임의의 기저에서 직교기저 만들기
- [ ] QR Decomposition / QR 분해와 수치적으로 나은 이유
- [ ] Orthogonal Projection onto Subspace / 부분공간 사영행렬 유도
- [ ] Least Squares / 정규방정식으로 최소제곱해 구하기

---

# PART 4 · Eigenvalues and Decompositions

## 9. Eigenvalues and Eigenvectors

- [ ] Characteristic Polynomial / 특성방정식으로 고유값 구하기
- [ ] Eigenvector Geometry / 변환이 방향을 안 바꾸는 축을 그림으로 확인
- [ ] Diagonalization / 대각화 가능 조건 판정과 계산
- [ ] Matrix Powers via Eigen / 거듭제곱·점화식을 고유값으로 빠르게 처리
- [ ] Symmetric Matrices and Spectral Theorem / 대칭행렬의 직교 대각화

## 10. Decompositions

- [ ] Eigendecomposition / 고유값 분해의 계산과 기하적 의미
- [ ] Singular Value Decomposition / SVD를 계산하고 세 행렬이 뭘 하는지 말하기
- [ ] Low-Rank Approximation / 랭크를 잘라 이미지 한 장 압축해보기
- [ ] Pseudoinverse / 유사역행렬과 최소제곱이 같은 답인 이유
- [ ] Positive Definiteness and Cholesky / 양정치 판정과 이차형식, 촐레스키 분해

---

# PART 5 · Putting It to Use

## 11. Linear Algebra in Machine Learning

- [ ] Data Matrix Layout / 샘플×특징 배치와 연산 방향 맞추기
- [ ] Covariance Matrix / 공분산행렬의 구조와 대칭성
- [ ] PCA via Eigen or SVD / 주성분분석을 데이터 하나로 직접 계산
- [ ] Matrix Calculus Shapes / 그래디언트·야코비안의 형태를 어긋나지 않게 맞추기
- [ ] Norms as Regularizers / L1·L2 규제가 만드는 해의 모양 차이

## 12. Linear Algebra in Graphics

- [ ] Model-View-Projection / 3D 파이프라인의 행렬 체인 순서대로 세우기
- [ ] Rotation Representations / 오일러각·회전행렬·쿼터니언의 장단 비교
- [ ] Normal Transformation / 법선벡터가 역전치로 변환되는 이유
- [ ] Barycentric Coordinates / 삼각형 내부 보간을 좌표로 처리

## 13. Numerical Reality

- [ ] Floating Point Error / 소거법에서 오차가 폭발하는 지점 재현
- [ ] Condition Number / 조건수로 문제의 민감도 재기
- [ ] Iterative Methods / 큰 행렬에서 직접법 대신 반복법을 쓰는 이유
- [ ] Sparse Matrices / 희소행렬 저장 방식과 연산 비용

---

# 이 로드맵 밖

- 극한·다변수 미분·야코비안 `academics/math/calculus.md`
- 공분산·회귀·주성분의 통계적 해석 `academics/math/statistics.md`
- 그래프의 인접행렬·유한체 `academics/math/discrete-math.md`
