from data.Datasend import Datasend
from data.Dataverify import Dataverify
from display.Display import Display
from timemeasure.Timeconsumption import Timeconsumption

class main:

    def __init__(self):
        self.__datasend = Datasend("https://i-ba-pren.flaviowaser.ch/upload-data.php")
        self.__dataverify = Dataverify("http://18.192.48.168:5000/cubes/", "team33")
        self.__display = Display()
        self.__timemeasure = Timeconsumption()

    def start(self):
        self.__timemeasure.setstarttime()
        self.__display.drawInitialDisplay()
        if self.__dataverify.checkavailability():
            self.__display.updateDisplay(10, 30, 'Connection PREN-Server OK')
        else:
            self.__display.updateDisplay(10, 30, 'Connection PREN-Server NOK')


    def end(self, energy):
        self.__timemeasure.setendtime()
        self.__display.loop()
        self.__datasend.send(energy, self.__timemeasure.getelapsedtime())



main().start()