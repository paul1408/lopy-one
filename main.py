#main code
import machine
import time
from acc import Sensor_acc
from lora_raw import Lora_raw
#variables
nodes_nr = 0
_MAX_NODES = 1
nodes = list()

#init board and sensors
accel = Sensor_acc()
uart.write('Acc setup OK')
lora_net = Lora_raw(id)
uart.write('Lora-gateway setup OK')

#wait for nodes broadcast
while (nodes_nr < _MAX_NODES):
    node_id = lora_net.recv_msg()
    if not node_id == ''
        nodes.append()
        nodes_nr += 1

#listing nodes
uart.write("Network node(s): ")
uart.write(nodes)
#receive
    while True:
        msg = lora_net.recv_msg()
        if not msg = ''
        uart.write(msg)    