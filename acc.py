#acc from pysense
from LIS2HH12 import LIS2HH12
from pysense import Pysense

class Sensor_acc:

    def __init__(self):
        self.py = Pysense()
        self.sensor = LIS2HH12()

    def getacc(self):
        a = self.sensor.acceleration()
        return a

    def getpitch(self):
        p = self.sensor.pitch()
        return p

    def getroll(roll):
        r = self.sensor.roll()
        return r