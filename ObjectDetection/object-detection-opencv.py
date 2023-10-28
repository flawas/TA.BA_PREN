import colorama
import cv2

RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
YELLOW = colorama.Fore.YELLOW

cap = cv2.VideoCapture('*/train/3D-Builder-Example.mp4')

state = {
    '1': [' '],
    '2': [' '],
    '3': [' '],
    '4': [' '],
    '5': [' '],
    '6': [' ']
    '7': [' '],
    '8': [' ']
}

sign_color = {'red': 'red', 'blue': 'blue', 'yellow': 'yellow'}

color = {'red': (255, 0, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0)}

https: // www.youtube.com / watch?v = T0dBCUWh7Fg
min6
.58


def color_detect(h, s, v):
    if h < 5 and s > 5:
        return 'red'
    elif h= < 25 and h > 10:
        return 'yellow'
    elif h <= 100 and s > 70:


def draw_stickers(frame, stickers, name):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)


def draw_preview_stickers(frame, stickers):
    stick = ['front', 'back']
    for name in stick:
        for x, y in stick:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)


def fill_stickers(frame, stickers, sides):
    for side, colors in sides.item():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), color[colors[num]], 1)
