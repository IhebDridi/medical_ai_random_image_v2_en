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
                {"role": "user", "content": f"Please return the following text exactly as it is: {data}"}
            ]
        )
        return response.choices[0].message.content.strip()

    def send_data(self, data):
        return self.process_data(data)

    def chat(self, data):
        # just an alias for process_data to match chat_page() usage
        return self.process_data(data)
