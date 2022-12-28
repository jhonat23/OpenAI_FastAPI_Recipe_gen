from fastapi import FastAPI
from utils import generate_example_recipe

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

## Generate recipe 
@app.get(
    path='/example-recipe',
    description='Delivers a example recipe with basis ingredients',
    tags=['Recipes']
)
def get_example_recipe():
    result = generate_example_recipe()
    return result