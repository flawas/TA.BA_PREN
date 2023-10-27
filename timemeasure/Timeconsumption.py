import time


class Timeconsumption:

    def __init__(self):
        self.__starttime = 0
        self.__endtime = 0

    def setstarttime(self):
        t = time.localtime()
        self.__starttime = time.perf_counter()

    def setendtime(self):
        t = time.localtime()
        self.__endtime = time.perf_counter()

    def getelapsedtime(self):
        print("Elapsedtime: " + str(self.__endtime - self.__starttime))
        return round(((self.__endtime - self.__starttime) / 1000), 2)
