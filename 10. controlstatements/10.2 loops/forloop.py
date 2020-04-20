# Note - when working with for loops, it's always important to remember that
# vectorizing data and operating on it is a much more computationally efficient way.
# check out the section 3.2 on, "Vectorization"

import pandas as pd
from pandas import *

# we put data.csv into the dataframe, dataframe is similar to a Matlab cell or struct
df = read_csv('data.csv')

# one way to iterate through the data is to use enumerate
for i, row in enumerate(df.values):
    date = df.index[i]
    open, high, low, close, adjclose = row
    #now perform analysis on open/close based on date, etc..


for index, row in df.iterrows():

    # do some logic here
#!/usr/bin/env python
