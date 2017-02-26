# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import datetime
import time
import psutil
import platform
import ModifyProfile

from PyQt5.QtWidgets import QSizePolicy, qApp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import AddFriendDialog
from DeviceinfoThread import DeviceInfoThread
from LoginFrame import LoginFrame
from model.Device import DeviceInfo
from Myhttp import ThreadFriendInfoCommunication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

booting_t = datetime.datetime.fromtimestamp(psutil.boot_time())

mac_address = []
ip_address = []

def get_mac_address(): # Mac Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 18:  # Mac 주소
                mac_address.append(i.address)
        return mac_address

    elif platform.system() == "Windows":
        #print()
        addrs = psutil.net_if_addrs().get('Wi-Fi')
        if addrs == None:
            addrs = psutil.net_if_addrs().get('로컬 영역 연결')

        for i in addrs:
            if i.family == -1:  # Mac 주소
                mac_address.append(i.address)
        return mac_address


def get_ip_address(): # IP Address function
    if platform.system() == "Darwin":
        addrs = psutil.net_if_addrs().get('en0')
        for i in addrs:
            if i.family == 2:  # IP 주소
                ip_address.append(i.address)
        return ip_address

class Ui_MainWindow(object):

    friends = []
    cpu_data = []
    ram_data = []

    centralwidget = None
    verticalLayoutWidget = None
    verticalLayout = None
    listWidget = None
    horizontalLayout_3 = None
    pushButton_add = None
    pushButton_del = None
    verticalLayoutWidget_2 = None
    verticalLayout_2 = None
    label_name = None
    label_name_v = None
    horizontalLayout = None
    verticalLayout_3 = None
    label_mac = None
    label_mac_v = None
    horizontalLayout_2 = None
    verticalLayout_6 = None
    label_booting = None
    label_booting_v = None
    verticalLayout_7 = None
    label_usage = None
    label_usage_v = None
    label_cpu = None
    label_cpu_v = None
    graphView_cpu = None
    label_ram = None
    label_ram_v = None
    graphView_ram = None
    menubar = None
    menuConnect = None
    menuExit = None
    menuSetting = None
    menuHelp = None
    statusbar = None
    actionconnect = None
    actionexit = None
    actionsetting = None
    actionhelp = None
    menuConnect = None
    menuExit = None
    menuSetting = None
    menuHelp = None
    retranslateUi = None

    def __init__(Ui_MainWindow, mainwindow):
        super().__init__()
        Ui_MainWindow.setupUi(mainwindow)
        Ui_MainWindow.t_status = thread_status(Ui_MainWindow)
        Ui_MainWindow.t_status.start()

    def setupUi(Ui_MainWindow, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 620)
        Ui_MainWindow.centralwidget = QtWidgets.QWidget(MainWindow)
        Ui_MainWindow.centralwidget.setObjectName("centralwidget")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.white)
        MainWindow.setPalette(palette)
        Ui_MainWindow.verticalLayoutWidget = QtWidgets.QWidget(Ui_MainWindow.centralwidget)
        Ui_MainWindow.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 240, 570))
        Ui_MainWindow.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        Ui_MainWindow.verticalLayout = QtWidgets.QVBoxLayout(Ui_MainWindow.verticalLayoutWidget)
        Ui_MainWindow.verticalLayout.setContentsMargins(5, 5, 0, 0)
        Ui_MainWindow.verticalLayout.setObjectName("verticalLayout")
        Ui_MainWindow.listWidget = QtWidgets.QListWidget(Ui_MainWindow.verticalLayoutWidget)
        Ui_MainWindow.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(15)
        Ui_MainWindow.listWidget.setFont(font)
        Ui_MainWindow.listWidget.setIconSize(QtCore.QSize(50, 50))
        Ui_MainWindow.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        Ui_MainWindow.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        Ui_MainWindow.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        Ui_MainWindow.listWidget.setModelColumn(0)
        Ui_MainWindow.listWidget.setObjectName("listWidget")

        Ui_MainWindow.verticalLayout.addWidget(Ui_MainWindow.listWidget)
        Ui_MainWindow.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_3.setObjectName("horizontalLayout_3")
        Ui_MainWindow.pushButton_add = QtWidgets.QPushButton(Ui_MainWindow.verticalLayoutWidget)
        Ui_MainWindow.pushButton_add.setMinimumSize(QtCore.QSize(0, 50))
        Ui_MainWindow.pushButton_add.setObjectName("pushButton_add")
        Ui_MainWindow.horizontalLayout_3.addWidget(Ui_MainWindow.pushButton_add)
        Ui_MainWindow.pushButton_del = QtWidgets.QPushButton(Ui_MainWindow.verticalLayoutWidget)
        Ui_MainWindow.pushButton_del.setMinimumSize(QtCore.QSize(0, 50))
        Ui_MainWindow.pushButton_del.setObjectName("pushButton_del")
        Ui_MainWindow.horizontalLayout_3.addWidget(Ui_MainWindow.pushButton_del)
        Ui_MainWindow.verticalLayout.addLayout(Ui_MainWindow.horizontalLayout_3)
        Ui_MainWindow.verticalLayoutWidget_2 = QtWidgets.QWidget(Ui_MainWindow.centralwidget)
        Ui_MainWindow.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 411, 561))
        Ui_MainWindow.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        Ui_MainWindow.verticalLayout_2 = QtWidgets.QVBoxLayout(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        Ui_MainWindow.verticalLayout_2.setObjectName("verticalLayout_2")

        Ui_MainWindow.label_name = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_name.setObjectName("label_name")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_name)

        Ui_MainWindow.label_name_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_name_v.setEnabled(True)
        Ui_MainWindow.label_name_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_name_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        Ui_MainWindow.label_name_v.setObjectName("label_name_v")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_name_v)

        Ui_MainWindow.horizontalLayout = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout.setObjectName("horizontalLayout")
        Ui_MainWindow.verticalLayout_5 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_5.setObjectName("verticalLayout_5")

        Ui_MainWindow.label_ip = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_ip.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_ip.setObjectName("label_ip")
        Ui_MainWindow.verticalLayout_5.addWidget(Ui_MainWindow.label_ip)
        Ui_MainWindow.label_ip_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_ip_v.setEnabled(True)
        Ui_MainWindow.label_ip_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_ip_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        Ui_MainWindow.label_ip_v.setObjectName("label_ip_v")
        Ui_MainWindow.verticalLayout_5.addWidget(Ui_MainWindow.label_ip_v)

        Ui_MainWindow.horizontalLayout.addLayout(Ui_MainWindow.verticalLayout_5)
        Ui_MainWindow.verticalLayout_3 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_3.setObjectName("verticalLayout_3")

        Ui_MainWindow.label_mac = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_mac.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_mac.setObjectName("label_mac")
        Ui_MainWindow.verticalLayout_3.addWidget(Ui_MainWindow.label_mac)
        Ui_MainWindow.label_mac_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_mac_v.setEnabled(True)
        Ui_MainWindow.label_mac_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_mac_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        Ui_MainWindow.label_mac_v.setObjectName("label_mac_v")
        Ui_MainWindow.verticalLayout_3.addWidget(Ui_MainWindow.label_mac_v)

        Ui_MainWindow.horizontalLayout.addLayout(Ui_MainWindow.verticalLayout_3)
        Ui_MainWindow.verticalLayout_2.addLayout(Ui_MainWindow.horizontalLayout)

        Ui_MainWindow.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_2.setObjectName("horizontalLayout_2")
        Ui_MainWindow.horizontalLayout_2.setContentsMargins(0,10,0,0)
        Ui_MainWindow.verticalLayout_6 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_6.setObjectName("verticalLayout_6")

        Ui_MainWindow.label_booting = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_booting.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_booting.setObjectName("label_usage")
        Ui_MainWindow.verticalLayout_6.addWidget(Ui_MainWindow.label_booting)

        Ui_MainWindow.label_booting_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_booting_v.setEnabled(True)
        Ui_MainWindow.label_booting_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_booting_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        Ui_MainWindow.label_booting_v.setObjectName("label_booting_v")
        Ui_MainWindow.verticalLayout_6.addWidget(Ui_MainWindow.label_booting_v)

        Ui_MainWindow.horizontalLayout_2.addLayout(Ui_MainWindow.verticalLayout_6)
        Ui_MainWindow.verticalLayout_7 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_7.setObjectName("verticalLayout_7")


        Ui_MainWindow.label_usage = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_usage.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_usage.setObjectName("label_access")
        Ui_MainWindow.verticalLayout_7.addWidget(Ui_MainWindow.label_usage)

        Ui_MainWindow.label_usage_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_usage_v.setEnabled(True)
        Ui_MainWindow.label_usage_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_usage_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        Ui_MainWindow.label_usage_v.setObjectName("label_access_v")
        Ui_MainWindow.verticalLayout_7.addWidget(Ui_MainWindow.label_usage_v)

        Ui_MainWindow.horizontalLayout_2.addLayout(Ui_MainWindow.verticalLayout_7)
        Ui_MainWindow.verticalLayout_2.addLayout(Ui_MainWindow.horizontalLayout_2)


        Ui_MainWindow.label_cpu = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_cpu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_cpu.setObjectName("label_cpu")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_cpu)

        Ui_MainWindow.label_cpu_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_cpu_v.setEnabled(True)
        Ui_MainWindow.label_cpu_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_cpu_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        Ui_MainWindow.label_cpu_v.setObjectName("label_cpu_v")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_cpu_v)

        Ui_MainWindow.graphView_cpu = PlotCanvas(Ui_MainWindow, width=6, height=2)
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.graphView_cpu)

        Ui_MainWindow.label_ram = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_ram.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        Ui_MainWindow.label_ram.setObjectName("label_ram")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_ram)

        Ui_MainWindow.label_ram_v = QtWidgets.QLabel(Ui_MainWindow.verticalLayoutWidget_2)
        Ui_MainWindow.label_ram_v.setEnabled(True)
        Ui_MainWindow.label_ram_v.setMinimumSize(QtCore.QSize(0, 0))
        Ui_MainWindow.label_ram_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        Ui_MainWindow.label_ram_v.setObjectName("label_ram_v")
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.label_ram_v)

        Ui_MainWindow.graphView_ram = PlotCanvas(Ui_MainWindow, width=6, height=2)
        Ui_MainWindow.verticalLayout_2.addWidget(Ui_MainWindow.graphView_ram)


        Ui_MainWindow.verticalLayoutWidget.raise_()
        Ui_MainWindow.verticalLayoutWidget_2.raise_()
        Ui_MainWindow.listWidget.raise_()
        MainWindow.setCentralWidget(Ui_MainWindow.centralwidget)
        Ui_MainWindow.menubar = QtWidgets.QMenuBar(MainWindow)
        Ui_MainWindow.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        Ui_MainWindow.menubar.setObjectName("menubar")

        Ui_MainWindow.menuConnect = QtWidgets.QMenu(Ui_MainWindow.menubar)
        Ui_MainWindow.menuConnect.setObjectName("menuConnect")
        Ui_MainWindow.menuExit = QtWidgets.QMenu(Ui_MainWindow.menubar)
        Ui_MainWindow.menuExit.setObjectName("menuExit")

        Ui_MainWindow.menuSetting = QtWidgets.QMenu(Ui_MainWindow.menubar)
        Ui_MainWindow.menuSetting.setObjectName("menuSetting")
        Ui_MainWindow.menuHelp = QtWidgets.QMenu(Ui_MainWindow.menubar)
        Ui_MainWindow.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(Ui_MainWindow.menubar)
        Ui_MainWindow.statusbar = QtWidgets.QStatusBar(MainWindow)
        Ui_MainWindow.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(Ui_MainWindow.statusbar)

        Ui_MainWindow.actionconnect = QtWidgets.QAction(MainWindow)
        Ui_MainWindow.actionconnect.setObjectName("actionconnect")
        Ui_MainWindow.actionexit = QtWidgets.QAction(MainWindow)
        Ui_MainWindow.actionexit.setObjectName("actionexit")

        Ui_MainWindow.actionsetting = QtWidgets.QAction(MainWindow)
        Ui_MainWindow.actionsetting.setObjectName("actionsetting")
        Ui_MainWindow.actionhelp = QtWidgets.QAction(MainWindow)
        Ui_MainWindow.actionhelp.setObjectName("actionhelp")

        Ui_MainWindow.menuConnect.addAction(Ui_MainWindow.actionconnect)
        Ui_MainWindow.menuExit.addAction(Ui_MainWindow.actionexit)
        Ui_MainWindow.menuSetting.addAction(Ui_MainWindow.actionsetting)
        Ui_MainWindow.menuHelp.addAction(Ui_MainWindow.actionhelp)

        Ui_MainWindow.menubar.addAction(Ui_MainWindow.menuConnect.menuAction())
        Ui_MainWindow.menubar.addAction(Ui_MainWindow.menuExit.menuAction())
        Ui_MainWindow.menubar.addAction(Ui_MainWindow.menuSetting.menuAction())
        Ui_MainWindow.menubar.addAction(Ui_MainWindow.menuHelp.menuAction())

        Ui_MainWindow.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        Ui_MainWindow.listWidget.itemClicked.connect(Ui_MainWindow.friend_list_click_event)
        Ui_MainWindow.listWidget.itemDoubleClicked.connect(Ui_MainWindow.friend_list_double_click_event)

    def set_text(Ui_MainWindow, device_info):
        _translate = QtCore.QCoreApplication.translate

        try:
            Ui_MainWindow.label_ip_v.setText(_translate("MainWindow", device_info.d_ip))
            Ui_MainWindow.label_mac_v.setText(_translate("MainWindow", device_info.d_mac))
            Ui_MainWindow.label_name_v.setText(_translate("MainWindow", device_info.d_name))
            Ui_MainWindow.label_booting_v.setText(_translate("MainWindow", str(device_info.d_boot_t)))
            Ui_MainWindow.label_cpu_v.setText(_translate("MainWindow", "percent : " + str(device_info.d_cpu_per) + "%"))
            Ui_MainWindow.label_ram_v.setText(_translate("MainWindow", "percent : " + str(device_info.d_mem_per) + "%  total : " + str(round(device_info.d_mem_total / 1024 / 1024)) + "MB  available : " + str(round(device_info.d_mem_avail / 1024 / 1024)) + "MB"))

            if(len(Ui_MainWindow.cpu_data) > 10):
                Ui_MainWindow.cpu_data.pop(0)
            Ui_MainWindow.cpu_data.append(device_info.d_cpu_per)
            Ui_MainWindow.graphView_cpu.plot(Ui_MainWindow.cpu_data)

            if (len(Ui_MainWindow.ram_data) > 10):
                Ui_MainWindow.ram_data.pop(0)
            Ui_MainWindow.ram_data.append(device_info.d_mem_per)
            Ui_MainWindow.graphView_ram.plot(Ui_MainWindow.ram_data)

            usage_time = datetime.datetime.now() - device_info.d_boot_t
            usage_ts = usage_time.total_seconds()
            usage_h = int(usage_ts / 3600)
            usage_m = int((usage_ts - (usage_h * 3600)) / 60)
            usage_s = int(usage_ts - (usage_h * 3600) - (usage_m * 60))

            Ui_MainWindow.label_usage_v.setText(_translate("MainWindow", str(usage_h) + "시간 " + str(usage_m) + "분 " + str(usage_s) + "초"))
        except Exception as e:
            print(e)


    def retranslateUi(Ui_MainWindow, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HackerViewer"))
        __sortingEnabled = Ui_MainWindow.listWidget.isSortingEnabled()
        Ui_MainWindow.listWidget.setSortingEnabled(False)

        DeviceInfoThread.friend_device_info.append(DeviceInfo('Sung Kyungmo', 'sung'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Park Minwoo', 'pmw9027'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Choi Jinseok', 'choi'))
        DeviceInfoThread.friend_device_info.append(DeviceInfo('Kim Heejoong', 'theway'))

        Ui_MainWindow.listwidget_item()

        Ui_MainWindow.listWidget.setSortingEnabled(__sortingEnabled)
        Ui_MainWindow.pushButton_add.setText(_translate("MainWindow", "+"))
        Ui_MainWindow.pushButton_add.clicked.connect(AddFriendDialog.AddFriendDialog.widget_show)
        Ui_MainWindow.pushButton_del.setText(_translate("MainWindow", "-"))
        Ui_MainWindow.pushButton_del.clicked.connect(Ui_MainWindow.del_friend)
        Ui_MainWindow.label_ip.setText(_translate("MainWindow", "IP"))
        Ui_MainWindow.label_mac.setText(_translate("MainWindow", "MAC"))
        Ui_MainWindow.label_name.setText(_translate("MainWindow", "NAME"))
        Ui_MainWindow.label_cpu.setText(_translate("MainWindow", "CPU"))
        Ui_MainWindow.label_ram.setText(_translate("MainWindow", "RAM"))
        Ui_MainWindow.label_usage.setText(_translate("MainWindow", "Usage Time"))
        Ui_MainWindow.label_booting.setText(_translate("MainWindow", "Booting Time"))
        Ui_MainWindow.menuConnect.setTitle(_translate("MainWindow","Connect"))
        Ui_MainWindow.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        Ui_MainWindow.menuHelp.setTitle(_translate("MainWindow", "Help"))

        Ui_MainWindow.actionconnect.setText(_translate("MainWindow","login"))
        Ui_MainWindow.actionexit = Ui_MainWindow.menuConnect.addAction('exit')
        Ui_MainWindow.actionsetting.setText(_translate("MainWindow", "setting"))
        Ui_MainWindow.actionhelp.setText(_translate("MainWindow", "help"))

        Ui_MainWindow.actionconnect.triggered.connect(LoginFrame.init)

        Ui_MainWindow.actionexit.triggered.connect(qApp.quit)



    def listwidget_item(Ui_MainWindow):

        _translate = QtCore.QCoreApplication.translate

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        Ui_MainWindow.listWidget.clear()

        for index, i in enumerate(DeviceInfoThread.friend_device_info):
            listitem = QtWidgets.QListWidgetItem()
            listitem.setIcon(icon)
            listitem.setBackground(brush)

            Ui_MainWindow.listWidget.addItem(listitem)
            item = Ui_MainWindow.listWidget.item(index)
            if index is 0:
                item.setText(_translate("MainWindow", "( me )"))
            else:
                item.setText(_translate("MainWindow", i.name))


    def friend_list_click_event(Ui_MainWindow):
        for x in Ui_MainWindow.listWidget.selectedIndexes():
            ThreadFriendInfoCommunication.u_id = DeviceInfoThread.friend_device_info[x.row()].u_id
            thread_status.selected = x.row()

    def friend_list_double_click_event(Ui_MainWindow):
        for x in Ui_MainWindow.listWidget.selectedIndexes():
            ModifyProfile.ModifyProfile.init()
            if x.row()!=0:
                ModifyProfile.ModifyProfile.hide_button()
            ModifyProfile.ModifyProfile.set_info(DeviceInfoThread.friend_device_info[x.row()].name,DeviceInfoThread.friend_device_info[x.row()].u_id)
            print(DeviceInfoThread.friend_device_info[x.row()].u_id)


    def del_friend(Ui_MainWindow):
        listitems = Ui_MainWindow.listWidget.selectedItems()
        if not listitems: return
        for item in listitems:
            del DeviceInfoThread.friend_device_info[Ui_MainWindow.listWidget.row(item)]
            Ui_MainWindow.listWidget.takeItem(Ui_MainWindow.listWidget.row(item))


class thread_status(QThread):

    selected = 0

    def __init__(Ui_MainWindow, main_frame):
        QThread.__init__(Ui_MainWindow)
        Ui_MainWindow.main_frame = main_frame

    def __del__(Ui_MainWindow):
        Ui_MainWindow.wait()

    def run(Ui_MainWindow):
        while True:
            Ui_MainWindow.main_frame.set_text(DeviceInfoThread.friend_device_info[thread_status.selected])
            time.sleep(1)


class PlotCanvas(FigureCanvas):
    def __init__(Ui_MainWindow, parent=None, width=6, height=2, dpi=60):
        fig = Figure(figsize=(width, height), dpi=dpi)
        Ui_MainWindow.axes = fig.add_subplot(1,1,1)

        FigureCanvas.__init__(Ui_MainWindow, fig)

        FigureCanvas.setSizePolicy(Ui_MainWindow, 100, 20)
        FigureCanvas.updateGeometry(Ui_MainWindow)



    def plot(Ui_MainWindow,data):
        ax = Ui_MainWindow.figure.add_subplot(1,1,1)
        ax.clear()
        ax.plot(data, 'r-',linewidth=1.5)
        ax.plot(0)
        ax.plot(100)
        Ui_MainWindow.draw()




