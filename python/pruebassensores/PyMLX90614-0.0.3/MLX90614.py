from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print (sensor.get_ambient())
print (sensor.get_object_1())
bus.close()
