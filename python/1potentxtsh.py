
import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setmode(GPIO.BCM)

b_pin = 21

arc=open("while.txt","w")
def discharge():
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    count=[]
    a=0
    while not GPIO.input(b_pin):
        a=a+1
        count.append(a)
        b=[]
        b.append(count)
    return a

def analog_read():
    discharge()
    return charge_time()

while True:
    print(analog_read())
    arc.write(str(analog_read()))
    arc.write(", ") 
    print("")
    time.sleep(1)

arc.close()
