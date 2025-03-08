from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import init_db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

@app.get("/")
def read_root():
    return {"Hello": "World"}