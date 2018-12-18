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
x_int32 = int32(x);	% 32-bit signed integer arrays
x_int64 = int64(x);	% 64-bit signed integer arrays
x_int8 = uint8(x);	% 8-bit unsigned integer arrays
x_int16 = uint16(x); % 16-bit unsigned integer arrays
x_int32 = uint32(x); % 32-bit unsigned integer arrays
x_int64 = uint64(x); % 64-bit unsigned integer arrays
