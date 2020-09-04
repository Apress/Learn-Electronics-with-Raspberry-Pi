#!/usr/bin/python3
from gpiozero import Button
import picamera
import os

# PIR sensor on GPIO pin 4
BUTTON_PIN = 10

image_dir = '/home/pi/film/'

# Create pir and camera objects
button = Button(BUTTON_PIN)
camera = picamera.PiCamera(resolution=(720,576))
camera.hflip=True
camera.vflip=True

image_number = 1

while True:
    filename = "{}frame{:03d}.jpg".format(image_dir, image_number)
    # Loop to ensure that filename is unique
    while os.path.isfile(filename):
        image_number += 1
        filename = "{}frame{:03d}.jpg".format(image_dir, image_number)
    camera.start_preview()
    button.wait_for_press()
    print ("Taking photo {}".format(image_number))
    camera.capture(filename)
    image_number += 1