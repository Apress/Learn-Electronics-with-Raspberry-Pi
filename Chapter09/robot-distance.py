#!/usr/bin/python3
import time
from gpiozero import Robot, DistanceSensor

# Pin numbres
# CamJam 10,9 - 8,7
# STS-Pi 19,20 - 21,26
robot = Robot(left=(19, 20), right=(21, 26))
distance_sensor = DistanceSensor(25, 6)

min_distance = 0.13
speed = 0.5

while True:
    distance = distance_sensor.distance
    print ("Distance "+str(distance))
    # if we are close to a wall then turn right
    if (distance < min_distance) :
        print ("Too close turning")
        robot.right(speed)
    else :
        robot.forward(speed)
    time.sleep(1)
