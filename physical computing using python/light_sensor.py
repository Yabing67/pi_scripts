from gpiozero import LightSensor, Buzzer

# show how strong the light is
ldr = LightSensor(4) # alter if using a different pin
while True:
    print(ldr.value)