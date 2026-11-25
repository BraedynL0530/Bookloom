import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.widgets.NavBar import NavBar
from gui.windows.Home import Home
from gui.windows.Reading import Reading
from gui.windows.Watching import Watching

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windows = [Home,Reading,Watching]
        self.current_screen = "Home"# or just Home?