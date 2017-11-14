#lora communication setup
from network import LoRa
import socket

class Lora_raw:

    def __init__(self):
        self.lora = LoRa(mode=LoRa.LORA)
        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    