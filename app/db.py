from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session
import os

load_dotenv()

DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = F"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@DB/5432/{DATABASE_NAME}"

# echo will need to be made into an env variable as it is a dev logger
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


