from agents import Agent,OpenAIChatCompletionsModel,Runner,function_tool
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()


google_key=os.getenv("google_api_key")


client=AsyncOpenAI(
    api_key=google_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    
)

@function_tool
def get_weather (city : str):
    return f"The weather in {city} is sunny"

# class bets(BaseModel):
#     statement:str
#     options: list

# @function_tool
# def hello():
#     return " hello "


agent=Agent(
    name="Assistent Agent",
    instructions="you are help full agent",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    output_type=[get_weather,]
    # tools=[hello]

)
query="lahore weather today temprature"

Result= Runner.run_sync(
    agent,
    query,

)

print(Result)