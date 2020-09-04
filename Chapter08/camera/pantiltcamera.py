#!/usr/bin/python3
from gpiozero import Servo
from time import sleep
import sys
import pantilthat
from bottle import Bottle, route, request, response, template, static_file

app = Bottle()

STEP_SIZE = 5

# Change IPADDRESS if access is required from another computer
IPADDRESS = '0.0.0.0'
# Where the files are stored
DOCUMENT_ROOT = '/home/pi/camera'

#Setup lights as NeoPixels
pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)


# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")

@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT+"/public")

@app.route ('/move')
def move_motor():
    getvar_dict = request.query.decode()
    pantilt = request.query.pantilt
    direction = int(request.query.direction)

    if pantilt == "pan":
        pan_value = pantilthat.get_pan()
        if direction == -1:
            if pan_value - STEP_SIZE >= -90:
                pantilthat.pan (pan_value - STEP_SIZE)
                return ("Pan right")
            else:
                return ("Pan right limit reached")
        elif direction == 1:
            if pan_value + STEP_SIZE <= 90:
                pantilthat.pan (pan_value + STEP_SIZE)
                return ("Pan left")
            else:
                return ("Pan left limit reached")
        else:
            return ("Invalid direction")
    elif pantilt == "tilt":
        tilt_value = pantilthat.get_tilt()
        if direction == -1:
            if tilt_value - STEP_SIZE >= -90:
                pantilthat.tilt (tilt_value - STEP_SIZE)
                return ("Tilt up")
            else:
                return ("Tilt up limit reached")
        elif direction == 1:
            if tilt_value + STEP_SIZE <= 90:
                pantilthat.tilt (tilt_value + STEP_SIZE)
                return ("Tilt down")
            else:
                return ("Tilt down limit reached")
        else:
            return ("Invalid direction")
    else:
        return ("Invalid command")


@app.route ('/light')
def set_light():
    getvar_dict = request.query.decode()
    set = request.query.set
    if (set == "on"):
        pantilthat.set_all(0,0,0,255)
        pantilthat.show()
        return ("Light On")
    else:
        pantilthat.clear()
        pantilthat.show()
        return ("Light Off")

app.run(host=IPADDRESS)