#!/usr/bin/python3
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(25, 6)

while True:
    print('Distance is ' + str(sensor.distance) + 'm')
    sleep(1)
