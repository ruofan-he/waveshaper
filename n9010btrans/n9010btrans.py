import string
import pyvisa
import numpy as np

# データだけ転送する
class N9010BtransData:
    def __init__(self, visa_address):
        self.visa_address = visa_address
        self.rm = pyvisa.ResourceManager()
        with self.rm.open_resource(self.visa_address) as inst:
            print(inst.query('*IDN?'))

    def transfer(self, channel):
        assert channel in [1,2,3,4,5,6]
        trace = None
        with self.rm.open_resource(self.visa_address) as inst:
            result = inst.query(f"TRAC? TRACE{channel}")
            trace = np.array(list(map(float,result.split(','))))
        return trace

    