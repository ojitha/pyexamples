import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt

s= [10,20,5,40,50]
ser = pd.Series(s, name='dummy' ,index=['a','b','c','d','e'])

ser.name
ax = ser.plot()
ax.set_xlabel("x label")
ax.set_ylabel("y label")

#save series to file
ser.to_csv('test.csv', header=True, index_label='no#')
#read from a file
serff= pd.Series.from_csv('test.csv')
#read with the headers
serffh = pd.Series.from_csv('test.csv',header=0)
# no#
# a    10
# b    20
# c     5
# d    40
# e    50
# Name: dummy, dtype: int64

#read as data frame (df)
df = pd.read_csv('test.csv')
# no#	dummy
# 0	a	10
# 1	b	20
# 2	c	5
# 3	d	40
# 4	e	50

ser_from_df = df['dummy']
# 0    10
# 1    20
# 2     5
# 3    40
# 4    50
# Name: dummy, dtype: int64
