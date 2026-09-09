# PyTorch `AI 생성`

> AI가 작성한 로드맵 · roadmap.sh 원본 아님 · 2026-08-22

# PART 1 · Introduction to PyTorch

## 1. What is PyTorch?

### Overview of PyTorch

- [ ] Define-by-Run / 코드를 실행하면서 그래프가 그때그때 생기는 방식
- [ ] Pythonic API / 넘파이·클래스 문법 그대로 모델을 짜는 인터페이스
- [ ] Research-First Ecosystem / 논문 재현·실험 속도에 맞춘 생태계
- [ ] PyTorch 2.x / torch.compile로 그래프를 미리 컴파일하는 시대

### Ecosystem at a Glance

- [ ] torchvision, torchaudio, torchtext / 비전·오디오·텍스트 전용 서브패키지
- [ ] TorchServe and ExecuTorch / 서버·온디바이스로 학습된 모델을 내보내는 경로
- [ ] PyTorch Lightning / 학습 루프를 대신 짜주는 상위 프레임워크
- [ ] Hugging Face Integration / 사전학습 모델을 바로 불러쓰는 연동

### PyTorch vs TensorFlow

- [ ] Debugging and Flexibility Comparison / 즉시 실행 디버깅과 유연성 비교
- [ ] Selection Criteria / 연구냐 배포냐로 프레임워크 고르는 기준

## 2. Getting Started

### Installation `택 1`

- [ ] pip + venv / 가상환경에 패키지만 설치하는 방법 `추천`
- [ ] Conda / 파이썬과 CUDA 버전까지 같이 관리하는 방법
- [ ] Docker GPU Image / CUDA 드라이버까지 컨테이너에 박아두는 방법
- [ ] Google Colab and Kaggle / GPU를 공짜로 빌려 노트북에서 돌리는 환경

### Runtime Environment

- [ ] CUDA Build Matching / is_available로 GPU 빌드가 맞는지 확인하는 방법
- [ ] Device Object / cuda·cpu·mps 중 연산 장치를 고르는 객체
- [ ] .to(device) Transfer Rules / 텐서·모델을 장치 간 옮기는 규칙
- [ ] GPU Memory Inspection / memory_allocated·empty_cache로 점유량 확인하는 방법

## 3. Tensor Basics

### Tensor Creation

- [ ] Creation Functions / tensor·zeros·ones·arange·randn로 텐서 만드는 방법
- [ ] dtype, device, requires_grad / 텐서 생성 시 지정하는 핵심 속성 3가지
- [ ] NumPy Bridge / from_numpy·.numpy()로 메모리를 공유해 변환하는 방법

### Operators

- [ ] Element-wise Ops / add·mul·pow·clamp처럼 원소마다 적용하는 연산
- [ ] Reduction / sum·mean·max·argmax로 차원을 줄이는 연산
- [ ] Matrix Ops / matmul·@·bmm·einsum으로 행렬을 곱하는 방법
- [ ] Shape Manipulation / view·reshape·permute로 텐서 형태를 바꾸는 방법
- [ ] Concatenation / cat·stack·split·chunk로 텐서를 합치고 나누는 방법
- [ ] Indexing / masked_select·gather로 조건부 원소를 뽑는 방법
- [ ] Broadcasting Rules / 크기가 다른 텐서를 자동 확장해 연산하는 규칙
- [ ] In-place Ops / add_처럼 언더스코어가 붙으면 원본을 바꾸는 연산

### Memory Model

- [ ] Contiguity / contiguous()로 메모리 배치를 순서대로 맞추는 방법
- [ ] View vs Copy / 메모리를 공유하는지 새로 복사하는지의 차이
- [ ] Storage and Stride / 실제 메모리 블록과 건너뛰는 간격 구조

---

# PART 2 · Models and Training

## 4. Autograd

- [ ] Computational Graph / grad_fn으로 연산 이력을 추적하는 그래프
- [ ] backward() / 그래프를 거슬러 그래디언트를 계산하는 호출
- [ ] .grad Accumulation and zero_grad / 그래디언트가 누적되니 매 스텝 비우는 규칙
- [ ] detach() and no_grad() / 그래프 추적을 끊거나 잠시 멈추는 방법
- [ ] inference_mode() / no_grad보다 더 빠른 추론 전용 모드
- [ ] torch.autograd.grad / .grad 없이 그래디언트 값만 바로 얻는 함수
- [ ] Gradient Clipping / clip_grad_norm_으로 그래디언트 폭주를 막는 방법
- [ ] retain_graph and create_graph / backward를 여러 번 부르기 위한 옵션
- [ ] Anomaly Detection / detect_anomaly로 NaN 발생 지점을 추적하는 기능

## 5. Building Models

### nn.Module

- [ ] __init__ and forward / 가중치를 정의하고 계산 순서를 쓰는 두 메서드
- [ ] Parameter vs Buffer / 학습되는 값과 학습 안 되는 상태값의 차이
- [ ] Module Containers / Sequential·ModuleList로 레이어를 묶는 방법
- [ ] state_dict Structure / 모든 파라미터를 이름-텐서 사전으로 담는 구조
- [ ] train() and eval() / Dropout·BatchNorm 동작이 바뀌는 모드 전환
- [ ] apply / 모든 서브모듈에 초기화 함수를 재귀 적용하는 방법

### Key Layers

- [ ] Linear, Dropout, Flatten / 완전연결·드롭아웃·평탄화 기본 레이어
- [ ] Convolution / Conv2d·MaxPool2d로 이미지 특징을 뽑는 레이어
- [ ] Recurrent / LSTM·GRU로 순서 있는 데이터를 처리하는 레이어
- [ ] Attention / MultiheadAttention으로 토큰 간 관계를 계산하는 레이어
- [ ] Normalization / BatchNorm·LayerNorm으로 분포를 맞추는 레이어
- [ ] Embedding / 정수 인덱스를 벡터로 바꾸는 조회 테이블

### Loss and Optimizer

- [ ] Loss Modules / CrossEntropyLoss 등 손실 함수를 담은 모듈
- [ ] Optimizers / SGD·Adam·AdamW로 파라미터를 갱신하는 알고리즘
- [ ] Parameter Groups / 레이어마다 학습률을 다르게 주는 방법
- [ ] LR Scheduler / StepLR·CosineAnnealing으로 학습률을 조절하는 방법

## 6. Data Loading

- [ ] Dataset / __len__·__getitem__을 구현해 데이터를 정의하는 클래스
- [ ] IterableDataset / 인덱싱 없이 스트리밍으로 순회하는 데이터셋
- [ ] DataLoader / batch_size·shuffle로 배치를 자동 생성하는 클래스
- [ ] collate_fn Customization / 샘플들을 배치 텐서로 묶는 방식을 직접 정의
- [ ] Sampler / WeightedRandomSampler로 샘플 뽑는 순서를 조절하는 방법
- [ ] num_workers and pin_memory / 데이터 로딩을 병렬화·고정메모리화하는 옵션
- [ ] torchvision.transforms / 이미지를 자르고 정규화하는 전처리 파이프라인
- [ ] Train and Val Split / 검증용으로 데이터 일부를 떼어놓는 방법

## 7. Training Loop

- [ ] Standard Five-Step Loop / forward·loss·backward·step 5단계 순서
- [ ] Epoch and Step / 전체 순회와 배치 단위를 구분하는 단위
- [ ] Validation Loop / 그래디언트 없이 검증 성능만 재는 루프
- [ ] Gradient Accumulation / 여러 스텝의 그래디언트를 모아 큰 배치처럼 쓰는 방법
- [ ] Custom nn.Module Authoring / 표준 레이어에 없는 계산을 직접 클래스로 짜는 방법
- [ ] Custom Loss Authoring / 문제에 맞는 손실 함수를 직접 정의하는 방법
- [ ] Forward and Backward Hook / 중간 레이어의 입출력·그래디언트를 가로채는 함수

## 8. Evaluation and Checkpointing

- [ ] state_dict Save and Load / 파라미터만 저장해뒀다 나중에 불러오는 방법
- [ ] Optimizer and Scheduler State / 재개 학습을 위해 옵티마이저 상태까지 저장
- [ ] Resume Training / 저장된 체크포인트에서 학습을 이어가는 방법
- [ ] Best Model Selection and Early Stopping / 검증 성능 기준으로 저장·중단을 직접 짜는 로직
- [ ] TensorBoard / SummaryWriter로 학습 곡선을 로그로 남기는 도구
- [ ] Weights & Biases / 실험을 클라우드에 기록·비교하는 외부 도구 `선택`
- [ ] torchmetrics / 정확도·F1 등 평가지표를 계산해주는 라이브러리 `선택`

---

# PART 3 · Performance and Scaling

## 9. Performance Optimization

- [ ] torch.compile / 모델을 그래프로 컴파일해 속도를 높이는 기능
- [ ] Mixed Precision / autocast·GradScaler로 fp16 연산을 섞는 방법
- [ ] channels_last Memory Format / 합성곱 연산에 유리하게 채널을 배치하는 형식
- [ ] cudnn.benchmark / 입력 크기가 고정일 때 최적 커널을 자동 탐색하는 옵션
- [ ] DataLoader Bottleneck Diagnosis / GPU가 데이터 대기로 노는지 확인하는 방법
- [ ] torch.profiler / 연산별 시간·메모리 사용량을 측정하는 도구
- [ ] CUDA Graphs / 커널 실행 순서를 캡처해 반복 재생하는 기능 `선택`
- [ ] Gradient Checkpointing / 활성값을 버렸다 역전파 때 재계산해 메모리 절약

## 10. Distributed Training

- [ ] DataParallel vs DistributedDataParallel / 단일 프로세스와 프로세스별 병렬 학습의 차이
- [ ] DDP / 프로세스마다 모델을 복제해 그래디언트를 동기화하는 방식 `추천`
- [ ] torchrun / Process Group으로 여러 프로세스를 묶어 실행하는 명령
- [ ] DistributedSampler / 데이터를 프로세스마다 겹치지 않게 나누는 샘플러
- [ ] Backend / NCCL·Gloo 중 통신 방식을 고르는 설정
- [ ] FSDP / 파라미터를 프로세스마다 쪼개 저장하는 샤딩 학습
- [ ] Multi-node Launch / 여러 서버에 걸쳐 학습을 띄우는 방법

## 11. Extending PyTorch

- [ ] Custom autograd.Function / forward·backward를 직접 정의하는 저수준 연산
- [ ] Custom Sampler and Dataset / 기본 클래스 대신 직접 순회 로직을 짜는 방법
- [ ] register_buffer Usage / 학습은 안 되지만 저장은 되는 값을 등록하는 방법
- [ ] C++ and CUDA Extension / 파이썬보다 빠른 연산을 네이티브 코드로 짜는 방법 `선택`
- [ ] torch.fx / 모델 그래프를 분석·변환하는 심볼릭 트레이싱 도구 `선택`

## 12. Ecosystem Libraries

- [ ] torchvision / 사전학습 모델·데이터셋을 함께 제공하는 패키지
- [ ] torchaudio / 오디오 로딩·변환·모델을 다루는 전용 패키지
- [ ] PyTorch Lightning / 학습 루프 보일러플레이트를 대신 짜주는 프레임워크 `추천`
- [ ] Hugging Face Transformers Integration / 사전학습 트랜스포머를 PyTorch로 불러쓰는 연동
- [ ] Accelerate / 분산·혼합정밀 설정을 코드 거의 그대로 적용하는 라이브러리
- [ ] PEFT / LoRA로 일부 파라미터만 얹어 가볍게 파인튜닝하는 기법 `선택`

---

# PART 4 · Deployment and Operations

## 13. Export

- [ ] TorchScript / trace·script 두 방식으로 모델을 직렬화하는 기능
- [ ] torch.export / 모델을 배포용 그래프 형식으로 내보내는 API
- [ ] ONNX Export / 다른 프레임워크에서도 쓰게 표준 형식으로 변환
- [ ] Dynamic Shape Handling / 입력 크기가 바뀌어도 대응하도록 내보내는 방법
- [ ] Export Output Verification / 내보낸 모델과 원본 출력이 같은지 대조하는 방법

## 14. Serving

- [ ] TorchServe / 모델을 REST API로 서빙해주는 전용 서버
- [ ] Model Archive / .mar 확장자로 모델·코드를 묶는 배포 단위
- [ ] Custom Handler / 요청을 받아 전처리·추론·후처리를 잇는 코드
- [ ] REST and gRPC Endpoint / 추론 요청을 받는 두 가지 통신 방식
- [ ] ONNX Runtime Inference / 별도 런타임으로 ONNX 모델을 실행하는 방법

## 15. Compression and Edge

- [ ] Quantization / Dynamic·Static·QAT로 가중치를 저정밀로 줄이는 방법
- [ ] Pruning / torch.nn.utils.prune로 불필요한 가중치를 잘라내는 방법
- [ ] Knowledge Distillation / 큰 모델의 출력을 작은 모델이 따라 배우게 하는 방법
- [ ] ExecuTorch / Mobile 기기 위에서 직접 모델을 돌리는 런타임
- [ ] Latency and Memory Benchmarking / 배포 전 속도·메모리 사용량을 재는 방법

## 16. Debugging and Reproducibility

- [ ] Shape Mismatch Diagnosis / 텐서 크기가 안 맞는 에러의 원인을 찾는 방법
- [ ] CUDA OOM Recovery / GPU 메모리 부족 에러에서 복구하는 방법
- [ ] NaN Loss Tracing / 손실값이 NaN이 되는 지점을 역추적하는 방법
- [ ] Seed Fixing / manual_seed로 난수를 고정해 재현하는 방법
- [ ] use_deterministic_algorithms / 비결정적 CUDA 연산까지 고정하는 옵션
- [ ] DataLoader Worker Reproducibility / 워커별 난수까지 고정해 로딩을 재현하는 방법

---

# 이 로드맵 밖

- 머신러닝 이론 · 신경망 구조 `software/role-based/machine-learning.md`
- TensorFlow `software/skill-based/AI/tensorflow.md`
- Python `software/skill-based/Languages/python.md`
- 데이터 분석 라이브러리 `software/skill-based/Data-DB/python-data-analysis.md`
- 모델 운영 · 실험 관리 `software/role-based/mlops.md`
- 컨테이너 실행 `software/skill-based/Infra-DevOps/docker.md`, `kubernetes.md`
