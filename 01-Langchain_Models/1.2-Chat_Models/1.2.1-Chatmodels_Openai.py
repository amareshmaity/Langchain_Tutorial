from langchain_openai import ChatOpenAI # import openai chatmodel
from dotenv import load_dotenv

## Load environment variable
load_dotenv()

## Instantiate chatmodel
model = ChatOpenAI(
    model="gpt-4.1-nano"
)

## Call the chatbot model
response = model.invoke("What is the capital of South Korea")

print(response)