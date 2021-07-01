from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0)
pot1 = MCP3008(channel=1)

while True:
    print("pot:", pot.value)
    print ('\n' + '\t')
    print("pot1:", pot1.value)
    print ('\n' + '\t')
    sleep(0.5)
