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

    print(dataconfig.getconfig())

    # 1 = Gelb, 2 = Rot, 3 = Blau, 4= Nothing
    turner = {1: -1, 2: 0, 3: 1}

    for x in range(1, 9):
        print(dataconfig.getPos(x) + " legen")

        if (dataconfig.getPos(x) == "Red"):
            Engine.solRed()
        if (dataconfig.getPos(x) == "Yellow"):
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnRight()
        if (dataconfig.getPos(x) == "Blue"):
            Engine.turnRight()
            Engine.solBlue()
            Engine.turnLeft()
        if (dataconfig.getPos(x) == "Nothing"):
            print("Nothing to do")

        if (x == 1):
            Engine.turnRight()
        if (x == 2):
            print("No turn")
        if (x == 3):
            Engine.turnLeft()
        if (x == 4):
            Engine.turnRight()
            Engine.turnRight()
        if (x == 5):
            Engine.turnRight()
        if (x == 6):
            print("No turn")
        if (x == 7):
            Engine.turnLeft()
        if (x == 8):
            Engine.turnRight()
            Engine.turnRight()

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

    # Display.drawInitialDisplay(epd, background, backgroundmodified, font)
    # Display.updateDisplay(epd, 10, 30, '', background, backgroundmodified, font)

    DataPreparation.setPos(1, "Yellow")
    DataPreparation.setPos(2, "Red")
    DataPreparation.setPos(3, "Yellow")
    DataPreparation.setPos(4, "Red")
    DataPreparation.setPos(5, "Blue")
    DataPreparation.setPos(6, "Blue")
    DataPreparation.setPos(7, "Red")
    DataPreparation.setPos(8, "Yellow")

    # Engine Setup
    Engine.setup()
    threadEngine = threading.Thread(target=worker, args=(DataPreparation,))

    # Button Threads
    # threadStartButton = threading.Thread(target = startButton)
    # threadEmergencyButton = threading.Thread(target = emergencyWatcher)
    # threadEmergencyButton.start()
    # threadStartButton.start()
    # threadStartButton.join()
    # Display.updateDisplay(epd, 10, 30, 'Bob the builder is running...', background, backgroundmodified, font)

    threadEngine.start()

    Engine.piezo()
    Display.updateDisplay(epd, 10, 30, 'Bob the builder finished!', background, backgroundmodified, font)
    time.sleep(10)
    Display.shutdownDisplay(epd)
