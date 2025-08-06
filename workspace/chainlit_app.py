import chainlit as cl
import json
from datetime import datetime
from advanced_chatbot import AdvancedOllamaChatbot
from typing import Dict, Any


class ChainlitOllamaChatbot:
    def __init__(self):
        self.chatbot = None
        self.session_data = {}

    async def initialize_chatbot(self):
        """Initialize the chatbot instance"""
        try:
            self.chatbot = AdvancedOllamaChatbot()
            return True
        except Exception as e:
            await cl.Message(
                content=f"❌ Failed to initialize chatbot: {str(e)}\n\nPlease make sure your .env file is configured correctly.",
                author="System"
            ).send()
            return False


# Global instance
chatbot_instance = ChainlitOllamaChatbot()


@cl.on_chat_start
async def start():
    """Initialize the chat session"""
    # Initialize chatbot
    success = await chatbot_instance.initialize_chatbot()
    
    if success:
        # Send welcome message
        welcome_text = f"""
# 🤖 Advanced Ollama Chatbot

Welcome to the Chainlit interface for your Ollama chatbot!

**Current Configuration:**
- Model: `{chatbot_instance.chatbot.model}`
- Session started: {chatbot_instance.chatbot.session_start.strftime('%Y-%m-%d %H:%M:%S')}

**Available Commands:**
- `/help` - Show help message
- `/clear` - Clear conversation history
- `/history` - Show conversation history
- `/save` - Save conversation to file
- `/model <name>` - Change AI model
- `/models` - List available models
- `/stats` - Show session statistics

Just type any message to start chatting, or use the commands above!
        """
        
        await cl.Message(content=welcome_text, author="System").send()
        
        # Store session info
        cl.user_session.set("chatbot", chatbot_instance.chatbot)
        cl.user_session.set("session_start", datetime.now())
    
    else:
        await cl.Message(
            content="❌ Failed to initialize. Please check your configuration.",
            author="System"
        ).send()


@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages"""
    chatbot = cl.user_session.get("chatbot")
    
    if not chatbot:
        await cl.Message(
            content="❌ Chatbot not initialized. Please refresh the page.",
            author="System"
        ).send()
        return
    
    user_input = message.content.strip()
    
    # Check if it's a command (starting with /)
    if user_input.startswith('/'):
        command = user_input[1:]  # Remove the '/' prefix
        await handle_command(command, chatbot)
        return
    
    # Regular chat message
    await handle_chat(user_input, chatbot)


async def handle_command(command: str, chatbot: AdvancedOllamaChatbot):
    """Handle special commands"""
    parts = command.strip().split()
    if not parts:
        return
    
    cmd = parts[0].lower()
    
    try:
        if cmd == 'help':
            help_text = """
# 📚 Help - Available Commands

**Chat Commands:**
- `/help` - Show this help message
- `/clear` - Clear conversation history
- `/history` - Show conversation history
- `/save` - Save conversation to file
- `/model <name>` - Change AI model (e.g., `/model llama2`)
- `/models` - List available models
- `/stats` - Show session statistics

**Usage:**
- Type any message without `/` to chat normally
- Commands must start with `/`
- Example: `/model gpt-oss:120b`
            """
            await cl.Message(content=help_text, author="System").send()
            
        elif cmd == 'clear':
            chatbot.clear_history()
            await cl.Message(content="🧹 Conversation history cleared!", author="System").send()
            
        elif cmd == 'history':
            if not chatbot.conversation_history:
                await cl.Message(content="📝 No conversation history yet.", author="System").send()
                return
            
            history_text = "# 📝 Conversation History\n\n"
            for i, msg in enumerate(chatbot.conversation_history, 1):
                role_icon = "👤" if msg['role'] == 'user' else "🤖"
                timestamp = datetime.fromisoformat(msg['timestamp']).strftime('%H:%M:%S')
                content_preview = msg['content'][:100] + ('...' if len(msg['content']) > 100 else '')
                history_text += f"**{i}.** `[{timestamp}]` {role_icon} **{msg['role'].title()}:** {content_preview}\n\n"
            
            await cl.Message(content=history_text, author="System").send()
            
        elif cmd == 'save':
            if not chatbot.conversation_history:
                await cl.Message(content="📝 No conversation to save.", author="System").send()
                return
            
            # Save conversation
            chatbot.save_conversation()
            await cl.Message(content="💾 Conversation saved successfully!", author="System").send()
            
        elif cmd == 'model' and len(parts) > 1:
            model_name = parts[1]
            if model_name in chatbot.available_models:
                chatbot.model = model_name
                await cl.Message(content=f"🎯 Model changed to: `{model_name}`", author="System").send()
            else:
                models_list = ', '.join([f"`{m}`" for m in chatbot.available_models])
                await cl.Message(
                    content=f"❌ Model `{model_name}` not available.\n\n**Available models:** {models_list}",
                    author="System"
                ).send()
                
        elif cmd == 'models':
            models_text = "# 🎯 Available Models\n\n"
            for i, model in enumerate(chatbot.available_models, 1):
                current = " *(current)*" if model == chatbot.model else ""
                models_text += f"{i}. `{model}`{current}\n"
            
            await cl.Message(content=models_text, author="System").send()
            
        elif cmd == 'stats':
            duration = datetime.now() - chatbot.session_start
            user_messages = len([msg for msg in chatbot.conversation_history if msg['role'] == 'user'])
            ai_messages = len([msg for msg in chatbot.conversation_history if msg['role'] == 'assistant'])
            
            stats_text = f"""
# 📊 Session Statistics

- **Session duration:** {str(duration).split('.')[0]}
- **Current model:** `{chatbot.model}`
- **Total messages:** {len(chatbot.conversation_history)}
- **User messages:** {user_messages}
- **AI responses:** {ai_messages}
- **History limit:** {chatbot.max_history}
            """
            
            await cl.Message(content=stats_text, author="System").send()
            
        else:
            await cl.Message(
                content=f"❌ Unknown command: `/{cmd}`\n\nType `/help` to see available commands.",
                author="System"
            ).send()
            
    except Exception as e:
        await cl.Message(
            content=f"❌ Error processing command: {str(e)}",
            author="System"
        ).send()


async def handle_chat(user_input: str, chatbot: AdvancedOllamaChatbot):
    """Handle regular chat messages"""
    try:
        # Add user message to history
        chatbot.add_message('user', user_input)
        
        # Prepare messages for API (without timestamps)
        api_messages = [{'role': msg['role'], 'content': msg['content']} 
                       for msg in chatbot.conversation_history]
        
        # Create assistant message that will be updated with streaming response
        assistant_message = cl.Message(content="", author="Assistant")
        await assistant_message.send()
        
        # Get streaming response from Ollama API
        response_content = ""
        
        try:
            for part in chatbot.client.chat(chatbot.model, messages=api_messages, stream=True):
                content = part['message']['content']
                response_content += content
                # Stream the content by sending new parts
                assistant_message.content = response_content
                await assistant_message.stream_token(content)
                
        except Exception as api_error:
            error_msg = f"❌ API Error: {str(api_error)}"
            await cl.Message(content=error_msg, author="System").send()
            return
        
        # Add assistant response to history
        chatbot.add_message('assistant', response_content)
        
    except Exception as e:
        await cl.Message(
            content=f"❌ Error: {str(e)}",
            author="System"
        ).send()


@cl.on_chat_end
async def end():
    """Handle chat session end"""
    chatbot = cl.user_session.get("chatbot")
    if chatbot and chatbot.conversation_history:
        # Optionally save conversation on exit
        try:
            chatbot.save_conversation()
        except:
            pass  # Ignore save errors on exit


if __name__ == "__main__":
    # This allows running the file directly for testing
    import chainlit as cl
    cl.run()
