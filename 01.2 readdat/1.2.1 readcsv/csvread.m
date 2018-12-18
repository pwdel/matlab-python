% Read a CSV File Called "test.csv"
R1=1; % offset the row by 1
C1=0; % offset the column by 0
M = csvread("test.csv",R1,C1);

% Put the first column into X, second column into Y
X = M(:,1);
Y = M(:,2);

% Plot X vs Y on a Scatter 
scatter(X,Y)