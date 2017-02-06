import sys

from PyQt5 import QtWidgets

import yaml
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from joinFrame import JoinFrame
from loginFrame import LoginFrame
from mainFrame import Ui_MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    view = QWebEngineView(MainWindow)
    view.load(QUrl('http://192.168.0.203:3000'))
    view.resize(300, 100)
    view.show()

    form1 = QtWidgets.QMainWindow()


    login = LoginFrame(form1, view)
    form1.show()

    JoinFrame()


    sys.exit(app.exec_())



    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    #
    # btn = QPushButton('Button', self)
    # btn.setToolTip('This is a <b>QPushButton</b> widget')
    # btn.resize(btn.sizeHint())
    # btn.move(50, 50)

