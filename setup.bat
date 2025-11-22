@echo off
echo ============================================================
echo SHL Assessment Recommendation System - Quick Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/5] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/5] Running setup script...
python setup.py
if errorlevel 1 (
    echo Error: Setup script failed
    pause
    exit /b 1
)

echo [5/5] Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Please edit .env file and add your Google Gemini API key
)

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo To start the application:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Add your API key to .env file
echo   3. Run: python api/app.py
echo   4. Open: http://localhost:5000
echo.
pause
