print("=" * 50)
print("🤖 Welcome to AI Chatbot")
print("Type 'bye' to exit.")
print("=" * 50)

responses = {
    "hello": "Hello! Welcome to DecodeLabs AI Chatbot.",
    "hi": "Hi! How can I help you today?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm a Rule-Based AI Chatbot built using Python.",
    "who created you": "I was created by Dhanik Baba for the DecodeLabs Internship.",
    "what can you do": "I can answer simple predefined questions.",
    "python": "Python is a popular programming language used for AI and Machine Learning.",
    "ai": "Artificial Intelligence enables machines to mimic human intelligence.",
    "thank you": "You're welcome! 😊",
}

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    response = responses.get(
        user,
        "Sorry, I don't understand that. Please try another question."
    )

    print("Bot:", response)