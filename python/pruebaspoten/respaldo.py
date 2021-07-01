import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)

b_pin = 21
a_pin = 20

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
    count = 0
    while not GPIO.input(b_pin):
        count = count +1
    return count


def charge_timea():
    GPIO.setup(a_pin, GPIO.IN)
    counta = 0
    while not GPIO.input(a_pin):
        counta = counta +1
    return counta

def analog_read():
    discharge()
    return charge_time()

def analog_reada():
    dischargea()
    return charge_timea()


while True:
    print(analog_read())
    print("")
    print(analog_reada())
    time.sleep(1)

a = [analog_read()]
b = np.array(a).reshape(())
np.savetxt('datos.txt',b,fmt='%d')
