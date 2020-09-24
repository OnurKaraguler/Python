import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton

class Login(QWidget):
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
        self.btn_login = QPushButton('Login')
        self.btn_login.clicked.connect(self.funcLogin)

    def layouts(self):
        self.mainLayout = QFormLayout()
        self.setLayout(self.mainLayout)
        ##############Add Widgets#################
        self.mainLayout.addRow('Username', self.le_username)
        self.mainLayout.addRow('Password', self.le_password)
        self.mainLayout.addRow('', self.btn_login)

    def funcLogin(self):
        pass
        # self.users = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec_())