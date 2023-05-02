import os

def write_txt():
    file = open("./" + "test.txt", "w")
    file.write("the program is running")
    file.close()

def hello():
    print("hello")
