import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import QIcon
from PyQt5.QtCore import Qt
# import register_15_5, login_15_5
import json
import os

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Users Login Page')
        self.setGeometry(400,200,400,300)
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.widget()
        self.layout()

    def toolBar(self):
        self.tb = self.addToolBar('User')
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ##############Toolbar Buttons#################
        ##############Register#################
        self.register_tb = QAction(QIcon('icons/register.png'), 'Register', self)
        self.tb.addAction(self.register_tb)
        self.register_tb.triggered.connect(self.funcRegister)
        ##############Login#################
        self.login_tb = QAction(QIcon('icons/login.png'), 'Login', self)
        self.tb.addAction(self.login_tb)
        # self.login_tb.triggered.connect(self.funcLogin)
        ##############Logout#################
        self.logout_tb = QAction(QIcon('icons/logout.png'), 'Logout', self)
        self.tb.addAction(self.logout_tb)
        ##############Logout#################
        self.identity_tb = QAction(QIcon('icons/identity.png'), 'Identity', self)
        self.tb.addAction(self.identity_tb)
        ##############Exit#################
        self.exit_tb = QAction(QIcon('icons/exit.png'), 'Exit', self)
        self.tb.addAction(self.exit_tb)
        self.exit_tb.triggered.connect(self.funcExit)

    def widget(self):
        pass

    def layout(self):
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

    def funcRegister(self):
        # self.register = register_15_5.Register()     # yeni bir obje oluşturmalısın
        self.register = Register()

    def funcLogin(self):
        pass
        # self.login = login_15_5.Login()

    def funcExit(self):
        sys.exit()


########################################################################
########################################################################
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

        user = User(username=username,password=password,email=email)
        repository.register(user)

        # print(repository.users)



########################################################################
########################################################################
class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

########################################################################
########################################################################
class UserRepository():
    def __init__(self):

        self.users = []
        self.isloggedIn = False
        self.currentUser ={}

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):        # dosya daha önce oluşturuldu mu?
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user:User):
        self.users.append(user)
        self.saveToFile()
        print('Kullanıcı oluşturuldu.')

    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('userssss.json', 'w') as file:
            json.dump(list, file)

            self.loadUsers()


repository = UserRepository()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

