# shows hello on Sense HAT emulator

from sense_emu import SenseHat
sense = SenseHat()
green = (0,255,0)
red = (255, 0, 0)
blue = (0, 0 ,255)
sense.show_message("Han Bao!", text_colou = green)