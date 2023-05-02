import os
import time

os.chdir("/home/asterix/esoTrace/esoTraceTools-4.3.6/esoTraceTools-4.3.6-cli")

def logging():
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    output_folder = now + ".esotrace"
    print("esotrace logging started")
    # print(os.getcwd())
    os.system("java -jar ./tools/jtracecapture.jar -o " + output_folder + " 172.16.250.248")
    print("esotrace logging finished")

def to_log(input_folder):
    # convert eso trace stream to readable logs
    os.system("java -jar ./tools/jtracedump.jar -o esotrace.log" + input_folder)
    print("converted to readable logs")

if __name__ == "__main__":
    # logging()
    print("current worrking path is: " + os.getcwd())
    input_folder = input("please give the path of your esotrace log: ")
    to_log(input_folder)