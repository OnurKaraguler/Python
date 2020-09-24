import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout, \
    QLabel, QVBoxLayout, QPushButton, QComboBox, QGroupBox, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import requests, json, threading

class ExchangeCurrency(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exchange Currency')
        self.setGeometry(400,200,380,400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layout()
        self.timer = threading.Timer(2.0, self.currentCurrency)
        self.timer.start()
        print("Start")

    def widgets(self):
        self.currencyBought_co = QComboBox()
        self.currencyBought_co.addItems(['USD','EUR','TRY'])
        self.currencyReceived_co = QComboBox()
        self.currencyReceived_co.addItems(['USD','EUR','TRY'])

        self.amount_le = QLineEdit('1')

        self.currentCurrency_lb = QLabel()
        self.currentCurrency_lb.setStyleSheet("color: blue;""background-color: pink;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        self.updating_lb = QLabel()
        self.updating_lb.setStyleSheet("color: blue;""background-color: yellow;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        self.result_lb = QLabel()
        self.result_lb.setStyleSheet("color: blue;""background-color: yellow;""font:12pt Times Bold;"
                        "selection-color: yellow;""border:2px solid gray;""border-radius:15px;"
                        "padding: 10px;""selection-background-color: blue;")
        # self.result_lb.setAlignment(Qt.AlignTop)

        self.calc_btn = QPushButton('Exchange')
        self.calc_btn.setStyleSheet("background-color: #9bc9ff;""border-style: outset;""border-width: 2px;"
                                    "border-radius: 10px;""border-color: beige;""font: bold 14px;"
                                    "min-width: 10em;""padding: 6px;")
        self.calc_btn.clicked.connect(self.exchangeCalculation)

        self.closeUpd_btn = QPushButton('Stop Update')
        self.closeUpd_btn.setStyleSheet("background-color: red;""border-style: outset;""border-width: 2px;"
                                    "border-radius: 10px;""border-color: beige;""font: bold 14px;"
                                    "min-width: 10em;""padding: 6px;")
        self.closeUpd_btn.clicked.connect(self.closeUpdate)

        self.openUpd_btn = QPushButton('Update')
        self.openUpd_btn.setStyleSheet("background-color: green;""border-style: outset;""border-width: 2px;"
                                    "border-radius: 10px;""border-color: beige;""font: bold 14px;"
                                    "min-width: 10em;""padding: 6px;")
        self.openUpd_btn.clicked.connect(self.currentCurrency)

    def layout(self):
        self.mainTopLayout = QFormLayout()
        self.mainMiddleLayout = QHBoxLayout()
        self.mainBottomLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.topGroupBox = QGroupBox('Currency Exchange')
        self.topGroupBox.setStyleSheet(""" QGroupBox{background-color: #9bc9ff; font:12pt Times Bold; color:white;
        border:2px solid gray; border-radius:15px;}""")
        # self.topGroupBox.setAlignment(Qt.AlignBottom)
        # self.topGroupBox.setFixedSize(350,100)
        # self.topGroupBox.setCheckable(True)
        # self.topGroupBox.setAlignment(1)

        self.topGroupBox.setLayout(self.mainTopLayout)

        self.mainLayout.addWidget(self.topGroupBox,25)
        self.mainLayout.addLayout(self.mainMiddleLayout)
        self.mainLayout.addLayout(self.mainBottomLayout)
        self.setLayout(self.mainLayout)
        ##################Add Widgets##############
        self.mainTopLayout.addRow('Currency to sell',self.currencyBought_co)
        self.mainTopLayout.addRow('Currency to recieve',self.currencyReceived_co)
        self.mainTopLayout.addRow('Amount',self.amount_le)

        self.mainMiddleLayout.addStretch()
        self.mainMiddleLayout.addWidget(self.calc_btn)

        self.mainBottomLayout.addWidget(self.closeUpd_btn)
        self.mainBottomLayout.addWidget(self.openUpd_btn)

        self.mainLayout.addLayout(self.mainTopLayout)
        self.mainLayout.addWidget(self.currentCurrency_lb,20)
        self.mainLayout.addWidget(self.updating_lb,10)
        self.mainLayout.addWidget(self.result_lb,10)

    def exchangeCalculation(self):
        self.currencyBought = self.currencyBought_co.currentText()
        self.currencyReceived = self.currencyReceived_co.currentText()
        # self.amount = int(self.amount_le.text())
        self.amount = self.amount_le.text()

        try:
            self.amount = int(self.amount)

            api_url = 'https://api.exchangeratesapi.io/latest?base='

            self.result = requests.get(api_url + self.currencyBought)
            self.result = json.loads(self.result.text)

            self.result_lb.setText("{0} {1} = {2} {3}".format(self.amount, self.currencyBought,
                                  self.amount * self.result['rates'][self.currencyReceived], [self.currencyReceived]))
        except Exception:
            QMessageBox.information(self,'Info','Input can only be a number')

    def currentCurrency(self):
        self.currencyBought = self.currencyBought_co.currentText()
        self.currencyReceived = self.currencyReceived_co.currentText()

        api_url = 'https://api.exchangeratesapi.io/latest?base='

        self.result_USD = requests.get(api_url + 'USD')
        self.result_USD = json.loads(self.result_USD.text)
        self.result_EUR = requests.get(api_url + 'EUR')
        self.result_EUR = json.loads(self.result_EUR.text)
        self.result_TRY = requests.get(api_url + 'TRY')
        self.result_TRY = json.loads(self.result_TRY.text)
        # self.currentCurrency_lb.setText("1 {0} = {1} {2}".format(self.currencyBought, self.result["rates"][self.currencyReceived],self.currencyReceived))
        self.currentCurrency_lb.setText(f"1 USD = {self.result_USD['rates']['TRY']} TRY \n1 EUR = {self.result_EUR['rates']['TRY']} TRY"
                                        f"\n1 EUR = {self.result_EUR['rates']['USD']} USD")
        self.updating_lb.setText('Updating is running.')
        print('updating')
        self.timer = threading.Timer(2.0, self.currentCurrency)
        self.timer.start()

    def closeUpdate(self):
        self.timer.cancel()
        self.updating_lb.setText('Updating is stopped.')
        print('timer kapatıldı')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExchangeCurrency()
    sys.exit(app.exec_())