import cv2
import numpy as np
import argparse
import time
import colorama

RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
YELLOW = colorama.Fore.YELLOW

cap = cv2.VideoCapture('*/train/3D-Builder-Example.mp4')

state = {
    '1':[' '],
    '2':[' '],
    '3':[' '],
    '4':[' '],
    '5':[' '],
    '6':[' ']
    '7':[' '],
    '8':[' ']
}

sign_color = {'red': 'red', 'blue': 'blue', 'yellow': 'yellow'}

color = { 'red': (0,0,255), 'blue': (255,0,0), 'yellow': (0,255,255)}

https://www.youtube.com/watch?v=T0dBCUWh7Fg min6.58