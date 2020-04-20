% vectorization https://www.mathworks.com/help/matlab/matlab_prog/vectorization.html
% Some of these examples were taken from the Matlab website address shown above.

% This code computes the sine of 1,001 values ranging from 0 to 10:

i = 0;
for t = 0:.01:10
    i = i + 1;
    y(i) = sin(t);
end

% This is a vectorized version of the same code:

t = 0:.01:10;
y = sin(t);

% The second code sample usually executes faster than the first and is a more efficient use of MATLAB.
% Test execution speed on your system by creating scripts that contain the code shown,
% and then use the tic and toc functions to measure their execution time.

% Array Operations
% Array operators perform the same operation for all elements in the data set.
% These types of operations are useful for repetitive calculations.
% For example, suppose you collect the volume (V) of various cones by recording their diameter (D) and height (H).
% If you collect the information for just one cone, you can calculate the volume for that single cone:

V = 1/12*pi*(D^2)*H;

% Now, collect information on 1000 cones:

for n = 1:10000
   V(n) = 1/12*pi*(D(n)^2)*H(n));
end

% With MATLAB, you can perform the calculation for each element of a vector with similar syntax as the scalar case:
% Just use the dot matrix multiplicative function .*

% Vectorized Calculation
V = 1/12*pi*(D.^2).*H;
