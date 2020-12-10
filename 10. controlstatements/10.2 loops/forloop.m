% For loop through a matrix of strings
fruits = ["apple", "banana", "cherry"]

for c = 1:length(fruits)
  fruits(c)
end

% For loop through a fixed numeric range
% Repeating a for loop 10 times
s = 10;
H = zeros(s);
for c = 1:s
    for r = 1:s
        H(r,c) = 1/(r+c-1);
    end
end
