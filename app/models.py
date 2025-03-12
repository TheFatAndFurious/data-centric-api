from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

class Exercice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False)
    muscle: str = Field(unique=True, nullable=True)

class Workout(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(nullable=False)
    notes: Optional[str] = Field(default=None)

class Set(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="workout.id", nullable=False)
    exercice_id: int = Field(foreign_key="exercice.id", nullable=False)
    repetitions: int = Field(nullable=False)
    weight: float = Field(nullable=False)





