from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from mainscreen import ViewPassword

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 200)

        self.label_username = QLabel(self)
        self.label_username.setText("Username:")
        self.textbox_username = QLineEdit(self)

        self.label_password = QLabel(self)
        self.label_password.setText("Password:")
        self.textbox_password = QLineEdit(self)
        self.textbox_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton(self)
        self.button_login.setText("Login")
        self.button_login.clicked.connect(self.login)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label_username)
        layout.addWidget(self.textbox_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textbox_password)
        layout.addWidget(self.button_login)

    def login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        if username == "1" and password == "2":
            self.hide()  # Hide the login window
            self.view_password = ViewPassword()  # Create an instance of the new page window
            self.view_password.show()  # Show the new page window
