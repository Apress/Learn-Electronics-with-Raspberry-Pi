from gpiozero import MCP3008, PWMLED
from time import sleep

LED_PIN = 18

adc = MCP3008(channel=0)
pwm_led = PWMLED(LED_PIN)

pwm_led.on()


while True:
    print ("{:.0%}".format(adc.value))
    pwm_led.value = adc.value
    sleep(0.2)