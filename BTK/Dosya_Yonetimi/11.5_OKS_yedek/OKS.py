import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from OKS_Window import Ui_Form
from OKS_Window_Remove import Ui_Form_Remove

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.qPushbutton_kaydet.clicked.connect(self.not_gir)
        self.ui.qPushbutton_oku.clicked.connect(self.ortalamalari_oku)

    def not_gir(self):
        self.isim = self.ui.lineEdit_isim.text()
        self.soyisim = self.ui.lineEdit_soyisim.text()
        self.not1 = self.ui.lineEdit_not1.text()
        self.not2 = self.ui.lineEdit_not2.text()
        self.not3 = self.ui.lineEdit_not3.text()

        if (self.isim == '' or self.soyisim == '' or self.not1 == '' or self.not2 == '' or self.not3 == ''):
            self.ui.qLabel_aciklama.setText("Veriler kontrol ediniz!")
        elif (int(self.not1) or int(self.not1) or int(self.not1) == int):
            self.ui.qLabel_aciklama.setText("Notları sayı olarak giriniz!")
            print("Notları sayı olarak giriniz")
        else:
            with open("sinav_notlari.txt", "a", encoding='utf-8') as file:
                file.write(self.isim + ' ' + self.soyisim + ':' + self.not1 + ',' + self.not2 + ',' + self.not3 + '\n')

            self.ui.lineEdit_isim_remove.clear()
            self.ui.lineEdit_soyisim_remove.clear()
            self.ui.lineEdit_not1.clear()
            self.ui.lineEdit_not2.clear()
            self.ui.lineEdit_not3.clear()

            self.notlari_kayitet()

    def notlari_kayitet(self):
        with open('sinav_notlari.txt', "r", encoding='utf-8') as file:
            self.listem = []

            for i in file:
                self.satir = i[:-1]
                self.list = self.satir.split(':')
                self.ogrenciAdi = self.list[0]
                self.notlar = self.list[1].split(',')
                # print(self.notlar)

                self.not1 = int(self.notlar[0])
                self.not2 = int(self.notlar[1])
                self.not3 = int(self.notlar[2])

                self.ortalama = (self.not1 + self.not2 + self.not3) / 3
                self.listem.append(f"{self.ogrenciAdi}: {self.not_hesapla(self.ortalama)}\n")

                print(self.listem)

                with open("sonuclar.txt", "w", encoding='utf-8') as file2:
                    for i in self.listem:
                        file2.write(i)

    def not_hesapla(self,ortalama):

        if ortalama  >= 90 and self.ortalama  < 100:
            harf = 'AA'
        elif ortalama  >= 85 and self.ortalama  < 89:
            harf = 'BA'
        elif ortalama  >= 80 and self.ortalama  < 84:
            harf = 'BB'
        elif ortalama  >= 75 and self.ortalama  < 79:
            harf = 'CB'
        elif ortalama  >= 70 and self.ortalama  < 74:
            harf = 'CC'
        elif ortalama  >= 65 and self.ortalama  < 69:
            harf = 'DC'
        elif ortalama  >= 60 and self.ortalama  < 64:
            harf = 'DD'
        elif ortalama  >= 50 and self.ortalama  < 59:
            harf = 'FD'
        else:
            harf = 'FF'

        return harf

    def ortalamalari_oku(self):
        with open("sonuclar.txt", "r", encoding='utf-8') as file:
            self.liste_ortalama = []

            for satir2 in file:
                self.liste_ortalama.append(satir2)

            liste_ortalama = "".join(self.liste_ortalama)
            self.ui.qLabel_aciklama.setText(liste_ortalama)

class Remove(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form_Remove()
        self.ui.setupUi(self)

        self.removeFromList = Ui_Form_Remove()

        self.ui.qPushbutton_removeWindow.clicked.connect(self.listedenBul)

    def listedenBul(self):
        print('Merhaba')
        self.removeFromList.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
