#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image, ImageDraw, ImageFont


class Display():

    def __init__(self):
        logging.info("Display init")
        self.__font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 16)
        self.__epd = epd1in54_V2.EPD()
        self.__epd.init(1)
        self.__background = Image.open(os.path.join(picdir, 'background.bmp'))
        self.__epd.displayPartBaseImage(self.__epd.getbuffer(self.__background))

        # epd.init(1) # into partial refresh mode
        self.__draw = ImageDraw.Draw(self.__background)

    def getepd(self):
        return self.__epd

    def clearDisplay(self):
        logging.info("Display clear")
        try:
            self.__epd = epd1in54_V2.EPD()
            self.__epd.init(0)
            self.__epd.Clear(0xFF)
            self.__epd.init(1)
            time.sleep(1)

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.warning("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def drawPicture(self, picture):
        logging.info("Display drawPicture")
        try:
            self.__epd = epd1in54_V2.EPD()
            self.__epd.init(0)
            image = Image.open(os.path.join(picdir, picture))
            self.__epd.display(self.__epd.getbuffer(image))
            time.sleep(15)

        except IOError as e:
            logging.error(e)

        except KeyboardInterrupt:
            logging.warning("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def shutdownDisplay(self):
        logging.info("Display shutdown")
        self.__epd = epd1in54_V2.EPD()
        self.__epd.init(0)
        self.__epd.Clear(0xFF)
        self.__epd.sleep()

    def drawInitialDisplay(self):
        logging.info("Display draw initial display")
        try:
            self.__epd.init(1)
            self.updateDisplay(10, 10, 'PREN TEAM 33')
            # self.updateDisplay(10, 30, 'Initialisierung')
            self.updateDisplay(10, 80, 'Beanspruchte Zeit')
            # self.updateDisplay(10, 100, 'Sekunden')
            self.updateDisplay(10, 150, 'Stromverbrauch')
            # self.updateDisplay(10, 170, 'kW')

        except IOError as e:
            logging.error(e)

        except KeyboardInterrupt:
            logging.warning("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def updateDisplay(self, x, y, text):
        logging.info("Display update: x:" + str(x) + ", y: " + str(y) + ", text: " + str(text))
        try:
            self.__epd.init(1)

            self.__draw.rectangle((x, y, 200, y + 20), fill=0)
            newimage = self.__background.crop([x, y, 200, y + 20])
            self.__background.paste(newimage, (x, y))
            self.__epd.displayPart(self.__epd.getbuffer(self.__background))

            self.__draw.rectangle((x, y, 200, y + 20), fill=(255, 255, 255))
            newimage = self.__background.crop([x, y, 200, y + 20])
            self.__background.paste(newimage, (x, y))
            self.__epd.displayPart(self.__epd.getbuffer(self.__background))

            self.__draw.text((x, y), text, font=self.__font, fill=0)
            newimage = self.__background.crop([x, y, 200, y + 20])

            self.__background.paste(newimage, (x, y))
            self.__epd.displayPart(self.__epd.getbuffer(self.__background))

            self.__background.save("background_modified.png")

        except IOError as e:
            logging.error(e)

        except KeyboardInterrupt:
            logging.warning("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def loop(self):
        self.drawPicture('qrcode.bmp')
        self.clearDisplay()
