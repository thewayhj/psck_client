# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mainFrame
from deviceinfoThread import DeviceInfoThread
from model.device import DeviceInfo


class AddDialog(object):

    Dialog = None
    main_window = None

    @staticmethod
    def init(main_window):
        AddDialog.main_window = main_window
        AddDialog.Dialog = QtWidgets.QDialog()
        AddDialog.buttonBox = QtWidgets.QDialogButtonBox(AddDialog.Dialog)
        AddDialog.lineEdit = QtWidgets.QLineEdit(AddDialog.Dialog)
        AddDialog.label = QtWidgets.QLabel(AddDialog.Dialog)
        AddDialog.label_2 = QtWidgets.QLabel(AddDialog.Dialog)
        AddDialog.setupUi()

    @staticmethod
    def setupUi():
        AddDialog.Dialog.setObjectName("Dialog")
        AddDialog.Dialog.resize(321, 158)
        AddDialog.buttonBox.setGeometry(QtCore.QRect(20, 110, 281, 32))
        AddDialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        AddDialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        AddDialog.buttonBox.setObjectName("buttonBox")
        AddDialog.lineEdit.setGeometry(QtCore.QRect(70, 70, 221, 21))
        AddDialog.lineEdit.setText("")
        AddDialog.lineEdit.setObjectName("lineEdit")
        AddDialog.label.setGeometry(QtCore.QRect(20, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        AddDialog.label.setFont(font)
        AddDialog.label.setTextFormat(QtCore.Qt.PlainText)
        AddDialog.label.setAlignment(QtCore.Qt.AlignCenter)
        AddDialog.label.setObjectName("label")
        AddDialog.label_2.setGeometry(QtCore.QRect(30, 70, 60, 16))
        AddDialog.label_2.setObjectName("label_2")

        AddDialog.retranslateUi()
        AddDialog.buttonBox.accepted.connect(AddDialog.ok_btn_click)
        AddDialog.buttonBox.rejected.connect(AddDialog.cancel_btn_click)
        QtCore.QMetaObject.connectSlotsByName(AddDialog.Dialog)

    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        AddDialog.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        AddDialog.label.setText(_translate("Dialog", "Add User"))
        AddDialog.label_2.setText(_translate("Dialog", "I D"))



    @staticmethod
    def widget_show():
        AddDialog.Dialog.show()

    @staticmethod
    def widget_hide():
        AddDialog.Dialog.hide()

    @staticmethod
    def ok_btn_click():

        DeviceInfoThread.friend_device_info.append(DeviceInfo('Kim Heejoong', AddDialog.lineEdit.text()))

        AddDialog.main_window.listwidget_item()
        AddDialog.widget_hide()

    @staticmethod
    def cancel_btn_click():
        AddDialog.widget_hide()
