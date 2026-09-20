def chatbot():
    print("=" * 40)
    print("          BASIC CHATBOT")
    print("=" * 40)
    print("Hello! I am a simple chatbot.")
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I am doing great! Thanks for asking.")

        elif user_input == "what is your name":
            print("Bot: I am a Basic Python Chatbot.")

        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, ask my name, or say bye.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that yet.")


def main():
    chatbot()


if __name__ == "__main__":
    main()
