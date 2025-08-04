def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 ChatBot: Hi!")
        elif user_input == "how are you":
            print("🤖 ChatBot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 ChatBot: Goodbye!")
            break
        else:
            print("🤖 ChatBot: I didn't understand that.")

chatbot()
