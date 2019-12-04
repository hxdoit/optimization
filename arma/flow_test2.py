import pandas as pd
import numpy as np
import math
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
import matplotlib.pylab as plt
import sys

data= pd.read_csv(sys.argv[1])
ts=data['flow']
ts_diff = ts.diff(1)
#ts_diff.dropna(inplace=True)
ts_list=[]
for i in range(ts_diff.size): 
    if i ==0:
        continue
    ts_list.append(ts_diff[i])
#plot_pacf(ts_diff,lags=100)
#plot_acf(ts_diff,lags=100)
#plot_pacf(ts_diff,lags=40)
#plot_acf(ts_diff,lags=40)
#plt.plot(ts_diff)
#plt.plot(ts_log)
#plt.plot(ts_diff)
#moving_avg= ts.rolling(5).mean()
#moving_std= ts.rolling(5).std()
#plt.plot(moving_avg)
#plt.plot(moving_std)
#exweight = ts.ewm(span=2,ignore_na=False, adjust= True).mean()
#plt.plot(exweight)
#plt.show()

def adf_test(ts):
    adftest = adfuller(ts)
    adf_res = pd.Series(adftest[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])

    for key, value in adftest[4].items():
        adf_res['Critical Value (%s)' % key] = value
    return adf_res

#print adf_test(ts_diff)

import sys
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_model import ARIMA
def _proper_model(ts_log_diff, maxLag):
    best_p = 0 
    best_q = 0
    best_bic = sys.maxint
    best_model=None
    for p in np.arange(maxLag):
        for q in np.arange(maxLag):
            model = ARMA(ts_log_diff, order=(p, q))
            try:
                results_ARMA = model.fit(disp=-1)
            except:
                continue
            bic = results_ARMA.bic
            print bic, best_bic
            if bic < best_bic:
                best_p = p
                best_q = q
                best_bic = bic
                best_model = results_ARMA
    return best_p,best_q,best_model
#print _proper_model(ts_list,10) 


arParams=[-0.807344, -0.648254, -0.49305, -0.356703, -0.226996, -0.121837]

tsShift =  ts.shift(1)

model = ARIMA(ts,order=(6,1,0)) 
results_AR = model.fit(disp=-1)
plt.plot(ts,color='green')

history=[]
history_shift=[0]

myPredict=[]
i=0
while i < ts.size:
    print "-------",i
    if i<7:
        history.insert(0,ts[i])
        myPredict.append(ts[i])
        if i > 0:
            history_shift.insert(0,ts[i-1])
        i+=1
        continue
    tempP = 0
    for j in range(6):
        tempP +=  results_AR.arparams[j] * (history[j]-history_shift[j])
    #print history
    #print history_shift
    #sys.exit(0)

    temp0 = tempP + history[0] 
    myPredict.append(temp0)
    if i==227:
        print history
        print history_shift

    temp1=temp0 + ts[i]
    temp2=temp0 - ts[i]
    diff = temp2 / ts[i]
    if abs(diff)>0.2:
        if temp1>0:
            temp3 = math.sqrt((temp2**2) / (temp1/2))
            if temp3>2 and abs(temp1)>15:
                plt.plot(i,ts[i],'bo') 
                print "-----hit",i
                i+=1 
                continue
    history_shift.insert(0,history[0])
    history.insert(0,ts[i])
    history.pop()
    history_shift.pop()
    i+=1
    
#print myPredict
#print results_AR.fittedvalues 
        
#predict=results_AR.fittedvalues+ts.shift(1)
plt.plot(myPredict, color='red') 
#plt.plot(ts_diff,color='blue')
#plt.plot(results_AR.fittedvalues, color='red') 
#plt.title('RSS:%.4f' % sum((results_AR.fittedvalues-ts_diff)**2))
print results_AR.arparams
print results_AR.maparams
#print ts_diff
#print results_AR.fittedvalues
#print ts
#print ts_diff
#print results_AR.fittedvalues
#print results_AR.fittedvalues+ts.shift(1)
plt.xlabel("time(5min)")
plt.ylabel("flow(pcu)")
plt.show()
