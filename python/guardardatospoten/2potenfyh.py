import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setmode(GPIO.BCM)
ahora = time.strftime("%c")

b_pin = 21
a_pin = 20

arc=open("2po.txt","a")
def discharge():
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)

def dischargea():
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, False)
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

def charge_timea():
    GPIO.setup(a_pin, GPIO.IN)
    counta=[]
    aa=0
    while not GPIO.input(a_pin):
        aa=aa+1
        counta.append(aa)
        ba=[]
        ba.append(counta)
    return aa

def analog_read():
    discharge()
    return charge_time()

def analog_reada():
    dischargea()
    return charge_timea()


while True:
    print(analog_read())
    print(analog_reada())
    arc.write(str(ahora) + '\n' + '\t')
    arc.write(str(analog_read()))
    arc.write(", ")
    arc.write(str(analog_reada()) + '\n')
    print("")
    time.sleep(1)

arc.close()
