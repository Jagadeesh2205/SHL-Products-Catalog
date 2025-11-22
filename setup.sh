#!/bin/bash

echo "============================================================"
echo "SHL Assessment Recommendation System - Quick Setup"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo "[4/5] Running setup script..."
python setup.py
if [ $? -ne 0 ]; then
    echo "Error: Setup script failed"
    exit 1
fi

echo "[5/5] Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please edit .env file and add your Google Gemini API key"
fi

echo ""
echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo ""
echo "To start the application:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Add your API key to .env file"
echo "  3. Run: python api/app.py"
echo "  4. Open: http://localhost:5000"
echo ""
