from data.Datasend import Datasend
from data.Dataverify import Dataverify
from display.display import Display

class main:

    def __init__(self):
        self.__datasend = Datasend("https://i-ba-pren.flaviowaser.ch/upload-data.php")
        self.__dataverify = Dataverify("http://18.192.48.168:5000/cubes/", "team33")
        self.__display = Display()

    def start(self):
        if(self.__dataverify.checkavailability()):



    def running(self):

    def completing(self):


    def end(self, energy, time):
        self.__datasend.send(energy, time)
