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


% generate a magic matrix
A = magic(4)

% sort each column in ascending order
B = sort(A)

% sort each coulmn in descending order
C = sort(A,2,'descend')

% https://www.mathworks.com/help/matlab/ref/sortrows.html?s_tid=doc_ta
% sort entire rows together
D = sortrows(A)

% sort a range - first extract the range from the matrix, sort the sub-range
% put the range back into the matrix
Nkeep = 3; % size to keep
E = A(2:Nkeep,2:Nkeep) % from 2,2 out to size of matrix 3,3
E = sort(E) % sort each row
A(2:Nkeep,2:Nkeep) = E; % place back into matrix at exact location
