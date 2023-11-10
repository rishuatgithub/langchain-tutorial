import os
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"


# print(OPENAI_API_KEY)

## using the latest openai release and using chatModel.
def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    result = llm.predict(
        "Give me 5 topics for an interesting youtube video on python"
    )
    print(result)


if __name__ == "__main__":
    main()
