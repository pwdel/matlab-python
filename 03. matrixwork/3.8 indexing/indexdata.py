import pandas as pd

# Pandas supports three types of multi-axis indexing:

# .loc - label based, may be used with a boolean array.

# .iloc is integer position based from 0 to n of the axis

# [] indexing

# Generate a dataframe.

dates = pd.date_Range('1.1.2000',periods=8)

df = pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])

# [] indexing

# set s equal to the dataframe 'A' column
s = df['A']
# index the 'dates' of that column, specificall 5 (with a start at 0 numbering system)
s[dates[5]]
# this will display the value at column 'A' and the 6th row element, having started at row 0

# Selection by position - iloc

# to slice off the top three rows, we do:
df.iloc[:3]

# to pick the very first top left value:
df.iloc[0,0]
# this is the same as:
df.iat[0,0]
