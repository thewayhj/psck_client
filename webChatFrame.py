from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QUrlQuery
from Util import MyYaml

class WebChatFrame(object):
    url = "http://" + MyYaml.node_js_host + ":" + str(MyYaml.node_js_port)
    @staticmethod
    def init(my_id = '', oppenent_id = ''):
        WebChatFrame.q_widget = QtWidgets.QWidget()
        WebChatFrame.q_widget.show()
        WebChatFrame.q_widget.resize(400, 600)

        view = QtWebEngineWidgets.QWebEngineView(WebChatFrame.q_widget)
        view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)

        url = QUrl(WebChatFrame.url+'/chat')
        urldata = QUrlQuery()
        urldata.addQueryItem('my_id', my_id)
        urldata.addQueryItem('oppenent_id', oppenent_id)
        url.setQuery(urldata)

        view.setUrl(url)
        view.show()

