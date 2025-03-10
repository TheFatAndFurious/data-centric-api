from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.params import Depends
from sqlmodel import Session

from app.db import init_db, get_session
from app.models import Exercice, create_exercice

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/exercices/", response_model=Exercice)
def create_exercice_endpoint(name: str, session: Session = Depends(get_session)):
    return create_exercice(session, name)


@app.get("/tasoeur/")
def read_shit():
    return {"Elle bat": "bakool"}