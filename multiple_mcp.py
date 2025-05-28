import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")


async def main():

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["/Users/krzysztofkokot/Projects/mcp-servers/mcp-langchain/servers/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            }
        }
    )
    tools = await client.get_tools()
    print(tools)
    agent = create_react_agent("openai:gpt-4.1", tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print(math_response["messages"][-1].content)
    print(weather_response["messages"][-1].content)
   

if __name__ == "__main__":
    asyncio.run(main())