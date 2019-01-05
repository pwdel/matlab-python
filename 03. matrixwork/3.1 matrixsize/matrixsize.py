import numpy as np

# circularly shift everything by a certain number of spaces clockwise
# create np.matrix
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html

# Create matrix
# Note - in Matlab it was Am = [1 2 3; 4 5 6; 7 8 9]
# Here in python we use individual lists for each row.
Am = np.array([ [1,2,3], [4,5,6], [7,8,9] ])

# Creating column vector
Ac = np.array([1,2,3]).reshape(3,1)

# Creating a row vector
Ar = np.array([1,2,3]).reshape(1, 3)


# circularly shift everything by a certain number of spaces clockwise
X = np.matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
print X
# circular shift by axis 1 (note this is the matlab default, "sideways counterclockwise")
Y = np.roll(X, 2, axis=1)
print Y


# rotate matricies 3 times counterclockwise by 90 degrees - rot90
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.rot90.html
A = np.matrix('1 2 3 4 5 6 7 8 9 10')
print A
B = np.rot90(A,k=3);
print B


# generate a magic matrix - note, we have to define this as a function, it's not built if __name__ == '__main__':
def magic(n):
  n = int(n)
  if n < 3:
    raise ValueError("Size must be at least 3")
  if n % 2 == 1:
    p = np.arange(1, n+1)
    return n*np.mod(p[:, None] + p - (n+3)//2, n) + np.mod(p[:, None] + 2*p-2, n) + 1
  elif n % 4 == 0:
    J = np.mod(np.arange(1, n+1), 4) // 2
    K = J[:, None] == J
    M = np.arange(1, n*n+1, n)[:, None] + np.arange(n)
    M[K] = n*n + 1 - M[K]
  else:
    p = n//2
    M = magic(p)
    M = np.block([[M, M+2*p*p], [M+3*p*p, M+p*p]])
    i = np.arange(p)
    k = (n-2)//4
    j = np.concatenate((np.arange(k), np.arange(n-k+1, n)))
    M[np.ix_(np.concatenate((i, i+p)), j)] = M[np.ix_(np.concatenate((i+p, i)), j)]
    M[np.ix_([k, k+p], [0, k])] = M[np.ix_([k+p, k], [0, k])]
  return M

A = magic(4)
A

# sort each column in ascending order (bigger going down), note column = 0 axis
# use https://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html
B = np.sort(A, axis=0, kind='quicksort', order=None)
B

# sort each coulmn in descending order (smaller going down)
# Note, the method A.sort sorts the current array where as np.sort(A) creates a new array
# hence, the method A.sort is more computationally efficient
C = np.sort(A[::],axis=0)[::-1] # we sort on axis 0, then reverse the sort order on all columns

# sort entire rows together, keeping consistent as with excel "sortrange"
I = np.argsort(A[:,0],axis=0) # extract the first column into indicies
D = A[I,:] # sort the whole matrix according to the index from the sort above

# Extract a range
# sort a range - first extract the range from the matrix, sort the sub-range
# put the range back into the matrix
Nkeep = 3; # size to keep
E = A[0:Nkeep,0:Nkeep] # extract 0:Nkeep range from A
En = np.sort(E, axis=1, kind='quicksort', order=None) # sort each row
A[0:Nkeep,0:Nkeep] = En # put micromatrix back into

# Dynamicly Grow a Matrix as Data is Generated or Read
# .append method
