# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import ipaddress
import socket
import threading
import datetime
import time
import os
import psutil
import sys
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QUrl
from psutil import virtual_memory

from devicedo import DeviceDo

booting_t=datetime.datetime.fromtimestamp(psutil.boot_time())

mac_address = []
ip_address = []

addrs = psutil.net_if_addrs().get('en0')



for i in addrs:
    if i.family == 18:  # Mac 주소
       mac_address.append(i.address)
    if i.family == 2:   # IP 주소
        ip_address.append(i.address)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setIconSize(QtCore.QSize(50, 50))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(200)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/profile_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 0, 411, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_ip = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout_2.addWidget(self.label_ip)

        self.label_ip_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ip_v.setEnabled(True)
        self.label_ip_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ip_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_ip_v.setObjectName("label_ip_v")
        self.verticalLayout_2.addWidget(self.label_ip_v)

        self.label_mac = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_mac.setObjectName("label_mac")
        self.verticalLayout_2.addWidget(self.label_mac)

        self.label_mac_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_mac_v.setEnabled(True)
        self.label_mac_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_mac_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_mac_v.setObjectName("label_mac_v")
        self.verticalLayout_2.addWidget(self.label_mac_v)

        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)

        self.label_name_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_name_v.setEnabled(True)
        self.label_name_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_name_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_name_v.setObjectName("label_name_v")
        self.verticalLayout_2.addWidget(self.label_name_v)

        self.label_cpu = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_cpu.setObjectName("label_cpu")
        self.verticalLayout_2.addWidget(self.label_cpu)

        self.label_cpu_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_cpu_v.setEnabled(True)
        self.label_cpu_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_cpu_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_cpu_v.setObjectName("label_cpu_v")
        self.verticalLayout_2.addWidget(self.label_cpu_v)

        self.label_ram = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_ram.setObjectName("label_ram")
        self.verticalLayout_2.addWidget(self.label_ram)

        self.label_ram_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_ram_v.setEnabled(True)
        self.label_ram_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_ram_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_ram_v.setObjectName("label_ram_v")
        self.verticalLayout_2.addWidget(self.label_ram_v)

        self.label_usage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_usage.setObjectName("label_access")
        self.verticalLayout_2.addWidget(self.label_usage)

        self.label_usage_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_usage_v.setEnabled(True)
        self.label_usage_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_usage_v.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_usage_v.setObjectName("label_access_v")
        self.verticalLayout_2.addWidget(self.label_usage_v)

        self.label_booting = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_booting.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_booting.setObjectName("label_usage")
        self.verticalLayout_2.addWidget(self.label_booting)

        self.label_booting_v = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_booting_v.setEnabled(True)
        self.label_booting_v.setMinimumSize(QtCore.QSize(0, 0))
        self.label_booting_v.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_booting_v.setObjectName("label_booting_v")
        self.verticalLayout_2.addWidget(self.label_booting_v)

        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuSetting.addAction(self.actionsetting)
        self.menuHelp.addAction(self.actionhelp)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HackerViewer"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Sung Kyungmo"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Park Minwoo"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Choi Jinseok"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Kim Heejoong"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_ip.setText(_translate("MainWindow", "IP"))
        self.label_ip_v.setText(_translate("MainWindow", ""+str(ip_address)))

        self.label_mac.setText(_translate("MainWindow", "MAC"))
        self.label_mac_v.setText(_translate("MainWindow", ""+str(mac_address)))

        self.label_name.setText(_translate("MainWindow", "NAME"))
        self.label_name_v.setText(_translate("MainWindow", ""+socket.gethostname()))

        self.label_cpu.setText(_translate("MainWindow", "CPU"))
        label_cpu_v_t=self.label_cpu_v

        self.label_ram.setText(_translate("MainWindow", "RAM"))
        label_ram_v_t=self.label_ram_v

        self.label_usage.setText(_translate("MainWindow", "Usage Time"))
        label_usage_v_t=self.label_usage_v

        self.label_booting.setText(_translate("MainWindow", "Booting Time"))
        self.label_booting_v.setText(_translate("MainWindow", ""+datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")))

        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionhelp.setText(_translate("MainWindow", "help"))

        class thread_status(QThread):
            def __init__(self):
                QThread.__init__(self)

            def __del__(self):
                self.wait()
            def run(self):
                while (True):
                    label_cpu_v_t.setText(_translate("MainWindow", "percent : " + str(psutil.cpu_percent()) + "%"))
                    label_ram_v_t.setText(_translate("MainWindow", "total : " + str(
                        round(psutil.virtual_memory().total / 1024 / 1024)) + "MB  available : " + str(
                        round(psutil.virtual_memory().available / 1024 / 1024)) + "MB  \npercent : " + str(
                        psutil.virtual_memory().percent) + "%"))  # i.totalRam
                    usage_time = datetime.datetime.now() - booting_t

                    usage_ts = usage_time.total_seconds()
                    usage_h = int(usage_ts / 3600)
                    usage_m = int((usage_ts - (usage_h * 3600)) / 60)
                    usage_s = int(usage_ts - (usage_h * 3600) - (usage_m * 60))

                    label_usage_v_t.setText(
                        _translate("MainWindow", str(usage_h) + "시간 " + str(usage_m) + "분 " + str(usage_s) + "초"))

                    time.sleep(1)

        self.t_status = thread_status()
        self.t_status.start()

