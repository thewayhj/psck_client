# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main,user
import mainFrame


class Add_Dialog(object):

    Dialog=None
    ui78 = None
    @staticmethod
    def init():

        import sys
        app = QtWidgets.QApplication(sys.argv)
        Add_Dialog.Dialog = QtWidgets.QDialog()

        Add_Dialog.buttonBox = QtWidgets.QDialogButtonBox(Add_Dialog.Dialog)
        Add_Dialog.lineEdit = QtWidgets.QLineEdit(Add_Dialog.Dialog)
        Add_Dialog.label = QtWidgets.QLabel(Add_Dialog.Dialog)
        Add_Dialog.label_2 = QtWidgets.QLabel(Add_Dialog.Dialog)

        Add_Dialog.setupUi()
        sys.exit(app.exec_())

    @staticmethod
    def setupUi():
        Add_Dialog.Dialog.setObjectName("Dialog")
        Add_Dialog.Dialog.resize(321, 158)
        Add_Dialog.buttonBox.setGeometry(QtCore.QRect(20, 110, 281, 32))
        Add_Dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        Add_Dialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        Add_Dialog.buttonBox.setObjectName("buttonBox")
        Add_Dialog.lineEdit.setGeometry(QtCore.QRect(70, 70, 221, 21))
        Add_Dialog.lineEdit.setText("")
        Add_Dialog.lineEdit.setObjectName("lineEdit")
        Add_Dialog.label.setGeometry(QtCore.QRect(20, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        Add_Dialog.label.setFont(font)
        Add_Dialog.label.setTextFormat(QtCore.Qt.PlainText)
        Add_Dialog.label.setAlignment(QtCore.Qt.AlignCenter)
        Add_Dialog.label.setObjectName("label")
        Add_Dialog.label_2.setGeometry(QtCore.QRect(30, 70, 60, 16))
        Add_Dialog.label_2.setObjectName("label_2")

        Add_Dialog.retranslateUi()
        Add_Dialog.buttonBox.accepted.connect(Add_Dialog.ok_btn_click)
        Add_Dialog.buttonBox.rejected.connect(Add_Dialog.cancel_btn_click)
        QtCore.QMetaObject.connectSlotsByName(Add_Dialog.Dialog)

    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        Add_Dialog.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Add_Dialog.label.setText(_translate("Dialog", "Add User"))
        Add_Dialog.label_2.setText(_translate("Dialog", "I D"))



    @staticmethod
    def widget_show():
        Add_Dialog.Dialog.show()

    @staticmethod
    def widget_hide():
        Add_Dialog.Dialog.hide()

    @staticmethod
    def ok_btn_click():
        main.users.append(user.User(Add_Dialog.lineEdit.text()))

        Add_Dialog.ui78.listupdate()

        Add_Dialog.widget_hide()

    @staticmethod
    def cancel_btn_click():
        Add_Dialog.widget_hide()
