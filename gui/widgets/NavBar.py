import sys
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton

#should be in main window only.
class NavBar(QWidget):
    def __init__(self):
        super().__init__()

        self.drop_down = QPushButton()

        self.home = QPushButton()#need an icon
        self.web = QPushButton()
        self.read = QPushButton()
        self.shop = QPushButton()
        self.watch = QPushButton()

        self.current_page ="home"

        self.pages = {
            "home": self.home,
            "watch":self.watch,
            "read":self.read
        }

        #idk what else, because Reading and Watching are just isloated windows to read/watch so ig web?
        
    def navigate(self,page:str) -> None:
        for key, value in enumerate(self.pages.items):
            if key == page:
                self.current_page = page
                return value
#Todo:check if thers already a nav func and if i wasted my time + way to simplfy this without any more helpeer funcs