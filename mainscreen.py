from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QInputDialog, QMessageBox
from generate import generate_pass
from savepass import save
     
class ViewPassword(QMainWindow):
    def __init__(self):
        super().__init__()

        def read_passwords():
            with open("passwords.txt") as file:
                contents = file.read()
            self.textbox.setText(contents)
        
        def generate_button():
            self.hide()
            self.generate_button = GenerateSave()
            self.generate_button.show()

        self.setWindowTitle("Passwords")
        self.setGeometry(100, 100, 300, 200)

        self.textbox = QTextEdit()

        self.generate_btn = QPushButton("Generate New Password")
        self.generate_btn.clicked.connect(generate_button)

        self.view_button = QPushButton('View Passwords')
        self.view_button.clicked.connect(read_passwords)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.view_button)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.textbox)


class GenerateSave(QMainWindow):
    def __init__(self):
        super().__init__()

        def generate_password():
            min_len, ok = QInputDialog.getInt(self, "Generate Password", "Enter the minimum length:")
            if ok:
                has_num, ok = QInputDialog.getText(self, "Generate Password", "Do you want numbers? (y/n)")
                if ok:
                    has_special, ok = QInputDialog.getText(self, "Generate Password", "Do you want special characters? (y/n)")
                    if ok:
                        has_num = has_num.lower() == 'y'
                        has_special = has_special.lower() == 'y'
                        pwd = generate_pass(min_len, has_num, has_special)
                        self.textbox.setText(pwd)

        def save_password():
            save_name, ok = QInputDialog.getText(self, "Save Password", "Enter the name of the password:")
            if ok:
                pwd = self.textbox.toPlainText()
                save(pwd, save_name)
                QMessageBox.information(self, "Password Saved", "Password has been saved.")
        
        def go_back():
            self.hide()
            self.go_back = ViewPassword()
            self.go_back.show()

        self.setWindowTitle("Generate Password")
        self.setGeometry(100, 200, 400, 400)
        self.textbox = QTextEdit()

        self.generate_button = QPushButton("Generate New Password")
        self.generate_button.clicked.connect(generate_password)

        self.save_button = QPushButton("Save Password")
        self.save_button.clicked.connect(save_password)

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(go_back)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.textbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.back_button)

