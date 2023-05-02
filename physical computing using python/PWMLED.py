from gpiozero import PWMLED
# control the brightness of an LED using PWM, or pulse-width modulation
from gpiozero import MCP3008

pot = MCP3008(0)
led = PWMLED(21)

def PWMLED_bright():
    led.source = pot.values # using analogue signal to control the light brightness
# or the following loop is equivalent
# while True:
#     led.value = pot.value

# cange the blink times according to potentiometer values
pot2 = MCP3008(1)
def PWMLED_blink():
    while True:
        led.blink(on_time=pot.value, off_time=pot2.value, n=1, backgroung=False)

def PWMLED_fade():
    while True:
        led.pulse(fade_in_time=pot.value, fade_out_time=pot2.value, n=1, backgroung=False)