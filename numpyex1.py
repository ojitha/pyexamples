import numpy as np
import pandas as pd

#create numpy list
a = [1,2,3,4,5]
type(a)
na = np.array(a)
type(na)

print na.sum()

#create panda series from the above array
series = pd.Series(na)
type(series)

#filtering
filter = pd.Series([True,False,True,False,True])
series[filter]

series [(series > 2) & (series < 4)]

series.index

#character index
series2 = pd.Series(a, name='series2', index=['a','b','c','d','e'])

dates = pd.date_range('20160101', periods=5)

date_series = pd.Series(a,name='date_series' ,index = dates)

series4 = pd.Series(a, name='series2', index=[1,1,1,3,4])
