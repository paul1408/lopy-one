#main code
from network import LoRa
import socket
import machine
import time
from acc import Sensor_acc
#setup LoRa network and socket
#lora = LoRa(mode=LoRa.LORA)
#s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

accel = Sensor_acc()

#read from UART
while True:
    acc_all = accel.getacc()
    print('Acc: {}'.format(acc_all))
    time.sleep_ms(500)