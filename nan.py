import pandas as pd

s= [10,20,30,40,None]
ser = pd.Series(s, index=['a','b','c','d','e'])
# a    10.0
# b    20.0
# c    30.0
# d    40.0
# e     NaN
# dtype: float64

s1= [10,20,30,40,50]
ser1 = pd.Series(s1, index=['a','b','c','d',None])
# a      10
# b      20
# c      30
# d      40
# NaN    50
# dtype: int64

ser2 = ser1.append( pd.Series([None], index=['f']))
# 0    None
# dtype: object

len(ser2)
#6

ser2.count()
#5

ser2.isnull()
# a      False
# b      False
# c      False
# d      False
# NaN    False
# f       True
# dtype: bool

ser2.isnull().any()
#True

ser2.isnull().all()
#False

mask = ser2.isnull()
# a      False
# b      False
# c      False
# d      False
# NaN    False
# f       True
# dtype: bool
ser2[mask]
# f    None
# dtype: object

ser2.dropna()
# a      10
# b      20
# c      30
# d      40
# NaN    50
# dtype: object

ser2.fillna(method='ffill')
# a      10
# b      20
# c      30
# d      40
# NaN    50 --fill the --\
# f      50 <------------/
# dtype: int64

import numpy as np
pd.Series([np.nan])
# 0   NaN
# dtype: float64
