from fastapi import FastAPI, status, Form
from app.utils import generate_recipe, origins
from fastapi.middleware.cors import CORSMiddleware

from app.models import Recipe

app = FastAPI()

## adding middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Main routes

## Root
@app.get(
    path='/',
    description='Main endpoint',
    tags=['Root'],
    status_code=status.HTTP_200_OK
    
)
def root():
    return {'Message': 'Hi! this my receipt generator using OpenAI. Please, read carefully the preparations maybe you find some wreid topics'}

## Generate example recipe
@app.get(
    path='/example-recipe',
    summary='Delivers a example recipe',
    description='Delivers a example recipe with basis ingredients: 3 potatoes, 1 onion, 2 tomatoes, salt, pepper, spagetti and fish',
    tags=['Recipes'],
    status_code=status.HTTP_200_OK,
    response_description='This is the example recipe'
)
def get_example_recipe():
    example_prompt = """Write a short recipe based on following ingredients. These ingredients can be arranged as a long string or a list: 

    1. 3 potatoes
    2. 1 onion
    3. 2 tomatoes
    4. salt
    5. pepper
    6. spaguetti
    7.  fish"""
    result = generate_recipe(example_prompt)
    return result

## Generate a recipe
@app.post(
    path='/user-recipe',
    summary='Gets a recipe from user form prompt',
    description='Delivers a recipe with user prompt ingredients through form',
    tags=['Recipes'],
    response_model=Recipe,
    status_code=status.HTTP_200_OK,
    response_description='This is the user recipe'
)
def get_recipe(ingredients: str=Form(...)):
    user_prompt = """Write a short recipe based on following ingredients. These ingredients can be arranged as a long string or a list: """ + ingredients

    if len(ingredients) <= 10:
        return Recipe(instructions="Hey! your prompt doesn't have enough data ¯\_(ツ)_/¯")

    result = generate_recipe(user_prompt)
    return Recipe(instructions=result['choices'][0]['text'])