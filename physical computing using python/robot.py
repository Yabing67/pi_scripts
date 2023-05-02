from gpiozero import Robot

# robot with two wheels and control the two motors together rather than separately

robot = Robot((4,14), (17,27)) # pin numbers for two motors
# or robot = Robot(left = (4,14), right = (17,27))

robot.forward() # both motors should be driving forwards
robot.backward()
robot.forward(0.5)

robot.right() # left wheel go forward and right wheel go backward
robot.left()
robot.stop()