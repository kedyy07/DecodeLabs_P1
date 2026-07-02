import random
import datetime

print("=" * 55)
print("🤖 DecodeLabs AI Chatbot")
print("Type 'exit' anytime to quit.")
print("=" * 55)

greetings = [
    "Hello!",
    "Hi there!",
    "Hey! Nice to meet you.",
    "Welcome!"
]

while True:

    user = input("\nYou : ").lower().strip()

    if user in ["hello", "hi", "hey", "good morning", "good evening"]:
        print("Bot :", random.choice(greetings))

    elif "how are you" in user:
        print("Bot : I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot : I'm DecodeBot, your Rule-Based AI Assistant.")

    elif "time" in user:
        current = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot : Current time is", current)

    elif "date" in user:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's date is", today)

    elif "bye" in user or user == "exit":
        print("Bot : Goodbye! Have a wonderful day.")
        break

    elif "thank" in user:
        print("Bot : You're welcome!")

    elif "who created you" in user:
        print("Bot : I was created as part of DecodeLabs AI Project 1.")

    elif "help" in user:
        print("""
I can answer:
• Hello
• Time
• Date
• How are you
• Your name
• Who created you
• Thanks
• Exit
""")

    else:
        print("Bot : Sorry, I don't understand that yet.")
