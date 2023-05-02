import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
# mode = GPIO.getmode()
# print(mode)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)