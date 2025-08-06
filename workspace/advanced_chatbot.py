import os
import json
from datetime import datetime
from dotenv import load_dotenv
from ollama import Client

class AdvancedOllamaChatbot:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Get API key from environment
        api_key = os.getenv('ollama_api_key')
        if not api_key:
            raise ValueError("API key not found. Please check your .env file.")
        
        # Initialize Ollama client
        self.client = Client(
            host="https://ollama.com",
            headers={'Authorization': api_key}
        )
        
        # Configuration
        self.model = 'gpt-oss:120b'
        self.max_history = 20  # Limit conversation history
        
        # Initialize conversation history
        self.conversation_history = []
        self.session_start = datetime.now()
        
        # Available models (you can expand this list)
        self.available_models = [
            'gpt-oss:120b',
            'llama2',
            'mistral',
            'codellama'
        ]
        
        self.show_welcome_message()

    def show_welcome_message(self):
        """Display welcome message and available commands"""
        print("🤖 Advanced Ollama Chatbot initialized successfully!")
        print(f"📅 Session started: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🎯 Current model: {self.model}")
        print()
        print("Available commands:")
        print("  • Type any message to chat")
        print("  • 'help' - Show this help message")
        print("  • 'clear' - Clear conversation history")
        print("  • 'history' - Show conversation history")
        print("  • 'save' - Save conversation to file")
        print("  • 'model <name>' - Change AI model")
        print("  • 'models' - List available models")
        print("  • 'stats' - Show session statistics")
        print("  • 'quit', 'exit', or 'bye' - End conversation")
        print("-" * 60)

    def add_message(self, role, content):
        """Add a message to the conversation history with timestamp"""
        message = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        }
        self.conversation_history.append(message)
        
        # Limit history to prevent context overflow
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("🧹 Conversation history cleared!")

    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("📝 No conversation history yet.")
            return
        
        print("📝 Conversation History:")
        print("-" * 40)
        for i, msg in enumerate(self.conversation_history, 1):
            role_icon = "👤" if msg['role'] == 'user' else "🤖"
            timestamp = datetime.fromisoformat(msg['timestamp']).strftime('%H:%M:%S')
            print(f"{i}. [{timestamp}] {role_icon} {msg['role'].title()}: {msg['content'][:100]}{'...' if len(msg['content']) > 100 else ''}")
        print("-" * 40)

    def save_conversation(self):
        """Save conversation to a JSON file"""
        if not self.conversation_history:
            print("📝 No conversation to save.")
            return
        
        filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        
        data = {
            'session_start': self.session_start.isoformat(),
            'model': self.model,
            'conversation': self.conversation_history
        }
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 Conversation saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving conversation: {str(e)}")

    def change_model(self, model_name):
        """Change the AI model"""
        if model_name in self.available_models:
            self.model = model_name
            print(f"🎯 Model changed to: {model_name}")
        else:
            print(f"❌ Model '{model_name}' not available.")
            print(f"Available models: {', '.join(self.available_models)}")

    def show_models(self):
        """Show available models"""
        print("🎯 Available models:")
        for i, model in enumerate(self.available_models, 1):
            current = " (current)" if model == self.model else ""
            print(f"  {i}. {model}{current}")

    def show_stats(self):
        """Show session statistics"""
        duration = datetime.now() - self.session_start
        user_messages = len([msg for msg in self.conversation_history if msg['role'] == 'user'])
        ai_messages = len([msg for msg in self.conversation_history if msg['role'] == 'assistant'])
        
        print("📊 Session Statistics:")
        print(f"  • Session duration: {str(duration).split('.')[0]}")
        print(f"  • Current model: {self.model}")
        print(f"  • Total messages: {len(self.conversation_history)}")
        print(f"  • User messages: {user_messages}")
        print(f"  • AI responses: {ai_messages}")
        print(f"  • History limit: {self.max_history}")

    def chat(self, user_input):
        """Send a message and get response from Ollama"""
        try:
            # Add user message to history (only role and content for API)
            self.add_message('user', user_input)
            
            # Prepare messages for API (without timestamps)
            api_messages = [{'role': msg['role'], 'content': msg['content']} 
                          for msg in self.conversation_history]
            
            # Get response from Ollama API
            print("🤖 Assistant: ", end='', flush=True)
            
            response_content = ""
            for part in self.client.chat(self.model, messages=api_messages, stream=True):
                content = part['message']['content']
                print(content, end='', flush=True)
                response_content += content
            
            print()  # New line after response
            
            # Add assistant response to history
            self.add_message('assistant', response_content)
            
            return response_content
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None

    def process_command(self, user_input):
        """Process special commands"""
        parts = user_input.strip().split()
        command = parts[0].lower()
        
        if command == 'help':
            self.show_welcome_message()
        elif command == 'clear':
            self.clear_history()
        elif command == 'history':
            self.show_history()
        elif command == 'save':
            self.save_conversation()
        elif command == 'model' and len(parts) > 1:
            self.change_model(parts[1])
        elif command == 'models':
            self.show_models()
        elif command == 'stats':
            self.show_stats()
        else:
            return False  # Not a command, treat as regular message
        
        return True  # Command processed

    def run(self):
        """Main chat loop"""
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye! Thanks for chatting!")
                    break
                
                # Process special commands
                if self.process_command(user_input):
                    continue
                
                # Send message and get response
                self.chat(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {str(e)}")

def main():
    try:
        # Create and run chatbot
        chatbot = AdvancedOllamaChatbot()
        chatbot.run()
    except Exception as e:
        print(f"❌ Failed to initialize chatbot: {str(e)}")

if __name__ == "__main__":
    main()
