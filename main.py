from fastapi import FastAPI, Form
from utils import generate_recipe

from models import Recipe

app = FastAPI()

# Main routes

## Root
@app.get(
    path='/',
    description='Main endpoint',
    tags=['Root']
)
def root():
    return {'Message': 'Hi! this my receipt generator using OpenAI. Please, read carefully the preparations maybe you find some wreid topics'}

## Generate example recipe
@app.get(
    path='/example-recipe',
    description='Delivers a example recipe with basis ingredients',
    tags=['Recipes']
)
def get_example_recipe():
    example_prompt = 'Write a short recipe based on these ingredients and instructions:\n\nFrito Pie\n\nIngredients:\nFritos\nChili\nShredded cheddar cheese\nSweet white or red onions, diced small\nSour cream'
    result = generate_recipe(example_prompt)
    return result

## Generate a recipe
@app.post(
    path='/recipe',
    description='Delivers a recipe',
    tags=['Recipes'],
    response_model=Recipe
)
def get_recipe(recipe: str=Form(...)):
    result = generate_recipe(recipe)
    return Recipe(instructions=result['choices'][0]['text'])