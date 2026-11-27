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
async def import_cbz(path, book_id: Optional[str] = None, book_chapter: Optional[int] = None):#str may mean uuid i forgot if i switched towards
    if not path.endswith(".cbz"):
        return
    if path.endswith(".cbz"):
        if book_id and book_chapter:
            try:
                session = sessionmaker(bind=engine)()
                book = session.get(Book, book_id)
                title = book.title

                Signal.emit("import_cbz", path, book_id, title,book_chapter)#may need updating im just doing stuff
                chapter_path = Path(f"~/.local/share/Bookloom/Books/{title}").expanduser()
                shutil.move(path, chapter_path)
                chapter = Chapter(book_id=book_id, title=f"Chapter {book_chapter}", chapter_path=str(chapter_path))

                with session as s: #i hear this is is better 4 error handling
                    s.add(chapter)
                    s.commit
            except Exception as e:
                print(e)

        else:
            try:
                data = await Signal.wait_for_next(30) #should return a tuple of title and author minium, and more if user fills out
                if data is not None and len(data) >= 2:
                    title, author, *extra = data
                    book = Book(
                        title=title,
                        author=author,
                        description=extra[0] if extra else "",
                        source="local",
                    )
                    chapter = Chapter(book_id=book.id, title="Chapter 1", chapter_path=str(Path(path).expanduser()))

                else:
                    raise TypeError("Data not provided")


                book_path = Path(f"~/.local/share/Bookloom/Books/{book.title}").expanduser()
                os.mkdir(book_path)
                shutil.move(path, book_path)
                Signal.emit("import_new_cbz")
                session = sessionmaker(bind=engine)()
                #TODO: addd user prompt to update book info ALSO JUST REALIZED THEYRE GONNA BE IMPORTINF FROM GUI SO PROMPT SHOULD ACTUALLY COME FIRST!
                with session as s:
                    s.add(book)
                    s.add(chapter)
                    s.commit()

            except Exception as e: #shouldnt be needed tho
                print(e)
                Signal.emit("error", "Please enter book id and chapter number")


#TODO:make this for epubs.