# encoding:utf8
import numpy as np
from sklearn.datasets import make_blobs
from itertools import cycle
import matplotlib.pyplot as plt


def dist(T, i, j):
    total= sum(T[i:j+1])
    average = float(total) / (j - i + 1)
    distance = [(T[k] - average)**2 for k in range(i, j+1)]
    return sum(distance)
    


# read data
T = [0]
with open('data.txt', 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        T.append(int(lines))
N=len(T)
print T

# cal distance matrix
D = np.zeros((N, N))
for i in range(1, N):
    for j in range(i+1, N):
        D[i][j] = dist(T, i,  j)

#divide num clusters
num=5
K = num+1
#lost
L = np.zeros((N, K))
#divide plan
P = np.zeros((N, K))


for i in range(2, N):
    tempL = []
    tempLidx=[]
    for j in range(1, i):
        tempL.append(D[1][j] + D[j+1][i])
        tempLidx.append(j)
    minL = min(tempL)
    minIdx = tempLidx[tempL.index(minL)]
    L[i][2] = minL
    P[i][2] =  minIdx
        
        
for i in range(3, K):
    for j in range(i, N):
        tempL=[]
        tempLidx=[]
        for k in range(i-1, j):
           tempL.append(L[k][i-1] + D[k+1][j])
           tempLidx.append(k)
        minL = min(tempL)
        minIdx = tempLidx[tempL.index(minL)]
        L[j][i] = minL
        P[j][i] =  minIdx
        
    
print L[N-1]

plt.scatter(range(N), T, color='r')

line=N-1
splitIdx=num
while P[line][splitIdx]>0:
    line = int(P[line][splitIdx])
    plt.plot([line, line], [0, 200], label="2", color="green", linewidth = 1, linestyle = '-')
    print line
    print "->"
    splitIdx=splitIdx-1


plt.show()
