# MCP LangChain Project

This project demonstrates the integration of MCP (Model Control Protocol) servers with LangChain, featuring both simple and multiple server configurations.

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd mcp-langchain
```

2. Create and activate a virtual environment using uv:

```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies using uv:

```bash
uv pip install -r requirements.txt
```

## Project Structure

- `simple_mcp.py`: Demonstrates a single MCP server integration with LangChain
- `multiple_mcp.py`: Shows how to work with multiple MCP servers simultaneously
- `servers/`: Contains the MCP server implementations
  - `weather_server.py`: Weather information server
  - `math_server.py`: Mathematical operations server

## Running the Servers

### Weather Server

To run the weather server separately:

```bash
uv run servers/weather_server.py
```

### Math Server

To run the math server separately:

```bash
uv run servers/math_server.py
```

## Usage Examples

### Simple MCP Example

The `simple_mcp.py` demonstrates a basic integration with a single MCP server. It:

- Connects to a math server
- Uses LangChain to create an agent
- Processes mathematical queries

Run it with:

```bash
uv run simple_mcp.py
```

### Multiple MCP Example

The `multiple_mcp.py` shows how to work with multiple MCP servers simultaneously. It:

- Connects to both math and weather servers
- Creates an agent that can handle both mathematical and weather-related queries
- Demonstrates multi-server communication

Run it with:

```bash
uv run multiple_mcp.py
```

## Environment Variables

Create a `.env` file in the project root with:

```
OPENAI_API_KEY=your_openai_api_key
```

## Notes

- Make sure all required environment variables are set before running the examples
- The weather server runs on port 8000 by default
- The math server uses stdio transport
- Both examples use GPT-4 for processing queries
