import pandas as pd
serInt = pd.Series(range(1))
serInt.dtype
#dtype('int64')

serFloat = pd.Series([1.0,2.0])
serFloat.dtype
#dtype('float64')

setStr = pd.Series(['a','b'])
setStr.dtype
#dtype('O')

serdictInt = pd.Series({'one':1, 'two':2})
serdictInt.dtype
#dtype('int64')

serDictFloat = pd.Series({'one':1.0, 'two':2.0})
serDictFloat.dtype
#dtype('float64')

sertDictStr = pd.Series({'one':'I', 'two':'II'})
sertDictStr.dtype
#dtype('O')

sertDictStrKey = pd.Series({'one':'I', 'two':'II'})
sertDictStrKey.dtype
#dtype('O')

serDate = pd.Series([pd.to_datetime('2016-01-01')])
serDate.dtype
#dtype('<M8[ns]')

serCategorical = pd.Series(['a','b'],dtype='category')
serCategorical.dtype
#category
