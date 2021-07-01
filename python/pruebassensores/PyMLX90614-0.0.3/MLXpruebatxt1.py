import time
import numpy as np
from smbus2 import SMBus
from mlx90614 import MLX90614

arc=open("temperatura.txt","a")
def hora():
    ahora = time.strftime("%c")
    print (ahora)
    time.sleep(1)
    return (ahora)

def mlx(sensor):
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    bus.close()
    time.sleep(0.005)
    return (bus, sensor)

def objeto(ob):
    ob=sensor.get_object_1()
    print ("el obejto tiene de temperatura",ob)
    return (ob)


def ambiente(sensor):
    am=sensor.get_ambient()
    print ("el ambiente tiene de temperatura",am)
    return (am)


while True:
    hora()
    objeto()
    ambiente()
    arc.write(str(hora()) + '\n' + '\t')
    arc.write(str(mlx()))
    time.sleep(1)

arc.close()
