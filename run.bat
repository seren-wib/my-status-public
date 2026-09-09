@echo off
chcp 65001 >nul
title 내 상태창
cd /d "%~dp0"

set PY=python
where python >nul 2>nul || set PY=py
where %PY% >nul 2>nul || goto :nopython

echo 상태창을 여는 중...
%PY% "tools\serve.py" 8000 --open
if errorlevel 1 pause
exit /b

:nopython
echo.
echo [에러] Python을 찾을 수 없습니다.
echo https://www.python.org/downloads/ 에서 설치한 뒤 다시 실행하세요.
echo (설치할 때 "Add Python to PATH" 체크)
echo.
pause
