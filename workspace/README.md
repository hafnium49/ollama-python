# Ollama Chatbot

A Python chatbot application using the Ollama API for conversational AI.

## Features

- Interactive command-line chatbot
- Conversation history management
- Streaming responses
- Environment-based configuration
- Simple and extensible design

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key:**
   Make sure your `.env` file contains your Ollama API key:
   ```
   ollama_api_key="your_api_key_here"
   ```

## Usage

### Quick Start (Windows)
Use the PowerShell launcher script:
```powershell
.\run_chatbot.ps1
```

### Advanced Chatbot
Run the advanced chatbot with extra features:
```bash
python advanced_chatbot.py
```

**Additional features:**
- Session statistics and history management
- Conversation saving to JSON files
- Model switching capabilities
- Enhanced command system
- Timestamps for all messages

### Interactive Chatbot
Run the main chatbot application:
```bash
python chatbot.py
```

**Available commands:**
- Type any message to chat with the AI
- `clear` - Clear conversation history
- `quit`, `exit`, or `bye` - Exit the chatbot
- `Ctrl+C` - Force exit

### Simple Example
Run the basic example (based on your original code snippet):
```bash
python simple_example.py
```

## Files

- `chatbot.py` - Main interactive chatbot application
- `advanced_chatbot.py` - Advanced chatbot with extra features
- `simple_example.py` - Basic usage example
- `requirements.txt` - Python dependencies
- `run_chatbot.ps1` - PowerShell launcher script
- `.env` - Environment variables (API key)
- `README.md` - This file

## Configuration

The chatbot uses the following default settings:
- **Model:** `gpt-oss:120b`
- **Host:** `https://ollama.com`
- **Streaming:** Enabled

You can modify these settings in the code as needed.

## Example Conversation

```
🤖 Ollama Chatbot initialized successfully!
Type 'quit', 'exit', or 'bye' to end the conversation.
Type 'clear' to clear conversation history.
--------------------------------------------------

👤 You: Hello! How are you?
🤖 Assistant: Hello! I'm doing well, thank you for asking. I'm here and ready to help you with any questions or tasks you might have. How are you doing today?

👤 You: Can you explain quantum computing?
🤖 Assistant: Quantum computing is a revolutionary approach to computation that harnesses the principles of quantum mechanics...

👤 You: quit
👋 Goodbye!
```

## Error Handling

The chatbot includes error handling for:
- Missing API keys
- Network connectivity issues
- API errors
- Invalid user input

## Customization

You can easily customize the chatbot by:
- Changing the model in the `chat()` method
- Modifying the conversation history management
- Adding new commands
- Implementing different output formats
