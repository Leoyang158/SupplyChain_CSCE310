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
AdvancedSelections = ['Fraud', 'Order Status', 'Product Counts','Good Counts',
                      'Count of Countries Product (GO)', 'Count of Countries Product (Come)',
                      'Count of Countries Specific Order Status',
                      'Count of Customer Countries Specific Order Status',
                      'Count of countries specific category of goods (Go)',
                      'Count of countries specific category of goods (Come)'
                      ]
# Advanced Query: 'Lasted Product'


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
        return cur.fetchall()

    # Two Conditions
    def basicQuery2(self, table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input):
        print("Making basic query 2")
        cur = self.conn.cursor()
        print(table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input)
        queryStr = "SELECT * FROM " + table + " WHERE " + attr_1 + " " + symbol_1 + " " + "\'" + attr_1_Input + "\'"\
                   + " " + sign + " " + attr_2 + " " + symbol_2 + " \'" + attr_2_Input + "\'" + ";"
        print(queryStr)
        cur.execute(queryStr)
        return cur.fetchall()

    # Advanced Query
    # Fraud
    # done

    def LastedProduct(self):
        cur = self.conn.cursor()
        query_str = ""
        cur.execute(query_str)
        return cur.fetchone()

    def fraud_query(self, country1, country2):
        cur = self.conn.cursor()
        query_str = "select product.name, count(product.name) from product join (\
		            select * from orders join customer on orders.customer_id = customer.id where\
		            orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    and orders.shipping_real > shipping_planned) as orders_filtered \
	                on product.id = orders_filtered.product_id group by product.name;" 
        cur.execute(query_str)
        return cur.fetchone()

    # done
    def order_status(self, country1, country2):
        cur = self.conn.cursor()
        query_str = "select order_status, count(order_status) from orders join customer on \
	                orders.customer_id = customer.id where orders.country = \'" + country1 + "\' \
                    and customer.country = \'" + country2 + "\' group by order_status;" 
        cur.execute(query_str)
        return cur.fetchone()

    # done
    def product_counts(self, country1, country2):
        curr = self.conn.cursor()
        query_str = "select product.name, count(product.name) from product join ( \
	                select * from orders join customer on orders.customer_id = customer.id \
		            where orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    as orders_filtered on product.id = orders_filtered.product_id group by product.name;"
        
        curr.execute(query_str)
        return curr.fetchone()

    # done
    def goods_count(self, country1, country2):
        curr = self.conn.cursor()
        query_str = "select product.category, count(product.category) from product join ( \
	                select * from orders join customer on orders.customer_id = customer.id \
		            where orders.country = \'" + country1 + "\' and customer.country = \'" + country2 + "\' \
                    ) as orders_filtered on product.id = orders_filtered.product_id group by product.category;"
        curr.execute(query_str)
        return curr.fetchone()

    # done
    def country_count_product(self, product):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from product join orders \
	                on product.id = orders.product_id where product.name = \'" + product + \
                    "\' group by country;"
        
        curr.execute(query_str)
        return curr.fetchone()

    # done
    def customer_country_count_product(self, product):
        curr = self.conn.cursor()
        query_str = "select orders_filtered.country, count(orders_filtered.country) from product join ( \
	                select customer.country, orders.product_id from orders join customer on \
		            orders.customer_id = customer.id ) as orders_filtered on product.id = orders_filtered.product_id \
	                where product.name = \'" + product + "\' group by orders_filtered.country;"
        
        curr.execute(query_str)
        return curr.fetchone()

    # done
    def country_count_status(self, status):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from orders where order_status = \' " + status + "\' \
                    group by country;"
    
        curr.execute(query_str)
        return curr.fetchone()

    # done
    def customer_country_count_status(self, status):
        curr = self.conn.cursor()
        query_str = "select customer.country, count(customer.country) from orders join customer \
	                on orders.customer_id = customer.id where order_status = \' " + status + "\' \
	                group by customer.country; "

        curr.execute(query_str)
        return curr.fetchone()

    # done
    def country_count_good_to(self, category):
        curr = self.conn.cursor()
        query_str = "select country, count(country) from orders join product \
            on orders.product_id = product.id where category = \' " + category + "\' \
            group by country;"  
        
        curr.execute(query_str)
        return curr.fetchone()

    # done
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
        loadUi("mainPage_New.ui", self)

        # print(mainDB.makeQuery())

        # Components' Connection
        self.uiOrderSubmit.clicked.connect(self.orderResult)
        self.uiCustomerSubmit.clicked.connect(self.customerResult)
        self.uiProductSubmit.clicked.connect(self.productResult)
        self.uiAdvancedPopUp.clicked.connect(self.advancedQuery)
        self.uiCustomerAdd.clicked.connect(self.addCustomer)
        self.uiOrderAdd.clicked.connect(self.addOrder)
        self.uiProductAdd.clicked.connect(self.addProduct)

        for i in AdvancedSelections:
            if i != "End":
                self.uiAdvancedQueriesSelection.addItem(i)

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
        # making table
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
        # making table
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
        # making table
        productView = ResultPage()
        widget.addWidget(productView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def advancedQuery(self):
        # print(MainPage.mainDB.fraud_query("Indonesia", "Puerto Rico"))
        # print(MainPage.mainDB.order_status("Indonesia", "Puerto Rico"))
        # print(MainPage.mainDB.country_count_good_from("Electronics"))
        # print(MainPage.mainDB.country_count_product("Baby Sweater"))
        advanceView = AdvancedPage(self.uiAdvancedQueriesSelection.currentText())
        widget.addWidget(advanceView)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AdvancedPage(QtWidgets.QMainWindow):
    def __init__(self, querySelection):
        # Loading UI Files
        super(AdvancedPage, self).__init__()
        loadUi("advancedQuery_new.ui", self)
        # print(querySelection)
        self.selection = querySelection
        # Components' Connection
        self.uiSubmitAdvanced.clicked.connect(self.advancedResult)

        # Hide and Change text
        if self.selection == "Count of Countries Product (GO)" or self.selection == "Count of Countries Product (Come)":
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiAdvancedInput1.setText("Product")
        if self.selection == "Count of Countries Specific Order Status" or self.selection == "Count of Customer Countries Specific Order Status":
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiAdvancedInput1.setText("Status")
        if self.selection == "Count of countries specific category of goods (Go)" or self.selection == "Count of countries specific category of goods (Come)":
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiAdvancedInput1.setText("Category")
    def make_table(self, sql_output):
        print("hello world")
    def make_graph(self, sql_output):
        print("hello world")
    def advancedResult(self):
        if self.selection == "Fraud":
            data = self.invoke_fraud()
        elif self.selection == "Order Status":
            data = self.invoke_Order_Status()
        elif self.selection == "Product Counts":
            data = self.invoke_Product_Counts()
        elif self.selection == "Good Counts":
            data = self.invoke_Good_Counts()
        elif self.selection == "Count of Countries Product (GO)":
            data = self.invoke_Country_Count_Product()
        elif self.selection == "Count of Countries Product (Come)":
            data = self.invoke_Customer_Country_Count_Product()
        elif self.selection == "Count of Countries Specific Order Status":
            data = self.invoke_invoke_Country_Count_Status()
        elif self.selection == "Count of Customer Countries Specific Order Status":
            data = self.invoke_Customer_Country_Count_Status()
        elif self.selection == "Count of countries specific category of goods (Go)":
            data = self.invoke_Country_Count_Good_To()
        elif self.selection == "Count of countries specific category of goods (Come)":
            data = self.invoke_Country_Count_Good_From()
        print(data)
        resView = ResultPage()
        widget.addWidget(resView)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def invoke_fraud(self):
        return MainPage.mainDB.fraud_query(self.uiInput1.text(), self.uiInput2.text())

    def invoke_Order_Status(self):
        return MainPage.mainDB.order_status(self.uiInput1.text(), self.uiInput2.text())

    def invoke_Product_Counts(self):
        return MainPage.mainDB.product_counts(self.uiInput1.text(), self.uiInput2.text())

    def invoke_Good_Counts(self):
        return MainPage.mainDB.goods_count(self.uiInput1.text(), self.uiInput2.text())

    def invoke_Country_Count_Product(self):
        return MainPage.mainDB.country_count_product(self.uiInput1.text())

    def invoke_Customer_Country_Count_Product(self):
        return MainPage.mainDB.customer_country_count_product(self.uiInput1.text())

    def invoke_Country_Count_Status(self):
        return MainPage.mainDB.country_count_status(self.uiInput1.text())

    def invoke_Customer_Country_Count_Status(self):
        return MainPage.mainDB.customer_country_count_status(self.uiInput1.text())

    def invoke_Country_Count_Good_To(self):
        return MainPage.mainDB.country_count_good_to(self.uiInput1.text())

    def invoke_Country_Count_Good_From(self):
        return MainPage.mainDB.country_count_good_from(self.uiInput1.text())


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
