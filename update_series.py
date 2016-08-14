import pandas as pd

s= [10,20,30]
ser = pd.Series(s, index=['a','b','c'])
# a    10
# b    20
# c    30
# dtype: int64

#update the position
ser['c'] = 40
# a    10
# b    20
# c    40
# dtype: int64

ser.iloc[0] = 5
# a     5
# b    20
# c    30
# dtype: int64

#add series
ser.append(pd.Series([100])) #new series  returned but not mutate the existing.
# a      5
# b     20
# c     30
# 0    100
# dtype: int64

ser.set_value('a',-10) #mutate the series
# a   -10
# b    20
# c    30
# dtype: int64

#mutate with new values
ser.set_value('d',50)
# a   -10
# b    20
# c    30
# d    50
# dtype: int64
