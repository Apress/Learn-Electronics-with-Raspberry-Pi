#!/usr/bin/python3
# Set the pixels back to off


from rpi_ws281x import PixelStrip, Color
import time

LEDCOUNT = 2       # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True       # Invert required when using inverting buffer
BRIGHTNESS = 255


strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

# First LED white
strip.setPixelColor(0, Color(0,0,0))
strip.setPixelColor(1, Color(0,0,0))
strip.show()
