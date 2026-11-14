import uuid
from datetime import datetime
from typing import Optional
from sqlalchemy import String, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infastructure.storage.storage import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), default="not found")
    source: Mapped[str] = mapped_column(String(50), default="")  # web or local
    chapter_count: Mapped[int] = mapped_column(default=0)
    chapter_name: Mapped[str] = mapped_column(String(255), default="")
    current_chapter: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    last_viewed: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    cover_img_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    tags: Mapped[list[str]] = mapped_column(JSON, default=list)

    chapters: Mapped[list["Chapter"]] = relationship(back_populates="book", cascade="all, delete-orphan")

    def add_tag(self, tag: str):
        if not self.tags:
            self.tags = []
        self.tags = self.tags + [tag]

    def remove_tag(self, tag: str):
        if self.tags and tag in self.tags:
            self.tags = [t for t in self.tags if t != tag]

    def update_chapter(self, chapter: str):
        self.current_chapter = chapter

    def update_chapters(self, chapters: list):
        self.chapters = chapters

    def update_last_viewed(self, last_viewed: datetime):
        self.last_viewed = last_viewed
