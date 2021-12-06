import sys, csv
# import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSql, QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt

Math_Symbol = ['=', '-', '+']
AND_OR_Symbol = ['&', '|']
Customer_Attribute = ['id', 'city', 'country', 'state', 'department', 'zipcode']
Order_Attribute = ['type', 'shipping_real', 'shipping_planned', 'delivery_satus', 'customer_id', 'city', 'country',
                   'data', 'id','quantity', 'region', 'state', 'order_status', 'product_id']
Product_Attribute = ['id', 'name', 'category', 'price']
AdvancedSelections = ['Late Query', 'Order Status', 'Product Counts','Good Counts',
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
        # host = 'ec2-44-199-86-61.compute-1.amazonaws.com'
        # dbname = 'd9gadra8cohjt0'
        # user = 'jytzjupaqfytoj'
        # port = '5432'
        # password = '2235f9e7e2f3c4a1778c6dc71fd709d492b59563698615697430ebf7262767f1'
        # self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

        self.conn = QSqlDatabase.addDatabase("QPSQL")
        self.conn.setDatabaseName("d9gadra8cohjt0")
        self.conn.setHostName("ec2-44-199-86-61.compute-1.amazonaws.com")
        self.conn.setUserName("jytzjupaqfytoj")
        self.conn.setPassword("2235f9e7e2f3c4a1778c6dc71fd709d492b59563698615697430ebf7262767f1")
        self.conn.open()

    # One Condition
    def basicQuery(self, table, attr, symbol, attr_Input):
        print("Making basic query 1")
        qry = QSqlQuery(self.conn)
        queryStr = "SELECT * FROM " + table + " WHERE " + attr + " " + symbol + " \'" + attr_Input + "\'"\
                   + " LIMIT 5;"
        # queryStr = "SELECT * FROM orders LIMIT 1;"
        print(queryStr)
        qry.prepare(queryStr)
        qry.exec()
        # cur.execute("SELECT * FROM orders LIMIT 1;")
        return qry 

    # Two Conditions
    def basicQuery2(self, table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input):
        print("Making basic query 2")
        # cur = self.conn.cursor()
        qry = QSqlQuery(self.conn)
        print(table, attr_1, symbol_1, attr_1_Input, sign, attr_2, symbol_2, attr_2_Input)
        queryStr = "SELECT * FROM " + table + " WHERE " + attr_1 + " " + symbol_1 + " " + "\'" + attr_1_Input + "\'"\
                   + " " + sign + " " + attr_2 + " " + symbol_2 + " \'" + attr_2_Input + "\'" + ";"
        print(queryStr)
        qry.prepare(queryStr)
        qry.exec()
        # cur.execute(queryStr)
        return qry

    # Advanced Query
    def late_query(self, order_country, cust_country, order_state = "%", cust_state = "%", start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE
        if order_state == "":
            order_state = "%"
        
        if cust_state == "":
            cust_state = "%"
        
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"
        order_country = "'" + order_country + "'"
        cust_country = "'" + cust_country + "'"
        order_state = "'" + order_state + "'"
        cust_state= "'" + cust_state + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        # cur = self.conn.cursor()
        qry = QSqlQuery(self.conn)
        query_str = "select product.name, count(product.name) from product join ( \
		            select * from orders join customer on orders.customer_id = customer.id where \
			        orders.country = " + order_country + " and customer.country = " + cust_country + " \
			        and orders.state like " + order_state + " and customer.state like " + cust_state + " \
                    and orders.shipping_real > shipping_planned) as orders_filtered on product.id = \
                    orders_filtered.product_id where date > " + start_date + " and date < " + end_date + " group by product.name;"

        
        
        query_str = (' '*1).join(query_str.split())
        print(query_str)
        qry.prepare(query_str)
        # cur.execute(query_str)
        # return cur.fetchone()
        qry.exec()
        return qry

    def order_status(self, order_country, cust_country, order_state = "%", cust_state = "%", start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a GRAPH
        if order_state == "":
            order_state = "%"
        
        if cust_state == "":
            cust_state = "%"
        
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"
        order_country = "'" + order_country + "'"
        cust_country = "'" + cust_country + "'"
        order_state = "'" + order_state + "'"
        cust_state= "'" + cust_state + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select order_status, count(order_status) from orders join customer on \
                    orders.customer_id = customer.id where orders.country = " + order_country + \
                    " and customer.country = " + cust_country + " and orders.state like " + order_state + \
                    " and customer.state like " + cust_state + " and date > " + start_date + " and date < " \
                    + end_date + " group by order_status;"
        print(query_str)
        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def product_counts(self,  order_country, cust_country, order_state = "%", cust_state = "%", start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE
        if order_state == "":
            order_state = "%"
        
        if cust_state == "":
            cust_state = "%"
        
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        order_country = "'" + order_country + "'"
        cust_country = "'" + cust_country + "'"
        order_state = "'" + order_state + "'"
        cust_state= "'" + cust_state + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select product.name, count(product.name) from product join (select * from orders join customer on \
		            orders.customer_id = customer.id where orders.country = " + order_country + " and customer.country = " + cust_country + " \
                    and orders.state like " + order_state + " and customer.state like " + cust_state + " ) as orders_filtered on product.id = \
                    orders_filtered.product_id where date > " + start_date + " and date < " + end_date + " group by product.name;"
        
        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def goods_count(self,  order_country, cust_country, order_state = "%", cust_state = "%", start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE
        if order_state == "":
            order_state = "%"
        
        if cust_state == "":
            cust_state = "%"
        
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        order_country = "'" + order_country + "'"
        cust_country = "'" + cust_country + "'"
        order_state = "'" + order_state + "'"
        cust_state= "'" + cust_state + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select product.category, count(product.category) from product join ( select * from orders join customer on \
		            orders.customer_id = customer.id where orders.country = " + order_country + " and customer.country = " + cust_country + \
		            " and orders.state like " + order_state + " and customer.state like " + cust_state + " ) as orders_filtered on product.id = \
                    orders_filtered.product_id where date > " + start_date + " and date < " + end_date + " group by product.category;"

        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def country_count_product(self, product, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        product = "'" + product + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select country, count(country) from product join orders on product.id = orders.product_id \
	                where product.name = " + product + " and date > " + start_date + " and date < " + end_date + \
	                " group by country; "
        
        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def customer_country_count_product(self, product, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a GRAPH    
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        product = "'" + product + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select orders_filtered.country, count(orders_filtered.country) from product join ( \
	                select customer.country, orders.product_id, orders.date from orders join customer on \
		            orders.customer_id = customer.id ) as orders_filtered on product.id = orders_filtered.product_id \
	                where product.name = " + product + " and date > " + start_date + " and date < " + end_date + \
	                " group by orders_filtered.country;"
        
        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def country_count_status(self, status, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        status = "'" + status + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select country, count(country) from orders where order_status = " + status + \
	                " and date > " + start_date + " and date < " + end_date + " group by country;"
        
        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def customer_country_count_status(self, status, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a GRAPH
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        status = "'" + status + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select customer.country, count(customer.country) from orders join customer on orders.customer_id \
                = customer.id where order_status = " + status + " and date > " + start_date + " and date < " + end_date + \
	            " group by customer.country;"

        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def country_count_good_to(self, category, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a TABLE  
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        category = "'" + category + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select country, count(country) from orders join product  on orders.product_id = product.id \
                where category = " + category + " and  date > " + start_date + " and date < " + end_date + \
	            " group by country;"

        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry

    def country_count_good_from(self, category, start_date = "01-01-1990", end_date = "12-30-2019"):
        # Will output a GRAPH
        if start_date == "":
            start_date = "01-01-1990"
        
        if end_date == "":
            end_date = "12-30-2019"

        category = "'" + category + "'"
        start_date = "'" + start_date + "'"
        end_date = "'" + end_date + "'"

        qry = QSqlQuery(self.conn)
        query_str = "select orders_filtered.country, count(orders_filtered.country) from product join ( \
	                select customer.country, orders.product_id, orders.date from orders join customer on \
		            orders.customer_id = customer.id ) as orders_filtered on product.id = orders_filtered.product_id \
	                where product.category = " + category + " and date > " + start_date + " and date < " + end_date + \
	                " group by orders_filtered.country;"

        query_str = (' '*1).join(query_str.split())
        qry.prepare(query_str)
        qry.exec()
        return qry


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

    def make_table(self, sql_output):
        model = QSqlQueryModel()
        model.setQuery(sql_output)

        # Set the table's  model to the model made above.
        self.uiBasicTable.setModel(model)

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
        # the basic query output is here....
        # call the function to create table or graph (base)
        self.make_table(customerResult)

        # customerView = ResultPage()
        # widget.addWidget(customerView)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

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
        # the basic query output is here....
        # Create a query model object and set the query to the query above
        self.make_table(orderRes)

        # call the function to create table or graph (base)

        # orderView = ResultPage()
        # widget.addWidget(orderView)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

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
        # the basic query output is here....
        # call the function to create table or graph (base)
        self.make_table(productRes)

        # productView = ResultPage()
        # widget.addWidget(productView)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

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
        print(querySelection)
        self.selection = querySelection
        # Components' Connection
        self.uiSubmitAdvanced.clicked.connect(self.advancedResult)
        self.uiAdvancedBack.clicked.connect(self.backToMain)
        # Hide and Change text
        if self.selection == "Late Query" or self.selection == "Order Status" or self.selection == "Product Counts" or self.selection == "'Good Counts":
            # print("here")
            self.uiAdvancedInput2.setVisible(True)
            self.uiInput3.setVisible(True)
            self.uiAdvancedInput3.setVisible(True)
            self.uiInput4.setVisible(True)
            self.uiAdvancedInput4.setVisible(True)
            self.line_2.setVisible(True)
            self.uiAdvancedInput1.setText("Country 1")
        elif self.selection == "Count of Countries Product (GO)" or self.selection == "Count of Countries Product (Come)":
            # print("here")
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiInput3.setVisible(False)
            self.uiAdvancedInput3.setVisible(False)
            self.uiInput4.setVisible(False)
            self.uiAdvancedInput4.setVisible(False)
            self.line_2.setVisible(False)
            self.uiAdvancedInput1.setText("Product")
        elif self.selection == "Count of Countries Specific Order Status" or self.selection == "Count of Customer Countries Specific Order Status":
            # print("here")
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiInput3.setVisible(False)
            self.uiAdvancedInput3.setVisible(False)
            self.uiInput4.setVisible(False)
            self.uiAdvancedInput4.setVisible(False)
            self.line_2.setVisible(False)
            self.uiAdvancedInput1.setText("Status")
        elif self.selection == "Count of countries specific category of goods (Go)" or self.selection == "Count of countries specific category of goods (Come)":
            # print("here")
            self.uiInput2.setVisible(False)
            self.uiAdvancedInput2.setVisible(False)
            self.uiInput3.setVisible(False)
            self.uiAdvancedInput3.setVisible(False)
            self.uiInput4.setVisible(False)
            self.uiAdvancedInput4.setVisible(False)
            self.line_2.setVisible(False)
            self.uiAdvancedInput1.setText("Category")


    def make_table(self, sql_output):
        model = QSqlQueryModel()
        model.setQuery(sql_output)

        # Set the table's  model to the model made above.
        self.uiAdvancedTable.setModel(model)

    def make_graph(self, sql_output, queryName = ""):
         # start the sql graph here (advanced)
        xAxis = []
        yAxis = []

        # Puts data into format useable by graph
        max = -1
        while sql_output.next():
            xAxis.append(sql_output.value(0))
            yAxis.append(sql_output.value(1))
            if(max < sql_output.value(1)):
                max = sql_output.value(1)

        # Deletes any widgets that were in the vertical layout
        # Important so that you don't have multiple graphs everytime you do a search
        for i in range(self.verticalLayout.count()):
            if(isinstance(self.verticalLayout.itemAt(i).widget(), QChartView)):
                self.verticalLayout.itemAt(i).widget().setParent(None)

        # Still not sure if you need this here but keep it just in case
        set0 = QBarSet('X0')

        # Add the y-axis to the set
        set0.append(yAxis)

        # Add the data set to the series
        series = QBarSeries()
        series.append(set0)

        # Create the chart object and add the series to it
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(queryName)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Create the x-axis object
        axisX = QBarCategoryAxis()
        axisX.append(xAxis)
        axisX.setLabelsAngle(-90)

        # Create the y axis object and set it's range
        # Data is not stored in the y-axis, it's stored in the series you created earlier
        axisY = QValueAxis()
        axisY.setRange(0, max)

        # Add x-axis and y-axis to chart
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        # Removes the useless legend
        chart.legend().setVisible(False)

        # Create the chart view from the chart object
        chartView = QChartView(chart)
        chartView.setFixedHeight(400)

        # Add the chart view to the vertical layout (which should be added via the UI creator.)
        self.uiAdvancedTable.setVisible(False)

        # vbox = QVBoxLayout()
        # self.uiAdvancedGraph.setLayout(vbox)
        # vbox.addWidget(chartView)
    
        self.verticalLayout.addWidget(chartView)

    def backToMain(self):
        result = ResultPage()
        widget.addWidget(result)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def advancedResult(self):
        # queryRes: represent the result object 
        if self.selection == "Late Query":
            queryRes = self.invoke_fraud()
            self.make_table(queryRes)
        elif self.selection == "Order Status":
            queryRes = self.invoke_Order_Status()
            self.make_graph(queryRes, "Order Status")
        elif self.selection == "Product Counts":
            queryRes = self.invoke_Product_Counts()
            self.make_table(queryRes)
        elif self.selection == "Good Counts":
            queryRes = self.invoke_Good_Counts()
            self.make_table(queryRes)
        elif self.selection == "Count of Countries Product (GO)":
            queryRes = self.invoke_Country_Count_Product()
            self.make_table(queryRes)
        elif self.selection == "Count of Countries Product (Come)":
            queryRes = self.invoke_Customer_Country_Count_Product()
            self.make_graph(queryRes, "Count of Countries Product (Come)")
        elif self.selection == "Count of Countries Specific Order Status":
            queryRes = self.invoke_Country_Count_Status()
            self.make_table(queryRes)
        elif self.selection == "Count of Customer Countries Specific Order Status":
            queryRes = self.invoke_Customer_Country_Count_Status()
            self.make_graph(queryRes, "Count of Customer Countries Specific Order Status")
        elif self.selection == "Count of countries specific category of goods (Go)":
            queryRes = self.invoke_Country_Count_Good_To()
            self.make_table(queryRes)
        elif self.selection == "Count of countries specific category of goods (Come)":
            queryRes = self.invoke_Country_Count_Good_From()
            self.make_graph(queryRes, "Count of countries specific category of goods (Come)")
        # the advanced output is here....
        # call the function to create table or graph

        # self.make_table(queryRes)

    def invoke_fraud(self):
        return MainPage.mainDB.late_query(self.uiInput1.text(), self.uiInput2.text(), self.uiInput3.text(), self.uiInput4.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Order_Status(self):
        return MainPage.mainDB.order_status(self.uiInput1.text(), self.uiInput2.text(), self.uiInput3.text(), self.uiInput4.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Product_Counts(self):
        return MainPage.mainDB.product_counts(self.uiInput1.text(), self.uiInput2.text(), self.uiInput3.text(), self.uiInput4.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Good_Counts(self):
        return MainPage.mainDB.goods_count(self.uiInput1.text(), self.uiInput2.text(), self.uiInput3.text(), self.uiInput4.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Country_Count_Product(self):
        return MainPage.mainDB.country_count_product(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Customer_Country_Count_Product(self):
        return MainPage.mainDB.customer_country_count_product(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Country_Count_Status(self):
        return MainPage.mainDB.country_count_status(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Customer_Country_Count_Status(self):
        return MainPage.mainDB.customer_country_count_status(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Country_Count_Good_To(self):
        return MainPage.mainDB.country_count_good_to(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())

    def invoke_Country_Count_Good_From(self):
        return MainPage.mainDB.country_count_good_from(self.uiInput1.text(), self.uiInput5.text(), self.uiInput6.text())


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
    """
    test = DataBase()
    print(test.late_query("Indonesia", "Puerto Rico", start_date="01-15-2018", end_date = "01-31-2018"))
    print(test.order_status("Indonesia", "Puerto Rico", start_date="01-15-2018", end_date = "01-31-2018"))
    print(test.product_counts("Indonesia", "Puerto Rico", start_date="01-15-2018", end_date = "01-31-2018"))
    print(test.goods_count("Indonesia", "Puerto Rico", start_date="01-15-2018", end_date = "01-31-2018"))
    print(test.country_count_product("Baby sweater", "12-01-2017", "12-30-2017"))
    print(test.customer_country_count_product("Baby sweater", "12-01-2017", "12-30-2017"))
    print(test.country_count_status("COMPLETE", "12-01-2017", "12-30-2017"))
    print(test.customer_country_count_status("COMPLETE", "12-01-2017", "12-30-2017"))
    print(test.country_count_good_to("Electronics", "01-01-2017", "12-30-2017"))
    print(test.country_count_good_from("Electronics", "01-01-2017", "12-30-2017"))
    """
    app = QApplication(sys.argv)
    window = MainPage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedWidth(700)
    widget.setFixedHeight(1000)
    widget.show()
    app.exec_()



