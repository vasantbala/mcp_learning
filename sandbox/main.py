import asyncio
import os
import shutil
import subprocess
import time

from typing import Any
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, gen_trace_id, trace, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

load_dotenv()
set_tracing_disabled(True)

async def run(mcp_server: MCPServer):
    model_name = "llama-3.3-70b-versatile"
    
    client = AsyncOpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")
    )

    agent = Agent(
        name="Assistant",
        instructions="Use the tools to answer the questions.",
        mcp_servers=[mcp_server],
        model=OpenAIChatCompletionsModel( 
            model=model_name,            
            openai_client=client
        ),
        model_settings=ModelSettings(tool_choice="required")
    )

    # Use the `add` tool to add two numbers
    message = "Add these numbers: 7 and 22."
    print(f"Running: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

    # Run the `get_weather` tool
    message = "What's the weather in Tokyo?"
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)

    # Run the `get_secret_word` tool
    message = "What's the secret word?"
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=message)
    print(result.final_output)


async def main():
    async with MCPServerSse(
        name="SSE Python Server",
        params={
            "url": "http://localhost:8000/sse",
        },
    ) as server:
        # trace_id = gen_trace_id()
        # with trace(workflow_name="SSE Example", trace_id=trace_id):
        #     print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await run(server)


if __name__ == "__main__":
    # Let's make sure the user has uv installed
    if not shutil.which("uv"):
        raise RuntimeError(
            "uv is not installed. Please install it: https://docs.astral.sh/uv/getting-started/installation/"
        )
    asyncio.run(main())