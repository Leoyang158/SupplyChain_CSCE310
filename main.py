import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainPage.ui", self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # widget = QtWidgets.QStackedWidget()
    # widget.addWidget(window)
    # widget.setFixedHeight(620)
    # widget.setFixedWidth(480)
    # window.show()
    app.exec()
