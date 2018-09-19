% number types in Matlab
% help file here https://www.mathworks.com/help/matlab/numeric-types.html

% double	Double-precision arrays is the default Class in Matlab
% whos can be used to identify the data Class
x = 10;
% this should print out with Name, Size (matrix dimension), Bytes and Class
% (double)
whos x
% If you want to convert to a double, you use double(x)
x_double = double(x);
% Same with other data types
x_single = single(x);
x_int8 = int8(x);
x_int16 = int16(x);	% 16-bit signed integer arrays
int32	32-bit signed integer arrays
int64	64-bit signed integer arrays
uint8	8-bit unsigned integer arrays
uint16	16-bit unsigned integer arrays
uint32	32-bit unsigned integer arrays
uint64	64-bit unsigned integer arrays
