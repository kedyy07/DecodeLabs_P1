# chatbot.py
# Artificial Intelligence Project 1 - DecodeLabs
# Rule-Based AI Chatbot

def main():
    print("Welcome to the DecodeLabs Rule-Based AI Chatbot!")
    print("Type 'exit' to end the conversation.\n")

    # KNOWLEDGE BASE: Dictionary with 5+ intents for O(1) lookup efficiency
    responses = {
        'hello': 'Hi there! How can I help you today?',
        'hi': 'Hello! Welcome to the system.',
        'how are you': 'I am just a deterministic logic engine, but I am operating at 100% efficiency!',
        'what is your name': 'I am the Project 1 Rule-Based Chatbot.',
        'what is ai': 'AI (Artificial Intelligence) is the simulation of human intelligence by machines.',
        'who created you': 'I was created by an AI Engineer intern at DecodeLabs.',
        'help': 'I can respond to basic greetings and questions about my identity. Try saying "hello" or "what is ai".',
        'bye': 'Goodbye! Have a great day!'
    }

    # THE INFINITE LOOP
    while True:
        # INPUT & SANITIZATION
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # EXIT STRATEGY (Kill Command)
        if clean_input == 'exit':
            print("Chatbot: Shutting down. Goodbye!")
            break
        
        # Skip empty inputs if the user just presses Enter
        if not clean_input:
            continue

        # INTENT MATCHING & FALLBACK
        # Using the .get() method for atomic lookup and fallback
        reply = responses.get(clean_input, "I do not understand. Could you please rephrase?")
        
        # RESPONSE ENGINE (Output)
        print(f"Chatbot: {reply}")

if __name__ == "__main__":
    main()