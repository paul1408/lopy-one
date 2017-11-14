#main code
import machine
import time
from acc import Sensor_acc
from lora_raw import Lora_raw


accel = Sensor_acc()
print('Acc setup')
lora_net = Lora_raw()
print('Lora setup')
func = 'm' #m - mobile, s - station 
var2 = "Ping"
if func == 'm':
    #broadcast data
    while True:
        time.sleep(2)
        lora_net.sendText(var2)
else:
    while True:
        txt = lora_net.recText(32)
        print('Received: {}'.format(txt))
        if (txt == b'Ping'):
            print('Succesful')