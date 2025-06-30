from agents import agent,Runner

agent=agent(
    name="Assistant",
    instruction="you are help full agent "
)

query="hello how are you"

result=Runner.run_sync(
    agent,
    query,
)