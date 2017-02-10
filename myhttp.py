import json
import urllib.request
import urllib.parse

from util import MyYaml


class Communication(object):

    @staticmethod
    def send2():
        url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port) + "/" + "test"
        temp = "http://127.0.0.1:3000/test"
        apikey = "DAUM_SEARCH_DEMO_APIKEY"
        output = "xml"
        q = "OpenAPI"

        params = urllib.parse.urlencode({
            'apikey': apikey,
            'output': output,
            'q': q
        })
        binary_data = params.encode()

        data = urllib.request.urlopen(url, binary_data).read()

        print(data)
        #data = urllib.request.urlopen(url, binary_data).read()


class FriendCommunication(object):

    url_base = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port) + "/" + "friend"

    @staticmethod
    def add():
        test = "http://127.0.0.1:3000/friend/add"

        url = FriendCommunication.url_base + '/add'
        params = urllib.parse.urlencode({
            'my_id': 'pmw9027',
            'add_id': 'theway'
        })

        binary_data = params.encode()

        #req = urllib.request.Request(test, headers=hdr);
        print(binary_data);
        data = urllib.request.urlopen(test, binary_data).read()

        print(data)
        #data = urllib.request.urlopen(url, binary_data).read()
