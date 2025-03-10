from sqlmodel import SQLModel, Field, Session

class Exercice(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(unique=True)

def create_exercice(session: Session, name: str) :
    new_exercice = Exercice(name=name)
    session.add(new_exercice)
    session.commit()
    session.refresh(new_exercice)
    return new_exercice




