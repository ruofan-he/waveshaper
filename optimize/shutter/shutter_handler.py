# 光シャッターのコントロールクラス
import serial
from time import sleep

class servo_shutter:
    def __init__(self, port="COM4", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        #self.setDTR(False)     # DTRを常にLOWにしReset阻止
        self.timeout = 3

    def open(self, shutter_list: list):
        with serial.Serial(self.port, self.baudrate, timeout = self.timeout, dsrdtr=False) as ser:
            buffer = 'open: ' + ' '.join(map(str, shutter_list)) + '\n'
            ser.write(buffer.encode())
    
    def close(self, shutter_list: list):
        with serial.Serial(self.port, self.baudrate, timeout = self.timeout, dsrdtr=False) as ser:
            buffer = 'close: ' + ' '.join(map(str, shutter_list)) + '\n'
            ser.write(buffer.encode())