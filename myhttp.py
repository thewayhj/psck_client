
import urllib.request


class Communication():
    f = urllib.request.urlopen("http://127.0.0.1:3000/client")
    print(f.read())