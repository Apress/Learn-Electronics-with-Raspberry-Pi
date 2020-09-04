from gpiozero import LED
from time import sleep

# GPIO port numbers for the light
#9 = gnd, 7 = GPIO 4, 11 = GPIO 17, 16 = GPIO 23, 18 = GPIO 24
LED_PINS = [4, 17, 23, 24]
# Time between each step in the sequence in seconds
DELAY = 1

lights = [LED(LED_PINS[0]), LED(LED_PINS[1]), LED(LED_PINS[2]), LED(LED_PINS[3])]


def all_on():
    for x in range (4):
        lights[x].on()

def all_off():
    for x in range (4):
        lights[x].off()

def sequence():
    for x in range (4):
        for y in range (4):
            lights[y].off()
        lights[x].on()
        sleep(DELAY)


def repeat_sequence(num_sequences):
    for x in range (num_sequences):
        sequence()

# Main code starts here
all_off()
sleep(DELAY)
all_on()
sleep(DELAY)
sequence()
sleep(DELAY)
repeat_sequence(6)