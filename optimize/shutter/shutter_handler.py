# 光シャッターのコントロールクラス
import serial
from time import sleep

class servo_shutter:
    def __init__(self, port="COM4", baudrate=9600):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = 9600
        self.ser.setDTR(False)     #DTRを常にLOWにしReset阻止
        self.ser.timeout = 3

    def open(self, shutter_list: list):
        with self.ser as ser:
            buffer = 'open: ' + ' '.join(map(str, shutter_list)) + '\n'
            ser.write(buffer.encode())
    
    def close(self, shutter_list: list):
        with self.ser as ser:
            buffer = 'close: ' + ' '.join(map(str, shutter_list)) + '\n'
            ser.write(buffer.encode())

    def read_switch_mode(self):
        with self.ser as ser:
            ser.write(b'read_switch_mode\n')
            result_str = ser.readline().decode().rstrip()
            return list(map(int,result_str.split(' ')))
    
    def read_servo_mode(self):
        with self.ser as ser:
            ser.write(b'read_servo_mode\n')
            result_str = ser.readline().decode().rstrip()
            return list(map(int,result_str.split(' ')))
        
    def set_to_switch(self,target):
        with self.ser as ser:
            buffer = 'set_to_switch:' + ' '.join(list(map(str,target))) + '\n'
            ser.write(buffer.encode())
    
    def read_serial_num(self):
        with self.ser as ser:
            ser.write(b'read_serial_num\n')
            return ser.readline().decode().rstrip()