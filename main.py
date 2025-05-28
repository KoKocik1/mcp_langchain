import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from servers.math_server import mcp as math_mcp
from servers.weather_server import mcp as weather_mcp

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/krzysztofkokot/Projects/mcp-servers/mcp-langchain/servers/math_server.py"]
)


async def main():
    print("Hello from mcp-langchain!")
    print(os.getenv("OPENAI_API_KEY"))

if __name__ == "__main__":
    asyncio.run(main())
