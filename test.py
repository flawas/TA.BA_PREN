from PREN_flawas import Engine, Display, DataPreparation
import os, threading, time, json, sys
import RPi.GPIO as GPIO
from multiprocessing import Process
from waveshare_epd import epd1in54_V2, epdconfig
from PIL import Image, ImageDraw, ImageFont


def display():
    print("Pause")


def worker(dataconfig):
    # Engine.setup()
    print(dataconfig)
    Engine.turnRight()
    time.sleep(1)
    Engine.turnLeft()
    time.sleep(1)
    Engine.turnLeft()

    while (True):
        Engine.solRed()
        time.sleep(5)
    sys.exit(0)


def startButton():
    Engine.wait_startButton()
    sys.exit(0)


def emergencyWatcher():
    Engine.wait_emergencyButton()
    sys.exit(0)


if __name__ == '__main__':
    # picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
    # epd = epd1in54_V2.EPD()
    # epd.init(1)
    # background = os.path.join('/home/pi/Desktop/PREN_2/pic/background.bmp')
    # backgroundmodified = os.path.join('/home/pi/Desktop/PREN_2/pic/background_modified.bmp')
    # font = os.path.join('/home/pi/Desktop/PREN_2/pic/Font.ttc')
    # Display.clearDisplay(epd)
    # Display.shutdownDisplay()

    # Display Thread
    # threadDisplay = threading.Thread(target = display)
    # threadDisplay.start()
    # threadDisplay.join()

    DataPreparation.setPos(1, "Blue")
    DataPreparation.setPos(2, "Red")
    DataPreparation.setPos(3, "Yellow")
    DataPreparation.setPos(4, "Nothing")
    DataPreparation.setPos(5, "Blue")
    DataPreparation.setPos(6, "Red")
    DataPreparation.setPos(7, "Yellow")
    DataPreparation.setPos(8, "Blue")
    print("Konfiguration" + DataPreparation.getconfig())
    dataconfig = DataPreparation.getconfig()

    # Engine Setup
    Engine.setup()

    threadEngine = threading.Thread(target=worker, args=(dataconfig,))
    threadEngine.start()

    # Button Threads
    # threadStartButton = threading.Thread(target = startButton)
    # threadEmergencyButton = threading.Thread(target = emergencyWatcher)
    # threadEmergencyButton.start()
    # threadStartButton.start()
    # threadStartButton.join()

    threadEngine.start()
