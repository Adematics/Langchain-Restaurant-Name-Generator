from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)

def generate_resturant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variable = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food, Suggest a fancy name for this."
    )

    chain = prompt_template_name | llm

    response = chain.invoke(cuisine)

    if response:
        restaurant_name = response.strip()
        return restaurant_name
    
    return "No name generated"

if __name__ == "__main__" : 
    print(generate_resturant_name_and_items("Italian"))






