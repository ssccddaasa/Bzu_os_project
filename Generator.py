from pros import *
import random
# make Workload file
numPro = int(input("Number of processes: "))
maxArr = int(input("Max arrival time: "))
numCbr = int(input("Max No. of CPU Burst: "))
minIobr = int(input("Min IO burst duration: "))
maxIobr = int(input("Max IO burst duration: "))
minCbr = int(input("Min CPU burst duration: "))
maxCbr = int(input("Max CPU burst duration: "))
Info = []
for i in range(numPro):
    rnum = random.randint(1, numCbr)
    ls = []
    for j in range(rnum-1):
        x1 = random.randint(minIobr, maxIobr)
        x2 = random.randint(minCbr, maxCbr)
        ls.append(x2)
        ls.append(x1)
    x3 = random.randint(minCbr, maxCbr)
    ls.append(x3)
    ar = random.randint(0, maxArr)
    temp = pro(i, ar, ls)
    Info.append(temp)

f = open("Workload.txt","w")
for x in Info:
    f.write(x.toStr()+"\n")