% The following .m file will run the function "mymax" which we created.
% This function simply finds the maximum of the three input numbers given.

[max] = mymax(1, 5, 7)

% note that any variables created while the function was running are not
% stored in the Workspace.

% Annonymous functions - you can create functions on the fly.
% f = @(arglist)expression
% The function itself will be stored in, "value" within the Workspace.

power = @(x, n) x.^n;
% We can call our above defined on-the-fly function and put them into a
% variable.  This function will remain stored in the variables.

result1 = power(7, 3)

% Matlab global variables
% Global variables can be declared which work inside all functions as shown:

global TOTAL;
TOTAL = 10;
n = [34, 45, 25, 45, 33, 19, 40, 34, 38, 42];
avg = average1(n)

% Other Notes on functions - functions can be "nested" meaning that functions can
% call other functions, mid-function.
