import numpy as np
import matplotlib.pyplot as plt
import random

M = 10 
T = []

with open('temp1', 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        T.append(int(lines)) 
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

lamda=0.9
W = (Xmat.T * Xmat + lamda*np.eye(M+1)).I * Xmat.T * Tmat.T
Wa = W.getA()
print Wa

pltY1 = []
for i in range(N):
    temp = 0
    for j in range(M + 1):
        temp += Wa[j][0]*(i**j)
    pltY1.append(temp)

print sum(pltY1)-sum(T)

pltY2 = []
for i in range(N):
    temp = 0
    for j in range(1, M + 1):
        temp += j*Wa[j][0]*(i**(j-1))
    pltY2.append(temp)

#plt.plot(range(N), pltY1, label="1", color="green", linewidth = 1, linestyle = '-')
plt.plot(range(N), pltY2, label="1", color="green", linewidth = 1, linestyle = '-')
#plt.plot(range(N), T, label="2", color="red", linewidth = 1, linestyle = '-')
plt.xlabel("time(s)")
plt.ylabel("distance(m)")
plt.title("multiband")
plt.show()
