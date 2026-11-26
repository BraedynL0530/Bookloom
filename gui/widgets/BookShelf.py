from PyQt6.QtWidgets import QLabel, QWidget,QGridLayout
from infastructure.storage.storage import engine
from sqlalchemy.orm import sessionmaker#ignore the not imported stuff i have it on linux (arch btw)
# im lowkey a geek that doesnt know how to import without pycharm
from core.classes.Bookshelf import Bookshelf

#GAHHHHHHHHHHHH AI IS SO STUPID POP THE BUBBLE
class BookShelfObject(QWidget):
    def __init__(self, parent = ...):
        super().__init__(parent)
        self.layout = QGridLayout()#idk makes the most sense
        self.shelf_img = "temp_path/to/image"
        self.session = sessionmaker(bind=engine)() #probally not idomatic or wahtever but idec


    def get_or_create(self,Bookshelf):
        with self.session as s:
            smt =s.select(Bookshelf)
            instance = s.scalar(smt).one_or_none()

            if instance:
                return instance, False

            instance = Bookshelf()

            return instance, True


        #its the next day btw