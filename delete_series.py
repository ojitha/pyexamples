import pandas as pd

d1 = {'one': 1, 'two':2}
#{'one': 1, 'two': 2}

del d1['two']
#{'one': 1}

s= [10,20,30]
ser = pd.Series(s, index=['a','b','c'])
# a    10
# b    20
# c    30
dtype: int64

del ser['b'] #mutated
# a    10
# c    30
# dtype: int64

#masking
mask = ser > 20
# a    False
# c     True
# dtype: bool

ser[mask]
# c    30
# dtype: int64

ser.index
#Index([u'a', u'c'], dtype='object')

#masking the index
mask = ser.index == 'a'
#array([ True, False], dtype=bool)

ser[mask]
# a    10
# dtype: int64
