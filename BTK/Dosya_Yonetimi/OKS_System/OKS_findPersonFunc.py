import sys
sys.path.append('C:/Python_Examples/BTK/BTK_QT/Dosya_Yonetimi/OKS_System/')
from PyQt5.QtWidgets import *
from OKS_Remove_Win import Ui_Form_Remove

class OKS_findPerson(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Remove()
        self.ui.setupUi(self)


        self.ui.qPushbutton_find_remove.clicked.connect(self.findPerson)
        # self.ui.qPushbutton_remove.clicked.connect(self.removePerson)

    def findPerson(self):
        with open ('sinav_notlari_sonuclari.txt', 'r', encoding='utf-8') as file:
            students = []
            for i in file:
                students.append(i)

            word = self.ui.lineEdit_isim_remove.text()
            for a in students:
                if word in a:
                    self.ui.qLabel_aciklama_remove.setText(a)
                    # if self.ui.qPushbutton_remove.clicked:
                    #     print(a)

    # def removePerson(self):
    #     self.remove_text = self.ui.qLabel_aciklama_remove.text()
    #     self.ui.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OKS_findPerson()
    window.show()
    sys.exit(app.exec_())