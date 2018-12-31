
"""
Looking at an overview of the data types within Matlab, we have roughly the following conversions

matlab table -> python pandas library tables

matlab array -> python numpy array

matlab cell array -> python list

matlab structure -> python dict

Python Sets
https://docs.python.org/2/library/sets.html

Python Tuples

Python Dictionaries

"""

# String https://www.w3schools.com/python/python_strings.asp
a = "Hello, World!"
print(a)
b = 'Hello, World!'
print(b)

an = 123
str(an)
print(an)

"""
Datetime
https://docs.python.org/3/library/datetime.html
There are two kinds of date and time objects: “naive” and “aware”.

An aware object has sufficient knowledge of applicable algorithmic and political
time adjustments, such as time zone and daylight saving time information, to locate
itself relative to other aware objects.

A naive object does not contain enough information to unambiguously locate itself
relative to other date/time objects. Whether a naive object represents Coordinated
Universal Time (UTC), local time, or time in some other timezone is purely up to the program.

Data Structure

object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime

"""
# https://docs.python.org/3/library/datetime.html
from datetime import datetime
now1 = datetime.now()
print(now1) # print current time
now1iso = datetime.isoformat(now1)
print(now1iso) # print current time iso format


Y=2018; M=12; D=30; h=18; m=30; s=15; ms=12;
t1 = datetime(Y,M,D,h,m,s,ms)
print(t1) # print arbitrary naive datetime

"""
timedelta is used to measure the difference between two points in time
"""
# note that timedelta does not include minutes, hours but just days/seconds/miliseconds
from datetime import timedelta
d = timedelta(days=1,microseconds=1)
(d.days, d.seconds, d.microseconds)

# Comparing timezones - much more information in documentation
from datetime import tzinfo
now2 = datetime.now()
now3 = datetime.utcnow()
print(now2) # print local timezone time
print(now3) # print utc time

"""
Time module
https://docs.python.org/3/library/time.html#module-time
This is different than the datetime module.
"""

# Get postix time
import time
t7 = time.time()
print(t7)

# Convert to Postix or Unix Time to Readable Timestring
from datetime import datetime
ts = int(t7)
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
# Refer to https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
t8 = datetime.utcfromtimestamp(t7).strftime('%Y-%m-%d %H:%M:%S')
print(t8)

"""
Tabular Data - Pandas
Exercises found here:

https://pandas.pydata.org/pandas-docs/stable/10min.html

"""
# Creating a Series by passing a list of values, letting pandas create a default integer index:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
now10 = datetime.now() # get the datetime including hour, minute, seconds
now10s = now10.date() # get the simple format of datetime.now()
dates = pd.date_range(now10s, periods=6) # generate 6+days
print('Print out pd.date_range for 6 periods (days) into an index: ')
print(dates)
print('Print out Dataframe with columns of random numbers in a 6x4 table with column labels ABCD')
print('Dataframe is essentially a table.')
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })
df2
print('Print out the DataFrame constructed from dictionary objects: ')
print(df2)

# Here is how to view the top and bottom rows of the frame:
print('Here is how to view the top and bottom rows of the frame: ')
print(df.head())
print(df.tail(3))

# Print row index and column labels
print('Print out the index of each row (datetimes): ')
print(df.index)
print('Print out the labels of each column (datetimes): ')
print(df.columns)

# The values - matrix / numpy array values inside the table
print('Print out the values inside of the table (matrix format): ')
print(df.values)

# Sorting by values:
print('Sorting by values: ')
print(df.sort_values(by='B',ascending=False)) # ascending=False means highest value on top

# Selecting a single column
print('Selecting a single column: ')
print(df['B'])

# Slicing Rows - Slice Row 0 through 2 (goes right before 3)
print('Slicing Rows - Slice Row 0 through 2 (goes right before 3): ')
print(df[0:3])

print('Selection by Label, Select by first Date: ')
df.loc[dates[0]]

# Boolean Indexing and Filtering
print('Boolean slice based upon values in column A greater than zero: ')
print(df[df.A > 0])
print('Filtering all values greater than zero: ')
print(df[df > 0])

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print('Expanded matrix with column E representing filterable values: ')
print(df2)
print('Filtering based upon two and four values: ')
print(df2[df2['E'].isin(['two','four'])])

# There are a variety of additional interesting tools here:
# https://pandas.pydata.org/pandas-docs/stable/10min.html

"""
As a library rather than a whole platform, Pandas has its own operations.
"""
print('Performing a descriptive statistic on each column (axis-0) (mean): ')
print(df.mean(0)) # axis-0 is coming from the "top" looking downward
print('Perform (mean) on each row (axis-1):')
print(df.mean(1)) # axis-1 is each row, coming from the "left" looking forward

"""
Various other operations can be done on Pandas tables.

Append
https://pandas.pydata.org/pandas-docs/stable/10min.html#append

SQL Style Merges from Json Type Data
https://pandas.pydata.org/pandas-docs/stable/10min.html#join

Concatenation
https://pandas.pydata.org/pandas-docs/stable/10min.html#concat

String Methods
https://pandas.pydata.org/pandas-docs/stable/10min.html#string-methods

Grouping - Basically, splitting data into parts, doing functions on those parts
https://pandas.pydata.org/pandas-docs/stable/10min.html#grouping

Reshaping
https://pandas.pydata.org/pandas-docs/stable/10min.html#reshaping

Time Series - Binning Data into Time Boxes (As with Financial Data)
https://pandas.pydata.org/pandas-docs/stable/10min.html#time-series

Categorical Data (Such as Grades - Non-Numerical Labels, etc.)
https://pandas.pydata.org/pandas-docs/stable/10min.html#categoricals

"""

# Plotting of Pandas DataFrames
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot() # note - this only appears to work in iPython Notebook
