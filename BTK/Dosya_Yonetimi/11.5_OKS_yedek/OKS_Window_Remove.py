import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QGridLayout, QPushButton

class Ui_Form_Remove():
    def setupUi(self,Form):
        Form.setWindowTitle("Form")
        Form.setMaximumSize(600,400)
        Form.setMinimumSize(300,200)

        self.top = 150
        self.left = 300
        self.width = 400
        self.height = 300
        Form.setGeometry(self.left, self.top, self.width, self.height)

        # ===============================================================================
        self.qLabel_isim_remove = QLabel()
        self.qLabel_isim_remove.setText("İsim")
        self.qLabel_isim_remove.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_isim_remove = QLineEdit(Form)

        self.qLabel_soyisim = QLabel()
        self.qLabel_soyisim.setText("Soyisim")
        self.qLabel_soyisim.setFont(QtGui.QFont("Sanserif", 10))
        self.lineEdit_soyisim_remove = QLineEdit(Form)


        self.qPushbutton_remove = QPushButton()
        self.qPushbutton_remove.setGeometry(QtCore.QRect(150, 172, 111, 51))
        self.qPushbutton_remove.setText("Çıkar")

        self.qPushbutton_bul = QPushButton()
        self.qPushbutton_bul.setGeometry(QtCore.QRect(150, 172, 111, 51))
        self.qPushbutton_bul.setText("Bul")

        self.qLabel_aciklama = QLabel()
        self.qLabel_aciklama.setText("Aciklama")
        self.qLabel_aciklama.setFont(QtGui.QFont("Sanserif", 10))

#===============================================================================
        qhbox = QHBoxLayout()
        qhbox.addWidget(self.qLabel_isim_remove)
        qhbox.addWidget(self.lineEdit_isim_remove)
        qhbox.addWidget(self.qLabel_soyisim)
        qhbox.addWidget(self.lineEdit_soyisim_remove)


        qhbox2 = QHBoxLayout()
        qhbox2.addStretch()
        qhbox2.addWidget(self.qPushbutton_remove)


        qvbox = QVBoxLayout(Form)
        qvbox.addLayout(qhbox)
        qvbox.addWidget(self.qPushbutton_bul)
        qvbox.addWidget(self.qLabel_aciklama)
        qvbox.addStretch()
        qvbox.addLayout(qhbox2)


        Form.setLayout(qvbox)

#===============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form_Remove()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())