#!/usr/bin/python3

import pantilthat
from time import sleep

while True:
    # pan from one side to another
    pantilthat.pan(-90)
    sleep (5)
    pantilthat.pan(90)
    sleep (5)
    # pan to the middle
    pantilthat.pan(0)
    sleep (5)
    # tilt up
    pantilthat.tilt(-90)
    sleep (5)
    # tilt down
    pantilthat.tilt(90)
    sleep (5)
    # tilt to center
    pantilthat.tilt(0)
    sleep (5)
