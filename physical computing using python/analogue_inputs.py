from gpiozero import MCP3008

pot = MCP3008(0) # an object representing your analogue device
# 0 represents the ADC channel 0, there are 8 channels, 0-7
while True:
    print(pot.value)