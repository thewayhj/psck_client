class User:
    def __init__(self,id):
        self.id = id
        self.name = 'unknown-pc'
        self.ip = '111.111.111.111'
        self.mac = 'ff:ff:ff:ff:ff:ff'

    def setName(self,name):
        self.name = name

    def setAddr(self, ip, mac):
        self.ip = ip
        self.mac = mac


