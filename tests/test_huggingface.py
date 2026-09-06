import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


token = os.getenv("HF_TOKEN")


client = InferenceClient(
    api_key=token
)


response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "What is an IT helpdesk? Answer in one sentence."
        }
    ],
)


print(response.choices[0].message.content)

