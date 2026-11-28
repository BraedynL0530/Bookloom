from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QImage, QPixmap
from sqlalchemy import select
from infastructure.storage.storage import engine
from sqlalchemy.orm import sessionmaker
import pymupdf
from core.classes.Chapters import Chapter

THEMES = {
    "beige": ("#F5EFE6", "#2C221E"),
    "white": ("#FFFFFF", "#111111"),
    "dark": ("#18181B", "#E4E4E7"),
}

class Reader(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)


        self.container = QVBoxLayout()
        self.doc = None
        self.page_idx = 0
        self.theme = "beige"

        self.pages = QHBoxLayout
        self.left_page = QLabel()
        self.right_page = QLabel()

        self.pages.addWidget(self.left_page)
        self.pages.addWidget(self.right_page)


        self.container.addWidget(self.pages)


        self.corners = QHBoxLayout()
        self.left_num = QLabel(alignment=Qt.AlignmentFlag.AlignLeft)
        self.right_num = QLabel(alignment=Qt.AlignmentFlag.AlignRight)

        self.corners.addWidget(self.left_num)
        self.corners.addWidget(self.right_num)
        self.container.addWidget(self.corners)
        




        self.nav = QHBoxLayout()

        self.next = QPushButton("->")# icons later
        self.chapter = QLabel("temp: chapter 11/24")
        self.previous = QPushButton("<-")

        
        self.nav.addWidget(self.previous)
        self.nav.addWidget(self.chapter)
        self.nav.addWidget(self.next)

        self.container.addWidget(self.nav)


        


        #TODO:
        #NEEDS:
        # 2 page viewer that u can flip pages
        #vertical viewer for cbz


        def read_local_chapter(self, id:str) -> None:

            session = sessionmaker(bind=engine)()
            stmt = select(Chapter).where(Chapter.id==id)
            with session:
                chapter = session.scalars(stmt)
            path = chapter.chapter_path
        
            #now to actually get the data...


        def render_page(self, index:int) ->QPixmap: #gemni helped here because idk this lib nor how epubs work but no ai code? or ai didnt do it for me.
            if not self.doc or index < 0:
                return QPixmap() #so empty pages can exist/not break render

            pix = self.doc[index].get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)

            img = QImage(
                pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888
            )
            qpix = QPixmap.fromImage(img)
            return qpix

        def render_spread(self, index:int): 
            self.left_page.setPixmap(self.render_page(index))
            self.left_page.setPixmap(self.render_page(index+1))

            self.left_num.setText(str(index+1))
            self.left_num.setText(
                str(self.index+2) if self.index +1 < len(self.doc) else ""
            )


        def turn_page():
            pass


        def read_local_epub(self, id:str) -> None:  #heh, ill take it from here gemni

            session = sessionmaker(bind=engine)()
            stmt = select(Chapter).where(Chapter.id==id)

            with session:
                chapter = session.scalars(stmt)

            path = chapter.chapter_path
            if chapter.current_page:
                self.page_idx = chapter.current_page - 1

            self.doc = pymupdf(path)#idk yet ignore this
            
            

        def web_viewer(self, viewer:object): #uses the Browser interface
            pass




