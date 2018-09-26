# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createMealScheduleGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createMealScheduleDialog(object):
    def setupUi(self, createMealScheduleDialog):
        createMealScheduleDialog.setObjectName("createMealScheduleDialog")
        createMealScheduleDialog.resize(500, 168)
        createMealScheduleDialog.setMinimumSize(QtCore.QSize(500, 100))
        createMealScheduleDialog.setMaximumSize(QtCore.QSize(500, 260))
        font = QtGui.QFont()
        font.setPointSize(11)
        createMealScheduleDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(createMealScheduleDialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 10, 81, 111))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(createMealScheduleDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 390, 146))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.flightIdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.flightIdLabel.setObjectName("flightIdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.flightIdLabel)
        self.flightIdLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.flightIdLineEdit.setToolTip("")
        self.flightIdLineEdit.setInputMask("")
        self.flightIdLineEdit.setText("")
        self.flightIdLineEdit.setMaxLength(3)
        self.flightIdLineEdit.setFrame(True)
        self.flightIdLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.flightIdLineEdit.setCursorPosition(0)
        self.flightIdLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.flightIdLineEdit.setObjectName("flightIdLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.flightIdLineEdit)
        self.classLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classLabel.setObjectName("classLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.classLabel)
        self.classComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.classComboBox.setEditable(True)
        self.classComboBox.setObjectName("classComboBox")
        self.classComboBox.addItem("")
        self.classComboBox.addItem("")
        self.classComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.classComboBox)
        self.mealTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.mealTypeLabel.setObjectName("mealTypeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mealTypeLabel)
        self.mealTypeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.mealTypeComboBox.setEditable(True)
        self.mealTypeComboBox.setObjectName("mealTypeComboBox")
        self.mealTypeComboBox.addItem("")
        self.mealTypeComboBox.addItem("")
        self.mealTypeComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mealTypeComboBox)
        self.timeServedLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timeServedLabel.setObjectName("timeServedLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.timeServedLabel)
        self.timeServedDateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.timeServedDateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 9, 1), QtCore.QTime(0, 0, 0)))
        self.timeServedDateTimeEdit.setCalendarPopup(True)
        self.timeServedDateTimeEdit.setObjectName("timeServedDateTimeEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.timeServedDateTimeEdit)
        self.serviceOrderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.serviceOrderLabel.setObjectName("serviceOrderLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.serviceOrderLabel)
        self.serviceOrderSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.serviceOrderSpinBox.setMinimum(1)
        self.serviceOrderSpinBox.setMaximum(9)
        self.serviceOrderSpinBox.setObjectName("serviceOrderSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.serviceOrderSpinBox)
        self.timeServedLabel.setBuddy(self.timeServedDateTimeEdit)

        self.retranslateUi(createMealScheduleDialog)
        self.buttonBox.accepted.connect(createMealScheduleDialog.accept)
        self.buttonBox.rejected.connect(createMealScheduleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(createMealScheduleDialog)

    def retranslateUi(self, createMealScheduleDialog):
        _translate = QtCore.QCoreApplication.translate
        createMealScheduleDialog.setWindowTitle(_translate("createMealScheduleDialog", "Dialog"))
        self.flightIdLabel.setToolTip(_translate("createMealScheduleDialog", "Enter Flight Number Here (Maximum 3 Numbers)"))
        self.flightIdLabel.setText(_translate("createMealScheduleDialog", "Flight ID"))
        self.flightIdLineEdit.setPlaceholderText(_translate("createMealScheduleDialog", "e.g. 15"))
        self.classLabel.setText(_translate("createMealScheduleDialog", "Class"))
        self.classComboBox.setItemText(0, _translate("createMealScheduleDialog", "First"))
        self.classComboBox.setItemText(1, _translate("createMealScheduleDialog", "Business"))
        self.classComboBox.setItemText(2, _translate("createMealScheduleDialog", "Economy"))
        self.mealTypeLabel.setText(_translate("createMealScheduleDialog", "Meal Type"))
        self.mealTypeComboBox.setItemText(0, _translate("createMealScheduleDialog", "Breakfast"))
        self.mealTypeComboBox.setItemText(1, _translate("createMealScheduleDialog", "Lunch"))
        self.mealTypeComboBox.setItemText(2, _translate("createMealScheduleDialog", "Dinner"))
        self.timeServedLabel.setText(_translate("createMealScheduleDialog", "Time Served"))
        self.serviceOrderLabel.setText(_translate("createMealScheduleDialog", "Service Order"))

