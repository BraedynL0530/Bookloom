import sqlalchemy as sa
from sqlalchemy import create_engine, String, Integer, Text, TypeDecorator
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)# change in future

metadta = sa.MetaData()

Book = sa.Table(
    "books",
    metadta,
    sa.Column("book_id", Integer, primary_key=True),
    sa.Column("book_name", Text, nullable=False),
    sa.Column("book_author", Text, nullable=True),
    sa.Column("book_title", Text, nullable=True),
    sa.Column("book_description", Text, nullable=True),
    sa.Column("book_source", Text, nullable=False),
    sa.Column("book_chapters", int, nullable=True),
    sa.Column("book_current_chapter", int, nullable=True),
)