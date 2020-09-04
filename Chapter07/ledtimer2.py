#!/usr/bin/python3
from gpiozero import LED
from time import sleep
import sys

# Time to keep the light on in seconds
DEFAULT_DELAY = 30

# GPIO port numbers for the LED
LED_PIN = 4

if len(sys.argv) > 1:
    try:
        delay = int (sys.argv[1])
    except:
        print ("Invalid argument. The argument must be a number.")
        exit (0)

    if delay < 1 :
        print ("Invalid number. The argument must be a positive number.")
        exit (0)
else:
    delay = DEFAULT_DELAY

led = LED(LED_PIN)

while True:
    input_text = input("Press enter to turn the light on for "+str(delay)+" seconds")
    if input_text == "q":
        exit(0)
    led.on()
    sleep(delay)
    led.off()