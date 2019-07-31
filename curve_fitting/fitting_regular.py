import numpy as np
import sys
import matplotlib.pyplot as plt
import random

M =10 
data = []

with open('temp1', 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        data.append(int(lines)) 
        
plt.plot(range(len(data)), data, label="2", color="red", linewidth = 1, linestyle = '-')
        

def fit(T, M, startIdx):
    N = len(T)
    X = np.zeros((N, M + 1))
    Tmat = np.mat(T)
    
    for i in range(N):
        for j in range(M + 1):
            if j == 0:
                X[i][j] = 1 
            else:
                X[i][j] = i**j 
    Xmat = np.mat(X)
    
    lamda=0
    tempMat = lamda*np.eye(M+1)
    tempMat[0][0]=0
    W = (Xmat.T * Xmat + tempMat).I * Xmat.T * Tmat.T
    Wa = W.getA()
    print Wa
    
    pltY1 = []
    for i in range(N):
        temp = 0
        for j in range(M + 1):
            temp += Wa[j][0]*(i**j)
        pltY1.append(temp)
    
    print sum(pltY1)-sum(T)
    plt.plot([k+startIdx for k in range(N)], pltY1, label="1", color="green", linewidth = 1, linestyle = '-')

    last1 = 0
    last2 = 0
    for i in range(N*10):
        temp = 0
        for j in range(1, M):
            temp += j*Wa[j][0]*((i*0.1)**(j-1))
        if last1 !=0 and last2 !=0 and (last2 > last1 and last2 > temp or last2 < last1  and last2 < temp):
            jizhiX=0.1*(i-1)+startIdx 
            plt.plot([jizhiX, jizhiX], [0, 400], label="1", color="green", linewidth = 1, linestyle = '-')
        last1=last2      
        last2=temp


start=0
hours = int(len(data) / 4)
for hour in range(0, hours-5, 6):
    start = 4*hour
    end = start+24
    fit(data[start:end], M, start)

plt.xlabel("time(15min)")
plt.ylabel("flow(pcu)")
plt.title("fit")
plt.show()
