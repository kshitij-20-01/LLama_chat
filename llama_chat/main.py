import model_handler
from chat_interface import ChatSession

def main():
    print("Loading LLaMA 3.2 model...")
    model, tokenizer = model_handler.load_model()
    print("Model loaded successfully!")

    chat_session = ChatSession()

    print("Welcome to the LLaMA 3.2 Chat Interface!")
    print("Type 'quit' to exit the chat.")

    while True:
        user_input = chat_session.get_user_input()
        
        if user_input.lower() == 'quit':
            print("Thank you for chatting. Goodbye!")
            break

        response = model_handler.generate_response(model, tokenizer, user_input)
        chat_session.display_response(response)
        chat_session.update_history(user_input, response)

if __name__ == "__main__":
    main()