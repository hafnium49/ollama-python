# PowerShell script to run the Chainlit chatbot
Write-Host "🚀 Starting Advanced Ollama Chatbot with Chainlit..." -ForegroundColor Green

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠️  No virtual environment found. Creating one..." -ForegroundColor Yellow
    python -m venv venv
    & .\venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual environment created and activated." -ForegroundColor Green
}

# Install requirements
Write-Host "📥 Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "⚠️  .env file not found!" -ForegroundColor Red
    Write-Host "Please create a .env file with your Ollama API key:" -ForegroundColor Yellow
    Write-Host "ollama_api_key=your_api_key_here" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Press Enter to continue anyway or Ctrl+C to exit"
}

# Run Chainlit app
Write-Host "🌐 Starting Chainlit server..." -ForegroundColor Green
Write-Host "The app will open in your browser automatically." -ForegroundColor Cyan
Write-Host "If it doesn't open, go to: http://localhost:8000" -ForegroundColor Cyan
Write-Host ""

chainlit run chainlit_app.py -w
