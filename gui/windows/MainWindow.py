import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui.windows import Home, Reading,Watching

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
