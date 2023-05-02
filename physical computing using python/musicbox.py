# when press the button, hear the sound play

from gpiozero import Button
import pygame

pygame.init()

btn = Button(17)

# create a sound object, file need to be in wav format
beat1 = pagame.mixer.Sound("path to wav file")

def btn17():
    print("button 17 pressed")
    beat1.play()
	
btn.when_pressed = hello