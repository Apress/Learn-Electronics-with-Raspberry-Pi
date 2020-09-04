from gpiozero import Button
from time import sleep

button_pins = {
    'JoyNorth' : 23,
    'JoyEast' : 17,
    'JoySouth' : 4,
    'JoyWest' : 25,
    'RedSwitch' : 22,
    'BlueSwitch' : 11,
    'WhiteSwitch' : 9,
    'GreenSwitch' : 18,
    'BlackSwitch' : 24,
    'BigButton' : 10
    }

buttons = {}

for button_name, gpio_num in button_pins.items():
    buttons[button_name] = Button (gpio_num)

while True:
    for button_name, this_button in buttons.items():
        if (this_button.is_pressed):
            print ("Button {} is pressed".format(button_name))
    sleep(0.2)
