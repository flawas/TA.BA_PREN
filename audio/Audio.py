from playsound import playsound
import logging
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

class Audio:
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    def __init__(self, soundfile):
        logging.info("Audio init")
        self.__soundfile = soundfile
        logging.info(libdir + "/" + self.__soundfile)


    def playaudio(self):
        logging.info("Audio playaudio" + str(self.__soundfile))
        playsound(str(libdir + "/" + self.__soundfile))