from gpiozero import Button
import time

def hello():
	print("hello")

def number():
    i = 1
    while True:
        print(i)
        i += 1


btn = Button(17)
	
 # btn.when_pressed = hello

i = 1
while True:
    if btn.is_pressed:
        print(i)
    i += 1
    time.sleep(0.5)
