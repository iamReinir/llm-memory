import tomli
from fastmcp import FastMCP

with open("config.toml", "rb") as f:
    data = tomli.load(f)

class config():
    DATABASE_URL = data['database']['path']

mcp = FastMCP(data['meta']['name'])
config = config()
