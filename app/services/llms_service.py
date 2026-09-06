
import os
from huggingface_hub import InferenceClient


HF_TOKEN=os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("LLM_MODEL")


client = InferenceClient(
    api_key=HF_TOKEN
)


def generate_answer(prompt: str):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

