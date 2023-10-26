import requests
import logging
from requests.structures import CaseInsensitiveDict


class Dataverify:

    def __init__(self, url, team):
        self.__url = url
        self.__team = team
        self.__teamurl = self.__url + self.__team

    def geturl(self):
        return self.__url

    def getteam(self):
        return self.__team

    def getteamurl(self):
        return self.__teamurl

    def checkavailability(self):
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        resp = requests.get(self.geturl(), headers=headers)
        if(resp.status_code == 200):
            return True
        else:
            return False

    def checkData(self):
        headers = CaseInsensitiveDict()
        headers["Auth"] = "testToken"
        headers["Content-Type"] = "application/json"

        data = {'time': '2023-10-20 11:27:05', 'config': {'1': 'red', '2': 'blue', '3': 'red', '4': 'yellow', '5': '','6': '','7': 'yellow', '8': 'red'}}
        resp = requests.post(self.getteamurl(), headers=headers, data=data)
        print(resp.status_code)


# df = Dataverify("http://18.192.48.168:5000/cubes/", "team33")
# df.checkavailability()