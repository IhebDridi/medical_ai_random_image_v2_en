from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


class ChatGPTAssistant:
    def __init__(self):
        pass

    def process_data(self, data):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                # You can uncomment this if you want the assistant to act more naturally
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": data}
            ]
        )
        # ✅ FIX: `response.choices[0].message.content` → correct attribute access
        return response.choices[0].message["content"].strip()

    def send_data(self, data):
        processed_data = self.process_data(data)
        print(f"This is your return from ChatGPT: {processed_data}")
