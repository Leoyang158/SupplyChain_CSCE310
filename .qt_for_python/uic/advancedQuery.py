# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vrav/SupplyChain_CSCE310/advancedQuery.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 20, 417, 194))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AdvancedQueryTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.AdvancedQueryTitle.setFont(font)
        self.AdvancedQueryTitle.setObjectName("AdvancedQueryTitle")
        self.verticalLayout_2.addWidget(self.AdvancedQueryTitle)
        self.NeededValueTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NeededValueTitle.setFont(font)
        self.NeededValueTitle.setObjectName("NeededValueTitle")
        self.verticalLayout_2.addWidget(self.NeededValueTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiValue1 = QtWidgets.QComboBox(self.widget)
        self.uiValue1.setObjectName("uiValue1")
        self.horizontalLayout.addWidget(self.uiValue1)
        self.uiValue2 = QtWidgets.QComboBox(self.widget)
        self.uiValue2.setObjectName("uiValue2")
        self.horizontalLayout.addWidget(self.uiValue2)
        self.uiValue3 = QtWidgets.QComboBox(self.widget)
        self.uiValue3.setObjectName("uiValue3")
        self.horizontalLayout.addWidget(self.uiValue3)
        self.uiValue4 = QtWidgets.QComboBox(self.widget)
        self.uiValue4.setObjectName("uiValue4")
        self.horizontalLayout.addWidget(self.uiValue4)
        self.uiSubmitAdvanced = QtWidgets.QPushButton(self.widget)
        self.uiSubmitAdvanced.setObjectName("uiSubmitAdvanced")
        self.horizontalLayout.addWidget(self.uiSubmitAdvanced)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OptionalValuesTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OptionalValuesTitle.setFont(font)
        self.OptionalValuesTitle.setObjectName("OptionalValuesTitle")
        self.verticalLayout.addWidget(self.OptionalValuesTitle)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiOptionalValue1 = QtWidgets.QComboBox(self.widget)
        self.uiOptionalValue1.setObjectName("uiOptionalValue1")
        self.horizontalLayout_2.addWidget(self.uiOptionalValue1)
        self.uiOptionalValue2 = QtWidgets.QComboBox(self.widget)
        self.uiOptionalValue2.setObjectName("uiOptionalValue2")
        self.horizontalLayout_2.addWidget(self.uiOptionalValue2)
        self.uiOptionalValue3 = QtWidgets.QLineEdit(self.widget)
        self.uiOptionalValue3.setObjectName("uiOptionalValue3")
        self.horizontalLayout_2.addWidget(self.uiOptionalValue3)
        self.uiAddAdvanced = QtWidgets.QToolButton(self.widget)
        self.uiAddAdvanced.setObjectName("uiAddAdvanced")
        self.horizontalLayout_2.addWidget(self.uiAddAdvanced)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.AdvancedQueryTitle.setText(_translate("MainWindow", "Advanced Query"))
        self.NeededValueTitle.setText(_translate("MainWindow", "Needed Value"))
        self.uiSubmitAdvanced.setText(_translate("MainWindow", "Submit"))
        self.OptionalValuesTitle.setText(_translate("MainWindow", "Optional Values"))
        self.uiAddAdvanced.setText(_translate("MainWindow", "+"))