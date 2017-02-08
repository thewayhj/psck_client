from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QUrl
from joinFrame import JoinFrame
from mongoDao import LoginDao


class LoginFrame(object):

    form1 = 1

    def __init__(self, form, view):
        super().__init__()

        self.form1 = form
        self.setupUi(form, view)
        form.show()

    def setupUi(self, Form, view):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 345, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.addWidget(view)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget.raise_()



        self.retranslateUi(Form)


        self.pushButton.clicked.connect(self.btnOkClicked)
        self.pushButton_2.clicked.connect(self.btnOkClicked)
        self.pushButton_3.clicked.connect(JoinFrame.widget_show)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.label_2.setText(_translate("Form", "ID"))
        self.label.setText(_translate("Form", "PW"))

        self.pushButton.setText(_translate("Form", "Cancel"))
        self.pushButton_2.setText(_translate("Form", "OK"))
        self.pushButton_3.setText(_translate("Form", "Join"))

    def btnOkClicked(self, i):

        if LoginDao.login(self.lineEdit.text(), self.lineEdit_2.text()):
            self.form1.hide()
        else:
            self.showdialog()

    def showdialog(self):
        d = QDialog()
        b1 = QPushButton("Ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Fail")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()