import json
import urllib.request
import urllib.parse

import time

import psutil
from PyQt5.QtCore import QThread

from util import MyYaml


class Communication(object):

    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    #url = "http://127.0.0.1:3000"

    @staticmethod
    def send():
        routes = "/device/info"
        params = urllib.parse.urlencode({
            'ip': psutil.net_if_addrs()
        })
        binary_data = params.encode()

        data = urllib.request.urlopen(Communication.url+routes, binary_data).read()

        print(data)
        #data = urllib.request.urlopen(url, binary_data).read()

    @staticmethod
    def login(my_id):
        routes = "/status/login"
        params = urllib.parse.urlencode({
            'id': my_id
        })
        binary_data = params.encode()
        data = urllib.request.urlopen(Communication.url+routes, binary_data).read()
        print(data)


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
            print('hello')
            Communication.send()
            time.sleep(1)