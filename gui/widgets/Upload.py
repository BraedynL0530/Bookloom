from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QDialog, QLabel
from core.events import Signal

class Upload(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.open_file_dialog)
        Signal.connect(self.import_new_cbz)

        self.Title = QLabel("Upload")
        self.Artist = QLabel("Artist")
        self.tags = QLabel("Tags")
        self.Description = QLabel("Description")

    def open_file_dialog(self) -> str | None:
        dialog = QFileDialog(self)
        dialog.setNameFilter("Books (*.epub *.cbz)")  # may add more support in future

        if dialog.exec() == QDialog.DialogCode.Accepted:
            return dialog.selectedFiles()


    def import_new_cbz(self): #fill info
        return