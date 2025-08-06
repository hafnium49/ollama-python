@echo off
echo 🚀 Starting Advanced Ollama Chatbot with Chainlit...

REM Check if virtual environment exists
if exist "venv" (
    echo 📦 Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo ⚠️ No virtual environment found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment created and activated.
)

REM Install requirements
echo 📥 Installing requirements...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️ .env file not found!
    echo Please create a .env file with your Ollama API key:
    echo ollama_api_key=your_api_key_here
    echo.
    pause
)

REM Run Chainlit app
echo 🌐 Starting Chainlit server...
echo The app will open in your browser automatically.
echo If it doesn't open, go to: http://localhost:8000
echo.

chainlit run chainlit_app.py -w
