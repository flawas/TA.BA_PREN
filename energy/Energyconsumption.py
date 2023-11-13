import logging
import requests
import json
import time

class Energyconsumption:

    def __init__(self, url, devid, authkey):
        logging.info("Energyconsumption  init")
        self.__url = url
        self.__devid = devid
        self.__authkey = authkey
        self.__endpower = 0
        self.__initialpower = 0

    def getdata(self):
        logging.info("Energyconsumption  getdata")
        data = {'id': self.__devid, 'auth_key': self.__authkey}
        reply = requests.post("https://shelly-21-eu.shelly.cloud/device/status", data=data)
        logging.info("Energyconsumption Data: " + str(reply.content))
        return reply.content

    def switchoff(self):
        requests.post(self.__url + "/relay/0?turn=off")
        logging.info("Energyconsumption Set Switch OFF")

    def switchon(self):
        requests.post(self.__url + "/relay/0?turn=on")
        logging.info("Energyconsumption Set Switch ON")

    def setinitialpower(self):
        j = json.loads(self.getdata())
        self.__initialpower = j["data"]["device_status"]["switch:0"]["aenergy"]["total"]
        logging.info("Energyconsumption Set Initial Power: " + str(self.__initialpower))

    def getinitialpower(self):
        return self.__initialpower

    def getendpower(self):
        return self.__endpower

    def setendpower(self):
        j = json.loads(self.getdata())
        self.__endpower = j["data"]["device_status"]["switch:0"]["aenergy"]["total"]
        logging.info("Energyconsumption Set End Power: " + str(self.__endpower))

    def getconsumtpion(self):
        # Wert wird in Watt-Stunden zurückgegeben
        logging.info("Energyconsumption getconsumption" + str(round(self.__endpower - self.__initialpower,2)))
        return (round(self.__endpower - self.__initialpower,2))

    def checkavailability(self):
        logging.info("Energyconsumption checkavailaility")
        data = {'id': self.__devid, 'auth_key': self.__authkey}
        try:
            resp = requests.post("https://shelly-21-eu.shelly.cloud/device/status", data=data, timeout=5)
            logging.info("Energyconsumption checkavailability " + str(resp.status_code))
            return True
        except requests.exceptions.Timeout:
            logging.error("Energyconsumption request timeout")
            return False