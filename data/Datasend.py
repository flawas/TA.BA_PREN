import logging

import requests


# JSON Format
# {
#  "time": 32,
#  "energy": 0.5
# }
#
class Datasend:

    def __init__(self, url):
        logging.info("Datasend init")
        self.__url = url

    def geturl(self):
        logging.info("Datasend geturl")
        return self.__url

    def send(self, time, energy):
        logging.info("Datasend send")
        reply = requests.post(url=self.geturl(), json={"time": time, "energy": energy})
        logging.info("Datasend Status Code: " + str(reply.status_code))
