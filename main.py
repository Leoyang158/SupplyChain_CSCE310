import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("mainPage.ui", self)
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiFraud.clicked.connect(self.advancedQuery)

    def orderResult(self):
        orderView = ResultPage()
        widget.addWidget(orderView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def customerResult(self):
        customerView = ResultPage()
        widget.addWidget(customerView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def productResult(self):
        productView = ResultPage()
        widget.addWidget(productView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def advancedQuery(self):
        advanceView = ResultPage()
        widget.addWidget(advanceView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class AdvancedPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdvancedPage, self).__init__()
        loadUi("advancedQuery.ui", self)
        # self.resultTable = ResultPage()
        self.uiSubmitAdvanced.clicked.connect(self.advancedResult)

    def advancedResult(self):
        resview = ResultPage()
        widget.addWidget(resview)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class ResultPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(ResultPage, self).__init__()
        loadUi("resultTable.ui", self)
        self.uiSearchButton.clicked.connect(self.newSearch)

    def newSearch(self):
        newView = MainPage()
        widget.addWidget(newView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedWidth(700)
    widget.setFixedHeight(720)
    widget.show()
    app.exec_()
