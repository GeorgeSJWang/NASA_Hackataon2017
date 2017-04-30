import time
import os

while True:
    os.system("python fireDataParser.py")
    os.system("python rangeDetect.py")
    time.sleep(300)

