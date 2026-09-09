# TensorFlow `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to TensorFlow

## 1. What is TensorFlow?

### Overview of TensorFlow

- [ ] End-to-End ML Platform / 데이터부터 배포까지 한 프레임워크로 묶는 방식
- [ ] Graph-based Computation / 연산을 그래프로 굳혀 최적화·배포하는 방식
- [ ] Eager Execution by Default / 그래프 빌드 없이 즉시 계산하는 기본 모드
- [ ] TF 1.x vs TF 2.x Differences / 세션 그래프 방식에서 즉시 실행 기본으로 바뀐 차이

### Ecosystem at a Glance

- [ ] Keras / 층·compile·fit으로 학습 루프를 대신 돌리는 고수준 API
- [ ] tf.data / 대용량 데이터를 배치·전처리하는 입력 파이프라인
- [ ] TensorBoard / 학습 로그를 시각화해 보는 도구
- [ ] TF Serving, TFLite, TF.js / 서버·모바일·브라우저용 배포 제품군
- [ ] TFX / 데이터 검증부터 배포까지 잇는 파이프라인 프레임워크

### TensorFlow vs PyTorch

- [ ] Deployment and Mobile Strengths / SavedModel·TFLite로 제품에 실기 쉬운 강점
- [ ] Selection Criteria / 연구는 동적성, 제품화는 표준 포맷 기준으로 고르는 법

## 2. Getting Started

### Installation `택 1`

- [ ] pip + venv / 가상환경에 pip로 설치하는 표준 방법 `추천`
- [ ] Conda / 패키지·환경을 함께 관리하는 설치 방법
- [ ] Docker GPU Image / GPU 드라이버 설정을 컨테이너에 담아 쓰는 방법
- [ ] Google Colab and Kaggle / GPU를 공짜로 빌려 노트북에서 돌리는 환경

### Runtime Environment

- [ ] Device Discovery / list_physical_devices로 잡힌 GPU를 확인하는 방법
- [ ] CUDA and cuDNN Version Matching / GPU 드라이버·라이브러리 버전을 맞추는 일
- [ ] Device Placement / tf.device로 연산을 어느 장치에서 돌릴지 지정
- [ ] GPU Memory Growth Configuration / GPU 메모리를 필요한 만큼만 늘려 잡는 설정

## 3. Tensor Fundamentals

### Tensor Basics

- [ ] tf.constant and tf.Variable / 값이 고정된 텐서와 학습으로 갱신되는 텐서의 차이
- [ ] dtype, shape, rank / 텐서의 자료형·형태·차원 수를 나타내는 속성
- [ ] Specialized Tensors / 길이가 다르거나 희소하거나 문자열인 텐서 형태

### Operators

- [ ] Element-wise Ops / add·multiply 등 원소 단위로 계산하는 연산
- [ ] Reduction / reduce_sum·argmax처럼 축을 따라 값을 줄이는 연산
- [ ] Matrix Ops / matmul·einsum 같은 행렬 연산
- [ ] Shape Manipulation / reshape·concat처럼 텐서 형태를 바꾸는 연산
- [ ] Indexing & Slicing / gather·where로 조건에 맞는 값만 뽑는 방법
- [ ] Broadcasting Rules / 크기가 다른 텐서를 자동으로 맞춰 연산하는 규칙
- [ ] NumPy Interop / .numpy()·convert_to_tensor로 넘파이와 오가는 방법

---

# PART 2 · Data and Models

## 4. tf.data Input Pipeline

### Dataset Creation

- [ ] from_tensor_slices / 배열·텐서를 그대로 Dataset으로 만드는 방법
- [ ] from_generator / 파이썬 제너레이터에서 Dataset을 만드는 방법
- [ ] File-based / TFRecordDataset·TextLineDataset처럼 파일에서 바로 읽는 방식

### Transformations

- [ ] map / num_parallel_calls로 전처리를 병렬로 돌리는 변환
- [ ] batch and padded_batch / 데이터를 묶고 길이를 맞춰 패딩까지 하는 배치 방식
- [ ] shuffle and repeat / 순서를 섞고 에폭을 반복하게 하는 설정
- [ ] Subset Selection / filter·take·skip으로 데이터 일부만 고르는 방법

### Pipeline Performance

- [ ] prefetch / AUTOTUNE으로 다음 배치를 미리 준비해 두는 최적화
- [ ] interleave / 여러 파일을 번갈아 읽어 병렬화하는 방법
- [ ] cache / 한 번 처리한 데이터를 메모리·디스크에 저장해 재사용
- [ ] Deterministic Order Tradeoff / 순서 보장과 병렬 처리 속도 사이의 절충

### Data Formats and Preprocessing

- [ ] TFRecord / tf.train.Example 구조로 직렬화하는 표준 저장 포맷
- [ ] tf.io Parsing / parse_example로 직렬화된 데이터를 복원하는 방법
- [ ] tf.image Preprocessing / 이미지 크기 조정·증강을 그래프 안에서 처리
- [ ] Keras Preprocessing Layers / Normalization·TextVectorization처럼 모델에 내장하는 전처리 층

## 5. Keras Model Building

### Model Definition Styles `택 1`

- [ ] Sequential API / 층을 순서대로 쌓기만 하는 가장 단순한 정의 방식
- [ ] Functional API / 입출력을 그래프로 연결해 분기·다중 입력을 표현 `추천`
- [ ] Model Subclassing / 클래스를 상속해 call을 직접 짜는 정의 방식

### Key Layers

- [ ] Core Layers / Dense·Dropout·Flatten 같은 기본 층
- [ ] Convolution / Conv2D·MaxPooling2D로 이미지 특징을 뽑는 층
- [ ] Recurrent / LSTM·GRU로 순서 있는 데이터를 처리하는 층
- [ ] Attention / MultiHeadAttention으로 입력 간 연관성을 학습하는 층
- [ ] Normalization / BatchNormalization·LayerNormalization으로 분포를 안정
- [ ] Embedding / 정수 인덱스를 밀집 벡터로 바꾸는 층

### Model Components

- [ ] Initializers / 가중치의 초기값을 정하는 방식
- [ ] Activations / 층 출력에 비선형성을 넣는 함수
- [ ] Regularizers / L1, L2로 가중치 크기에 페널티를 주는 방법
- [ ] Constraints / 학습 중 가중치 값 범위를 제한하는 방법

### Model Inspection

- [ ] model.summary() / 층 구조와 파라미터 수를 표로 보는 방법
- [ ] Layer and Weight Access / 층 객체와 가중치 텐서를 코드로 꺼내 보는 방법

## 6. Training with Keras

### compile

- [ ] Optimizers / SGD, Adam, AdamW 중 가중치 갱신 알고리즘을 고르는 것
- [ ] Losses / 내장 손실 함수를 쓰거나 직접 정의하는 방법
- [ ] Metrics / 배치마다 상태를 누적해 계산하는 지표 객체

### fit

- [ ] fit, evaluate, predict / 학습·평가·추론을 실행하는 세 메서드
- [ ] validation_split, validation_data / 검증 데이터를 비율로 떼거나 직접 지정
- [ ] class_weight, sample_weight / 클래스나 샘플마다 손실 가중치를 다르게 주는 옵션

### Callbacks

- [ ] ModelCheckpoint / 학습 중 가중치를 주기적으로 저장하는 콜백
- [ ] EarlyStopping / 지표가 나아지지 않으면 학습을 조기 종료하는 콜백
- [ ] ReduceLROnPlateau / 지표가 정체되면 학습률을 낮추는 콜백
- [ ] TensorBoard / 학습 로그를 자동으로 기록해 시각화하는 콜백
- [ ] LearningRateScheduler / 에폭·스텝에 따라 학습률을 규칙대로 바꾸는 콜백
- [ ] Custom Callback / on_epoch_end 등을 오버라이드해 만드는 콜백

---

# PART 3 · Low-Level Control

## 7. Automatic Differentiation

- [ ] tf.GradientTape / 연산을 기록해 그래디언트를 계산하는 명시적 방식
- [ ] watch and persistent Tape / 상수를 감시 대상에 넣고 테이프를 재사용
- [ ] Higher-order Gradients / 그래디언트의 그래디언트를 구하는 방법
- [ ] stop_gradient / 특정 텐서로 역전파가 흘러가지 않게 막는 함수
- [ ] Gradient Clipping / 그래디언트 크기를 제한해 폭주를 막는 방법
- [ ] apply_gradients / 계산된 그래디언트로 옵티마이저가 가중치를 갱신

## 8. Custom Training Loop

- [ ] train_step Override / fit은 유지하면서 학습 스텝만 바꾸는 방법
- [ ] Fully Manual Loop / fit 없이 순전파·역전파를 직접 짜는 루프
- [ ] Manual Metric Update and Reset / 지표를 스텝마다 갱신하고 에폭 끝에 초기화
- [ ] Custom Layer / build, call을 직접 정의해 만드는 층
- [ ] Custom Model / Model 클래스를 상속해 forward 흐름을 직접 짜는 방식
- [ ] Custom Loss and Metric / 내장에 없는 손실·지표를 직접 구현하는 방법
- [ ] Custom Optimizer / 가중치 갱신 규칙을 직접 정의하는 옵티마이저
- [ ] get_config and Serialization / 커스텀 객체를 저장·복원 가능하게 만드는 설정

## 9. Graph Execution & Performance

- [ ] tf.function / 파이썬 함수를 그래프로 컴파일하는 데코레이터
- [ ] AutoGraph / 파이썬 제어문을 그래프 연산으로 자동 변환하는 기능
- [ ] Tracing and Retracing / 입력 형태가 바뀔 때마다 그래프를 다시 그리는 문제
- [ ] input_signature / 입력 형태를 고정해 불필요한 재추적을 막는 옵션
- [ ] Python Side Effect Pitfalls / print 등 그래프 밖 부작용이 한 번만 실행되는 함정
- [ ] XLA / jit_compile로 연산을 더 최적화된 커널로 컴파일
- [ ] Mixed Precision / float16·bfloat16을 섞어 속도·메모리를 아끼는 방식
- [ ] Profiler / TensorBoard Profile로 병목 구간을 찾는 도구

## 10. Distributed Training

- [ ] tf.distribute.Strategy Overview / 분산 학습 방식을 통일된 API로 감싸는 개념
- [ ] MirroredStrategy / 한 머신의 여러 GPU에 모델을 복제해 동기 학습 `추천`
- [ ] MultiWorkerMirroredStrategy / 여러 머신에 걸쳐 동기 데이터 병렬 학습
- [ ] TPUStrategy / TPU 클러스터에서 분산 학습을 돌리는 전략
- [ ] ParameterServerStrategy / 파라미터 서버와 워커를 나눠 비동기 학습
- [ ] Global Batch Size and Loss Reduction / 장치별 손실을 어떻게 합산할지 정하는 것
- [ ] Distributed Dataset / 데이터를 각 장치에 자동으로 나눠 배분하는 Dataset

---

# PART 4 · Deployment and Operations

## 11. Saving and Loading

- [ ] Checkpoint / tf.train.Checkpoint로 가중치만 저장·복원하는 방식
- [ ] Keras Format / .keras 확장자로 모델 전체를 한 파일에 담는 포맷
- [ ] SavedModel Format / 그래프·가중치를 함께 담아 배포에 쓰는 표준 포맷
- [ ] Signatures / serving_default로 배포 시 입출력 계약을 정하는 것
- [ ] Custom Object Restoration / custom_objects로 직접 만든 층·손실을 복원

## 12. Serving and Inference

- [ ] TensorFlow Serving / SavedModel을 API 서버로 띄워 서빙하는 도구
- [ ] REST and gRPC Endpoint / 서빙 서버가 여는 두 가지 요청 방식
- [ ] Model Versioning / 여러 버전의 모델을 동시에 서빙·전환하는 방법
- [ ] Server-side Batching Configuration / 요청을 모아 한 번에 추론해 처리량을 올리는 설정

## 13. On-Device and Web

- [ ] TensorFlow Lite / LiteRT라는 이름으로 이어지는 모바일·엣지용 런타임
- [ ] TFLiteConverter / SavedModel을 경량 TFLite 포맷으로 변환하는 도구
- [ ] Quantization / PTQ, QAT로 가중치를 저정밀도로 줄여 경량화
- [ ] Pruning and Weight Clustering / 불필요한 가중치를 없애거나 값을 군집화해 압축
- [ ] TensorFlow.js / 브라우저·Node에서 모델을 돌리는 자바스크립트 런타임

## 14. Transfer Learning

- [ ] Keras Applications / ResNet 등 사전 학습된 모델을 바로 불러오는 모듈
- [ ] KerasHub and TensorFlow Hub / 사전 학습 모델을 공유·재사용하는 저장소
- [ ] Feature Extraction vs Fine-tuning / 사전 학습 층을 얼릴지 마저 학습할지의 차이
- [ ] Layer Freezing / trainable 속성으로 층 학습 여부를 고정하는 방법
- [ ] Data Augmentation Layers / 회전·반전 등 증강을 모델 안 층으로 넣는 방식

## 15. TFX Pipeline `선택`

- [ ] ExampleGen and StatisticsGen / 데이터를 읽어들이고 통계를 뽑는 단계
- [ ] Transform / 학습·서빙에 동일하게 적용할 전처리를 정의하는 단계
- [ ] Trainer and Tuner / 모델을 학습시키고 하이퍼파라미터를 튜닝하는 단계
- [ ] Evaluator and Model Validation / 새 모델의 배포 가능 여부를 검증하는 단계
- [ ] Pusher / 검증을 통과한 모델을 서빙 위치로 내보내는 단계

## 16. Debugging and Reproducibility

- [ ] run_eagerly=True / 그래프 없이 한 줄씩 실행해 디버깅하는 옵션
- [ ] NaN and Inf Tracking / enable_check_numerics로 값이 터진 지점을 찾는 방법
- [ ] Seed Fixing / set_seed로 난수를 고정해 실험을 재현하는 방법
- [ ] Determinism Options / GPU 연산까지 완전히 결정적으로 만드는 설정
- [ ] TensorBoard Log Reading / 기록된 로그를 읽어 학습 곡선을 확인하는 방법

---

# 이 로드맵 밖

- 머신러닝 이론 · 신경망 구조 `software/role-based/machine-learning.md`
- PyTorch `software/skill-based/AI/pytorch.md`
- Python `software/skill-based/Languages/python.md`
- 데이터 분석 라이브러리 `software/skill-based/Data-DB/python-data-analysis.md`
- 모델 운영 · 배포 파이프라인 `software/role-based/mlops.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
