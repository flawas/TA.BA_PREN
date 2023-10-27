from data.Datasend import Datasend
from data.Dataverify import Dataverify
from display.Display import Display
from timemeasure.Timeconsumption import Timeconsumption
import threading
from threading import Thread as Thread
import time


class main:

    def __init__(self):
        self.__datasend = Datasend("https://i-ba-pren.flaviowaser.ch/upload-data.php")
        self.__dataverify = Dataverify("http://18.192.48.168:5000/cubes/", "team33")
        self.__display = Display()
        # self.__display.clearDisplay()
        self.__timemeasure = Timeconsumption()

    def initialization(self):
        self.__display.drawInitialDisplay()
        self.__display.updateDisplay(10, 30, 'Initialisierung')
        if self.__dataverify.checkavailability():
            self.__display.updateDisplay(10, 30, 'Conn. PREN-Server OK')
        else:
            self.__display.updateDisplay(10, 30, 'Conn. PREN-Server NOK')

    def start(self):
        self.__display.updateDisplay(10, 30, 'Programm läuft')
        self.__timemeasure.setstarttime()

    def end(self):
        self.__timemeasure.setendtime()

        self.__display.updateDisplay(10, 10, 'PREN TEAM 33')
        self.__display.updateDisplay(10, 30, 'Programm beendet')
        self.__display.updateDisplay(10, 80, 'Beanspruchte Zeit')
        self.__display.updateDisplay(10, 100, str(self.__timemeasure.getelapsedtime()) + ' Sekunden')
        self.__display.updateDisplay(10, 150, 'Stromverbrauch')
        self.__display.updateDisplay(10, 170, 'kW')
        # time.sleep(5)
        # self.__display.loop()
        # self.__datasend.send(self.__timemeasure.getelapsedtime(), 0.5)


if __name__ == "__main__":
    main().initialization()
    main().start()
    main().end()
