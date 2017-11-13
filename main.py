#main code
from network import LoRa
import socket
import machine
import time
import acc #created module

#setup LoRa network and socket
#lora = LoRa(mode=LoRa.LORA)
#s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

#setup acc
acc.init_acc()

#read from UART
uart.write(acc.getacc)
time.sleep_ms(500)

