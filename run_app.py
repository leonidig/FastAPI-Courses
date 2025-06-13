import asyncio
from uvicorn import run as start
from app import app


if __name__ == "__main__": 
    start(app)