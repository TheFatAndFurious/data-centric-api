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
