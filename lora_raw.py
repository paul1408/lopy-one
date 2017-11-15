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

    _DEVICE_ID = 0x01
    _STATUS_OK = 100
    _LORA_ACK_SIZE = 3
    _MAX_ACK_TIME = 1000
    _RETRY_COUNT = 3


    def __init__(self, id):
        self.lora = LoRa(mode=LoRa.LORA, tx_iq = True)
        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self._DEVICE_ID = id

    def check_ack_time(self, start_t):
        current_t = time.ticks_ms()
        return (current_t - start_t < _MAX_ACK_TIME)

    def send_msg(self, msg):
        retry = _RETRY_COUNT
        while (retry > 0):
            retry -= 1
            pkg = struct.pack(_LORA_PKG_FORMAT % len(msg), 
                                _DEVICE_ID, len(msg), msg)
            self.s.send(pkg)

            start_time = time.ticks_ms()
            while(check_ack_time):
                recv_ack = self.s.recv(256)
                if (len(recv_ack) == 3):
                    dev_id, pkg_len, status = struct.unpack(_LORA_PKG_ACK_FORMAT, recv_ack)
                    if(dev_id == _DEVICE_ID and r_msg_id == msg_id and status == _STATUS_OK):
                        return True
                    else:
                        return False