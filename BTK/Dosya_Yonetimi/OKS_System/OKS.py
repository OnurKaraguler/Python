import sys
from PyQt5.QtWidgets import *
from OKS_Main_Win import Ui_Form
from OKS_Func.OKS_calculate_note import finding_success_grade

class OKS(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.Pushbutton_hesapla.clicked.connect(self.ortalama_hesapla)
        self.ui.qPushbutton_kaydet.clicked.connect(self.notlari_kaydet)
        self.ui.qPushbutton_oku.clicked.connect(self.ortalamalari_oku)

    def ortalama_hesapla(self):
        self.name = self.ui.lineEdit_isim.text()
        self.surname = self.ui.lineEdit_soyisim.text()
        self.score1 = self.ui.lineEdit_not1.text()
        self.score2 = self.ui.lineEdit_not2.text()
        self.score3 = self.ui.lineEdit_not3.text()

        if (self.name == '' or self.surname == '' or self.score1 == '' or self.score2 == '' or self.score3 == ''):
            self.ui.qLabel_aciklama.setText("Please check the data you entered")
        # elif (int(self.not1) or int(self.not1) or int(self.not1) == int):
        #     self.ui.qLabel_aciklama.setText("Notları sayı olarak giriniz!")
        #     print("Notları sayı olarak giriniz")
        else:
            average_score = (int(self.score1) + int(self.score2) + int(self.score3)) / 3
            success_grade = finding_success_grade(average_score)
            self.ui.qLabel_aciklama.setText(f" {average_score} average score is equivalent to {success_grade}.")

            self.average_score = average_score
            self.success_grade = success_grade
    def notlari_kaydet(self):
        with open("sinav_notlari_sonuclari.txt", "a", encoding='utf-8') as file:
            file.write(self.name + ' ' + self.surname + ':' + self.score1 + ',' + self.score2 + ',' + self.score3
                       +  '---ortalama:' + str(self.average_score) +  '---not:' + str(self.success_grade) + '\n')

            self.ui.lineEdit_isim.clear()
            self.ui.lineEdit_soyisim.clear()
            self.ui.lineEdit_not1.clear()
            self.ui.lineEdit_not2.clear()
            self.ui.lineEdit_not3.clear()

    def ortalamalari_oku(self):
        with open("sinav_notlari_sonuclari.txt", "r", encoding='utf-8') as file:
            self.liste_ortalama = []

            for satir2 in file:
                self.liste_ortalama.append(satir2)

            liste_ortalama = "".join(self.liste_ortalama)
            self.ui.qLabel_aciklama.setText(liste_ortalama)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OKS()
    window.show()
    sys.exit(app.exec_())