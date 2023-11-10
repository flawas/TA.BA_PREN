import logging
import requests
import json
from requests.structures import CaseInsensitiveDict

class Energyconsumption:

    def __init__(self, url):
        logging.info("Energyconsumption  init")
        self.__url = url

    def getdata(self):
        logging.info("Energyconsumption  getdata")
        reply = requests.get(url=self.__url + "/rpc/Switch.GetStatus?id=0")
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
        self.__initialpower = j["aenergy"]["total"]
        print(j["aenergy"]["total"])
        logging.info("Energyconsumption Set Initial Power: " + str(self.__initialpower))

    def setendpower(self):
        j = json.loads(self.getdata())
        self.__endpower = j["aenergy"]["total"]
        print(j["aenergy"]["total"])
        logging.info("Energyconsumption Set End Power: " + str(self.__initialpower))

    def getconsumtpion(self):
        # Wert wird in Watt-Stunden zurückgegeben
        logging.info("Energyconsumption getconsumption" + round(self.__endpower - self.__initialpower,2))
        return (round(self.__endpower - self.__initialpower,2))

    def checkavailability(self):
        logging.info("Energyconsumption checkavailaility")
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        try:
            resp = requests.get(self.geturl(), headers=headers, timeout=5)
            logging.info("Energyconsumption checkavailability " + str(resp.status_code))
            return True
        except requests.exceptions.Timeout:
            logging.error("Energyconsumption request timeout")
            return False