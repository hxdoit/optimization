import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
 
data = pd.read_csv("arima-demo.csv",parse_dates=['date'],index_col='date')
diff1=data.diff(1)
#data.plot(figsize=(12,6))
#diff1.plot(figsize=(12,6))
diff1.dropna(inplace=True)
fig = plt.figure(figsize=(12,8))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(diff1,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(diff1,lags=40,ax=ax2)
plt.show()
arma_mod70 = sm.tsa.ARMA(diff1,(7,0)).fit()
print("arma_mod70:",arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
arma_mod01 = sm.tsa.ARMA(diff1,(0,1)).fit()
print("arma_mod01:",arma_mod01.aic,arma_mod01.bic,arma_mod01.hqic)
arma_mod71 = sm.tsa.ARMA(diff1,(7,1)).fit()
print("arma_mod71:",arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
