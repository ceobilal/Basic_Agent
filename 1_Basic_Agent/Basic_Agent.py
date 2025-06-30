from agents import Agent, Runner,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

google_key=os.getenv("Google_Api_key")

client=AsyncOpenAI(
    api_key=google_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    )

query=input("Questions:  ")

result=Runner.run_sync(
    agent,
    query,
)



print(result.final_output)