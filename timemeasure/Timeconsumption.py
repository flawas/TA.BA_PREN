import logging
import time


class Timeconsumption:

    def __init__(self):
        logging.info("Timeconsumption init")
        self.__starttime = 0
        self.__endtime = 0

    def setstarttime(self):
        logging.info("Timeconsumption setstarttime")
        self.__starttime = time.perf_counter()

    def setendtime(self):
        logging.info("Timeconsumption setendtime")
        self.__endtime = time.perf_counter()

    def getelapsedtime(self):
        logging.info("Timeconsumption getelapsedtime")
        logging.info("Elapsedtime: " + str(self.__endtime - self.__starttime))
        return round(((self.__endtime - self.__starttime)), 2)
