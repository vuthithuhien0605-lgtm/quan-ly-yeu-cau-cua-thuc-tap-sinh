@echo off
echo ========================================
echo   HE THONG QUAN LY THUC TAP SINH
echo   Flask Application
echo ========================================
echo.

REM Kich hoat virtual environment neu co
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Dang khoi dong Flask server...
echo.
echo Truy cap: http://localhost:5000
echo.

REM Mo trinh duyet
start http://localhost:5000

REM Chay Flask app
python app.py

pause
