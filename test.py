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


def workerOne(cube):
    # 1 = Gelb, 2 = Rot, 3 = Blau, 4= Nothing
    if cube[1] == "red":
        Engine.solRed()
        if cube[2] == "yellow":
            Engine.solYellow()
        if cube[2] == "red":
            Engine.turnRight()
            Engine.solRed()
            Engine.turnLeft()
        if cube[2] == "blue":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solBlue()
            Engine.turnRight()
            Engine.turnRight()

    if cube[1] == "yellow":
        Engine.solYellow()
        if cube[2] == "nothing":
            Engine.turnRight()
        if cube[2] == "yellow":
            Engine.turnRight()
            Engine.solYellow()
        if cube[2] == "red":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solRed()
            Engine.turnLeft()
        if cube[2] == "blue":
            Engine.turnLeft()
            Engine.solBlue()
            Engine.turnLeft()
            Engine.turnLeft()

    if cube[1] == "blue":
        Engine.solBlue()
        if cube[2] == "nothing":
            Engine.turnLeft()
        if cube[2] == "yellow":
            Engine.turnLeft()
            Engine.solYellow()
        if cube[2] == "red":
            Engine.solRed()
            Engine.turnLeft()
        if cube[2] == "blue":
            Engine.turnLeft()
            Engine.solBlue()
            Engine.turnLeft()

    if cube[1] == "nothing":
        if cube[2] == "yellow":
            Engine.solYellow()
        if cube[2] == "red":
            Engine.solRed()
            Engine.turnLeft()
        if cube[2] == "blue":
            Engine.solBlue()
            Engine.turnLeft()
            Engine.turnLeft()
    sys.exit(0)

def workerTwo(cube):
    if cube[4] == "nothing":
        if cube[5] == "yellow":
            Engine.turnRight()
            Engine.solYellow()
            if cube[8] == "nothing":
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
                Engine.turnRight()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "red":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solRed()
            if cube[8] == "nothing":
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[8] == "blue":
            Engine.turnLeft()
            Engine.solBlue()
            if cube[8] == "nothing":
                Engine.turnRight()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.solBlue()
                Engine.turnRight()

    if cube[4] == "yellow":
        Engine.turnLeft()
        Engine.solYellow()
        if cube[5] == "nothing":
            Engine.turnRight()
        if cube[5] == "yellow":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solYellow()
            if cube[8] == "nothing":
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
                Engine.turnRight()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "red":
            Engine.turnLeft()
            Engine.solRed()
            if cube[8] == "nothing":
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "blue":
            Engine.solBlue()
            if cube[8] == "nothing":
                Engine.turnRight()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.solBlue()
                Engine.turnRight()

    if cube[4] == "red":
        Engine.solRed()
        if cube[5] == "yellow":
            Engine.turnRight()
            Engine.solYellow()
            if cube[8] == "nothing":
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
                Engine.turnRight()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "red":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solRed()
            if cube[8] == "nothing":
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "blue":
            Engine.turnLeft()
            Engine.solBlue()
            if cube[8] == "nothing":
                Engine.turnRight()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.solBlue()
                Engine.turnRight()

    if cube[4] == "blue":
        Engine.turnRight()
        Engine.solBlue()
        if cube[5] == "nothing":
            Engine.turnLeft()
        if cube[5] == "yellow":
            Engine.solYellow()
            if cube[8] == "nothing":
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
                Engine.turnRight()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "red":
            Engine.turnRight()
            Engine.solRed()
            if cube[8] == "nothing":
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.turnRight()
                Engine.solBlue()
                Engine.turnRight()

        if cube[5] == "blue":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solBlue()
            if cube[8] == "nothing":
                Engine.turnRight()
            if cube[8] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
            if cube[8] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[8] == "blue":
                Engine.solBlue()
                Engine.turnRight()
    sys.exit(0)

def workerThree(cube):
    if cube[3] == "nothing":
        if cube[6] == "yellow":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solYellow()
            if cube[7] == "nothing":
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.solYellow()
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "red":
            Engine.turnLeft()
            Engine.solRed()
            if cube[7] == "nothing":
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "blue":
            Engine.solBlue()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.solBlue()

    if cube[3] == "yellow":
        Engine.solYellow()
        if cube[6] == "yellow":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solYellow()
            if cube[7] == "nothing":
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.solYellow()
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "red":
            Engine.turnLeft()
            Engine.solRed()
            if cube[7] == "nothing":
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "blue":
            Engine.solBlue()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.solBlue()

    if cube[3] == "red":
        Engine.turnRight():
        Engine.solRed()
        if cube[6] == "nothing":
            Engine.turnLeft()
        if cube[6] == "yellow":
            Engine.turnRight()
            Engine.solYellow()
            if cube[7] == "nothing":
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.solYellow()
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "red":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solRed()
            if cube[7] == "nothing":
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "blue":
            Engine.turnLeft()
            Engine.solBlue()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.solBlue()

    if cube[3] == "blue":
        Engine.turnRight()
        Engine.turnRight()
        Engine.solBlue()
        if cube[6] == "nothing":
            Engine.turnRight()
            Engine.turnRight()
        if cube[6] == "yellow":
            Engine.solYellow()
            if cube[7] == "nothing":
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.solYellow()
                Engine.turnRight()
                Engine.turnRight()
            if cube[7] == "red":
                Engine.turnRight()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "red":
            Engine.turnRight()
            Engine.solRed()
            if cube[7] == "nothing":
                Engine.turnRight()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.turnRight()
                Engine.solBlue()

        if cube[6] == "blue":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solBlue()
            if cube[7] == "yellow":
                Engine.turnLeft()
                Engine.turnLeft()
                Engine.solYellow()
                Engine.turnLeft()
                Engine.turnLeft()
            if cube[7] == "red":
                Engine.turnLeft()
                Engine.solRed()
                Engine.turnRight()
            if cube[7] == "blue":
                Engine.solBlue()
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
    cube = ColorRecognition.getResult()

    # Bob the builder ONE
    threadEngineOne = threading.Thread(target=workerOne, args=(cube,))
    threadEngineOne.start()

    ColorRecognition.getColors(2, "Screenshot2.png")
    cube = ColorRecognition.getResult()

    # Bob the builder TWO
    threadEngineOne.join()
    threadEngineTwo = threading.Thread(target=workerTwo, args=(cube,))
    threadEngineTwo.start()

    ColorRecognition.getColors(3, "Screenshot3.png")
    cube = ColorRecognition.getResult()
    # Bob the builder Three
    threadEngineTwo.join()
    threadEngineThree = threading.Thread(target=workerThree, args=(cube,))
    threadEngineThree.start()


    if(ColorRecognition.getPosPlate() == 1):
        DataPreparation.setPos(1, cube[1])
        DataPreparation.setPos(2, cube[2])
        DataPreparation.setPos(3, cube[3])
        DataPreparation.setPos(4, cube[4])
        DataPreparation.setPos(5, cube[5])
        DataPreparation.setPos(6, cube[6])
        DataPreparation.setPos(7, cube[7])
        DataPreparation.setPos(8, cube[8])

    if(ColorRecognition.getPosPlate() == 2):
        DataPreparation.setPos(6, cube[1])
        DataPreparation.setPos(1, cube[2])
        DataPreparation.setPos(8, cube[3])
        DataPreparation.setPos(3, cube[4])
        DataPreparation.setPos(2, cube[5])
        DataPreparation.setPos(5, cube[6])
        DataPreparation.setPos(4, cube[7])
        DataPreparation.setPos(7, cube[8])

    if (ColorRecognition.getPosPlate() == 3):
        DataPreparation.setPos(2, cube[1])
        DataPreparation.setPos(5, cube[2])
        DataPreparation.setPos(4, cube[3])
        DataPreparation.setPos(7, cube[4])
        DataPreparation.setPos(6, cube[5])
        DataPreparation.setPos(1, cube[6])
        DataPreparation.setPos(3, cube[7])
        DataPreparation.setPos(8, cube[8])

    if (ColorRecognition.getPosPlate() == 4):
        DataPreparation.setPos(5, cube[1])
        DataPreparation.setPos(6, cube[2])
        DataPreparation.setPos(3, cube[3])
        DataPreparation.setPos(4, cube[4])
        DataPreparation.setPos(1, cube[5])
        DataPreparation.setPos(2, cube[6])
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
