from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QSlider, QLabel
from PyQt6.QtGui import QColor, QFont, QIcon, QPixmap
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

#TODO style it, and fix parts
class MusicPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pause_play = QPushButton('Paused')#emojis later! QICON
        self.skip = QPushButton('->')
        self.previous = QPushButton("<-")
        self.pause_play.clicked.connect(self.play_pause)
        self.progress_bar = QSlider()#horizontal, max = length when of song, update it with current time

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)

        self.track_name = QLabel()
        self.track_artist = QLabel()
        self.duration = QLabel()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress(self.player.position()))# use media palyers instead layer
        self.timer.start(100)

    def play_pause(self):
        if not self.player.isPlaying():
            self.player.play()
            self.update_buttons(True)
        else:
            self.player.pause()
            self.update_buttons(False)


    def set_track(self, track_name:str, track_artist:str, source:str):
        self.player.setSource(QUrl(source))
        duration = round(self.player.duration(),2)#more accurate but may not perfectly match slider
        self.duration.setText(str(duration))#needs async

        if track_name:
            self.track_name.setText(track_name)

        if track_artist:
            self.track_artist.setText(track_artist)

        self.progress_bar.setMaximum(int(duration))
        self.progress_bar.setValue(0)
        self.player.play()
        self.update_buttons(True)


    def update_progress(self,current_position:float): #float 64 type casted to int
        self.progress_bar.setValue(int(current_position))


    def update_buttons(self,playing):
        if playing == False:
            self.pause_play.setText("Paused")
        else:
            self.pause_play.setText("Playing")