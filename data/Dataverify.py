import requests
import logging
from requests.structures import CaseInsensitiveDict


class Dataverify:

    def __init__(self, url, team):
        logging.info("Dataverify init")
        self.__url = url
        self.__team = team
        self.__teamurl = self.__url + self.__team

    def geturl(self):
        logging.info("Dataverify geturl")
        return self.__url

    def getteam(self):
        logging.info("Dataverify getteam")
        return self.__team

    def getteamurl(self):
        logging.info("Dataverify getteamurl")
        return self.__teamurl

    def checkavailability(self):
        logging.info("Dataverify checkavailaility")
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        try:
                resp = requests.get(self.geturl(), headers=headers, timeout=5)
                logging.info("Dataverify checkavailability " + str(resp.status_code))
                return True
        except requests.exceptions.Timeout:
                logging.error('Dataverify request timeout')
                return False


    def checkData(self):
        logging.info("Dataverify checkData")
        headers = CaseInsensitiveDict()
        headers["Auth"] = "testToken"
        headers["Content-Type"] = "application/json"

        data = {'time': '2023-10-20 11:27:05', 'config': {'1': 'red', '2': 'blue', '3': 'red', '4': 'yellow', '5': '','6': '','7': 'yellow', '8': 'red'}}
        resp = requests.post(self.getteamurl(), headers=headers, data=data)
        logging.info('Dataverify request '+ str(resp.status_code))
