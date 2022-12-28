import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_example_recipe():
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt='Write a short recipe based on these ingredients and instructions:\n\nFrito Pie\n\nIngredients:\nFritos\nChili\nShredded cheddar cheese\nSweet white or red onions, diced small\nSour cream',
        temperature=0.6,
        max_tokens=200
    )
    return response
