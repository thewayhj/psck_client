import sys
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from example import Example
from mainFrame import Ui_MainWindow


stream = open("setting.yaml", 'r')
setting = yaml.load(stream)
HOST = setting['server']['host']
# HOST = '192.168.0.113'
PORT_UDP_SERVER = setting['server']['port_udp_server']
PORT_TCP_SERVER = setting['server']['port_tcp_server']
ADDR_TCP_SERVER = (HOST, PORT_TCP_SERVER)
ADDR_UDP_SERVER = (HOST, PORT_UDP_SERVER)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

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


    print(setting['server']['host'])
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(ADDR_TCP_SERVER)
        data = clientSocket.recv(1024)
        print(data)
        print(data)
    except:
        clientSocket.close()