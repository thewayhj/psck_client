
import urllib.request


class Communication():


    f = urllib.request.urlopen("http://192.168.0.203:3000/test")
    print(f.read())