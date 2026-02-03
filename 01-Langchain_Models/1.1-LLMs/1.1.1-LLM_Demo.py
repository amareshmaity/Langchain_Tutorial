from langchain_openai import OpenAI  # import openai from langchain
from dotenv import load_dotenv # to import environment variable


## Load the environment variable
load_dotenv()


## Create openai llm instance
llm = OpenAI(
    model="gpt-3.5-turbo-instruct"
)

## Call the llm
response = llm.invoke("What is the capital city of South Koria")
print(response)


## NOTE: Don't use llm in new days because this interface become old.


