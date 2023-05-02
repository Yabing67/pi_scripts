from gpiozero import Motor
from time import sleep

# create the instance using the pin numbers
motor1 = Motor(4, 14) # or Motor(forward = 4, backward = 14)
motor2 = Motor(17, 27)

motor1.forward(0.5) # drive with half speed
motor2.backward(0.5)
while True:
    sleep(5)
    motor1.reverse() # reverse the motor´s direction
    motor2.reverse()
