from gpiozero import Motor
from time import sleep

m1 = Motor (17, 18)
m2 = Motor (23, 22)

m1.forward()
m2.forward()

sleep (1)

m1.stop()
m2.stop()

m1.backward(0.5)
m2.backward(0.5)

sleep (1)

m1.stop()
m2.stop()