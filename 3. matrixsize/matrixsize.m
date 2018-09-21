% Matrix sizing and rotation in Matlab
% https://www.mathworks.com/help/matlab/math/reshaping-and-rearranging-arrays.html

% shifting and rotating

% circularly shift everything by a certain number of spaces clockwise
X = [1 2 3 4; 5 6 7 8; 9 10 11 12];
Y = circshift(X,[0 2]);

% rotate matricies 3 times counterclockwise by 90 degrees - rot90
A = [1 2 3 4 5 6 7 8 9 10];
B = rot90(A,3);

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

