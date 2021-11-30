import sys, psycopg2, csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

Math_Symbol = ['=', '-', '+']
AND_OR_Symbol = ['&', '|']
Customer_Attribute = ['id', 'city', 'country', 'state', 'department', 'zipcode']
Order_Attribute = ['type', 'shipping_real', 'shipping_planned', 'delivery_satus', 'customer_id', 'city', 'country',
                   'data', 'id','quantity', 'region', 'state', 'order_status', 'product_id']
Product_Attribute = ['id', 'name', 'category', 'price']

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

    # One Condition
    def basicQuery(self, table, attr, symbol, attr_Input):
        print("Making basic query 1")
        cur = self.conn.cursor()
        queryStr = "SELECT * FROM " + table + " WHERE " + attr + " " + symbol + " \'" + attr_Input + "\'"\
                   + " LIMIT 5;"
        # queryStr = "SELECT * FROM orders LIMIT 1;"
        print(queryStr)
        cur.execute(queryStr)
        # cur.execute("SELECT * FROM orders LIMIT 1;")
        return cur.fetchone()

    # Two Conditions
    def basicQuery2(self, table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input):
        print("Making basic query 2")
        cur = self.conn.cursor()
        print(table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input)
        queryStr = "SELECT * FROM " + table + " WHERE " + attr_1 + " " + symbol_1 + " " + "\'" + attr_1_Input + "\'"\
                   + " " + sign + " " + attr_2 + " " + symbol_2 + " \'" + attr_2_Input + "\'" + " LIMIT 5;"
        print(queryStr)
        cur.execute(queryStr)
        return cur.fetchone()

    # Advanced Query
    def fraud_query(self, country1, country2):
        cur = self.conn.cursor()
        query_str = "select product.name, count(product.name) from product join (\
		            select * from orders join customer on orders.customer_id = customer.id where\
		            orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    and orders.shipping_real > shipping_planned) as orders_filtered \
	                on product.id = orders_filtered.product_id group by product.name;" 
        cur.execute(query_str)
        return cur.fetchone()

    def order_status(self, country1, country2):
        cur = self.conn.cursor()
        query_str = "select order_status, count(order_status) from orders join customer on \
	                orders.customer_id = customer.id where orders.country = \'" + country1 + "\' \
                    and customer.country = \'" + country2 + "\' group by order_status;" 
        cur.execute(query_str)
        return cur.fetchone()

    def product_counts(self, country1, country2):
        curr = self.conn.cursor()
        query_str = "select product.name, count(product.name) from product join ( \
	                select * from orders join customer on orders.customer_id = customer.id \
		            where orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    as orders_filtered on product.id = orders_filtered.product_id group by product.name;"
        
        curr.execute(query_str)
        return curr.fetchone()

    def goods_count(self, country1, country2):
        curr = self.conn.cursor()
        query_str = "select product.category, count(product.category) from product join ( \
	                select * from orders join customer on orders.customer_id = customer.id \
		            where orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    ) as orders_filtered on product.id = orders_filtered.product_id group by product.category;"
        curr.execute(query_str)
        return curr.fetchone()

    def country_count_product(self, product):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from product join orders \
	                on product.id = orders.product_id where product.name = \'" + product + \
                    "\' group by country;"
        
        curr.execute(query_str)
        return curr.fetchone()

    def customer_country_count_product(self, product):
        curr = self.conn.cursor()
        query_str = "select orders_filtered.country, count(orders_filtered.country) from product join ( \
	                select customer.country, orders.product_id from orders join customer on \
		            orders.customer_id = customer.id ) as orders_filtered on product.id = orders_filtered.product_id \
	                where product.name = \'" + product + "\' group by orders_filtered.country;"
        
        curr.execute(query_str)
        return curr.fetchone()

    def country_count_status(self, status):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from orders where order_status = \' " + status + "\' \
                    group by country;"
    
        curr.execute(query_str)
        return curr.fetchone()

    def customer_country_count_status(self, status):
        curr = self.conn.cursor()
        query_str = "select customer.country, count(customer.country) from orders join customer \
	                on orders.customer_id = customer.id where order_status = \' " + status + "\' \
	                group by customer.country; "

        curr.execute(query_str)
        return curr.fetchone()

    def country_count_good_to(self, category):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from orders join product \
            on orders.product_id = product.id where category = \' " + category + "\' \
            group by country;"  
        
        curr.execute(query_str)
        return curr.fetchone()

    def country_count_good_from(self, category):
        curr = self.conn.cursor()
        query_str = "select orders_filtered.country, count(orders_filtered.country) from product join ( \
	                select customer.country, orders.product_id from orders join customer on \
		            orders.customer_id = customer.id ) as orders_filtered on product.id = orders_filtered.product_id \
	                where product.category = \' " + category + "\' group by orders_filtered.country;"
        
        curr.execute(query_str)
        return curr.fetchone()


class MainPage(QtWidgets.QMainWindow):
    # Make connection to Database
    mainDB = DataBase()
    def __init__(self):
        # Loading UI Files
        super(MainPage, self).__init__()
        loadUi("mainPage.ui", self)

        # print(mainDB.makeQuery())

        # Components' Connection
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiFraud.clicked.connect(self.advancedQuery)
        self.uiCustomerAdd.clicked.connect(self.addCustomer)
        self.uiOrderAdd.clicked.connect(self.addOrder)
        self.uiProductAdd.clicked.connect(self.addProduct)

        # Add Selection on ComboBox
        # Customer
        for i in Customer_Attribute:
            if i != "End":
                self.uiCustomerColumn.addItem(i)
                self.uiAddAttributeCombo.addItem(i)

        for i in Math_Symbol:
            if i != "End":
                self.uiCustomerSign.addItem(i)
                self.uiAddSignCombo.addItem(i)

        for i in AND_OR_Symbol:
            if i != "End":
                self.uiAddAndCombo.addItem(i)

        # Order
        for i in Order_Attribute:
            if i != "End":
                self.uiOrderColumn.addItem(i)
                self.uiAddAttributeCombo_2.addItem(i)

        for i in Math_Symbol:
            if i != "End":
                self.uiOrderSign.addItem(i)
                self.uiAddSignCombo_2.addItem(i)

        for i in AND_OR_Symbol:
            if i != "End":
                self.uiAddAndCombo_2.addItem(i)

        # Product
        for i in Product_Attribute:
            if i != "End":
                self.uiProductColumn.addItem(i)
                self.uiAddAttributeCombo_3.addItem(i)

        for i in Math_Symbol:
            if i != "End":
                self.uiProductSign.addItem(i)
                self.uiAddSignCombo_3.addItem(i)

        for i in AND_OR_Symbol:
            if i != "End":
                self.uiAddAndCombo_3.addItem(i)

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

    def customerResult(self):
        # Make Query For Customer
        if self.uiCustomerAdd.text() == "+":
            customerResult = MainPage.mainDB.basicQuery("customer", self.uiCustomerColumn.currentText(), self.uiCustomerSign.currentText(),
                                                     self.uiCustomerText.text())
        else:
            if self.uiAddAndCombo.currentText() == "&":
                sign = "AND"
            else:
                sign = "OR"
            customerResult = MainPage.mainDB.basicQuery2("customer", self.uiCustomerColumn.currentText(),
                                                     self.uiCustomerSign.currentText(),
                                                     self.uiCustomerText.text(), sign,
                                                     self.uiAddAttributeCombo.currentText(),
                                                     self.uiAddSignCombo.currentText(),
                                                     self.uiAddText.text())
        print(customerResult)
        customerView = ResultPage()
        widget.addWidget(customerView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def orderResult(self):
        # Make Query For Order
        if self.uiOrderAdd.text() == "+":
            orderRes = MainPage.mainDB.basicQuery("orders", self.uiOrderColumn.currentText(), self.uiOrderSign.currentText(),
                                              self.uiOrderText.text())
            # orderRes = MainPage.mainDB.basicQuery()
        else:
            if self.uiAddAndCombo_2.currentText() == "&":
                sign = "AND"
            else:
                sign = "OR"
            orderRes = MainPage.mainDB.basicQuery2("orders", self.uiOrderColumn.currentText(), self.uiOrderSign.currentText(),
                                               self.uiOrderText.text(), sign,
                                               self.uiAddAttributeCombo_2.currentText(),
                                               self.uiAddSignCombo_2.currentText(),
                                               self.uiAddText_2.text())
        print(orderRes)
        orderView = ResultPage()
        widget.addWidget(orderView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def productResult(self):
        # Make Query For Product
        if self.uiProductAdd.text() == "+":
            productRes = MainPage.mainDB.basicQuery("product", self.uiProductColumn.currentText(), self.uiProductSign.currentText(),
                                                           self.uiProductText.text())
        else:
            if self.uiAddAndCombo_3.currentText() == "&":
                sign = "AND"
            else:
                sign = "OR"
            print("This sign is " + sign)
            productRes = MainPage.mainDB.basicQuery2("product", self.uiProductColumn.currentText(),
                                                 self.uiProductSign.currentText(),
                                                 self.uiProductText.text(), sign,
                                                 self.uiAddAttributeCombo_3.currentText(),
                                                 self.uiAddSignCombo_3.currentText(),
                                                 self.uiAddText_3.text())
        print(productRes)
        productView = ResultPage()
        widget.addWidget(productView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def advancedQuery(self):
        print(MainPage.mainDB.fraud_query("Indonesia", "Puerto Rico"))
        print(MainPage.mainDB.order_status("Indonesia", "Puerto Rico"))
        print(MainPage.mainDB.country_count_good_from("Electronics"))
        print(MainPage.mainDB.country_count_product("Baby Sweater"))
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
