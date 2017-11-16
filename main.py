#main code
import machine
import time
from acc import Sensor_acc
from lora_gateway import Lora_gateway
#variables
nodes_nr = 0
_MAX_NODES = 1
nodes = list()

#init board and sensors
accel = Sensor_acc()
uart.write('Acc setup OK \r\n')
lora_net = Lora_()
uart.write('Lora-gateway setup OK\r\n')

#wait for nodes broadcast
while (nodes_nr < _MAX_NODES):
    node_id = lora_net.rec_msg()
    if not node_id == '':
        nodes.append()
        nodes_nr += 1

#listing nodes
uart.write("Network node(s): \r\n")
uart.write(nodes)
#receive
while True:
    msg = lora_net.recv_msg()
    if not msg == '':
        uart.write(msg)    