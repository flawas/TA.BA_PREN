#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
class Display:
    def __int__(self):
        self.picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
        self.libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

        if os.path.exists(self.libdir):
            sys.path.append(self.libdir)

        logging.basicConfig(level=logging.DEBUG)
        self.font = ImageFont.truetype(os.path.join(self.picdir, 'Font.ttc'), 16)

        self.epd = epd1in54_V2.EPD()
        self.epd.init(1)

        self.background = Image.open(os.path.join(self.picdir, 'background.bmp'))
        self.epd.displayPartBaseImage(self.epd.getbuffer(self.background))

        # epd.init(1) # into partial refresh mode
        self.draw = ImageDraw.Draw(self.background)

    def clearDisplay(self):
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

    def drawPicture(self, picture):
        try:
            epd = epd1in54_V2.EPD()
            epd.init(0)
            image = Image.open(os.path.join(self.picdir, picture))
            epd.display(epd.getbuffer(image))
            time.sleep(15)

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()
    def shutdownDisplay(self):

        self.epd.init(0)
        self.epd.Clear(0xFF)
        logging.info("Display Goto Sleep...")
        self.epd.sleep()

    def drawInitialDisplay(self):
        try:
            self.draw.rectangle((10, 10, 120, 30))
            self.draw.text((10, 10), 'PREN TEAM 33', font = font, fill = 0)

            self.draw.rectangle((10, 30, 120, 30))
            self.draw.text((10, 30), 'Ready', font = font, fill = 0)

            self.draw.rectangle((10, 80, 120, 30))
            self.draw.text((10, 80), 'Beanspruchte Zeit', font = font, fill = 0)

            self.draw.rectangle((10, 100, 120, 30))
            self.draw.text((10, 100), 'Sekunden', font = font, fill = 0)

            self.draw.rectangle((10, 150, 120, 30))
            self.draw.text((10, 150), 'Stromverbrauch', font = font, fill = 0)

            self.draw.rectangle((10, 170, 120, 30))
            self.draw.text((10, 170), 'kW', font = font, fill = 0)

            newimage = self.background.crop([10, 10, 120, 30])
            self.background.paste(newimage, (10, 10))
            newimage = self.background.crop([10, 30, 120, 30])
            self.background.paste(newimage, (10, 30))
            newimage = self.background.crop([10, 80, 120, 30])
            self.background.paste(newimage, (10, 80))
            newimage = self.background.crop([10, 100, 120, 30])
            self.background.paste(newimage, (10, 100))
            newimage = self.background.crop([10, 150, 120, 30])
            self.background.paste(newimage, (10, 150))
            newimage = self.background.crop([10, 170, 120, 30])
            self.background.paste(newimage, (10, 170))
            self.epd.displayPart(self.epd.getbuffer(self.background))
            self.background.save("background_modified.png")

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def updateDisplay(self, x,y,text):
        try:
            self.epd.init(1)

            self.draw.rectangle((x, y, 200, y+20), fill = 0)
            newimage = self.background.crop([x, y, 200, y+20])
            self.background.paste(newimage, (x, y))
            self.epd.displayPart(self.epd.getbuffer(self.background))

            self.draw.rectangle((x, y, 200, y+20), fill = (255, 255, 255))
            newimage = self.background.crop([x, y, 200, y+20])
            self.background.paste(newimage, (x, y))
            self.epd.displayPart(self.epd.getbuffer(self.background))

            self.draw.text((x, y), text, font = font, fill = 0)
            newimage = self.background.crop([x, y, 200, 50])

            self.background.paste(newimage, (x,y))
            self.epd.displayPart(self.epd.getbuffer(self.background))

            self.background.save("background_modified.png")

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd1in54_V2.epdconfig.module_exit()
            exit()

    def loop(self):

        self.drawPicture('qrcode.bmp')
        self.clearDisplay()
        self.shutdownDisplay()

    def start(self):
        self.drawInitialDisplay()