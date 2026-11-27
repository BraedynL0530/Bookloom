from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
