import json
from time import gmtime, strftime

class Datapreperation:

    def __init__(self):
        self.__1 = ""
        self.__2 = ""
        self.__3 = ""
        self.__4 = ""
        self.__5 = ""
        self.__6 = ""
        self.__7 = ""
        self.__8 = ""

    def setpos1(self, value):
        self.__1 = value

    def setpos2(self, value):
        self.__2 = value

    def setpos3(self, value):
        self.__3 = value

    def setpos4(self, value):
        self.__4 = value

    def setpos5(self, value):
        self.__5 = value

    def setpos6(self, value):
        self.__6 = value

    def setpos7(self, value):
        self.__7 = value

    def setpos8(self, value):
        self.__8 = value
    def getpos1(self):
        print(self.__1)

    def getpos2(self):
        print(self.__2)

    def getpos3(self):
        print(self.__3)

    def getpos4(self):
        print(self.__4)

    def getpos5(self):
        print(self.__5)

    def getpos6(self):
        print(self.__6)

    def getpos7(self):
        print(self.__7)

    def getpos8(self):
        print(self.__8)

    def getjson(self):
        data = {'time': strftime("%Y-%m-%d %H:%M:%S", gmtime()),'config': {'1': self.__1, '2': self.__2, '3': self.__3, '4': self.__4, '5': self.__5,'6': self.__6,'7': self.__7, '8': self.__8}}
        return json.dumps(data)