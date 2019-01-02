function [max] = mymax(n1, n2, n3)

% This function calculates the maximum of the 3 numbers given as input.
% Note that the name of the file must be the same as the function name.

max =  n1;
if(n2 > max)
   max = n2;
end
if(n3 > max)
   max = n3;
end

end