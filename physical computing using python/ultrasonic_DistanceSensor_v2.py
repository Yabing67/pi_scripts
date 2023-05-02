from gpiozero import DistanceSensor

def hello():
    print("Hello")

ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.thresgold_distance = 0.5
ultrasonic.when_in_range = hello
# defalut maximum is 1 meter

# it can be set through property max_distance
def bye():
    print("Bye")
ultrasonic.when_out_of_range = bye