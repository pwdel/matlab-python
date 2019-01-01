function [ avg ] = average1( nums )
%AVERAGE1 this function calculates the sum of input over global variable
%TOTAL
%   The purpose of this function is to show how global variables work.
global TOTAL
avg = sum(nums)/TOTAL;

end