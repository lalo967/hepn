import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(4, GPIO.OUT)         #LED output pin
arc=open ("pir.txt","a")

while True:
    i=GPIO.input(17)
    if i==0:                 #When output from motion sensor is LOW
        print "No intruders",i
	arc.write (str(i)+ '\n' + '\t')
        GPIO.output(4, 0)  #Turn OFF LED
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print "Intruder detected",i
        arc.write (str(i)+ '\n' + '\t')
    GPIO.output(4, 1)  #Turn ON LED
    time.sleep(0.1)

arc.close()

