from gpiozero import Button
import adb_log
import sys
#sys.path.append("/home/asterix")
# from scripts import test

btn = Button(2)	
# btn.when_pressed = adb_log.logging()
while True:
    if btn.is_pressed:
        adb_log.logging()

# print("\n")
# test.hello()