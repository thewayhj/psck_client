
import sys
from PyQt5 import QtWidgets

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    view = QWebEngineView(MainWindow)
    view.load(QUrl('http://192.168.0.203:3000'))
    view.resize(100, 200)
    view.show()
    sys.exit(app.exec_())