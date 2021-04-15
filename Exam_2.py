import math
import sys


def calcDist(x1,y1,x2,y2): 
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist 


def compute_distances(aData,bData,dData):
    count = 0
    counter = 0
    for i in aData:
        count = count + 1
        counter = 0
        storDist = 999999999999
        storX2 = 0
        storY2 = 0

        cut=i.split(',')
        x1=cut[0]
        y1=cut[1]

        x1 = float(x1)
        y1 = float(y1)

        #print ('X1:  ' + str(x1) + '  Y1:  ' + str(y1))

        for j in bData:
            counter = counter + 1
            snip=j.split(',')
            x2=snip[0]
            y2=snip[1]

            x2 = float(x2)
            y2 = float(y2)

            #print ('X2:  ' + str(x2) + '  Y2:  ' + str(y2))

            dist = calcDist(x1,y1,x2,y2)
            #print (dist)

            if dist < storDist:
                storDist = dist
                storCount = counter - 1

        finalLine = 'The closest point to A[' + str(count).rstrip() + '] is point B[' + str(storCount).rstrip() + ']  Distance = ' + str(storDist) + '\n'
        D.append(finalLine)
        

# I'm still going to attempt the read_data function on my own but I think it's stupid for this use case


A = []
B = []
D = []
theList = []


def read_data(filename):
    with open(filename) as f:
        theList = f.readlines()
    return theList


A = read_data(sys.argv[1])
B = read_data(sys.argv[2])

compute_distances(A,B,D)

for k in D:
    print(k)
