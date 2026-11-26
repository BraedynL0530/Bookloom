from PyQt6.QtWidgets import QLabel, QWidget,QGridLayout,QPushButton
from PyQt6.QtGui import QIcon
from infastructure.storage.storage import engine # is vs code stupid or is this a me issue?
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from core.classes.Bookshelf import Bookshelf
from core.classes.Book import Book
import random
class BookShelfObject(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.shelf_img = "temp_path/to/image"# base image 4 this widget,
        self.session = sessionmaker(bind=engine)() #probally not idomatic or wahtever but idec
        self.book_img =""# paths ofc
        self.book_img2 = ""
        self.book_img3 = ""

        self.books = [] #list of dicts, should be able to use everything from here to make
        self.favorites = []
        self.sort = ""

        self.rows = None
        self.books_per_row = 8 #random values idc

        self.create_object()
        self.init_ui()
        

        


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


    def create_object(self) -> None:
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

            #for favorite in shelf.favorite: #trying not to have 2 diffrent for loops but this should loop over favorites and append the title, worse case ill just append book.id but title would be nice
            #    self.favorites == [] #may change


                
    def init_ui(self): #may need to return ui idk!
        layout = QGridLayout()# gotta figure out how to manipiulate ts to arrange how i want,
        for book in self.books: #needs to make a button for each based on id, and then clicking on it pulls up an tab about the book and option to read!
            icon_list = [self.book_img, self.book_img2,self.book_img3]
            index = random.randint(0,2)
            btn = QPushButton(QIcon(icon_list[index]))
            btn.clicked.connect(self.book_info(book["id"])) #gemni is the worse teacher ever i ask it stimple stuff and it yaps and gives me every answer but the one i need!!

        #now i just need to figure out how to confgure the bookshelf to actually work!
        


    def book_info(self, id:str): #alr know what this cshould do just want a way to kill this specific function or something like that
        for book in self.books:
            if id == book["id"]:
                pass #make popup here
        


            #home lab planning break!