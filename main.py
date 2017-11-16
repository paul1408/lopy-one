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
uart.write('Acc setup OK\n')
lora_net = Lora_node(id)
uart.write('Lora-node setup OK\n')

#wait for gateway to ack
uart.write('Broadcasting node %d\n' % id)
while waitingFoRGate:
    waitingFoRGate = not lora_net.send_msg('%d' % id)
    time.delay(1)
#transmit
    while True:
        lora_net.send_msg('LoPy_%d' % id)
        uart.write('LoPy_%d\n  ' % id)
        time.delay_ms(200)