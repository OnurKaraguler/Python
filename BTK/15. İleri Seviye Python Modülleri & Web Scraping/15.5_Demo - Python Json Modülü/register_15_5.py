import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QPushButton
import main_15_5

# repository = main_15_5.UserRepository()

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(450,250,300,100)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.le_username = QLineEdit()
        self.le_password = QLineEdit()
        self.le_email = QLineEdit()
        self.btn_register = QPushButton('Register')
        self.btn_register.clicked.connect(self.register)

    def layouts(self):
        self.mainLayout = QFormLayout()
        self.setLayout(self.mainLayout)
        ##############Add Widgets#################
        self.mainLayout.addRow('username',self.le_username)
        self.mainLayout.addRow('Password', self.le_password)
        self.mainLayout.addRow('Email', self.le_email)
        self.mainLayout.addRow('', self.btn_register)

    def register(self):
        username = self.le_username.text()
        password = self.le_password.text()
        email = self.le_email.text()

        user = main_15_5.User(username=username,password=password,email=email)
        # repository.register(user)