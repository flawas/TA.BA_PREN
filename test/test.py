#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 16)

epd = epd1in54_V2.EPD()
epd.init(1)

background = Image.open(os.path.join(picdir, 'background.bmp'))
epd.displayPartBaseImage(epd.getbuffer(background))

# epd.init(1) # into partial refresh mode
draw = ImageDraw.Draw(background)


def clearDisplay():
    try:
        epd = epd1in54_V2.EPD()
        epd.init(0)
        epd.Clear(0xFF)
        epd.init(1)
        time.sleep(1)
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()


def drawPicture(picture):
    try:
        epd = epd1in54_V2.EPD()
        epd.init(0)
        image = Image.open(os.path.join(picdir, picture))
        epd.display(epd.getbuffer(image))
        time.sleep(15)

    except IOError as e:
        logging.info(e)


    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()


def shutdownDisplay():
    epd = epd1in54_V2.EPD()
    epd.init(0)
    epd.Clear(0xFF)
    logging.info("Display Goto Sleep...")
    epd.sleep()


def drawInitialDisplay():
    try:
        updateDisplay(10, 10, 'PREN TEAM 33')
        updateDisplay(10, 30, 'Ready')
        updateDisplay(10, 80, 'Beanspruchte Zeit')
        updateDisplay(10, 100, 'Sekunden')
        updateDisplay(10, 150, 'Stromverbrauch')
        updateDisplay(10, 170, 'kW')


    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()


def updateDisplay(x, y, text):
    try:
        epd.init(1)

        draw.rectangle((x, y, 200, y + 20), fill=0)
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        draw.rectangle((x, y, 200, y + 20), fill=(255, 255, 255))
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        draw.text((x, y), text, font=font, fill=0)
        newimage = background.crop([x, y, 200, y + 20])

        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        background.save("background_modified.png")


    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()


def loop():
    drawPicture('qrcode.bmp')
    clearDisplay()
    shutdownDisplay()


def start():
    drawInitialDisplay()


clearDisplay()
drawInitialDisplay()
