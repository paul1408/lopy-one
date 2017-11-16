#lora communication setup
from network import LoRa
import socket
import time
import struct

class Lora_raw:

    #package header
    # B: 1 byte for the deviceId
    # B: 1 byte for the pkg size
    # %ds: Formated string for string
    _LORA_PKG_FORMAT = "!BB%ds"

    # ack package
    # B: 1 byte for the deviceId
    # B: 1 byte for the pkg size
    # B: 1 byte for the Ok or error messages
    _LORA_PKG_ACK_FORMAT = "!BBB"

    _STATUS_OK = 100
    _LORA_ACK_SIZE = 3


    def __init__(self):
        self.lora = LoRa(mode=LoRa.LORA, rx_iq = True)
        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    def rec_msg(self):
        pkg = self.s.recv(512)
        
        if(len(pkg) > 2):
            pkg_len = pkg[1]
            #unpack
            if(len(pkg) == pkg_len + 2):
                dev_id, pkg_len, msg = struct.unpack(self._LORA_PKG_FORMAT % pkg_len, pkg)
                #acknoledge
                ack = struct.pack(self._LORA_PKG_ACK_FORMAT, dev_id, 1, self._STATUS_OK)
                self.s.send(ack)
                return msg
        m = ''        
        return m