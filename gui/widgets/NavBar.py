import sys
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton
from core.events.Signal import Signal

#should be in main window only.
class NavBar(QWidget):
    def __init__(self):
        super().__init__()

        self.drop_down = QPushButton()

        self.home = QPushButton()#need an icon
        self.web = QPushButton()# potentially
        self.read = QPushButton()
        self.shop = QPushButton()# potentially its own page elsewise itll go into home window
        self.watch = QPushButton()

        self.home.clicked.connect(self.navigate("home"))
        self.watch.clicked.connect(self.navigate("watch"))
        self.read.clicked.connect(self.navigate("read"))


        self.pages = {
            "home": self.home,
            "watch":self.watch,
            "read":self.read 
        }

        
        
    def navigate(self,page:str) -> QWidget: #gotta figure out how to plug it into app.py but should be simple enough.
        for key, value in enumerate(self.pages.items):
            if key == page:
                return value
#i no longer car if there is a navigator or such widget built in im too far inside.