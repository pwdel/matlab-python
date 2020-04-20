# https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html
# tutorial on vectorization for Performance
# https://hackernoon.com/speeding-up-your-code-2-vectorizing-the-loops-with-numpy-e380e939bed3
# Intersting Article:
# https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06

import numpy as np
import pandas as pd

# Create an identiy Matrix
imatrix = np.eye(3)


# https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html
N = 5 # number of zeros in array
zerosarray = np.array(np.zeros(N))

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html
# Numpy Append

# Iterating over Arrays
# https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html

# Create
