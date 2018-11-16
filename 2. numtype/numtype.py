# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
import numpy as np
X=2

# define a function whosMy to print information about all of the variables
def whosMy(*args): # take in all arguments
    # There are six sequence types: strings, Unicode strings, lists, tuples, buffers, and xrange objects.
    # dictionary, list and tuple
    # dictionaries have key/value pairs
    # lists are mutable tuples
    # tuples have a name and then just a list of stuff in them
  sequentialTypes = [dict, list, tuple]
  for var in args: # for each variable within all arguments
    t=type(var) # we get the type of the variable
    if t== np.ndarray:  # if the type is an array
        # about arrays https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
      print type(var),var.dtype, var.shape # print out the type, data type (dtype) and shape
    elif t in sequentialTypes: # otherwise if it's a dictionary, list or tuple
      print type(var), len(var) # print out just the type of the variable and the length of the variable
    else:
      print type(var) # otherwise just print the type of the variable

# Calling this function for X as it stands now, it should just show up as <type 'int'>
# this is the default number type within python but not Numpy.
whosMy(X)

# If we convert X or call other variables of different types, they should print out differently.
# The equivalent to a double in Matlab is a float64
# This means 63 bits (0s and 1s) with a maximum value of 18446744073709551615 with a sign.
Xfloat64 = np.float64(X)

whosMy(X,Xfloat64)

# Looking at other types:
# single point
Xfloat32 = np.float32(X)

# int8 (Byte -128 to 127)
Xint8 = np.int8(X)

# Checking multiple types
whosMy(X,Xfloat64,Xfloat32,Xint8)

# and so on according to the documentation.
