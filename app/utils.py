import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_recipe(prompt: str):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=1500
    )
    return response

# allowed origins (CORS)
origins = [
    'http://localhost:4200', ## frontend localhost for development
    'https://recipegenerator-a700b.firebaseapp.com',
    'https://recipegenerator-a700b.web.app'
]
