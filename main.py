from fastmcp import FastMCP
import memory
import database
from config import mcp
from fastapi import FastAPI
import sys
import uvicorn

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "-http":
        mcp_app = mcp.http_app(path='/mcp')
        app = FastAPI(lifespan=mcp_app.lifespan)
        app.mount("/llm-memory", mcp_app)
        uvicorn.run(app, host="0.0.0.0", port=3000)
    else:
        mcp.run(transport='stdio')
        #print("Database URL:", url)
