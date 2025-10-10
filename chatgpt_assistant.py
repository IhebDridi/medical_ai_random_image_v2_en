from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


class ChatGPTAssistant:
    def __init__(self):
        # ✅ store chat history (so assistant knows prior messages)
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    def process_data(self, data):
        # ✅ add user message to conversation
        self.messages.append({"role": "user", "content": data})

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=self.messages
        )

        reply = response.choices[0].message.content.strip()

        # ✅ add assistant reply to memory
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def send_data(self, data):
        processed_data = self.process_data(data)
        print(f"This is your return from ChatGPT: {processed_data}")

    def chat(self, data):
        # ✅ alias for process_data (used by chat.py)
        return self.process_data(data)
