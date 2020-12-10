# https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html
# tutorial on vectorization for Performance
# https://hackernoon.com/speeding-up-your-code-2-vectorizing-the-loops-with-numpy-e380e939bed3
# Intersting Article:
# https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06

import numpy as np
import pandas as pd


# For a more detailed dive into Vectorization for Python, check out my Google Colab Notebook on Vectorization:
# https://drive.google.com/drive/folders/1QFE09a63zwTBJR_60icKR_2DomnX4DFB

# As a part of vectorization, don't forget about pre-allocation.
# there are many ways to pre-allocate arrays in Python, the lowest mempory appears to be, np.empty
# Creating a 2D Array Up Front (Pre-Allocation)
huge_list = [0,1,2,3,4,5,6,7,8,9]
row_length = 1
my_array = np.empty([len(huge_list), row_length])
