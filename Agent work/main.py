from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

Google_key=os.getenv("google_api_key")

client=AsyncOpenAI(
    api_key= Google_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
agent = Agent(
    name="testing-agent",
    instructions="Meath expert agent",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),

)

query ="what is the best way to make a cake"

result=Runner.run_sync(
    agent,
    query,
)

print(result)