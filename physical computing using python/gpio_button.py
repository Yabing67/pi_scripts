from gpiozero import Button

button = Button(2)
def press_btn1():
    button.wait_for_press()
    print("You pushed me")

def press_btn2():
    while True:
        if button.is_pressed:
            print("Hello")
        else:
            print("Goodbye")

# rather than continuously printing one or the other,
# it only does it once per press
def press_btn3():
    while True:
        button.wait_for_press()
        print("Pressed")
        button.wait_for_release()
        print("Released")