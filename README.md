# MCP Demo Server

A simple MCP server demonstrating basic functionality with an addition tool.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd first-mcp
```

2. Create and activate a virtual environment:
```sh
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
## On Windows
.venv\Scripts\activate
## On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```sh
pip install mcp-python fastmcp
```

## Running the Local MCP Server

There are two ways to run the server:

### 1. Using Python directly

```sh
python server.py
```

### 2. Using VS Code

1. Open the project in VS Code
2. Make sure you have the Python extension installed
3. Press `F5` or use the Run and Debug menu to start the server
4. Select "Run MCP Server" configuration

The server includes one tool:
- `add`: A simple addition tool that takes two integers and returns their sum

## Configuration

The server configuration is managed through `.vscode/mcp.json`, which includes:
- Time server configuration for timezone management
- Add server configuration for the demo addition tool

## Development

The project uses VS Code settings for:
- Python path configuration
- Code linting
- Auto-formatting on save