# server.py
import sys
import os

# Add the path to the mcp module dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'mcp')))

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()

