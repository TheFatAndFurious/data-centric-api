from sqlalchemy import text
from sqlmodel import create_engine
from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = F"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost:5432/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("Database connection successful:", result.fetchone())