import sys
from os import fork

import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

from deviceinfoThread import DeviceInfoThread
from joinFrame import JoinFrame
from loginFrame import LoginFrame
from mainFrame import Ui_MainWindow
from model.device import DeviceInfo
from myhttp import ThreadCommunication, ThreadFriendInfoCommunication
from util import MyYaml


if __name__ == '__main__':

    my_info = DeviceInfo('1', '1')

    thread = DeviceInfoThread()
    thread.start()

    comm = ThreadCommunication()
    comm.start()

    comm2 = ThreadFriendInfoCommunication()
    comm2.start()

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()

    view = QWebEngineView(MainWindow)
    form1 = QtWidgets.QMainWindow()
    login = LoginFrame(form1, view)

    form1.show()

    JoinFrame.init1()

    sys.exit(app.exec_())



