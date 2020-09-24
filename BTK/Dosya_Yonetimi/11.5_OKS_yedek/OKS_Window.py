import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QGridLayout, QPushButton

class Ui_Form():
    def setupUi(self,Form):
        Form.setWindowTitle("Form")
        # Form.resize(400, 300)
        Form.setMaximumSize(600,400)
        Form.setMinimumSize(300,200)

        self.top = 150
        self.left = 300
        self.width = 400
        self.height = 300
        Form.setGeometry(self.left, self.top, self.width, self.height)

        # ===============================================================================
        self.qLabel_isim = QLabel()
        self.qLabel_isim.setText("İsim")
        self.qLabel_isim.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_isim = QLineEdit(Form)

        self.qLabel_soyisim = QLabel()
        self.qLabel_soyisim.setText("Soyisim")
        self.qLabel_soyisim.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_soyisim = QLineEdit(Form)

        self.qLabel_notlar = QLabel()
        self.qLabel_notlar.setText("Notlar")
        self.qLabel_notlar.setFont(QtGui.QFont("Sanserif", 10))

        self.qLabel_not1 = QLabel()
        self.qLabel_not1.setText("1")
        self.qLabel_not1.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_not1 = QLineEdit(Form)

        self.qLabel_not2 = QLabel()
        self.qLabel_not2.setText("2")
        self.qLabel_not2.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_not2 = QLineEdit()

        self.qLabel_not3 = QLabel()
        self.qLabel_not3.setText("3")
        self.qLabel_not3.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_not3 = QLineEdit()

        self.qPushbutton_removeWindow = QPushButton()
        self.qPushbutton_removeWindow.setGeometry(QtCore.QRect(150, 172, 111, 51))
        self.qPushbutton_removeWindow.setText("Çıkar")

        self.qPushbutton_kaydet = QPushButton()
        self.qPushbutton_kaydet.setGeometry(QtCore.QRect(150, 172, 111, 51))
        self.qPushbutton_kaydet.setText("Kaydet")

        self.qPushbutton_oku = QPushButton()
        self.qPushbutton_oku.setGeometry(QtCore.QRect(150, 172, 111, 51))
        self.qPushbutton_oku.setText("Oku")

        self.qLabel_aciklama = QLabel()
        self.qLabel_aciklama.setText("Aciklama")
        self.qLabel_aciklama.setFont(QtGui.QFont("Sanserif", 10))

#===============================================================================
        qhbox = QHBoxLayout()
        qhbox.addWidget(self.qLabel_isim)
        qhbox.addWidget(self.lineEdit_isim)
        qhbox.addWidget(self.qLabel_soyisim)
        qhbox.addWidget(self.lineEdit_soyisim)

        grid = QGridLayout()
        grid.addWidget(self.qLabel_not1, 1, 1)
        grid.addWidget(self.qLabel_not2, 1, 2)
        grid.addWidget(self.qLabel_not3, 1, 3)
        grid.addWidget(self.qLabel_notlar, 2, 0)
        grid.addWidget(self.lineEdit_not1, 2, 1)
        grid.addWidget(self.lineEdit_not2, 2, 2)
        grid.addWidget(self.lineEdit_not3, 2, 3)

        qhbox2 = QHBoxLayout()
        qhbox2.addWidget(self.qPushbutton_removeWindow)
        qhbox2.addStretch()
        qhbox2.addWidget(self.qPushbutton_oku)
        qhbox2.addWidget(self.qPushbutton_kaydet)


        qvbox = QVBoxLayout(Form)
        qvbox.addLayout(qhbox)
        qvbox.addLayout(grid)
        qvbox.addWidget(self.qLabel_aciklama)
        qvbox.addStretch()
        qvbox.addLayout(qhbox2)


        Form.setLayout(qvbox)

#===============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())