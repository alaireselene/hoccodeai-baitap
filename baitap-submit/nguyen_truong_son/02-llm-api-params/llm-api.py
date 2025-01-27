from openai import OpenAI
import os
from typing import List, Dict

# Configure OpenAI
client = OpenAI(
    api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx",
    base_url = "https://api.deepseek.com"
)


class Chatbot:
  def __init__(self):
    self.messages: List[Dict[str, str]] = [
      {"role": "system", "content": "You are a helpful assistant that run in terminal, answer in Vietnamese for all question with concise answer. No hallucination allowed. Always double-check your answer before sending. Use normal sentence, instead of listing format like bullet point, using normal sentence."}
    ]

  def get_response(self, user_input: str) -> None:
    # Add user message to history
    self.messages.append({"role": "user", "content": user_input})

    try:
      # Create stream response
      response_stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=self.messages,
        stream=True
      )

      # Process and display the streaming response
      collected_response = []
      print("\nTrợ lý: ", end="", flush=True)
      
      for chunk in response_stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="")
        collected_response.append(content)

      print("\n")
      
      # Add assistant's response to message history
      self.messages.append({
        "role": "assistant",
        "content": "".join(collected_response)
      })

    except Exception as e:
      print(f"\nLỗi: {str(e)}\n")

def main():
  chatbot = Chatbot()
  print("Đây là chatbot AI, cảm ơn bạn đã sử dụng! (Gõ 'quit' để thoát)")
  
  while True:
    user_input = input("Người: ").strip()
    if user_input.lower() == 'quit':
      break
    chatbot.get_response(user_input)

if __name__ == "__main__":
  main()