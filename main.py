import sys, psycopg2, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class DataBase:
    def __init__(self):
        # DataBase API Keys
        host = 'ec2-44-199-86-61.compute-1.amazonaws.com'
        dbname = 'd9gadra8cohjt0'
        user = 'jytzjupaqfytoj'
        port = '5432'
        password = '2235f9e7e2f3c4a1778c6dc71fd709d492b59563698615697430ebf7262767f1'
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("mainPage.ui", self)
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiFraud.clicked.connect(self.advancedQuery)
        self.uiAddAndCombo.setVisible(False)
        self.uiAddAttributeCombo.setVisible(False)
        self.uiAddSignCombo.setVisible(False)
        self.uiAddText.setVisible(False)
        self.uiCustomerAdd.clicked.connect(self.add)

    def add(self):
        self.uiAddAndCombo.setVisible(True)
        self.uiAddAttributeCombo.setVisible(True)
        self.uiAddSignCombo.setVisible(True)
        self.uiAddText.setVisible(True)

    def orderResult(self):
        orderView = ResultPage()
        widget.addWidget(orderView)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # Make Query For Order

    def customerResult(self):
        customerView = ResultPage()
        widget.addWidget(customerView)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # Make Query For Customer

    def productResult(self):
        productView = ResultPage()
        widget.addWidget(productView)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # Make Query For Product

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
