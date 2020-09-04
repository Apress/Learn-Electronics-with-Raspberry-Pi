from gpiozero import DigitalOutputDevice
from time import sleep

serial_pin = 22
serial_clock_pin = 23
register_clock_pin = 24

serial_out = DigitalOutputDevice(serial_pin)
serial_clock = DigitalOutputDevice(serial_clock_pin)
register_clock = DigitalOutputDevice(register_clock_pin)

def shift_bit (bit_value):
    serial_out.value = bit_value
    serial_clock.on()
    sleep(0.001)
    serial_clock.off()

def register_update ():
    register_clock.on()
    sleep(0.001)
    register_clock.off()

def shift_byte (byte_value):
    # shift data 1 bit at a time
    for i in range (0,8):
        # shift out 1 bit
        bit_value = byte_value & 0b00000001
        shift_bit (bit_value)
        byte_value >>= 1
    register_update ()

def slow_shift_byte (byte_value):
    # shift data 1 bit at a time
    for i in range (0,8):
        # shift out 1 bit
        bit_value = byte_value & 0b00000001
        shift_bit (bit_value)
        byte_value >>= 1
        register_update ()
        sleep(0.5)

print ("Resetting shift register")
shift_byte (0b00000000)
sleep(0.5)

print ("Slow shift to 00000001")
slow_shift_byte (0b00000001)
sleep(2)

print ("Slow shift to 10101011")
slow_shift_byte (0b10101011)
sleep(2)

print ("Shifting in 11001100")
shift_byte (0b11001100)
sleep(1)
print ("Shifting in 00110011")
shift_byte (0b00110011)