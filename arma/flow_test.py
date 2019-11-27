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
ts_diff.dropna(inplace=True)
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



model = ARIMA(ts,order=(6,1,0)) 
results_AR = model.fit(disp=-1)
plt.plot(ts,color='green')
predict=results_AR.fittedvalues+ts.shift(1)
plt.plot(predict, color='red') 
print (predict-ts)/ts
for i in range(predict.size):
    diff=(predict[i]-ts[i])/ts[i]
    if abs(diff)>0.5:
        if predict[i]+ts[i]<1:
            continue
        temp=math.sqrt((predict[i]-ts[i])**2/((predict[i]+ts[i])/2))
        if temp>2:
            plt.plot(i,ts[i],'bo') 
#plt.plot(ts_diff,color='blue')
#plt.plot(results_AR.fittedvalues, color='red') 
plt.title('RSS:%.4f' % sum((results_AR.fittedvalues-ts_diff)**2))
print results_AR.arparams
print results_AR.maparams
#print ts
#print ts_diff
#print results_AR.fittedvalues
#print results_AR.fittedvalues+ts.shift(1)
plt.show()
