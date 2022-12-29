import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_recipe(prompt: str):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.6,
        max_tokens=200
    )
    return response
