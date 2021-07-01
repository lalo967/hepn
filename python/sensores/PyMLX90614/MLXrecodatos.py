import time
import numpy as np
from smbus2 import SMBus
from mlx90614 import MLX90614


#arc=open("/tmp/tem.txt","a")
arc=open ("/home/pi/mnt/drive/tem.txt","a")
def hora():
    ahora = time.strftime("%c")
    print (ahora)
    print ('\n')
    time.sleep(0.005)
    return ahora

def objeto(): #se declara la funcion 
    bus = SMBus(1) #parte de la biblioteca para el sensor
    sensor = MLX90614(bus, address=0x5A)  #parte de la biblioteca para el sensor
    ob=sensor.get_object_1() # el objeto que se ocupa para el sensor lo asignamos a una variable
    float(ob) #hacemos un cast  para hacerlo float y podemos ocuparlo en funciones posteriores 
    print ("TO,",ob) #lo imprimimos
    print ('\n')
    bus.close()  #parte de la biblioteca para el sensor
    time.sleep(0.005)
    return ob #retornamos el valor de ob para poder ocuparlo en otras fucniones 

def ambiente():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    am=sensor.get_ambient()
    float(am)
    print ("TA,",am)
    print ('\n')
    bus.close()
    time.sleep(0.005)
    return am

while True:
    hora()
    #ob = objeto() #asi se llamada a una funcion
    arc.write ("TO")
    arc.write(str(objeto())+ ",") #hacemos otro cast para poder registrarlo en el txt
    am = ambiente
    arc.write("TA")
    arc.write(str(ambiente()) +",")
    arc.write(str(hora())+"," + '\n' )
    time.sleep(1)

arc.close()
#arc.close()
