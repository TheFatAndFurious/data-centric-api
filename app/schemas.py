from typing import Optional
from pydantic import BaseModel

class ExerciceUpdate(BaseModel):
    name: Optional[str] = None
    muscle: Optional[str] = None

