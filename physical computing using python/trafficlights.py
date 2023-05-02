from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

# three GPIO pin numbers one for each pin: red, amber,green
lights = TrafficLights(25, 8, 7)
button = Button(2)
buzzer = Buzzer(15)
# button for pedestrain crossing
button_ped = Button(17)

# trafficlights interface is similar to that individual LED,
# you can use on, off and blink, all of whic control all three lights at once
# you can also control each LED individually
# Buzzer works exactly like LED
while True:
    button.wait_for_press()
    lights.green.on()
    button_ped.wait_for_press()
    sleep(2)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    buzzer.on() # indicate it´s safe to cross
    sleep(5) # time to cross
    lights.amber.on()
    sleep(1)
    button.wait_for_press()
    buzzer.off()
    lights.green.on()
    sleep(1)
    lights.off()