from gpiozero import Motor, Button
from time import sleep

# GPIO numbers for motor
MOTOR_PIN_FWD = 17
MOTOR_PIN_REV = 18
# GPIO pin for reed switch
REED_PIN = 4

# max speed to reduce top speed
# maximum value is 1
MAX_SPEED = 0.9
# How long to wait between speed increases
ACC_DELAY = 0.5
# How long to wait at the station
STATION_DELAY = 10

m1 = Motor (MOTOR_PIN_FWD, MOTOR_PIN_REV)
reed_switch = Button (REED_PIN)

# Go from stop to max speed
def train_speed_up (max_speed):
    speed = 0
    while speed < max_speed:
        speed += 0.1
        m1.forward(speed)
        sleep(ACC_DELAY)

def train_slow_down (current_speed):
    speed = current_speed
    while speed > 0:
        speed -= 1
        m1.forward(speed)
        sleep(ACC_DELAY)


while True:
    print ("Leaving the station")
    # Accelerate up to full speed
    train_speed_up(MAX_SPEED)
    # wait until it triggers reed switch
    print ("Going to station")
    reed_switch.wait_for_press()
    print ("Stopping at station")
    train_slow_down(MAX_SPEED)
    sleep(STATION_DELAY)