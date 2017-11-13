from LIS2HH12 import LIS2HH12
from pysense import Pysense


def init_acc():
    py = Pysense()
    accel = LIS2HH12()

def getacc():
    return LIS2HH12.acceleration()
