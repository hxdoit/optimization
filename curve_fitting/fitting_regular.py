import numpy as np
import sys,math
import matplotlib.pyplot as plt
import random

M =10 
data = []
candidate=[]

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
    for i in range(N*100):
        temp = 0
        for j in range(M + 1):
            temp += Wa[j][0]*((i*0.01)**j)
        pltY1.append(temp)
    
    print sum(pltY1)-sum(T)
    plt.plot([k*0.01+startIdx for k in range(N*100)], pltY1, label="1", color="green", linewidth = 1, linestyle = '-')

    XX=[]
    YY=[]
    last1 = 0
    last2 = 0
    for i in range(N*100):
        jizhiX=0.01*(i-1)+startIdx 
        XX.append(jizhiX)
        temp = 0
        for j in range(1, M+1):
            temp += j*Wa[j][0]*((i*0.01)**(j-1))
        YY.append(abs(temp))
        if last1 !=0 and last2 !=0 and (last2 > last1 and last2 > temp or last2 < last1  and last2 < temp):
            plt.plot([jizhiX, jizhiX], [200, 400], label="1", color="green", linewidth = 1, linestyle = '-')
            candidate.append([jizhiX, abs(temp)])
        last1=last2      
        last2=temp
    plt.plot(XX,YY, label="1", color="green", linewidth = 1, linestyle = '-')


start=0
hours = int(len(data) / 4)
for hour in range(0, hours-5, 6):
    start = 4*hour
    end = start+24
    fit(data[start:end], M, start)

candidate.sort(key=lambda x:x[1], reverse=True)
print candidate
for mm in range(7):
    plt.plot([candidate[mm][0],  candidate[mm][0]],[0, 200], label="1", color="blue", linewidth = 1, linestyle = '-')
plt.xlabel("time(15min)")
plt.ylabel("flow(pcu)")
plt.title("fit")
plt.show()
