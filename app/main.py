from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.params import Depends
from sqlmodel import Session

from app.crud import create_exercice, get_exercices, get_single_exercice
from app.db import init_db, get_session
from app.models import Exercice

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/exercices/", response_model=Exercice)
def create_exercice_endpoint(name: str, muscle: str, session: Session = Depends(get_session)):
    return create_exercice(session, name, muscle=muscle)


@app.get("/exercices/", response_model=list[Exercice])
def get_all_exercices(muscle:str, session: Session = Depends(get_session)):
     return get_exercices(session, muscle=muscle)

@app.get("/exercices/{id}", response_model=Exercice)
def get_exercice_by_id(id: int, session: Session = Depends(get_session)):
    return get_single_exercice(session, id)
