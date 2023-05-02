from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)
# ultrasonic.threshold_distance = 0.5
while True:
    # print(ultrasonic.distance) # smaller the value is, closer the distance is
    ultrasonic.wait_for_in_range() # default range threshold is 0.3m
    print("in range")
    ultrasonic.wait_for_out_of_range()
    print("out oof range")


