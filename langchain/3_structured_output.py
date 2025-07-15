from typing import List
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI

from config.config import config

# Chat model
llm = ChatOpenAI(
    model=config.openai_model,
    api_key=config.openai_api_key
)

# Pydantic schema
class Recipe(BaseModel):
    """recipe data schema"""
    name: str = Field(description="name of the recipe")
    calorie: str = Field(description="calorie of the recipe")

    ingredients: List[str] = Field(description="ingredients of the recipe")

# Add schema to the model
structured_llm = llm.with_structured_output(Recipe, method="function_calling")

# Call the model
output = structured_llm.invoke("Vegetarian Pizza")
print(output)
