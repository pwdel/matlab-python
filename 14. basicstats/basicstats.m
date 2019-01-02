% A word on creating models:
% Creating predictive learning rests upon two main assumptions:
% 1. Available (past) data has the same or similar distribution as future data.
% 2. Simple models are favored over complex ones.
% Using the classical statistics approach to predictive learning, we first estimate
% the probabalistic model from training model in order to minimize the risk functional.

% Discriminative Models - risk minimization modelomg approach
% Works well if the system's output can be sufficiently imitated, minimizing prediction risk

% Generative Models - probabalistic modeling approach
% Works well if the conditional probability can be accurately estimated from the data

% Generate two-dimensional samples by Gaussian distribution.
% Means and covariance matrix of each:
% (See example) https://en.wikipedia.org/wiki/Multivariate_normal_distribution
% Setting up Multivariate Normal Distribution...
% https://www.mathworks.com/help/stats/normal-distribution.html
% https://www.mathworks.com/help/stats/mvnpdf.html

samplesize = 1000;

mu1 = [3,6]; 
sigma1 = [0.5,0;0,2];
X1 = mvnrnd(mu1,sigma1,samplesize); 
p1 = mvnpdf(X1,mu1,sigma1);

mu2 = [3,-2]; 
sigma2 = [2,0;0,2];
X2 = mvnrnd(mu2,sigma2,samplesize); 
p2 = mvnpdf(X2,mu2,sigma2);

figure(1)
scatter(X1(:,1),X1(:,2))
hold on
scatter(X2(:,1),X2(:,2))

% Another

mu3 = [3.0081,5.8363]; 
sigma3 = [0.3313,-0.6011;-0.6011,2.2407];
X3 = mvnrnd(mu1,sigma3,samplesize); 
p3 = mvnpdf(X3,mu3,sigma3);

mu4 = [2.6701,-2.3410]; 
sigma4 = [0.8797,0.3011;0.3011,1.9954];
X4 = mvnrnd(mu4,sigma4,samplesize); 
p4 = mvnpdf(X4,mu4,sigma4);

figure(2)
scatter(p3,p4)
