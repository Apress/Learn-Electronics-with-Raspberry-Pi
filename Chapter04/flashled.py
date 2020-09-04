from gpiozero import LED
from time import sleep

LED_PIN = 22

led = LED(LED_PIN)

print ("on")
led.on()
sleep(1)
print ("off")
led.off()
sleep(1)
print ("on")
led.on()
sleep(1)
print ("off")
led.off()
sleep(1)