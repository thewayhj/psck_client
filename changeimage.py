# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\thewa_000\Documents\Chat_Inter\changeimage.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

class Change_Image(object):
    def setupUi(Change_Image, Form):
        Form.setObjectName("Form")
        Form.resize(358, 171)
        Change_Image.pushButton = QtWidgets.QPushButton(Form)
        Change_Image.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 121))
        Change_Image.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Change_Image.pushButton.setObjectName("pushButton")
        Change_Image.pushButton.clicked.connect(Change_Image.openImage)
        Change_Image.label = QtWidgets.QLabel(Form)
        Change_Image.label.setGeometry(QtCore.QRect(190, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        font.bold()
        font.setBold(False)
        font.setWeight(50)
        Change_Image.label.setFont(font)
        Change_Image.label.setObjectName("label")
        Change_Image.label_2 = QtWidgets.QLabel(Form)
        Change_Image.label_2.setGeometry(QtCore.QRect(190, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        Change_Image.label_2.setFont(font)
        Change_Image.label_2.setObjectName("label_2")
        Change_Image.pushButton_2 = QtWidgets.QPushButton(Form)
        Change_Image.pushButton_2.setGeometry(QtCore.QRect(305, 44, 41, 31))
        Change_Image.pushButton_2.setIcon(QtGui.QIcon("img/modify.png"))
        Change_Image.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Change_Image.pushButton_2.setObjectName("pushButton_2")

        Change_Image.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(Change_Image, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Change_Image.pushButton.setText(_translate("Form", "PushButton"))
        Change_Image.label.setText(_translate("Form", "Kim Hee Joong"))
        Change_Image.label_2.setText(_translate("Form", "ID"))
        #self.pushButton_2.setText(_translate("Form", "ICON"))

    def openImage(Change_Image):
        fname = QFileDialog.getOpenFileName(Change_Image, 'Open file', "Image files (*.jpg *.gif *.png)")[0]
        Change_Image.le.setPixmap(QPixmap(fname))

    @staticmethod
    def widget_show():
        Change_Image.qwidget.show()

    @staticmethod
    def widget_hide():
        Change_Image.qwidget.hide()


