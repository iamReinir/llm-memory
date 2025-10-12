from mcp.server.fastmcp import FastMCP
import memory
import database
from config import mcp

if __name__ == "__main__":
    mcp.run(transport='stdio')
    #print("Database URL:", url)
