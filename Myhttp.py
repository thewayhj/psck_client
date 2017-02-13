import urllib.request
import urllib.parse
import time
from PyQt5.QtCore import QThread

from DeviceinfoThread import DeviceInfoThread
from model.Device import DeviceInfo
from model.User import User
from Util import MyYaml


class Communication(object):

    #url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    url = "http://127.0.0.1:3000"

    info = DeviceInfo('1', '1')

    @staticmethod
    def send():
        routes = "/device/info"
        params = urllib.parse.urlencode(DeviceInfoThread.friend_device_info[0].__dict__)
        binary_data = params.encode()

        try:
            data = urllib.request.urlopen(Communication.url+routes, binary_data).read()
        except Exception as e:
            print(e)


        #print(data)
        #data = urllib.request.urlopen(url, binary_data).read()

    @staticmethod
    def send2(u_id):
        routes = "/friend/info"
        params = urllib.parse.urlencode({
            'u_id': u_id
        })
        binary_data = params.encode()
        try:
            data = urllib.request.urlopen(Communication.url + routes, binary_data).read()
        except Exception as e:
            print(e)

    @staticmethod
    def login(my_id):
        routes = "/status/login"
        params = urllib.parse.urlencode({
            'id': my_id
        })
        binary_data = params.encode()
        try:
            data = urllib.request.urlopen(Communication.url+routes, binary_data).read()
        except Exception as e:
            print(e)



class FriendCommunication(object):

    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port) + "/" + "friend"

    @staticmethod
    def add():

        routes = '/friend/add'
        params = urllib.parse.urlencode({
            'my_id': 'pmw9027',
            'add_id': 'theway'
        })

        binary_data = params.encode()

        #req = urllib.request.Request(test, headers=hdr);
        print(binary_data);
        data = urllib.request.urlopen(FriendCommunication.url + routes, binary_data).read()

        print(data)
        #data = urllib.request.urlopen(url, binary_data).read()


class ThreadCommunication(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if User.is_login():
                Communication.send()
                time.sleep(1)


class ThreadFriendInfoCommunication(QThread):

    u_id = 0

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if ThreadFriendInfoCommunication.u_id is 0:
                continue
            else:
                Communication.send2(ThreadFriendInfoCommunication.u_id)
                time.sleep(1)