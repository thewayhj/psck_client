import pymongo
import yaml


class LoginDao(object):

    def __init__(self):

        stream = open("setting.yaml", 'r')
        setting = yaml.load(stream)
        host = setting['server']['host']
        port = setting['server']['mongodb_port']

        self.connection = pymongo.MongoClient(host, port)
        self.db = self.connection.test
        self.collection = self.db.user

    def login(self, u_id, u_pw):
        docs = self.collection.find({"id": u_id, "pw": u_pw})
        if docs.count():
            return True
        else:
            return False


class JoinDao(object):
    def __init__(self):

        stream = open("setting.yaml", 'r')
        setting = yaml.load(stream)
        host = setting['server']['host']
        port = setting['server']['mongodb_port']

        self.connection = pymongo.MongoClient(host, port)
        self.db = self.connection.test
        self.collection = self.db.user

    def join(self, u_id, u_pw):
        self.collection.insert({'id': u_id, 'pw': u_pw})
        return True


