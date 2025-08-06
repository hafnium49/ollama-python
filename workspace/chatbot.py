import os
from dotenv import load_dotenv
from ollama import Client

class OllamaChatbot:
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
        
        # Initialize conversation history
        self.conversation_history = []
        
        print("🤖 Ollama Chatbot initialized successfully!")
        print("Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("Type 'clear' to clear conversation history.")
        print("-" * 50)

    def add_message(self, role, content):
        """Add a message to the conversation history"""
        self.conversation_history.append({
            'role': role,
            'content': content
        })

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("🧹 Conversation history cleared!")

    def chat(self, user_input, model='gpt-oss:120b'):
        """Send a message and get response from Ollama"""
        try:
            # Add user message to history
            self.add_message('user', user_input)
            
            # Get response from Ollama API
            print("🤖 Assistant: ", end='', flush=True)
            
            response_content = ""
            for part in self.client.chat(model, messages=self.conversation_history, stream=True):
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

    def run(self):
        """Main chat loop"""
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                
                # Send message and get response
                self.chat(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {str(e)}")

def main():
    try:
        # Create and run chatbot
        chatbot = OllamaChatbot()
        chatbot.run()
    except Exception as e:
        print(f"❌ Failed to initialize chatbot: {str(e)}")

if __name__ == "__main__":
    main()
