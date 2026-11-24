import sys
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton

class NavBar(QWidget):
    def __init__(self):
        super().__init__()

        self.drop_down = QPushButton()

        self.home = QPushButton()#need an icon
        self.web = QPushButton()
        self.shop = QPushButton()
        self.watch = QPushButton()

        #idk what else, because Reading and Watching are just isloated windows to read/watch so ig back?
        
    def navigate(self,id):
        e = "bleh"
        pass

    #GAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    #I dont know what to code