from PREN_flawas import Engine, Display, DataPreparation, Videostream, DataVerify, ColorRecognition
import os, threading, json, sys, time
import RPi.GPIO as GPIO
from time import gmtime, strftime
from datetime import datetime
from multiprocessing import Process
from waveshare_epd import epd1in54_V2, epdconfig
from PIL import Image, ImageDraw, ImageFont


def picrecog():
    maxColor = Videostream.get_max_pixel('147.88.48.131', 'pren', '463997', 'pren_profile_med', 600)
    while (True):
        if (Videostream.open_camera_profile('147.88.48.131', 'pren', '463997', 'pren_profile_med', maxColor) == True):
            Videostream.writeScreenshot('147.88.48.131', 'pren', '463997', 'pren_profile_med', "Screenshot1")
            time.sleep(11.5)
            Videostream.writeScreenshot('147.88.48.131', 'pren', '463997', 'pren_profile_med', "Screenshot2")
            break


def worker(dataconfig):
    # 1 = Gelb, 2 = Rot, 3 = Blau, 4= Nothing
    print(dataconfig.getjson())

    for x in range(1, 9):
        print(dataconfig.getconfig())
        if (dataconfig.getPos(x) == "red"):
            Engine.solRed()
        if (dataconfig.getPos(x) == "yellow"):
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnRight()
        if (dataconfig.getPos(x) == "blue"):
            Engine.turnRight()
            Engine.solBlue()
            Engine.turnLeft()
        if (dataconfig.getPos(x) == "nothing"):
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

    Engine.solWeight()
    Engine.piezo()
    sys.exit(0)


def startButton():
    Engine.wait_startButton()
    sys.exit(0)


def emergencyWatcher():
    Engine.wait_emergencyButton()
    sys.exit(0)


if __name__ == '__main__':
    picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
    epd = epd1in54_V2.EPD()
    epd.init(1)
    background = os.path.join('/home/pi/Desktop/PREN_2/pic/background.bmp')
    backgroundmodified = os.path.join('/home/pi/Desktop/PREN_2/pic/background_modified.bmp')
    font = os.path.join('/home/pi/Desktop/PREN_2/pic/Font.ttc')
    Display.clearDisplay(epd)

    Display.drawInitialDisplay(epd, background, backgroundmodified, font)

    Display.clearDisplay(epd)
    Display.shutdownDisplay(epd)
    time.sleep(10)

    # Engine Setup
    Engine.setup()

    # Button Threads
    threadStartButton = threading.Thread(target=startButton)
    threadEmergencyButton = threading.Thread(target=emergencyWatcher)
    threadEmergencyButton.start()
    threadStartButton.start()
    Display.updateDisplay(epd, 10, 30, 'Bob the builder is ready!', background, backgroundmodified, font)

    ## Start nach StartButton Join
    threadStartButton.join()
    now = datetime.now()
    Engine.piezo()
    Display.updateDisplay(epd, 10, 30, 'Bob the builder is running...', background, backgroundmodified, font)
    DataVerify.sendStatus("https://oawz3wjih1.execute-api.eu-central-1.amazonaws.com/cubes/team33/start",
                          "QBg3kjqB59xN")

    # Bilderkennung
    threadPicRecOne = threading.Thread(target=picrecog)
    threadPicRecOne.start()
    threadPicRecOne.join()
    ColorRecognition.getColors(1, "Screenshot1.png")
    ColorRecognition.getColors(2, "Screenshot2.png")

    cube = ColorRecognition.getResult()

    DataPreparation.setPos(1, cube[1])
    DataPreparation.setPos(2, cube[2])
    DataPreparation.setPos(3, cube[3])
    DataPreparation.setPos(4, cube[4])
    DataPreparation.setPos(5, cube[5])
    DataPreparation.setPos(6, cube[6])
    DataPreparation.setPos(7, cube[7])
    DataPreparation.setPos(8, cube[8])

    '''
    # DEMO
    DataPreparation.setPos(1, "Red")
    DataPreparation.setPos(2, "Blue")
    DataPreparation.setPos(3, "Yellow")
    DataPreparation.setPos(4, "Red")
    DataPreparation.setPos(6, "Red")
    DataPreparation.setPos(7, "Blue")
    DataPreparation.setPos(8, "Yellow")
    '''
    data = DataPreparation.getjson()
    DataVerify.sendData("https://oawz3wjih1.execute-api.eu-central-1.amazonaws.com/cubes/team33/config", "QBg3kjqB59xN",
                        data)

    threadEngine = threading.Thread(target=worker, args=(DataPreparation,))
    threadEngine.start()

    threadEngine.join()
    DataVerify.sendStatus("https://oawz3wjih1.execute-api.eu-central-1.amazonaws.com/cubes/team33/end", "QBg3kjqB59xN")
    later = datetime.now()
    Display.updateDisplay(epd, 10, 30, 'Bob the builder finished!', background, backgroundmodified, font)
    difference = (later - now).total_seconds()
    print(f"Time difference in seconds: {int(difference)}")
    text = str(int(difference)) + " Sekunden"
    Display.updateDisplay(epd, 10, 100, text, background, backgroundmodified, font)
    Display.drawPicture(epd, 'pic/bob.bmp')
    time.sleep(10)
    Display.clearDisplay(epd)
    Display.shutdownDisplay(epd)
