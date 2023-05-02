# when you push the button the LED should come one for 3 seconds
from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

button.wait_for_press()
led.on()
sleep(3)
led.off()