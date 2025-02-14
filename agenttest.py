from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(task=input("whatup boss "), llm=ChatOpenAI(model = "gpt-4o"),)
    result = await agent.run()
    print(result)
asyncio.run(main())
