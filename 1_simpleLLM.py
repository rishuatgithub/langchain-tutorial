import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


# print(OPENAI_API_KEY)

## using the openai==0.28 pypi release (older). the default model using text-davinci-003 model api from OpenAI
def main():
    llm = OpenAI(verbose=True, openai_api_key=OPENAI_API_KEY, temperature=0.9)
    result = llm.predict(
        "Give me 5 topics for an interesting youtube video on python"
    )
    print(result)


if __name__ == "__main__":
    main()
