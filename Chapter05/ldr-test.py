from gpiozero import LightSensor
from time import sleep

LDR_PIN = 18

sensor = LightSensor(LDR_PIN)

while True:
    light_value = int(sensor.value*10)+1
    print ("Value is "+str(light_value))
    sleep(1)