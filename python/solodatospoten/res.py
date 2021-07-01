# include RPi libraries in to Python code
import RPi.GPIO as GPIO
import time

# instantiate GPIO as an objec
GPIO.setmode(GPIO.BCM)

b_pin = 21
a_pin = 20

# create discharge function for reading capacitor data
def discharge():
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)


def dischargea():
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, False)
    time.sleep(0.005)

# create time function for capturing analog count value
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


# create analog read function for reading charging and discharging data
def analog_read():
    discharge()
    return charge_time()

def analog_reada():
    dischargea()
    return charge_timea()


# provide a loop to display analog data count value on the screen
while True:
    print(analog_read())
    print("")
    print(analog_reada())
    time.sleep(1)
