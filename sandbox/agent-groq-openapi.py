from dotenv import load_dotenv
import os
import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()
set_tracing_disabled(True)

async def main():
    model_name = "llama-3.3-70b-versatile"
    client = AsyncOpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")
    )

    translation_agent = Agent(
        name = "English agent",
        instructions = "Translate to Spanish.",
        model=OpenAIChatCompletionsModel( 
            model=model_name,
            openai_client=client
        )
    )

    result = await Runner.run(translation_agent, "Hello.")
    print(result.final_output)

asyncio.run(main())
