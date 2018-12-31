% datatypes https://www.mathworks.com/help/matlab/data-types.html

%{
----- Summary of What's Out There -----

Characters and Strings
Text in character arrays and string arrays
Dates and Time
Arrays of date and time values that can be displayed in different formats
Categorical Arrays
Arrays of qualitative data with values from a finite set of discrete, nonnumeric data
Tables
Arrays in tabular form whose named columns can have different types
Timetables
Time-stamped data in tabular form
Structures
Arrays with named fields that can contain data of varying types and sizes
Cell Arrays
Arrays that can contain data of varying types and sizes
Function Handles
Variables that allow you to invoke a function indirectly
Map Containers
Objects with keys that index to values, where keys need not be integers
Time Series
Data vectors sampled over time
Data Type Identification
Determining data type of a variable
Data Type Conversion
Converting between numeric arrays, character arrays, cell arrays, structures, or tables
%}

% Characters & Strings

% https://www.mathworks.com/help/matlab/characters-and-strings.html
% basic string
c = 'hello world!'
% creating strings out of numbers
s1 = string(123)
% combine strings
s2 = c+s1

% Dates and Time
% Create scalar datetime array corresponding to the current date and time.
t = datetime
% You can enter in a matrix showing the date time as an argument
DateVectors = [2014 10 24 12 45 07]
% this will display as a datetime
t1 = datetime(DateVectors)
% Create datenumber from datetime
% Represents each point in time as the number of days from January 0, 0000
DateNumber = datenum(datetime)
% Convert from DateNumber to Datetime
t3 = datetime(DateNumber,'ConvertFrom','datenum')
% Convert to Postix or Unix time
p3 = posixtime(t3)

% Tables
% About Tables https://www.mathworks.com/help/matlab/tables.html
% Tabular Data https://www.mathworks.com/help/matlab/ref/table.html

LastName = {'Sanchez';'Johnson';'Li';'Diaz';'Brown'};
Age = [38;43;38;40;49];
Smoker = logical([1;0;1;0;1]);
Height = [71;69;64;67;64];
Weight = [176;163;131;133;119];
BloodPressure = [124 93; 109 77; 125 83; 117 75; 122 80];
% Create Table
T = table(LastName,Age,Smoker,Height,Weight,BloodPressure)
% Doing Operations on Columns - Example
meanHeight = mean(T.Height)
totalWeight = sum(T.Weight)

% Access the Table Data as a Matrix - the Data Types must be consistent, as
% follows:
TN = table(Age,Smoker,Height,Weight,BloodPressure)
% First, get the Dimension Names
T.Properties.DimensionNames
%  The default name of the second dimension is Variables.
%  The default name of the first dimension is Row.
%  Since all values are consistent types, we can put them into a matrix...
TM = TN.Variables
% You can rename the dimensions and then access those dimensions with new
% names, rather than "Variables"
% This is a construct which allows you to essentially label tables to
% access them.
TN.Properties.DimensionNames{2} = 'PatientData';
TN.PatientData
% Note - you can preallocate table sizes.


% Structures


% Cell Arrays
