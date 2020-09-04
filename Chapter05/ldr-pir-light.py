from gpiozero import LightSensor, LED, MotionSensor
from time import sleep

LDR_PIN = 18
LED_PIN = 22
PIR_SENSOR_PIN = 4
DELAY = 5

light_threshold = 5

sensor = LightSensor(LDR_PIN)
led = LED(LED_PIN)
pir = MotionSensor(PIR_SENSOR_PIN)

while True:
    light_value = int(sensor.value*10)+1
    if light_value < light_threshold and pir.motion_detected:
        led.on()
    else:
        led.off()
    print ("Light value is "+str(light_value) + " Motion " + str(pir.motion_detected) )
    sleep(DELAY)