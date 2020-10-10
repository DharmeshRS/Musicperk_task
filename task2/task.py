import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
from matplotlib import style

mydata = quandl.get("NSE/PNB", start_date="2017-12-31", end_date="2020-12-31")

print(mydata)

mydata['15d']=np.round(mydata['Close'].rolling(window=15).mean(),2)
mydata['40d']=np.round(mydata['Close'].rolling(window=40).mean(),2)

mydata[['Close','15d','40d']].plot(grid=True,figsize=(10,8))

mydata['15d-40d']=mydata['15d']-mydata['40d']

X=10
mydata['Stance']=np.where(mydata['15d-40d']>X,1,0)
mydata['Stance']=np.where(mydata['15d-40d']<X,-1,mydata['Stance'])
print(mydata['Stance'].value_counts())


mydata['Stock_Return']=np.log(mydata['Close']/mydata['Close'].shift(1))
mydata['SMAC_strategy']=mydata['Stock_Return']*mydata['Stance'].shift(1)
abc=mydata[['Stock_Return','SMAC_strategy']].plot(grid=True,figsize=(10,6))
plt.show()