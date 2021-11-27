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
        print("Create cur")

    def makeQuery(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM orders LIMIT 1;")
        return cur.fetchone()

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        # Loading UI Files
        super(MainPage, self).__init__()
        loadUi("mainPage.ui", self)

        # Make connection to Database
        mainDB = DataBase()
        print(mainDB.makeQuery())

        # Components' Connection
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiFraud.clicked.connect(self.advancedQuery)
        self.uiCustomerAdd.clicked.connect(self.addCustomer)
        self.uiOrderAdd.clicked.connect(self.addOrder)
        self.uiProductAdd.clicked.connect(self.addProduct)

        # Hide Some Components
        self.hideAddCustomer()
        self.hideAddOrder()
        self.hideAddProduct()

    def hideAddCustomer(self):
        self.uiAddAndCombo.setVisible(False)
        self.uiAddAttributeCombo.setVisible(False)
        self.uiAddSignCombo.setVisible(False)
        self.uiAddText.setVisible(False)

    def hideAddOrder(self):
        self.uiAddAndCombo_2.setVisible(False)
        self.uiAddAttributeCombo_2.setVisible(False)
        self.uiAddSignCombo_2.setVisible(False)
        self.uiAddText_2.setVisible(False)

    def hideAddProduct(self):
        self.uiAddAndCombo_3.setVisible(False)
        self.uiAddAttributeCombo_3.setVisible(False)
        self.uiAddSignCombo_3.setVisible(False)
        self.uiAddText_3.setVisible(False)

    def addCustomer(self):
        if self.uiCustomerAdd.text() == "-":
            self.uiCustomerAdd.setText("+")
            self.hideAddCustomer()
        else:
            self.uiCustomerAdd.setText("-")
            self.uiAddAndCombo.setVisible(True)
            self.uiAddAttributeCombo.setVisible(True)
            self.uiAddSignCombo.setVisible(True)
            self.uiAddText.setVisible(True)

    def addOrder(self):
        if self.uiOrderAdd.text() == "-":
            self.uiOrderAdd.setText("+")
            self.hideAddOrder()
        else:
            self.uiOrderAdd.setText("-")
            self.uiAddAndCombo_2.setVisible(True)
            self.uiAddAttributeCombo_2.setVisible(True)
            self.uiAddSignCombo_2.setVisible(True)
            self.uiAddText_2.setVisible(True)

    def addProduct(self):
        if self.uiProductAdd.text() == "-":
            self.uiProductAdd.setText("+")
            self.hideAddProduct()
        else:
            self.uiProductAdd.setText("-")
            self.uiAddAndCombo_3.setVisible(True)
            self.uiAddAttributeCombo_3.setVisible(True)
            self.uiAddSignCombo_3.setVisible(True)
            self.uiAddText_3.setVisible(True)

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
        # Loading UI Files
        super(AdvancedPage, self).__init__()
        loadUi("advancedQuery.ui", self)

        # Components' Connection
        self.uiSubmitAdvanced.clicked.connect(self.advancedResult)

    def advancedResult(self):
        resview = ResultPage()
        widget.addWidget(resview)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ResultPage(QtWidgets.QMainWindow):
    def __init__(self):
        # Loading UI Files
        super(ResultPage, self).__init__()
        loadUi("resultTable.ui", self)

        # Components' Connection
        self.uiSearchButton.clicked.connect(self.newSearch)

    def newSearch(self):
        newView = MainPage()
        widget.addWidget(newView)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# Main Execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainPage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedWidth(700)
    widget.setFixedHeight(720)
    widget.show()
    app.exec_()
