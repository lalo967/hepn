from gpiozero import MCP3008
from time import sleep
import numpy as np

pot = MCP3008(channel=0)
pot1 = MCP3008(channel=1)

arc=open("integrado.txt","w")

while True: 
    print(pot.value)
    print(pot1.value) 
    arc.write(str(pot.value) + '\n' ) 
    arc.write(str(pot1.value) )
    arc.write(", ")
    print("") 
    sleep(0.5)

arc.close()
