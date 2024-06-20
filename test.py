import logging
from PREN_flawas import Engine, Display, DataPreparation, DataVerify, ColorRecognition, Energy, DataSend
import os, threading, json, sys, time
import RPi.GPIO as GPIO
from time import gmtime, strftime
from datetime import datetime
from multiprocessing import Process
from waveshare_epd import epd1in54_V2, epdconfig
from PIL import Image, ImageDraw, ImageFont


def picrecog():
    ColorRecognition.open_camera_profile('147.88.48.131', 'pren', '463997', 'pren_profile_med', 'Screenshot1')
    logging.info("Screenshot 1 done")
    ColorRecognition.getColors(1, 'Screenshot1.png')
    time.sleep(5.8)
    print(ColorRecognition.getResult())
    ColorRecognition.writeScreenshot('147.88.48.131', 'pren', '463997', 'pren_profile_med', 'Screenshot2')
    logging.info("Screenshot 2 done")
    ColorRecognition.getColors(2, 'Screenshot2.png')
    time.sleep(5.2)
    print(ColorRecognition.getResult())
    ColorRecognition.writeScreenshot('147.88.48.131', 'pren', '463997', 'pren_profile_med', 'Screenshot3')
    logging.info("Screenshot 3 done")
    ColorRecognition.getColors(3, 'Screenshot3.png')
    logging.info(ColorRecognition.getResult())
    logging.info("PosPlate: " + str(ColorRecognition.getPosPlate()))


def workerOne(cube):
    logging.info("Worker One starting")
    logging.debug(cube)
    logging.debug(cube[1])
    # 1 = Gelb, 2 = Rot, 3 = Blau, 4= Nothing
    if cube[1] == "Yellow" and cube[2] == "Yellow":
        Engine.solYellow()
        Engine.turnRight()
        Engine.solYellow()
    if cube[1] == "Yellow" and cube[2] == "Red":
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnLeft()
    if cube[1] == "Yellow" and cube[2] == "Blue":
        Engine.solYellow()   
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[1] == "Yellow" and cube[2] == "":
        Engine.solYellow()
        Engine.turnRight()  
    if cube[1] == "Red" and cube[2] == "Yellow":
        Engine.solRed()
        Engine.solYellow()
    if cube[1] == "Red" and cube[2] == "Red":
        Engine.solRed()
        Engine.turnLeft()
        Engine.solRed()
    if cube[1] == "Red" and cube[2] == "Blue":
        Engine.solBlue()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
    if cube[1] == "Red" and cube[2] == "":
        Engine.solRed()   
    if cube[1] == "Blue" and cube[2] == "Yellow":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.solYellow()
    if cube[1] == "Blue" and cube[2] == "Red":
        Engine.solBlue()
        Engine.solRed()
        Engine.turnLeft()
    if cube[1] == "Blue" and cube[2] == "Blue":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
    if cube[1] == "Blue" and cube[2] == "":
        Engine.solBlue()
        Engine.turnLeft()
    if cube[1] == "" and cube[2] == "Yellow":
        Engine.solYellow()
    if cube[1] == "" and cube[2] == "Red":
        Engine.solRed()
        Engine.turnLeft()
    if cube[1] == "" and cube[2] == "Blue":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    """sys.exit(0)
def workerTwo(cube):"""
    if cube[4] == "" and cube[5] == "Yellow":
        Engine.turnRight()
        Engine.solYellow()
        if cube[8] == "Yellow":
            Engine.solYellow()
            Engine.turnLeft()
        if cube[8] == "Red":
            Engine.turnRight()
            Engine.solRed()
            Engine.turnRight()
            Engine.turnRight()
        if cube[8] == "Blue":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solBlue()
            Engine.turnRight()
        if cube[8] == "":
            Engine.turnLeft()
    if cube[4] == "" and cube[5] == "Red":
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solRed()
        if cube[8] == "Yellow":
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnLeft()
        if cube[8] == "Red":
            Engine.solRed()
            Engine.turnLeft()
            Engine.turnLeft()
        if cube[8] == "Blue":
            Engine.turnRight()
            Engine.solBlue()
            Engine.turnRight()
        if cube[8] == "":
            Engine.turnLeft()
            Engine.turnLeft()
    if cube[4] == "" and cube[5] == "Blue":
        Engine.turnLeft()
        Engine.solBlue()
        if cube[8] == "Yellow":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnLeft()
        if cube[8] == "Red":
            Engine.turnLeft()
            Engine.solRed()
            Engine.turnLeft()
            Engine.turnLeft()
        if cube[8] == "Blue":
            Engine.solBlue()
            Engine.turnRight()
        if cube[8] == "":
            Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "Yellow" and cube[8] == "Yellow":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Yellow" and cube[8] == "Red":
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "Yellow" and cube[8] == "Blue":
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "Yellow" and cube[8] == "":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Red" and cube[8] == "Yellow":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Red" and cube[8] == "Red":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Red" and cube[8] == "Blue":
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "Red" and cube[8] == "":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Blue" and cube[8] == "Yellow":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Blue" and cube[8] == "Red":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Yellow" and cube[5] == "Blue" and cube[8] == "Blue":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "Blue" and cube[8] == "":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Yellow" and cube[5] == "":
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "Yellow" and cube[8] == "Yellow":
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()    
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Yellow" and cube[8] == "Red":
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()    
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "Yellow" and cube[8] == "Blue":
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()    
        Engine.turnRight()
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "Yellow" and cube[8] == "":
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Red" and cube[8] == "Yellow":
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Red" and cube[8] == "Red":
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solRed()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Red" and cube[8] == "Blue":
        Engine.solRed()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "Red" and cube[8] == "":
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Blue" and cube[8] == "Yellow":
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Blue" and cube[8] == "Red":
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()    
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[4] == "Red" and cube[5] == "Blue" and cube[8] == "Blue":
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "Blue" and cube[8] == "":
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Red" and cube[5] == "":
        Engine.solRed()
    if cube[4] == "Blue" and cube[5] == "Yellow" and cube[8] == "Yellow":
        Engine.turnRight()
        Engine.solBlue()
        Engine.solYellow()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Yellow" and cube[8] == "Red":
        Engine.turnRight()
        Engine.solBlue()
        Engine.solYellow()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.turnRight()
    if cube[4] == "Blue" and cube[5] == "Yellow" and cube[8] == "Blue":
        Engine.turnRight()
        Engine.solBlue()
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Blue" and cube[5] == "Yellow" and cube[8] == "":
        Engine.turnRight()
        Engine.solBlue()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Red" and cube[8] == "Yellow":
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Red" and cube[8] == "Red":
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()
        Engine.solRed()
        Engine.turnRight()
        Engine.turnRight()
    if cube[4] == "Blue" and cube[5] == "Red" and cube[8] == "Blue":
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()    
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
    if cube[4] == "Blue" and cube[5] == "Red" and cube[8] == "":
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()    
        Engine.turnRight()
        Engine.turnRight()
    if cube[4] == "Blue" and cube[5] == "Blue" and cube[8] == "Yellow":
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()        
        Engine.solBlue()
        Engine.solYellow()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Blue" and cube[8] == "Red":
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.solRed()        
        Engine.turnLeft()        
        Engine.solBlue()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Blue" and cube[8] == "Blue":
        Engine.turnLeft()
        Engine.solBlue()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "Blue" and cube[8] == "":
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
    if cube[4] == "Blue" and cube[5] == "":
        Engine.turnRight()
        Engine.solBlue()
        Engine.turnLeft()
    """sys.exit(0)
    def workerThree(cube):"""
    if cube[3] == "" and cube[6] == "Yellow":
        Engine.turnRight()
        Engine.turnRight()
        Engine.solYellow()
        if cube[7] == "Yellow":
            Engine.solYellow()
            Engine.turnRight()
            Engine.turnRight()
        if cube[7] == "Red":
            Engine.turnRight()
            Engine.solRed()
            Engine.turnRight()
        if cube[7] == "Blue":
            Engine.turnRight()
            Engine.turnRight()
            Engine.solBlue()
        if cube[7] == "":
            Engine.turnRight()
            Engine.turnRight()
    if cube[3] == "" and cube[6] == "Red":
        Engine.turnLeft()
        Engine.solRed()
        if cube[7] == "Yellow":
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnLeft()
            Engine.turnLeft()
        if cube[7] == "Red":
            Engine.solRed()
            Engine.turnRight()
        if cube[7] == "Blue":
            Engine.turnRight()
            Engine.solBlue()
        if cube[7] == "":
            Engine.turnRight()
    if cube[3] == "" and cube[6] == "Blue":
        Engine.solBlue()
        if cube[7] == "Yellow":
            Engine.turnLeft()
            Engine.turnLeft()
            Engine.solYellow()
            Engine.turnLeft()
            Engine.turnLeft()
        if cube[7] == "Red":
            Engine.turnLeft()
            Engine.solRed()
            Engine.turnRight()
        if cube[7] == "Blue":
            Engine.solBlue()
    if cube[3] == "Yellow" and cube[6] == "Yellow" and cube[7] == "Yellow":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Yellow" and cube[6] == "Yellow" and cube[7] == "Red":
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solYellow()        
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Yellow" and cube[6] == "Yellow" and cube[7] == "Blue":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
    if cube[3] == "Yellow" and cube[6] == "Yellow" and cube[7] == "":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Yellow" and cube[6] == "Red" and cube[7] == "Yellow":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Yellow" and cube[6] == "Red" and cube[7] == "Red":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()           
        Engine.solRed()
        Engine.turnRight()      
    if cube[3] == "Yellow" and cube[6] == "Red" and cube[7] == "Blue":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()         
        Engine.turnRight()
        Engine.solBlue()
    if cube[3] == "Yellow" and cube[6] == "Red" and cube[7] == "":
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Yellow" and cube[6] == "Blue" and cube[7] == "Yellow":
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Yellow" and cube[6] == "Blue" and cube[7] == "Red":
        Engine.solYellow()
        Engine.solBlue()       
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Yellow" and cube[6] == "Blue" and cube[7] == "Blue":
        Engine.solYellow()
        Engine.solBlue()
        Engine.solBlue()
    if cube[3] == "Yellow" and cube[6] == "Blue" and cube[7] == "":
        Engine.solYellow()
        Engine.solBlue()
    if cube[3] == "Yellow" and cube[6] == "":
        Engine.solYellow()
    if cube[3] == "Red" and cube[6] == "Yellow" and cube[7] == "Yellow":
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()         
        Engine.solYellow()
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Yellow" and cube[7] == "Red":
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()         
        Engine.solYellow()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Yellow" and cube[7] == "Blue":
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()         
        Engine.solYellow()
        Engine.turnRight()    
        Engine.turnRight()
        Engine.solBlue()
    if cube[3] == "Red" and cube[6] == "Yellow" and cube[7] == "":
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Red" and cube[7] == "Yellow":       
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
    if cube[3] == "Red" and cube[6] == "Red" and cube[7] == "Red":
        Engine.turnLeft()
        Engine.solRed()
        Engine.solRed()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()        
    if cube[3] == "Red" and cube[6] == "Red" and cube[7] == "Blue":
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
        Engine.solBlue()
    if cube[3] == "Red" and cube[6] == "Red" and cube[7] == "":
        Engine.turnRight()
        Engine.solRed()    
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Blue" and cube[7] == "Yellow":
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()        
        Engine.turnRight()
        Engine.solYellow()
        Engine.turnRight()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Blue" and cube[7] == "Red":
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()        
        Engine.turnRight()
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Red" and cube[6] == "Blue" and cube[7] == "Blue":
        Engine.solBlue()
        Engine.solBlue()
        Engine.turnRight()
        Engine.solRed()        
        Engine.turnLeft()
    if cube[3] == "Red" and cube[6] == "":
        Engine.turnRight()
        Engine.solRed()        
        Engine.turnLeft()   
    if cube[3] == "Blue" and cube[6] == "Yellow" and cube[7] == "Yellow":
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Yellow" and cube[7] == "Red":
        Engine.turnRight()
        Engine.turnRight()
        Engine.solYellow()
        Engine.solBlue()              
        Engine.turnRight()
        Engine.solRed()
        Engine.turnRight()
    if cube[3] == "Blue" and cube[6] == "Yellow" and cube[7] == "Blue":
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()       
        Engine.solBlue()
    if cube[3] == "Blue" and cube[6] == "Yellow" and cube[7] == "":
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft() 
    if cube[3] == "Blue" and cube[6] == "Red" and cube[7] == "Yellow":
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.solYellow()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Red" and cube[7] == "Red":
        Engine.turnLeft()
        Engine.solRed()
        Engine.solRed()
        Engine.Left()
        Engine.solBlue()
        Engine.solLeft()
        Engine.solLeft()
    if cube[3] == "Blue" and cube[6] == "Red" and cube[7] == "Blue":
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
    if cube[3] == "Blue" and cube[6] == "Red" and cube[7] == "":
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Blue" and cube[7] == "Yellow":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solYellow()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Blue" and cube[7] == "Red":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.solRed()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Blue" and cube[7] == "Blue":
        Engine.solBlue()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "Blue" and cube[7] == "":
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if cube[3] == "Blue" and cube[6] == "":    
        Engine.turnLeft()
        Engine.turnLeft()
        Engine.solBlue()
        Engine.turnLeft()
        Engine.turnLeft()
    if (ColorRecognition.getPosPlate() == 2):
        Engine.turnRight()
    if (ColorRecognition.getPosPlate() == 3):
        Engine.turnLeft()
    if (ColorRecognition.getPosPlate() == 4):
        Engine.turnLeft()
        Engine.turnLeft()
    Engine.solWeight()
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

    # Display.clearDisplay(epd)
    # Display.shutdownDisplay(epd)
    # time.sleep(10)

    # Engine Setup
    Engine.setup()
    Energy.setup()

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
    ColorRecognition.getColors(2, "Screenshot2.png")  # Wieder entfernen
    ColorRecognition.getColors(3, "Screenshot3.png")  # Wieder entfernen
    cube = ColorRecognition.getResult()

    # Bob the builder ONE
    threadEngineOne = threading.Thread(target=workerOne, args=(cube,))
    threadEngineOne.start()

    """ColorRecognition.getColors(2, "Screenshot2.png")   
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
    threadEngineThree.start()"""

    if (ColorRecognition.getPosPlate() == 1):
        DataPreparation.setPos(1, cube[1])
        DataPreparation.setPos(2, cube[2])
        DataPreparation.setPos(3, cube[3])
        DataPreparation.setPos(4, cube[4])
        DataPreparation.setPos(5, cube[5])
        DataPreparation.setPos(6, cube[6])
        DataPreparation.setPos(7, cube[7])
        DataPreparation.setPos(8, cube[8])

    if (ColorRecognition.getPosPlate() == 2):
        DataPreparation.setPos(6, cube[1])
        DataPreparation.setPos(1, cube[2])
        DataPreparation.setPos(4, cube[3])
        DataPreparation.setPos(3, cube[4])
        DataPreparation.setPos(2, cube[5])
        DataPreparation.setPos(5, cube[6])
        DataPreparation.setPos(8, cube[7])
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

    threadEngineOne.join()
    Display.updateDisplay(epd, 10, 30, 'Bob the builder finished!', background, backgroundmodified, font)
    difference = (later - now).total_seconds()
    print(f"Time difference in seconds: {int(difference)}")
    text = str(int(difference)) + " Sekunden"
    Display.updateDisplay(epd, 10, 100, text, background, backgroundmodified, font)

    energy = Energy.Energy()
    text = str(int(energy)) + " Ws"
    Display.updateDisplay(epd, 10, 170, text, background, backgroundmodified, font)
    DataSend.send("https://www.i-ba-pren.flaviowaser.ch/upload-data.php", int(difference), int(energy))

    time.sleep(20)
    Display.drawPicture(epd, 'pic/bob.bmp')
    time.sleep(20)
    Display.clearDisplay(epd)
    Display.shutdownDisplay(epd)
    sys.exit(0)
