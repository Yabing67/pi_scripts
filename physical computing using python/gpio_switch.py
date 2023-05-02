# a single press and release on the button would
# change the LED state from off to on or on to off
from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

while True:
    button.wait_for_press()
    led.toggle()  # toggle the sate of LED
    sleep(0.5)