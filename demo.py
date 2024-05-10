import time

from PREN_flawas import DataPreparation, DataVerify, Engine

Engine.setup()

while True:
    int = 0

    while int < 5:
        Engine.solRed()
        Engine.solBlue()
        Engine.solYellow()

    int = 0
    time.sleep(15)