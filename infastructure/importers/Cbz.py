import os
import shutil
from pathlib import Path
from typing import Optional
from core.events import Signal
from core.classes.Book import Book
from core.classes.Chapters import Chapter
from infastructure.storage.storage import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

#note: untested but no immediate errors
def import_cbz(path, book_id: Optional[str] = None, book_chapter: Optional[int] = None):#str may mean uuid i forgot if i switched towards
    if not path.endswith(".cbz"):
        return
    if path.endswith(".cbz"):
        if book_id and book_chapter:
            try:
                session = sessionmaker(bind=engine)()
                book = session.get(Book, book_id)
                title = book.title

                Signal.emit("import_cbz", path, book_id, title,book_chapter)#may need updating im just doing stuff
                book_path = Path(f"~/.local/share/Bookloom/Books/{title}").expanduser()
                shutil.move(path, book_path)
                chapter = Chapter(book_id=book_id, title=f"Chapter {book_chapter}", chapter_path=str(book_path))

                with session as s: #i hear this is is better 4 error handling
                    s.add(chapter)
                    s.commit
            except Exception as e:
                print(e)

        else:
            try:
                Signal.connect(get_book_data, lambda title, author: (title, author))
                book = Book(
                    title = "New Book",
                    author = "New Author",

                )
                book_path = Path(f"~/.local/share/Bookloom/Books/{book.title}").expanduser()
                os.mkdir(book_path)
                shutil.move(path, book_path)
                Signal.emit("import_new_cbz")
                session = sessionmaker(bind=engine)()
                with session as s:
                    s.add(book)
                    s.commit()

            except Exception as e:
                print(e)
                Signal.emit("error", "Please enter book id and chapter number")


def get_book_data(title, author):
    return (
        title,
        author,
    )