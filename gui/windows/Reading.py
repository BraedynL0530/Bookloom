#been like 4 hours ^^
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from sqlalchemy import select
from infastructure.storage.storage import engine
from sqlalchemy.orm import sessionmaker
from ebooklib import epub #dependencys hell yeah!
from core.classes.Chapters import Chapter

class Reader(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)


        self.container = QVBoxLayout()

        #file here

        self.nav = QHBoxLayout()

        self.next = QPushButton("->")# icons later
        self.chapter = QLabel("temp: chapter 11/24")
        self.previous = QPushButton("<-")

        self.nav.addWidget(self.previous)
        self.nav.addWidget(self.chapter)
        self.nav.addWidget(self.next)

        


        #TODO:
        #NEEDS:
        # 2 page viewer that u can flip pages
        #vertical viewer for cbz
        # automatic 2 page VS vertical viewer for web. (use source would probally be best.)


        def read_local_chapter(self, id:str) -> None:
            session = sessionmaker(bind=engine)()
            stmt = select(Chapter).where(Chapter.id==id)
            with session:
                chapter = session.scalars(stmt)
            path = chapter.chapter_path
            self.book = epub.read_epub(path) #yay yay yay
            #now to actually get the data...
            


            self.container.addWidget(self.nav)
            pass

        def web_viewer(self, viewer:object): #uses the Browser interface


            self.container.addWidget(self.nav)
            pass

#GAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH


