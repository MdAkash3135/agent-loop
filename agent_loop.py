import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "user", "content": "Who wrote 'Romeo and Juliet'?"},
    {"role": "user", "content": "What is the largest planet in our solar system?"}
]

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    print(response.choices[0].message.content)
    if response.choices[0].finish_reason == "stop":
        break
    else:
        break