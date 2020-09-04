from gpiozero import MCP3008, PWMLED
from time import sleep

adc = MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)

while True:
    print ("{:.0%}".format(adc.value))
    sleep(1)