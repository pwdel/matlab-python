import numpy as np
import pandas as pd
# Note - when working with for loops, it's always important to remember that
# vectorizing data and operating on it is a much more computationally efficient way.
# check out the section 3.2 on, "Vectorization"

# For Loops with Python as a Programming Language:
# It's important to keep in mind that MATLAB is a mathematical language, while Python is designed primarily for programming overall.
# Hence, the most basic type of for loop involves just iterating through something like a string, not a Matrix.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# What we did above is basically create a regular python array (not a numbered array) and printed the values in that array
# However if we wanted to iterate through a ndarray (numbered array), analogous to a matrix, we would do the following:

# Before moving on, we should look at a regular for loop for a fixed numeric range.
# Whereas in Matlab, you iterate through a fixed numeric range by specifying the length of the range,
# first, declare an array

elements = []
for i in elements[0:5]:
    print("Element was: %d" % i)

# The starting 0 can be eliminated with:
for i in elements[:5]:
    print("Element was: %d" % i)


# np.arrange creates an array([0,1,2,3,4,5]) and .reshape(2,3) turns it into a 2x3 matrix
# the type of this variable will be numpy.ndarray
a = np.arange(6).reshape(2,3)

# then, we can use np.nditer to iterate through the numbered array
for x in np.nditer(a):
    print(x, end=' ')

# For Loops with Pandas - Note that we imported Pandas above.

# we put a from above into the dataframe, dataframe is similar to a Matlab cell or struct
# Note that we can name the columns and rows
df = pd.DataFrame(a, index=["row1","row2"], columns=["col1","col2","col3"])

# one way to iterate through the data labels themselves is with enumerate
print("iterating through rows")
for i, row in enumerate(df.values):
    rows = print(df.index[i])
    #now perform analysis on open/close based on date, etc..

# There are several ways to iterate through rows within Pandas and Numpy.
# There are multiple comparisons online on how to iterate through numbers.  Ultimately, using Pandas and Numpy
# vectorization as discussed above is going to be faster.  However for the purposes of this section, and simplifying
# we will just discuss two options:
# 1. The standard built in Pandas Loop, iterrows() and 2. itertuples
# The reason you would use iterrows is because it's faster, howeer itertuples preserves datatypes.
# That being said, not using vectorization defeats the purpose of using Pandas (as it also defeats the purpose of Matlab).
# See section 3.2 for more on vectorization.

# for the column and row in the DataFrame, you can index the column for a particular row in question
for i, row in df.iterrows():
    print(row["col1"],row["col2"])

# that should print out each column sequentially by row in order.  You can operate on the rows as follows:

for i, row in df.iterrows():
    w = row["col"]+2

# If you simply want to iterate down the column of a dataframe, keep in mind that the dataframe can be indexed as:
# my_dataframe[column][row]
# so as an example, you would use .count method which counts the number of rows
# whereas .size counts total number of elements in a frame, and df.shape lists the rows and columns
for i, row in df.count
    print(df[0][i])

# or...df.size[0] which gives you the rows from a tuple result, whereas 1 would give you the columns in a 2-dim dataframe
for i, row in df.size[0]

# ...to print out all of the rows for that column
