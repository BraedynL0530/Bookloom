import uuid
from typing import Optional
from sqlalchemy import String, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from infastructure.storage.storage import Base

class Bookshelf(Base):
    __tablename__ = "bookshelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    books_per_row: Mapped[int] = mapped_column(Integer, default=10)
    order: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    current_rows: Mapped[int] = mapped_column(Integer, default=1)

    books: Mapped[list[str]] = mapped_column(JSON, default=list)
    favorite: Mapped[list[str]] = mapped_column(JSON, default=list)

    def add_book(self, book_id: uuid.UUID):
        if not self.books:
            self.books = []
        self.books = self.books + [str(book_id)]
        self.update_shelf()

    def remove_book(self, book_id: uuid.UUID):
        str_id = str(book_id)
        if self.books and str_id in self.books:
            self.books = [b for b in self.books if b != str_id]
            self.update_shelf()

    def update_shelf(self):
        if not self.books:
            self.current_rows = 1
            return
        self.current_rows = max(1, (len(self.books) + self.books_per_row - 1) // self.books_per_row)

    def add_favorite(self, book_id: uuid.UUID):
        if not self.favorite:
            self.favorite = []
        self.favorite = self.favorite + [str(book_id)]

    def remove_favorite(self, book_id: uuid.UUID):
        str_id = str(book_id)
        if self.favorite and str_id in self.favorite:
            self.favorite = [f for f in self.favorite if f != str_id]

    def set_books_per_row(self, books_per_row: int):
        self.books_per_row = books_per_row
        self.update_shelf()

    def __len__(self):
        return len(self.books) if self.books else 0
