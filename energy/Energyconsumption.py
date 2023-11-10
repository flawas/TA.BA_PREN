import logging
import requests
import json
import time

class Energyconsumption:

    def __init__(self, url):
        logging.info("Energyconsumption  init")
        self.__url = url

    def resetstatus(self):
        requests.post(url=self.__url + "")

    def getdata(self):
        logging.info("Energyconsumption  getdata")
        reply = requests.get(url=self.__url + "/rpc/Switch.GetStatus?id=0")
        logging.info("Energyconsumption Data: " + str(reply.content))
        return reply.content

    def switchoff(self):
        requests.post(self.__url + "/relay/0?turn=off")

    def switchon(self):
        requests.post(self.__url + "/relay/0?turn=on")

    def setinitialpower(self):
        j = json.loads(self.getdata())
        self.__initialpower = j["aenergy"]["total"]
        print(j["aenergy"]["total"])
        logging.info("Set Initial Power: " + str(self.__initialpower))

    def setendpower(self):
        j = json.loads(self.getdata())
        self.__endpower = j["aenergy"]["total"]
        print(j["aenergy"]["total"])
        logging.info("Set End Power: " + str(self.__initialpower))

    def getconsumtpion(self):
        # Wert wird in Watt-Stunden zurückgegeben
        return (round(self.__endpower - self.__initialpower,2))