#main code
import machine
import time
from acc import Sensor_acc
from lora_node import Lora_node
#variables
waitingFoRGate = True
id = 0x01

#init board and sensors
accel = Sensor_acc()
uart.write('Acc setup OK')
lora_net = Lora_node(id)
uart.write('Lora setup OK')

#wait for gateway to ack
while waitingFoRGate:
    waitingFoRGate = not lora_net.send_msg(id)
    time.delay(1)
#transmit
    while True:
        lora_net.send_msg('LoPy_1')
    