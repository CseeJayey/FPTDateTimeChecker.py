@echo off

REM Check if Python is installed
python --version >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /B 1
)

REM Check if pip is installed
pip --version >nul 2>nul
if errorlevel 1 (
    echo pip is not installed. Please install pip and try again.
    exit /B 1
)

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo requirements.txt not found. Please create a requirements.txt file and try again.
    exit /B 1
)

REM Install requirements from requirements.txt
echo Checking and installing requirements from requirements.txt...
pip install -r requirements.txt

REM Run Tests
python -m unittest discover

pause