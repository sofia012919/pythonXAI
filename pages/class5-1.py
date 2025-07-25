import openai  # pip install openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("你：")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "你好，我是 Python 小助手！"},
        ],
    )

    assistant_message = response.choices[0].message.content

    print(f"AI：{assistant_message}")
