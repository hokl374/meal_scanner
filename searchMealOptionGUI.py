# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchMealOptionGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_searchMealOptionDialog(object):
    def setupUi(self, searchMealOptionDialog):
        searchMealOptionDialog.setObjectName("searchMealOptionDialog")
        searchMealOptionDialog.resize(628, 335)
        searchMealOptionDialog.setMinimumSize(QtCore.QSize(500, 260))
        searchMealOptionDialog.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        searchMealOptionDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(searchMealOptionDialog)
        self.buttonBox.setGeometry(QtCore.QRect(540, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(searchMealOptionDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.optionCodeCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.optionCodeCheckBox.setObjectName("optionCodeCheckBox")
        self.gridLayout.addWidget(self.optionCodeCheckBox, 2, 1, 1, 1)
        self.optionNameCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.optionNameCheckBox.setTristate(False)
        self.optionNameCheckBox.setObjectName("optionNameCheckBox")
        self.gridLayout.addWidget(self.optionNameCheckBox, 1, 1, 1, 1)
        self.weightCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.weightCheckBox.setObjectName("weightCheckBox")
        self.gridLayout.addWidget(self.weightCheckBox, 4, 1, 1, 1)
        self.mealIdCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.mealIdCheckBox.setObjectName("mealIdCheckBox")
        self.gridLayout.addWidget(self.mealIdCheckBox, 0, 1, 1, 1)
        self.colourLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.colourLineEdit.setMaxLength(3)
        self.colourLineEdit.setObjectName("colourLineEdit")
        self.gridLayout.addWidget(self.colourLineEdit, 3, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.unitsUpliftedSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.unitsUpliftedSpinBox.setMaximum(999)
        self.unitsUpliftedSpinBox.setObjectName("unitsUpliftedSpinBox")
        self.horizontalLayout_5.addWidget(self.unitsUpliftedSpinBox)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setIndent(18)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.unitsUpliftedSpinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.unitsUpliftedSpinBox_2.setMaximum(999)
        self.unitsUpliftedSpinBox_2.setObjectName("unitsUpliftedSpinBox_2")
        self.horizontalLayout_5.addWidget(self.unitsUpliftedSpinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 2, 1, 1)
        self.unitsLeftoverCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.unitsLeftoverCheckBox.setObjectName("unitsLeftoverCheckBox")
        self.gridLayout.addWidget(self.unitsLeftoverCheckBox, 6, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.weightSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.weightSpinBox.setMaximum(999)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.horizontalLayout_4.addWidget(self.weightSpinBox)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setIndent(18)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.weightSpinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.weightSpinBox_2.setMaximum(999)
        self.weightSpinBox_2.setObjectName("weightSpinBox_2")
        self.horizontalLayout_4.addWidget(self.weightSpinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)
        self.unitsUpliftedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.unitsUpliftedCheckBox.setObjectName("unitsUpliftedCheckBox")
        self.gridLayout.addWidget(self.unitsUpliftedCheckBox, 5, 1, 1, 1)
        self.colourCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.colourCheckBox.setObjectName("colourCheckBox")
        self.gridLayout.addWidget(self.colourCheckBox, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.unitsLeftoverSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.unitsLeftoverSpinBox.setMaximum(999)
        self.unitsLeftoverSpinBox.setObjectName("unitsLeftoverSpinBox")
        self.horizontalLayout_6.addWidget(self.unitsLeftoverSpinBox)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setIndent(18)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.unitsLeftoverSpinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.unitsLeftoverSpinBox_2.setMaximum(999)
        self.unitsLeftoverSpinBox_2.setObjectName("unitsLeftoverSpinBox_2")
        self.horizontalLayout_6.addWidget(self.unitsLeftoverSpinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 2, 1, 1)
        self.mealIdLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mealIdLineEdit.setToolTip("")
        self.mealIdLineEdit.setInputMask("")
        self.mealIdLineEdit.setText("")
        self.mealIdLineEdit.setMaxLength(3)
        self.mealIdLineEdit.setFrame(True)
        self.mealIdLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.mealIdLineEdit.setCursorPosition(0)
        self.mealIdLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.mealIdLineEdit.setObjectName("mealIdLineEdit")
        self.gridLayout.addWidget(self.mealIdLineEdit, 0, 2, 1, 1)
        self.optionNameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.optionNameLineEdit.setToolTip("")
        self.optionNameLineEdit.setInputMask("")
        self.optionNameLineEdit.setText("")
        self.optionNameLineEdit.setMaxLength(3)
        self.optionNameLineEdit.setFrame(True)
        self.optionNameLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.optionNameLineEdit.setCursorPosition(0)
        self.optionNameLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.optionNameLineEdit.setObjectName("optionNameLineEdit")
        self.gridLayout.addWidget(self.optionNameLineEdit, 1, 2, 1, 1)
        self.optionCodeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.optionCodeLineEdit.setToolTip("")
        self.optionCodeLineEdit.setInputMask("")
        self.optionCodeLineEdit.setText("")
        self.optionCodeLineEdit.setMaxLength(3)
        self.optionCodeLineEdit.setFrame(True)
        self.optionCodeLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.optionCodeLineEdit.setCursorPosition(0)
        self.optionCodeLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.optionCodeLineEdit.setObjectName("optionCodeLineEdit")
        self.gridLayout.addWidget(self.optionCodeLineEdit, 2, 2, 1, 1)
        self.wastageCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.wastageCheckBox.setObjectName("wastageCheckBox")
        self.gridLayout.addWidget(self.wastageCheckBox, 7, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setIndent(0)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.wastageSpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.wastageSpinBox.setMaximum(999)
        self.wastageSpinBox.setObjectName("wastageSpinBox")
        self.horizontalLayout_7.addWidget(self.wastageSpinBox)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setIndent(18)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.wastageSpinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.wastageSpinBox_2.setMaximum(999)
        self.wastageSpinBox_2.setObjectName("wastageSpinBox_2")
        self.horizontalLayout_7.addWidget(self.wastageSpinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 2, 1, 1)

        self.retranslateUi(searchMealOptionDialog)
        self.buttonBox.accepted.connect(searchMealOptionDialog.accept)
        self.buttonBox.rejected.connect(searchMealOptionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(searchMealOptionDialog)

    def retranslateUi(self, searchMealOptionDialog):
        _translate = QtCore.QCoreApplication.translate
        searchMealOptionDialog.setWindowTitle(_translate("searchMealOptionDialog", "Dialog"))
        self.optionCodeCheckBox.setText(_translate("searchMealOptionDialog", "Option Code"))
        self.optionNameCheckBox.setText(_translate("searchMealOptionDialog", "Option Name"))
        self.weightCheckBox.setText(_translate("searchMealOptionDialog", "Weight"))
        self.mealIdCheckBox.setText(_translate("searchMealOptionDialog", "Meal ID"))
        self.colourLineEdit.setPlaceholderText(_translate("searchMealOptionDialog", "e.g. blue"))
        self.label_7.setText(_translate("searchMealOptionDialog", "between"))
        self.label_9.setText(_translate("searchMealOptionDialog", "and"))
        self.unitsLeftoverCheckBox.setText(_translate("searchMealOptionDialog", "Units Leftover"))
        self.label_5.setText(_translate("searchMealOptionDialog", "between"))
        self.weightSpinBox.setSuffix(_translate("searchMealOptionDialog", " grams"))
        self.label_8.setText(_translate("searchMealOptionDialog", "and"))
        self.weightSpinBox_2.setSuffix(_translate("searchMealOptionDialog", " grams"))
        self.unitsUpliftedCheckBox.setText(_translate("searchMealOptionDialog", "Units Uplifted"))
        self.colourCheckBox.setText(_translate("searchMealOptionDialog", "Colour"))
        self.label_10.setText(_translate("searchMealOptionDialog", "between"))
        self.label_11.setText(_translate("searchMealOptionDialog", "and"))
        self.mealIdLineEdit.setPlaceholderText(_translate("searchMealOptionDialog", "e.g. 15"))
        self.optionNameLineEdit.setPlaceholderText(_translate("searchMealOptionDialog", "e.g. Chicken Noodles"))
        self.optionCodeLineEdit.setPlaceholderText(_translate("searchMealOptionDialog", "e.g. F003"))
        self.wastageCheckBox.setText(_translate("searchMealOptionDialog", "% Wastage"))
        self.label_12.setText(_translate("searchMealOptionDialog", "between"))
        self.wastageSpinBox.setSuffix(_translate("searchMealOptionDialog", " %"))
        self.label_13.setText(_translate("searchMealOptionDialog", "and"))
        self.wastageSpinBox_2.setSuffix(_translate("searchMealOptionDialog", " %"))

