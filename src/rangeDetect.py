import csv
import numpy as np

thr = 0.5

def load(path):
    return np.genfromtxt(path, delimiter=",")

def opfile(writeData):
    fp = open(writeData, 'w')
    return fp

def compare(fire, user, thr, fp):
    thr = thr * thr
    ran = fire.shape[0]
    ran2 = user.shape[0]
    invited = np.zeros(ran2)
    for i in range(ran2):
        for j in range(ran):
            pos_fire = fire[j, 0:2]
            pos_user = user[i, 4:6]
            if(np.sum(np.square(pos_fire-pos_user)) < thr):
                fp.write("{:d}.{:d}.{:d}.{:d}\n".format(int(user[i,0]),int(user[i,1]),int(user[i,2]),int(user[i,3])))
                break
        

fireData = './../data/fireData.csv'
userData = './../data/userData.csv'
writeData = './../data/dangerList.csv'

fire = load(fireData)
fire = fire[1:,:]
fire = fire[:, 0:2]

user = load(userData)
fp = opfile(writeData)

compare(fire, user, thr, fp)
