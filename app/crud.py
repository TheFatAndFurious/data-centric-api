from http.client import HTTPException
from typing import Dict, Any

from sqlmodel import Session, select

from app.models import Exercice


def create_exercice(session: Session, name: str, muscle: str = None) :
    new_exercice = Exercice(name=name, muscle=muscle)
    session.add(new_exercice)
    session.commit()
    session.refresh(new_exercice)
    return new_exercice

def get_exercices(session: Session, skip: int = 0, limit: int = 100, muscle: str = None)-> list[Exercice]:
    if muscle:
        statement = select(Exercice).where(Exercice.muscle == muscle).offset(skip).limit(limit)
        return session.exec(statement).all()
    else:
        statement = select(Exercice).offset(skip).limit(limit)
        return session.exec(statement).all()

def get_single_exercice(session: Session, id: int):
    statement = select(Exercice).where(Exercice.id == id)
    return session.exec(statement).first()

def delete_exercice(session: Session, id: int):
    exercice: Exercice = get_single_exercice(session, id)
    if not exercice:
        raise HTTPException(status_code=404, detail="Exercice not found")
    session.delete(exercice)
    session.commit()

def update_exercice(session: Session, id: int, update_data: Dict[str, Any]) -> Exercice:
    exercice: Exercice = get_single_exercice(session, id)
    if not exercice:
        raise HTTPException(status_code=404, detail="Exercice not found")
    for key, value in update_data.items():
        setattr(exercice, key, value)
    session.add(exercice)
    session.commit()
    session.refresh(exercice)
    return exercice
