from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


class ChatGPTAssistant:
    def __init__(self):
        # keep memory for context
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        print("[DEBUG] Assistant initialized")

    def process_data(self, data):
        print("\n[DEBUG] process_data() called with data:", data)

        # add user message
        self.messages.append({"role": "user", "content": data})
        print("[DEBUG] Messages before sending to API:")
        for m in self.messages:
            print("   ", m)

        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=self.messages
            )

            reply = response.choices[0].message.content.strip()
            print("[DEBUG] Raw API reply:", repr(reply))

            # add assistant reply to chat memory
            self.messages.append({"role": "assistant", "content": reply})

            print("[DEBUG] Updated messages after API call:")
            for m in self.messages:
                print("   ", m)

            return reply

        except Exception as e:
            print("[ERROR] Exception during API call:", e)
            return "failed"

    def send_data(self, data):
        print("[DEBUG] send_data() called")
        processed_data = self.process_data(data)
        print(f"[DEBUG] This is your return from ChatGPT: {processed_data}")

    def chat(self, data):
        print("[DEBUG] chat() called with:", data)
        return self.process_data(data)
