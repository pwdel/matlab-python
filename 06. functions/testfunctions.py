"""
The following python program will  test the same functions as tested in
testfunctions.m

Note that the key difference between Matlab and Python is the following:

Matlab: Once a function is defined in a .m file and in the same folder structure,
the function may be called ad-hoc by simply its name and understanding that the
name is the same as the function name.

Python: Once a fuction is defined in a .py file and in the same folder structure,
the function must first be imported as shown below, referring to the * portion of
the *.py filename as the "library" you are importing from.  Once you have completed
this import, you can call the function by name.

Note: You have to make sure the file you are importing is in the same directory.

"""
from mymax import mymax

max1 = mymax(1, 5, 7)
print(max1)

# Note - there is no Workspace in Python.

"""
Annonymous functions are known as lambda functions in python.
"""

power = lambda x, n: x**n # define lambda function on the fly
print(power(2,4)) # call arguments that we defined above.

"""
Python Global Variables

"""
