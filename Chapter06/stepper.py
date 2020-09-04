from gpiozero import DigitalOutputDevice
from time import sleep

motor_pins = [DigitalOutputDevice (17), DigitalOutputDevice (23), DigitalOutputDevice (18), DigitalOutputDevice (22)]

motor_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

while True:
    for seq_num in range (len(motor_seq)):
        for motor_pin in range (0,4):
            if motor_seq[seq_num][motor_pin] == 1:
                motor_pins[motor_pin].on()
            else:
                motor_pins[motor_pin].off()
        sleep(0.001)