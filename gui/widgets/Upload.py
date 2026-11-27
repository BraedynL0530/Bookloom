from PyQt6.QtWidgets import QWidget, QFileDialog, QPushButton, QDialog, QLabel, QLineEdit
from core.events.Signal import Signal

#TODO: layout
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
        self.import_button.connect(self.import_new_cbz)

    def open_file_dialog(self) -> str | None:
        dialog = QFileDialog(self)
        dialog.setNameFilter("Books (*.epub *.cbz)")  # may add more support in future

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.start_import()
            return dialog.selectedFiles()


    def start_import(self): 
        self.upload_button.hide()
        self.Title.show()
        self.Author.show()
        self.Tags.show()
        self.Description.show()
        self.import_button.show() 

        invalid_fields = {"", "Required: Upload", "Required: Artist", "Optional Tags", "Optional Description:","Invalid Feild"}

        for i in range(len(invalid_fields)):
            if self.Title.text() == i:
                self.Title.setText("Invalid Feild")
                self.import_button.setEnabled(False)
            elif self.Author.text() == i:
                self.import_button.setText("Invalid Feild")
                self.Author.setEnabled(False)
            else:
                self.import_button.setEnabled(True)


    def import_new_cbz(self):
        temp_metadata = [self.Description, self.Tags]
        invalid_fields = {"", "Required: Upload", "Required: Artist", "Optional Tags", "Optional Description:","Invalid Feild"}
        meta_data =[item for item in temp_metadata if not invalid_fields] #just heard no ai coding! ill fix that rn

        data = (
            self.Title,
            self.Author,   
        )

        for i in range(len(meta_data)):
            data += (i)

        return data

    #TODO: add hide function and reset after its sent via signal