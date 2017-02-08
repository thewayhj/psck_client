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


