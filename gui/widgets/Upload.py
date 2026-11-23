from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QDialog, QLabel, QLineEdit
from core.events import Signal

class Upload(QWidget): #this is like a mini page
    def __init__(self, parent=None):
        super().__init__(parent)
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.open_file_dialog)
        Signal.connect(self.import_new_cbz)
        #need a layout
        self.Title = QLineEdit("Required: Upload")
        self.Author = QLineEdit("Required: Artist")
        self.Tags = QLineEdit("Optional Tags")
        self.Description = QLineEdit("Optional Description:")#make these input
        self.import_button =QPushButton("Import Book")

        self.Title.hide()
        self.Author.hide()
        self.Tags.hide()
        self.Description.hide()
        self.import_button.hide()

    def open_file_dialog(self) -> str | None:
        dialog = QFileDialog(self)
        dialog.setNameFilter("Books (*.epub *.cbz)")  # may add more support in future

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.import_new_cbz()
            return dialog.selectedFiles()


    def import_new_cbz(self): 
        self.upload_button.hide()
        self.Title.show()
        self.Author.show()
        self.Tags.show()
        self.Description.show()
        self.import_button.show() # im thinking list comprehension for non needed feilds

        invalid_Feilds = ["", "Required: Upload", "Required: Artist"]
        for i in range(invalid_Feilds):
            if self.Title.text() == i:
                self.Title.setText("Invalid Feild")
            if self.Author.text() == i:
                self.Author.setText("Invalid Feild")

        

        return self.Title.text(), self.Author.text()

    #GAHHHHHHHHHH 


    #Alr im done for today i coded early and its a sunday