import numpy as np

# circularly shift everything by a certain number of spaces clockwise
# create np.matrix
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html

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

# sort each column in ascending order, note column = 0 axis
# use https://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html
B = np.sort(A, axis=0, kind='quicksort', order=None)
B

# sort each coulmn in descending order
# Note, the method A.sort sorts the current array where as np.sort(A) creates a new array
# hence, the method A.sort is more computationally efficient, but we need a new array
# in Matlab, the new array would be created and put into a new variable at ans
# Efficient method C = A[::-1].sort()
C = np.sort(A)[::-1]


# https://www.mathworks.com/help/matlab/ref/sortrows.html?s_tid=doc_ta
# sort entire rows together
D = sortrows(A)

# sort a range - first extract the range from the matrix, sort the sub-range
% put the range back into the matrix
Nkeep = 3; % size to keep
E = A(2:Nkeep,2:Nkeep) % from 2,2 out to size of matrix 3,3
E = sort(E) % sort each row
A(2:Nkeep,2:Nkeep) = E; % place back into matrix at exact location

# Sort entire Matrix by first column (or particular column)
Fc1 = A(:,1) % extract the first column
[Fc,I] = sort(Fc1) % sort first column, I is the indicies
F = A(I,:) % sort the whole matrix according to the index from the sort above
