import csv
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
aapl = pdr.get_data_google('AAPL','2017-01-01')
aapl_cls = pd.DataFrame(aapl['Close'])
aapl_cls['MA_9']=aapl_cls['Close'].rolling(9).mean().shift()
aapl_cls['MA_21']=aapl_cls['Close'].rolling(21).mean()
plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(aapl_cls['Close'],label = 'AAPL')
plt.plot(aapl_cls['MA_9'],label = '9 Day')
plt.plot(aapl_cls['MA_21'],label = '21 Day')
plt.legend(loc=2)
aapl_cls['Change'] = np.log(aapl_cls['Close']/aapl_cls['Close'].shift())
plt.plot(aapl_cls.Change)
aapl_cls['Volatility'] = aapl_cls.Change.rolling(21).std().shift()
aapl_cls['Volatility'].plot()
aapl_cls['Actual_Change'] = aapl_cls['Close']-aapl_cls['Close'].shift()
aapl_cls['Expected_Change'] = aapl_cls['Close']*aapl_cls['Volatility']
aapl_cls=aapl_cls.dropna()
aapl_cls.head()
aapl_cls['Magnitude']=aapl_cls['Actual_Change']/aapl_cls['Expected_Change']
plt.hist(aapl_cls['Magnitude'],bins=50)
