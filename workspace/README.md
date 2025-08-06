# Ollama Python Chatbot Workspace

This workspace contains multiple implementations of Ollama chatbots, from simple examples to advanced web interfaces.

## 📁 Files Overview

### Main Chatbot Implementations
- **`advanced_chatbot.py`** - Feature-rich terminal chatbot with history, model switching, and conversation saving
- **`chatbot.py`** - Interactive terminal-based chatbot application  
- **`simple_example.py`** - Basic Ollama usage example
- **`chainlit_app.py`** - 🆕 Advanced web-based chatbot with Chainlit frontend

### Configuration & Setup
- **`.env`** - Environment variables (API keys)
- **`requirements.txt`** - Python dependencies
- **`.chainlit/`** - Chainlit configuration directory
- **`chainlit.md`** - Welcome page for the web interface

### Launchers
- **`run_chatbot.ps1`** - PowerShell script to run terminal chatbot
- **`run_chainlit.ps1`** - 🆕 PowerShell script to run web interface
- **`run_chainlit.bat`** - 🆕 Windows batch script to run web interface

## 🚀 Quick Start

### 1. Terminal Chatbot
```powershell
# Run the advanced terminal chatbot
.\run_chatbot.ps1

# Or run directly
python advanced_chatbot.py
```

### 2. Web Interface (Chainlit) - 🆕
```powershell
# Run the web interface
.\run_chainlit.ps1

# Or run directly
chainlit run chainlit_app.py
```

The web interface will be available at: **http://localhost:8000**

## ✨ Features Comparison

| Feature | Terminal Chatbot | Web Interface |
|---------|------------------|---------------|
| 🎯 Model Switching | ✅ | ✅ |
| 📚 Conversation History | ✅ | ✅ |
| 💾 Save Conversations | ✅ | ✅ |
| 📊 Session Statistics | ✅ | ✅ |
| 🌐 Web UI | ❌ | ✅ |
| 💬 Real-time Streaming | ✅ | ✅ |
| 📱 Mobile Friendly | ❌ | ✅ |
| 🎨 Modern UI | ❌ | ✅ |
| 🔄 Auto-save Session | ❌ | ✅ |

## 🎮 Usage

### Terminal Commands
- `help` - Show available commands
- `clear` - Clear conversation history
- `history` - Show conversation history
- `save` - Save conversation to file
- `model <name>` - Change AI model
- `models` - List available models
- `stats` - Show session statistics
- `quit/exit/bye` - End conversation

### Web Interface Commands
Same commands but with `/` prefix:
- `/help` - Show help
- `/clear` - Clear history
- `/history` - Show history
- `/save` - Save conversation
- `/model <name>` - Change model
- `/models` - List models
- `/stats` - Show statistics

## 🔧 Configuration

### Environment Variables (.env)
```
ollama_api_key=your_api_key_here
```

### Available Models
- `gpt-oss:120b` (default)
- `llama2`
- `mistral` 
- `codellama`

## 📋 Requirements

- Python 3.8+
- Ollama API access
- Dependencies listed in `requirements.txt`

## 🛠️ Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   - Ensure your `.env` file contains: `ollama_api_key=your_key_here`
   - Verify Ollama API access

3. **Run the application:**
   - Terminal: `python advanced_chatbot.py`
   - Web: `chainlit run chainlit_app.py`

## 📚 Documentation

For detailed documentation about the web interface, see `CHAINLIT_README.md`.

## Example Usage

### Terminal Interface
```
🤖 Advanced Ollama Chatbot initialized successfully!
📅 Session started: 2025-01-07 10:30:45
🎯 Current model: gpt-oss:120b

👤 You: Hello! How are you?
🤖 Assistant: Hello! I'm doing well, thank you for asking...

👤 You: /model llama2
🎯 Model changed to: llama2

👤 You: /stats
📊 Session Statistics:
  • Session duration: 0:05:23
  • Current model: llama2
  • Total messages: 4
```

### Web Interface
The web interface provides the same functionality in a modern, responsive web UI with:
- Real-time streaming responses
- Markdown rendering
- Mobile-friendly design
- Persistent sessions
- Easy-to-use commands

---

**Choose your preferred interface and start chatting with Ollama! 🤖**
