from gpiozero import DigitalOutputDevice
from time import sleep

serial_pin = 22
serial_clock_pin = 23
register_clock_pin = 24

serial_out = DigitalOutputDevice(serial_pin)
serial_clock = DigitalOutputDevice(serial_clock_pin)
register_clock = DigitalOutputDevice(register_clock_pin)

number_values = [0b11111100,0b01100000, 0b11011010, 0b11110010, 0b01100110, 0b10110110, 0b10111110, 0b11100000, 0b11111110, 0b11110110]

def shift_bit (bit_value):
    serial_out.value = bit_value
    serial_clock.on()
    sleep (0.001)
    serial_clock.off()

def register_update ():
    register_clock.on()
    sleep (0.001)
    register_clock.off()

def shift_byte (byte_value, update=True):
    # shift data 1 bit at a time
    for i in range (0,8):
        # shift out 1 bit
        bit_value = byte_value & 0b00000001
        shift_bit (bit_value)
        byte_value >>= 1
    if update == True:
        register_update ()



shift_byte (number_values[2], False)
shift_byte (number_values[4], True)