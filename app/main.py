from contextlib import asynccontextmanager
from http.client import HTTPException
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Depends
from sqlmodel import Session

from app.crud import create_exercice, get_exercices, get_single_exercice, update_exercice
from app.db import init_db, get_session
from app.models import Exercice
from app.schemas import ExerciceUpdate
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:5174"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


@app.post("/exercices/", response_model=Exercice)
def create_exercice_endpoint(name: str, muscle: str, session: Session = Depends(get_session)):
    return create_exercice(session, name, muscle=muscle)


@app.get("/exercices/", response_model=list[Exercice])
def get_all_exercices(muscle:Optional[str] = None, session: Session = Depends(get_session)):
     return get_exercices(session, muscle=muscle)

@app.get("/exercices/{id}", response_model=Exercice)
def get_exercice_by_id(id: int, session: Session = Depends(get_session)):
    return get_single_exercice(session, id)

@app.delete("/exercices/{id}")
def delete_exercice_by_id(id: int, session: Session = Depends(get_session)):
    exercice = get_single_exercice(session, id)
    session.delete(exercice)
    session.commit()
    return {"message": "Exercice deleted successfully"}

@app.patch("/exercices/{id}")
def update_exercice_by_id(
        id:int,
        exercice_update: ExerciceUpdate,
        session: Session = Depends(get_session)):
    try:
        updated_data = exercice_update.model_dump(exclude_unset=True)
        updated_exercice = update_exercice(session, id, updated_data)
        return updated_exercice
    except HTTPException:
        raise
