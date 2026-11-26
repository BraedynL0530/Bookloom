from PyQt6.QtWidgets import QLabel, QWidget,QGridLayout
from infastructure.storage.storage import engine # is vs code stupid or is this a me issue?
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from core.classes.Bookshelf import Bookshelf
from core.classes.Book import Book

class BookShelfObject(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.layout = QGridLayout()#idk makes the most sense

        self.shelf_img = "temp_path/to/image"# base image 4 this widget,
        self.session = sessionmaker(bind=engine)() #probally not idomatic or wahtever but idec

        self.books = [] #list of dicts, should be able to use everything from here to make
        self.favorites = []
        self.sort = ""

        self.rows = None
        self.books_per_row = 8 #random values idc
        

        


    def get_or_create(self,Bookshelf):
        with self.session as s:
            stmt = select(Bookshelf)
            instance = s.scalar(stmt).one_or_none()

            if instance:
                return instance

            instance = Bookshelf()

            s.add(instance)
            s.commit()
            s.refresh(instance)
            return instance


    def create_object(self):
        shelf = self.get_or_create(Bookshelf)

        if not shelf.books:
            self.books = {} #NOTE: may need to change

        else:

            with self.session as s:
                #never mind im good
                stmt = select(shelf).where(Book.id.in_(shelf.books)) #was lowkey close just neeeded that last bit which i have no idea what was missing
                books = s.scalars(stmt) 

            for book in books:
                self.books.append({
                    "id":book.id,
                    "title":book.title,
                    "author":book.author,
                    "desc":book.description,
                    "source":book.source,
                    "chapterCount":book.chapter_count,
                    "currentChapter":book.current_chapter,
                    "lastViewed":book.last_viewed,
                })
                #yippe

    def init_ui(self):
        pass


            #i dispise gemeni, my first version was right though i just let myself and gemeni confused me.