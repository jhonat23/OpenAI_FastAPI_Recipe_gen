from pydantic import BaseModel, Field


# Models
class Recipe(BaseModel):
    instructions: str =  Field(...)