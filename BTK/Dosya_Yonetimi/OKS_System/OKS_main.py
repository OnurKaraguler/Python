import sys
from PyQt5.QtWidgets import *
from OKS import OKS

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OKS()
    window.show()
    sys.exit(app.exec_())