"""
Simple example of using the Ollama API
Based on the provided code snippet
"""

import os
from dotenv import load_dotenv
from ollama import Client

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key from .env file
    api_key = os.getenv('ollama_api_key')
    if not api_key:
        print("❌ Error: API key not found in .env file")
        return
    
    # Initialize client
    client = Client(
        host="https://ollama.com",
        headers={'Authorization': api_key}
    )
    
    # Sample conversation
    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ]
    
    print("🤖 Assistant: ", end='', flush=True)
    
    # Stream the response
    for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)
    
    print()  # New line at the end

if __name__ == "__main__":
    main()
