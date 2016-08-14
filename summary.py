import pandas as pd

s= [10,20,30,40,50]
ser = pd.Series(s, index=['a','b','c','d','e'])

ser.describe()
# count     5.000000
# mean     30.000000
# std      15.811388
# min      10.000000
# 25%      20.000000
# 50%      30.000000
# 75%      40.000000
# max      50.000000
# dtype: float64

ser.value_counts()
# 30    1
# 20    1
# 10    1
# 50    1
# 40    1
# dtype: int64

#categorical data
cat= ['mango','apple','banna','grape','date','apple','pinapple','apple','banna']
catser = pd.Series(cat, dtype='category')
catser.describe()
# count         9
# unique        6
# top       apple
# freq          3
# dtype: object

catser.value_counts()
# apple       3
# banna       2
# pinapple    1
# mango       1
# grape       1
# date        1
# dtype: int64

ser.duplicated()
# a    False
# b    False
# c    False
# d    False
# e    False
# dtype: bool

ser1 = ser.append(pd.Series([10],index=['f']))
# a    10
# b    20
# c    30
# d    40
# e    50
# f    10
# dtype: int64

ser1.duplicated() #last is duplicated with first one
# a    False
# b    False
# c    False
# d    False
# e    False
# f     True
# dtype: bool

ser.duplicated().any()
#False

ser1.duplicated().any()
#True

ser1.duplicated().all()
#False

ser1.duplicated(keep='last')
# a     True
# b    False
# c    False
# d    False
# e    False
# f    False
# dtype: bool

ser1.duplicated(keep=False)
# a     True
# b    False
# c    False
# d    False
# e    False
# f     True
# dtype: bool

#fitler the duplicated
mask = ser1.duplicated(keep=False)
ser1[mask]
# a    10
# f    10
# dtype: int64

#who were not duplicated
ser1[~mask]
# b    20
# c    30
# d    40
# e    50
# dtype: int64

ser1.drop_duplicates(keep=False) //immutable
# b    20
# c    30
# d    40
# e    50
# dtype: int64

#add the duplicated keys
ser_key_dups = ser.append(pd.Series([100], index=['a']))
# a     10
# b     20
# c     30
# d     40
# e     50
# a    100
# dtype: int64

ser_key_dups['a']
# a     10
# a    100
# dtype: int64
