#main code
import machine
import time
from acc import Sensor_acc
from lora_raw import Lora_raw


accel = Sensor_acc()
print('Acc setup')
#lora_net = Lora_raw()
#print('Lora setup')
func = input('Device type(s/n):')

#read from UART
while True:
    acc_all = accel.getacc()
    print('Acc: {}'.format(acc_all))
    time.sleep_ms(500)