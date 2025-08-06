# 🤖 Advanced Ollama Chatbot with Chainlit Frontend

Welcome to the advanced Ollama chatbot with a beautiful Chainlit web interface! This application provides a user-friendly web interface for your Ollama chatbot with features like conversation history, model switching, and session management.

## ✨ Features

- **🌐 Web Interface**: Beautiful, responsive web UI powered by Chainlit
- **💬 Real-time Streaming**: See AI responses as they're generated
- **📚 Conversation History**: Keep track of your chat history with timestamps
- **🎯 Model Switching**: Switch between different Ollama models on the fly
- **💾 Save Conversations**: Export your conversations to JSON files
- **📊 Session Statistics**: Track message counts and session duration
- **🎨 Modern UI**: Clean, professional interface with markdown support

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama API access and API key
- Internet connection

### Setup

1. **Clone and navigate to the workspace**:
   ```bash
   cd workspace
   ```

2. **Create a `.env` file** with your Ollama API key:
   ```
   ollama_api_key=your_actual_api_key_here
   ```

3. **Run the Chainlit app**:
   
   **Option 1: Using the PowerShell script (Recommended for Windows)**
   ```powershell
   .\run_chainlit.ps1
   ```

   **Option 2: Manual installation**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the Chainlit app
   chainlit run chainlit_app.py -w
   ```

4. **Open your browser** - The app will automatically open at `http://localhost:8000`

## 🎮 How to Use

### Basic Chat
- Simply type your message and press Enter to chat with the AI
- Responses are streamed in real-time for a smooth experience

### Commands
All commands start with a forward slash (`/`):

- `/help` - Show help message with all available commands
- `/clear` - Clear the conversation history
- `/history` - Display conversation history with timestamps
- `/save` - Save the current conversation to a JSON file
- `/model <name>` - Switch to a different AI model (e.g., `/model llama2`)
- `/models` - List all available models
- `/stats` - Show session statistics (duration, message counts, etc.)

### Examples

```
# Switch to a different model
/model gpt-oss:120b

# View conversation history
/history

# Save your conversation
/save

# Get session statistics
/stats
```

## 🛠️ Configuration

### Available Models
The chatbot comes pre-configured with these models:
- `gpt-oss:120b` (default)
- `llama2`
- `mistral`
- `codellama`

You can modify the available models in the `advanced_chatbot.py` file.

### Customization
- **UI Theme**: Modify `.chainlit` config file to customize colors and appearance
- **Session Settings**: Adjust timeout and caching in the config file
- **History Limit**: Change `max_history` in the chatbot class (default: 20 messages)

## 📁 File Structure

```
workspace/
├── chainlit_app.py          # Main Chainlit application
├── advanced_chatbot.py      # Core chatbot logic
├── .chainlit               # Chainlit configuration
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Python dependencies
├── run_chainlit.ps1       # PowerShell startup script
└── README.md              # This file
```

## 🔧 Troubleshooting

### Common Issues

1. **"API key not found" error**
   - Make sure your `.env` file exists and contains: `ollama_api_key=your_key_here`
   - Verify the API key is valid and has proper permissions

2. **"Import chainlit could not be resolved"**
   - Run `pip install chainlit` or use the provided script
   - Make sure you're in the correct directory

3. **Connection refused**
   - Ensure Ollama service is running and accessible
   - Check if the API endpoint is correct in the code

4. **Port already in use**
   - Chainlit uses port 8000 by default
   - Kill existing processes or specify a different port: `chainlit run chainlit_app.py -p 8080`

### Getting Help

If you encounter any issues:

1. Check the console/terminal output for error messages
2. Verify your `.env` file configuration
3. Ensure all dependencies are installed correctly
4. Check that your Ollama API key is valid and active

## 🌟 Advanced Features

### Session Management
- Conversations are automatically saved in memory during your session
- Use `/save` to export conversations to JSON files with timestamps
- Session statistics track your usage patterns

### Model Switching
- Switch between different AI models without losing conversation history
- Each model may have different capabilities and response styles
- History is preserved when switching models

### Conversation Export
Saved conversations include:
- Full message history with timestamps
- Session metadata (start time, model used)
- Structured JSON format for easy parsing

## 🤝 Contributing

This is part of the ollama-python workspace. Feel free to:
- Suggest new features
- Report bugs or issues
- Contribute improvements to the codebase

## 📄 License

This project follows the same license as the parent ollama-python repository.

---

Enjoy chatting with your advanced Ollama chatbot! 🎉
