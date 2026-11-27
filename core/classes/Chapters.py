import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infastructure.storage.storage import Base
from core.classes.Book import Book


class Chapter(Base):
    __tablename__ = "chapters"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    book_id: Mapped[str] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    book: Mapped["Book"] = relationship(back_populates="chapters")
    chapter_path: Mapped[str] = mapped_column(String(500), nullable=False)


    #TODO: figure out how to have it save browser based 
