import time

class Timeconsumption:

    def setstarttime(self):
        t = time.localtime()
        self.__starttime = time.perf_counter()

    def setendtime(self):
        t = time.localtime()
        self.__endtime = time.perf_counter()

    def getelapsedtime(self):
        return self.__endtime - self.__starttime