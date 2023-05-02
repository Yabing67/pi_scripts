import os
import time

def logging():
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    name = "log_" + now

    os.system("adb connect 172.16.250.248:5555")
    print("adb logging started")
    os.system("adb logcat -b all> " + "./" + name + ".txt")
    print("adb logging finished")

# file = open("/home/yabing/scripts/" + "asterix_test.txt", "w")
# file.write("log is running after booting")
# file.close()