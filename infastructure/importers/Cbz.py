import os
import shutil
from typing import Optional
from core.events import Signal
from core.classes.Book import Book


#NOTE THIS IS ERROUS OR BARELY WORKING CODE!!! gui cant send back name, and
def import_cbz(path, book_id: Optional[str] = None, book_chapter: Optional[float] = None):
    if path.endswith(".cbz"):
        if book_id and book_chapter:
            try:
                Signal.emit("import_cbz", path, book_id, book_chapter)#may need updating im just doing stuff
                shutil.move(path, f"~/.local/share/Bookloom/Books/{book_id}.cbz")
                return

            except Exception as e:
                print(e)

        else:
            try:
                Signal.emit("import_new_cbz")
                Signal.connect(get_book_data, lambda title, author: (title, author))
                book = Book(
                    title = "New Book",
                    author = "New Author",

                )
                os.mkdr(f"~/.local/share/Bookloom/Books/{book.title}") #update to title then we need a way to switch this if its for windows vs linux
                Signal.emit("import_new_cbz") #prompt user to get name of book and what chapter theyre importing

            except Exception as e:
                print(e)
                Signal.emit("error", "Please enter book id and chapter number")


    else:
        raise Exception("Not a cbz file")

def get_book_data(title, author):
    return (
        title,
        author,
    )