#lora communication setup
from network import LoRa
import socket

class Lora_raw:

    def __init__(self):
        self.lora = LoRa(mode=LoRa.LORA)
        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    
    def sendText(self, data):
        self.s.setblocking(True)
        self.s.send(data)
        self.s.setblocking(False)
    
    def recText(self, size):
        t = self.s.recv(size)
        return t