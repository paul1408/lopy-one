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
uart.write('Board setup OK\r\n')
lora_net = Lora_node(id)
uart.write('Lora-node setup OK\r\n')

#wait for gateway to ack

while waitingFoRGate:
    uart.write('Broadcasting node %d\r\n' % id)
    waitingFoRGate = not lora_net.send_msg('%d' % id)
    time.sleep(1)

#transmit
uart.write('Gateway found\r\n')
while True:
    lora_net.send_msg('LoPy_%d' % id)
    uart.write('LoPy_%d\r\n  ' % id)
    time.sleep(1)