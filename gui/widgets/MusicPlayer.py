from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor, QFont, QIcon, QPixmap


class MusicPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)