import sys

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Predefined rules for matching user inputs
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I am a chatbot, doing great! How about you?"
    elif "your name" in user_input:
        return "I am a Basic Python Chatbot."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't quite understand that. Can you try asking differently?"

def main():
    print("========================================")
    print("Welcome! Type 'exit' or 'bye' to quit.")
    print("========================================")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower().strip() in ['exit', 'bye']:
                print("Bot: Goodbye!")
                break
            
            response = get_response(user_input)
            print(f"Bot: {response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

if __name__ == "__main__":
    main()
