from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

# 1. Define the shared Declarative Base
class Base(DeclarativeBase):
    pass

# 2. Setup your database engine
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)
