from gpiozero import Button
from time import sleep

#for i in range(2,27):
#button = Button(7)
#while True:
    #if button.is_pressed:
        #print("Button is Pressed")
    #else:
        #print("Button is Released")
    #sleep(1)

for i in range(2,28):
    button = Button(i)
    button.wait_for_press()
    print("Button was Pressed")
