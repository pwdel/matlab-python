% A word on creating models:
% Creating predictive learning rests upon two main assumptions:
% 1. Available (past) data has the same or similar distribution as future data.
% 2. Simple models are favored over complex ones.
% Using the classical statistics approach to predictive learning, we first estimate
% the probabalistic model from training model in order to minimize the risk functional.

% Discriminative Models - risk minimization modeling approach
% Works well if the system's output can be sufficiently imitated, minimizing prediction risk
% Akin to Scientific Instrumentalism https://www.britannica.com/topic/instrumentalism
% The value of theories is extent to which they help to make accurate
% empirical predictions (aim for smallest empirical risk)

% Generative Models - probabalistic modeling approach
% Works well if the conditional probability can be accurately estimated from the data
% Akin to Scientific Realism - theories are modified to accomodate more and more 
% evidence, they more and more closely approximate the truth.
% (aim for minimization of misclassification costs)

% Conditional Probability - https://en.wikipedia.org/wiki/Conditional_probability

% Generate two-dimensional samples by Gaussian distribution.
% Means and covariance matrix of each:
% (See example) https://en.wikipedia.org/wiki/Multivariate_normal_distribution
% Setting up Multivariate Normal Distribution...
% https://www.mathworks.com/help/stats/normal-distribution.html
% https://www.mathworks.com/help/stats/mvnpdf.html

% We generate one set of samples...

samplesize = 1000;

% Class Zero Samples
mu1 = [3,6]; 
sigma1 = [0.5,0;0,2];
X1 = mvnrnd(mu1,sigma1,samplesize); 
p1 = mvnpdf(X1,mu1,sigma1);

% Class One Samples
mu2 = [3,-2]; 
sigma2 = [2,0;0,2];
X2 = mvnrnd(mu2,sigma2,samplesize); 
p2 = mvnpdf(X2,mu2,sigma2);

% Generate another set of samples...

mu3 = [3.0081,5.8363];
sigma3 = [0.3313,-0.6011;-0.6011,2.2407];
X3 = mvnrnd(mu3,sigma3,samplesize); 
p3 = mvnpdf(X3,mu3,sigma3);

mu4 = [2.6701,-2.3410]; 
sigma4 = [0.8797,0.3011;0.3011,1.9954];
X4 = mvnrnd(mu4,sigma4,samplesize); 
p4 = mvnpdf(X4,mu4,sigma4);

% Plot them out...

figure(1)
title('Two-Dimensional Samples by Gaussian Distribution')
subplot(2,1,1)
scatter(X1(:,1),X1(:,2))
hold on
scatter(X2(:,1),X2(:,2))
hold on
subplot(2,1,2)
scatter(X3(:,1),X3(:,2))
hold on
scatter(X4(:,1),X4(:,2))

% Using the generative modeling approach for binary classification,
% estimating the joint probability distribution amounts ot estimating the
% class-conditional densities from positive and negative training samples:

% p+(x) = p(x/y = +1)
% and
% p+(x) = p(x/y = +-1)

% We can take a bayesian approach to the above and "normalize" each
% function by dividing it by p(x).  Baysian thinking means "normalizing" to
% eliminate base rate fallacies.

% f(x) = +1 if p+(x)/p-(x) > C-P(y=-1)/C+P(y=+1) else f(x) = -1

% Classical statistics makes specific assumptions about the parametric form
% of the distribution (Guassian, Poisson, etc.) and uses training data to
% esimate its parameters, whereas predictive learning utilizes classical
% statistics as one toolset.

% Since we know the samples above are Guassian...
% Gaussian class distributions optimal decision boundary can be calculated
% as

