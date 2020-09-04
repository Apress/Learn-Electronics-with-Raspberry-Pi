from gpiozero import MotionSensor, LED
from time import sleep

# PIR sensor on GPIO pin 4
PIR_SENSOR_PIN = 4
# Pin for output signal
LED_PIN = 22
# How long to activate the light for
ON_TIME = 5

# Create pir and LED objects
pir = MotionSensor(PIR_SENSOR_PIN)
led = LED(LED_PIN)

while True:
    if (pir.motion_detected == True):
        led.on()
        time.sleep(ON_TIME)
    else:
        led.off()
