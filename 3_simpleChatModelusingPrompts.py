import os
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"

# PROMPT_COUNTRY_INFO_1 = """
# Provide top 5 tourist attractions in {country}.
# """

# PROMPT_COUNTRY_INFO_2 = """
# Provide information about {country}.
# {format_instructions}
# """

PROMPT_COUNTRY_INFO_3 = """
Provide information about {country}. If the country is not available, make something up.
{format_instructions}
"""


## setting the pydantic model
class Country(BaseModel):
    capital: str = Field(description="capital of the country")
    name: str = Field(description="name of the country")


## using the latest openai release and using chatModel and Prompts
def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    parser = PydanticOutputParser(pydantic_object=Country)

    # get user input
    country = input("Enter the name of the country: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO_3)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    # chat_prompt_with_values = chat_prompt.format_prompt(country=country)
    chat_prompt_with_values = chat_prompt.format_prompt(
        country=country, format_instructions=parser.get_format_instructions()
    )

    response = llm(chat_prompt_with_values.to_messages())
    data = parser.parse(response.content)

    # print(response)
    # print(data)
    # print(data.capital)
    print(f'The capital of {data.name} is {data.capital}')


if __name__ == "__main__":
    main()
