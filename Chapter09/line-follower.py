#!/usr/bin/python3
from gpiozero import Robot, LineSensor
from time import sleep

sensor_left = LineSensor(22)
sensor_center = LineSensor(23)
sensor_right = LineSensor(24)

# Pin numbers
# CamJam 10,9 - 8,7
# STS-Pi 19,20 - 21,26
# pins reversed as this robot goes the opposite direction
robot = Robot(right=(7, 8), left=(9, 10))


current_direction = "forward"
# speed is as a percentage (ie. 100 = top speed)
# start speed is 50% which is fairly slow on a flat surface
speed = 20

while True:
    # Convert speed from percentage to float (0 to 1)
    float_speed = speed / 100
    
    # Center detected - go forward
    if sensor_center.value == 1:
        robot.forward(float_speed)
    # Otherwise see if too far left or right
    if sensor_left.value == 1:
        robot.right(float_speed)
    elif sensor_right.value == 1:
        robot.left(float_speed)
    # Otherwise drive forward
    else:
        robot.forward(float_speed)
