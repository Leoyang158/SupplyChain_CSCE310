# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vrav/SupplyChain_CSCE310/advancedQuery_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(81, 22, 492, 831))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AdvancedQueryTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.AdvancedQueryTitle.setFont(font)
        self.AdvancedQueryTitle.setObjectName("AdvancedQueryTitle")
        self.verticalLayout.addWidget(self.AdvancedQueryTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiAdvancedBack = QtWidgets.QPushButton(self.layoutWidget)
        self.uiAdvancedBack.setObjectName("uiAdvancedBack")
        self.horizontalLayout.addWidget(self.uiAdvancedBack)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.NeededValueTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NeededValueTitle.setFont(font)
        self.NeededValueTitle.setObjectName("NeededValueTitle")
        self.verticalLayout.addWidget(self.NeededValueTitle)
        self.line_0 = QtWidgets.QFrame(self.layoutWidget)
        self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_0.setObjectName("line_0")
        self.verticalLayout.addWidget(self.line_0)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiAdvancedInput1 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput1.setObjectName("uiAdvancedInput1")
        self.horizontalLayout_2.addWidget(self.uiAdvancedInput1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.uiInput1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput1.setText("")
        self.uiInput1.setObjectName("uiInput1")
        self.horizontalLayout_2.addWidget(self.uiInput1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiAdvancedInput2 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput2.setObjectName("uiAdvancedInput2")
        self.horizontalLayout_5.addWidget(self.uiAdvancedInput2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.uiInput2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput2.setObjectName("uiInput2")
        self.horizontalLayout_5.addWidget(self.uiInput2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_1 = QtWidgets.QFrame(self.layoutWidget)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout.addWidget(self.line_1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAdvancedInput3 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput3.setObjectName("uiAdvancedInput3")
        self.horizontalLayout_3.addWidget(self.uiAdvancedInput3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.uiInput3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput3.setText("")
        self.uiInput3.setObjectName("uiInput3")
        self.horizontalLayout_3.addWidget(self.uiInput3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiAdvancedInput4 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput4.setObjectName("uiAdvancedInput4")
        self.horizontalLayout_4.addWidget(self.uiAdvancedInput4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.uiInput4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput4.setObjectName("uiInput4")
        self.horizontalLayout_4.addWidget(self.uiInput4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiAdvancedInput5 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput5.setObjectName("uiAdvancedInput5")
        self.horizontalLayout_7.addWidget(self.uiAdvancedInput5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.uiInput5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput5.setObjectName("uiInput5")
        self.horizontalLayout_7.addWidget(self.uiInput5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiAdvancedInput6 = QtWidgets.QLabel(self.layoutWidget)
        self.uiAdvancedInput6.setObjectName("uiAdvancedInput6")
        self.horizontalLayout_6.addWidget(self.uiAdvancedInput6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.uiInput6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiInput6.setObjectName("uiInput6")
        self.horizontalLayout_6.addWidget(self.uiInput6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.uiAdvancedTable = QtWidgets.QTableView(self.layoutWidget)
        self.uiAdvancedTable.setObjectName("uiAdvancedTable")
        self.verticalLayout.addWidget(self.uiAdvancedTable)
        self.uiSubmitAdvanced = QtWidgets.QPushButton(self.layoutWidget)
        self.uiSubmitAdvanced.setObjectName("uiSubmitAdvanced")
        self.verticalLayout.addWidget(self.uiSubmitAdvanced)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AdvancedQueryTitle.setText(_translate("MainWindow", "Advanced Query "))
        self.uiAdvancedBack.setText(_translate("MainWindow", "Back"))
        self.NeededValueTitle.setText(_translate("MainWindow", "Needed Value"))
        self.uiAdvancedInput1.setText(_translate("MainWindow", "Country 1"))
        self.uiAdvancedInput2.setText(_translate("MainWindow", "Country 2"))
        self.uiAdvancedInput3.setText(_translate("MainWindow", "State 1"))
        self.uiAdvancedInput4.setText(_translate("MainWindow", "State 2"))
        self.uiAdvancedInput5.setText(_translate("MainWindow", "Start Date"))
        self.uiAdvancedInput6.setText(_translate("MainWindow", "End Date"))
        self.uiSubmitAdvanced.setText(_translate("MainWindow", "Submit"))
