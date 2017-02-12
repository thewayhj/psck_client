import sys
from os import fork

import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from joinFrame import JoinFrame
from loginFrame import LoginFrame
from myhttp import Communication, ThreadCommunication
from util import MyYaml
import user,device,mainFrame,adduser

users = []
users.append(user.User('sung'))
users[0].setName('Kyungmo-notebook')
users[0].setAddr('192.168.111.111', 'aa:bb:cc:dd:ee:aa')
users.append(user.User('park'))
users[1].setName('minwoo-notebook')
users[1].setAddr('192.168.222.222', 'ff:ee:dd:cc:bb:ee')
users.append(user.User('kim'))
users[2].setName('heejung-notebook')
users[2].setAddr('192.168.333.333', 'cc:aa:ee:bb:dd:aa')

if __name__ == '__main__':

    comm = ThreadCommunication()
    comm.start()

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainFrame.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    adduser.Add_Dialog.ui78 = ui
    view = QWebEngineView(MainWindow)


    form1 = QtWidgets.QMainWindow()


    login = LoginFrame(form1, view)
    form1.show()

    JoinFrame.init1()
    adduser.Add_Dialog.init()


    sys.exit(app.exec_())




