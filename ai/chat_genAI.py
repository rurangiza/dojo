"""
A simple chat to ask questions to AI models using HuggingFace
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# initialize the client but point it to TGI
client = OpenAI(
  base_url="https://api-inference.huggingface.co/v1",
  api_key= os.getenv('API_KEY')
) 

def main():

    print("-------- Start of conversation --------")
    for _ in range(5):
        question = input("\nQ: ")

        chat_completion = client.chat.completions.create(
            model="google/gemma-7b-it",
            messages=[
                {"role": "user", "content": question},
            ],
            stream=True,
            max_tokens=200
        )

        # iterate and print stream
        for message in chat_completion:
            msg = message.choices[0].delta.content
            if "eos" not in msg:
                print(msg, end="")
    print("-------- End of conversation --------")

if __name__ == "__main__":
    main()