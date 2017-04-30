import time
import os

while True:
    os.system("python2.7 fireDataParser.py -o ../data/userData.csv")
    os.system("python2.7 rangeDetect.py")
    time.sleep(300)

