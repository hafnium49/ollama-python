#!/usr/bin/env pwsh

# Ollama Chatbot Launcher Script for PowerShell

Write-Host "🤖 Ollama Chatbot Launcher" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host ""

# Check if requirements are installed
try {
    python -c "import ollama, dotenv" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Missing dependencies. Installing..." -ForegroundColor Red
        pip install -r requirements.txt
    }
} catch {
    Write-Host "❌ Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "❌ .env file not found. Please create it with your API key." -ForegroundColor Red
    Write-Host "Example: ollama_api_key='your_key_here'" -ForegroundColor Yellow
    exit 1
}

Write-Host "Available chatbot options:" -ForegroundColor Green
Write-Host "1. Simple Example (based on your original code)"
Write-Host "2. Interactive Chatbot (basic)"
Write-Host "3. Advanced Chatbot (with extra features)"
Write-Host ""

$choice = Read-Host "Choose an option (1-3)"

switch ($choice) {
    "1" {
        Write-Host "🚀 Running Simple Example..." -ForegroundColor Green
        python simple_example.py
    }
    "2" {
        Write-Host "🚀 Starting Interactive Chatbot..." -ForegroundColor Green
        python chatbot.py
    }
    "3" {
        Write-Host "🚀 Starting Advanced Chatbot..." -ForegroundColor Green
        python advanced_chatbot.py
    }
    default {
        Write-Host "❌ Invalid choice. Please select 1, 2, or 3." -ForegroundColor Red
        exit 1
    }
}
