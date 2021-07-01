import smbus2
import time
bus = smbus2.SMBus(1)
time.sleep(1) #wait here to avoid 121 IO Error
while True:
        data = bus.read_i2c_block_data(0x04,0x02,4)
        result = 0
        for b in data:
                result = result * 256 + int(b)
        print(result)
        time.sleep(1)
