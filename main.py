import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainPage.ui", self)
        self.show()
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiFraud.clicked.connect(self.advancedQuery)
        self.advancePage = AdvancedPage()
        self.resultTable = ResultPage()

    def orderResult(self):
        self.resultTable.show()

    def customerResult(self):
        self.resultTable.show()

    def productResult(self):
        self.resultTable.show()

    def advancedQuery(self):
        self.advancedPage.show()

class AdvancedPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdvancedPage, self).__init__()
        loadUi("advancedQuery.ui", self)
        # self.resultTable = ResultPage()
        # self.uiSubmitAdvanced.clicked.connect(self.advancedResult)

    def advancedResult(self):
        self.resultTable.show()

class ResultPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("resultTable.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # widget = QtWidgets.QStackedWidget()
    # widget.addWidget(window)
    # widget.setFixedHeight(620)
    # widget.setFixedWidth(480)
    # window.show()
    app.exec()
