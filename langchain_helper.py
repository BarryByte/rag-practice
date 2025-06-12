import os
from dotenv import load_dotenv
load_dotenv()
gemini_key = os.getenv("gemini_key")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3, google_api_key=gemini_key)
def generate_restaurant_name_and_items(cuisine):
    
    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. only one name please")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="restaurant_name", verbose=True)
    prompt_template_items = PromptTemplate(
        input_variables = ['restraurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated")

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key= "menu_items",verbose=True)

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine' : cuisine})
    return response


if __name__ == '__main__':
    print(generate_restaurant_name_and_items("Italian"))
