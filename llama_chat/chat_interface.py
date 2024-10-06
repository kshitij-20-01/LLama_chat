from typing import List

class ChatSession:
    def __init__(self):
        self.history: List[str] = []

    def get_user_input(self) -> str:
        return input("You: ").strip()

    def display_response(self, response: str):
        print(f"AI: {response}")

    def update_history(self, user_input: str, ai_response: str):
        self.history.append(f"You: {user_input}")
        self.history.append(f"AI: {ai_response}")

    def display_history(self):
        for message in self.history:
            print(message)