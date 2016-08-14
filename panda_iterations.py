import pandas as pd

s = pd.Series([10,20,30,40])

for num in s:
    print(num)
# 10
# 20
# 30
# 40

1 in s
#True

10 in s
#False: because only index is looked

10 in s.values
#True or use the following
10 in set(s)
#True

#convert to dictionary
d = dict(s)
#{0: 10, 1: 20, 2: 30, 3: 40}

#directly iterate series
for lab, val in s.iteritems():
    print (lab, val)
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)

#samething in dictionary
for lab, val in dict(s).iteritems():
    print (lab, val)
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)
