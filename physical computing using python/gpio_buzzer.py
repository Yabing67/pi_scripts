from gpio import Buzzer
from time import sleep

buzzer = Buzzer(17)  # add a Buzzer object

while True: # Buzzer works exactly like an LED
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

# while True:
#    buzzer.beep()  # works like led blink