# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 793)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.flightManagerGUI = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flightManagerGUI.sizePolicy().hasHeightForWidth())
        self.flightManagerGUI.setSizePolicy(sizePolicy)
        self.flightManagerGUI.setObjectName("flightManagerGUI")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.flightManagerGUI)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Flight_CreateButton = QtWidgets.QPushButton(self.flightManagerGUI)
        self.Flight_CreateButton.setObjectName("Flight_CreateButton")
        self.horizontalLayout.addWidget(self.Flight_CreateButton)
        self.Flight_SearchButton = QtWidgets.QPushButton(self.flightManagerGUI)
        self.Flight_SearchButton.setObjectName("Flight_SearchButton")
        self.horizontalLayout.addWidget(self.Flight_SearchButton)
        self.Flight_UpdateButton = QtWidgets.QPushButton(self.flightManagerGUI)
        self.Flight_UpdateButton.setObjectName("Flight_UpdateButton")
        self.horizontalLayout.addWidget(self.Flight_UpdateButton)
        self.scanLeftoversButton = QtWidgets.QPushButton(self.flightManagerGUI)
        self.scanLeftoversButton.setObjectName("scanLeftoversButton")
        self.horizontalLayout.addWidget(self.scanLeftoversButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Flight_Table = QtWidgets.QTableView(self.flightManagerGUI)
        self.Flight_Table.setMinimumSize(QtCore.QSize(600, 400))
        self.Flight_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Flight_Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Flight_Table.setSortingEnabled(True)
        self.Flight_Table.setObjectName("Flight_Table")
        self.Flight_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Flight_Table.horizontalHeader().setDefaultSectionSize(150)
        self.Flight_Table.horizontalHeader().setSortIndicatorShown(True)
        self.Flight_Table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.Flight_Table)
        self.tabWidget.addTab(self.flightManagerGUI, "")
        self.mealScheduleManagerGUI = QtWidgets.QWidget()
        self.mealScheduleManagerGUI.setObjectName("mealScheduleManagerGUI")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mealScheduleManagerGUI)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MealSchedule_CreateButton = QtWidgets.QPushButton(self.mealScheduleManagerGUI)
        self.MealSchedule_CreateButton.setObjectName("MealSchedule_CreateButton")
        self.horizontalLayout_3.addWidget(self.MealSchedule_CreateButton)
        self.MealSchedule_SearchButton = QtWidgets.QPushButton(self.mealScheduleManagerGUI)
        self.MealSchedule_SearchButton.setObjectName("MealSchedule_SearchButton")
        self.horizontalLayout_3.addWidget(self.MealSchedule_SearchButton)
        self.MealSchedule_UpdateButton = QtWidgets.QPushButton(self.mealScheduleManagerGUI)
        self.MealSchedule_UpdateButton.setObjectName("MealSchedule_UpdateButton")
        self.horizontalLayout_3.addWidget(self.MealSchedule_UpdateButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.MealSchedule_Table = QtWidgets.QTableView(self.mealScheduleManagerGUI)
        self.MealSchedule_Table.setAlternatingRowColors(True)
        self.MealSchedule_Table.setObjectName("MealSchedule_Table")
        self.MealSchedule_Table.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_4.addWidget(self.MealSchedule_Table)
        self.tabWidget.addTab(self.mealScheduleManagerGUI, "")
        self.mealOptionManagerGUI = QtWidgets.QWidget()
        self.mealOptionManagerGUI.setObjectName("mealOptionManagerGUI")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mealOptionManagerGUI)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.MealOption_CreateButton = QtWidgets.QPushButton(self.mealOptionManagerGUI)
        self.MealOption_CreateButton.setObjectName("MealOption_CreateButton")
        self.horizontalLayout_4.addWidget(self.MealOption_CreateButton)
        self.MealOption_SearchButton = QtWidgets.QPushButton(self.mealOptionManagerGUI)
        self.MealOption_SearchButton.setObjectName("MealOption_SearchButton")
        self.horizontalLayout_4.addWidget(self.MealOption_SearchButton)
        self.MealOption_UpdateButton = QtWidgets.QPushButton(self.mealOptionManagerGUI)
        self.MealOption_UpdateButton.setObjectName("MealOption_UpdateButton")
        self.horizontalLayout_4.addWidget(self.MealOption_UpdateButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.MealOption_Table = QtWidgets.QTableView(self.mealOptionManagerGUI)
        self.MealOption_Table.setAlternatingRowColors(True)
        self.MealOption_Table.setObjectName("MealOption_Table")
        self.MealOption_Table.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_3.addWidget(self.MealOption_Table)
        self.tabWidget.addTab(self.mealOptionManagerGUI, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_Out = QtWidgets.QAction(MainWindow)
        self.actionLog_Out.setObjectName("actionLog_Out")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Singapore Airlines - In-flight Catering Manager"))
        self.Flight_CreateButton.setText(_translate("MainWindow", "Create New"))
        self.Flight_SearchButton.setText(_translate("MainWindow", "Search"))
        self.Flight_UpdateButton.setText(_translate("MainWindow", "Update Flights"))
        self.scanLeftoversButton.setText(_translate("MainWindow", "Scan Leftovers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flightManagerGUI), _translate("MainWindow", "Flight Manager"))
        self.MealSchedule_CreateButton.setText(_translate("MainWindow", "Create New"))
        self.MealSchedule_SearchButton.setText(_translate("MainWindow", "Search"))
        self.MealSchedule_UpdateButton.setText(_translate("MainWindow", "Update Meal Schedule"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mealScheduleManagerGUI), _translate("MainWindow", "Meal Schedule"))
        self.MealOption_CreateButton.setText(_translate("MainWindow", "Create New"))
        self.MealOption_SearchButton.setText(_translate("MainWindow", "Search"))
        self.MealOption_UpdateButton.setText(_translate("MainWindow", "Update Meal Options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mealOptionManagerGUI), _translate("MainWindow", "Meal Options"))
        self.actionLog_Out.setText(_translate("MainWindow", "Log Out"))
