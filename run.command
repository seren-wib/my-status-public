#!/bin/sh
# 맥에서 더블클릭으로 상태창 열기 (윈도우는 run.bat)
cd "$(dirname "$0")" || exit 1

if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "[에러] Python을 찾을 수 없습니다. python.org에서 설치한 뒤 다시 실행하세요."
  read -r _
  exit 1
fi

echo "상태창을 여는 중..."
exec "$PY" tools/serve.py 8000 --open
