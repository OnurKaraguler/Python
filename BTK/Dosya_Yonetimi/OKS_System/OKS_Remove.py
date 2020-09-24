import sys
from PyQt5.QtWidgets import *
from OKS_Remove_Win import Ui_Form_Remove

class Remove(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Remove()
        self.ui.setupUi(self)

        self.removeFromList = Ui_Form_Remove()

        self.qPushbutton_bul.clicked.connect(self.listedenBul)


    def listedenBul(self):
        print('Merhaba')
        name_in_list = self.ui.lineEdit_isim_remove.text()

        self.user_in_list_signal.emit(name_in_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Remove()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())