import pandas as pd

s= [10,20,30]
ser = pd.Series(s)

ser + 2
# 0    12
# 1    22
# 2    32
# dtype: int64


#s + 2 never work in python
# but
s * 2
#[10, 20, 30, 10, 20, 30]

#completely different idea from the standard python.
ser * 2
# 0    20
# 1    40
# 2    60
# dtype: int64

#s + ser or
ser + s
# 0    20
# 1    40
# 2    60
# dtype: int64

#create second series
s1 = [40,50,60]
ser1 = pd.Series(s1)

ser + ser1
# 0    50
# 1    70
# 2    90
# dtype: int64

ser3 = pd.Series(s1, index=[2,3,4])
# 2    40
# 3    50
# 4    60
# dtype: int64

#only the instersecting elements are added rest of the other are NaN
ser + ser3
# 0     NaN
# 1     NaN
# 2    70.0
# 3     NaN
# 4     NaN
# dtype: float64

def disp(val):
    return val

ser.apply(disp)
# 0    10
# 1    20
# 2    30
# dtype: int64

def add_2(val):
    return val + 2

ser.apply(add_2)
# 0    12
# 1    22
# 2    32
# dtype: int64

#to convert to float
ser.apply(float)
# 0    10.0
# 1    20.0
# 2    30.0
# dtype: float64

#but better to use
ser.astype(str)
# 0    10
# 1    20
# 2    30
# dtype: object
