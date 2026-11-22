from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,QHBoxLayout, QSlider
from PyQt6.QtGui import QColor, QFont, QIcon, QPixmap
from PyQt6.QtCore import QObject

class MusicPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.song_length = None
        self.is_playing = False
        self.current_time = 0 #time in seconds
        self.pause_play = QPushButton('Paused')#emojis later!
        self.skip = QPushButton('->')
        self.previous = QPushButton("<-")
        self.pause_play.clicked.connect(self.playPause)
        self.progress_bar = QSlider()#horizontal, max = length when of song, update it with current time
        self.player = QObject.QMediaPlayer(isPlaying=False)

    def playPause(self):
        self.is_playing = not self.is_playing
        self.update_buttons(self.is_playing)


    def set_song_length(self, song_length):
        self.song_length = song_length
        self.progress_bar.setMaximum(int(song_length))

    def update_progress(self, current_time):
        self.progress_bar.setValue(int(current_time))


    def update_buttons(self):
        if self.is_playing == True:
            self.pause_play.setText("Paused")
        else:
            self.pause_play.setText("Playing")

    def update_bar(self):
        self.set_song_length(self.song_length)
        while self.is_playing == True:
            self.update_progress()
            self.current_time1