import pandas as pd

s= [10,20,30]
ser = pd.Series(s)

s[0]
ser[0]
#10

#ser[-1] not work raised KeyError because there is no label with -1.
s[-1]
#30

#s[4] index out of range
#ser[4] is keyError

#s.loc[0] not work but:
ser.loc[0] #value based on the label
#10

#position based
#ser.loc[-1] not work but:
ser.iloc[-1]
#30

#ser.iloc[4] is IndexError

#but this is different from the string indexes,
#series use label always, not index. This is the proof
#character index
a = [1,2,3,4,5]
ser2 = pd.Series(a, name='ser2', index=['a','b','c','d','e'])
a[-1]
ser2[-1]
ser2.iloc[-1] #position based
#5
# ser2.loc[-1] label error
# ser2.loc[0] label error. But:
ser2.loc['a'] #label based
#1

#label based examples
ser3 = pd.Series(a, name='ser3', index = ['a','b',0,1,2])

ser3.iloc[0] #position
ser3['a']
#1

ser3.iloc[2] #position
ser3[0]
#3
