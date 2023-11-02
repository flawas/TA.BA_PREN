import logging
import os
import pygame

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')


class Audio:
    logging.basicConfig(encoding='utf-8', level=logging.INFO)

    def __init__(self, soundfile):
        logging.info("Audio init")
        self.__soundfile = soundfile
        logging.info("Audio init: " + libdir + "/" + self.__soundfile)

    def playaudio(self):
        logging.info("Audio playaudio: " + str(self.__soundfile))
        pygame.init()
        pygame.mixer.music.load(str(libdir + "/" + self.__soundfile))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue