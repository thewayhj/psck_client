import sys
#from os import fork

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
from myhttp import Communication, ThreadCommunication
import  adduser

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
    main_ui = Ui_MainWindow(MainWindow)
    MainWindow.show()

    adduser.AddDialog.init(main_ui)

    LoginFrame.init()

    JoinFrame.init()

    sys.exit(app.exec_())




