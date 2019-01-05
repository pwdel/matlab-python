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

% Generate two-dimensional samples by Gaussian distribution.
% Means and covariance matrix of each:
% (See example) https://en.wikipedia.org/wiki/Multivariate_normal_distribution
% Setting up Multivariate Normal Distribution...
% https://www.mathworks.com/help/stats/normal-distribution.html
% https://www.mathworks.com/help/stats/mvnpdf.html

% We generate one set of samples...

samplesize = 1000;

% Class Zero Samples - Samples which we will classify as Being = 0
mu0 = [3,6]; 
sigma0 = [0.5,0;0,2];
X0 = mvnrnd(mu0,sigma0,samplesize); 
p0 = mvnpdf(X0,mu0,sigma0);

% Class One Samples - Samples which we will classify as Being = 1
mu1 = [3,-2]; 
sigma1 = [2,0;0,2];
X1 = mvnrnd(mu1,sigma1,samplesize); 
p1 = mvnpdf(X1,mu1,sigma1);

% Plot them out...

figure(1)
title('Two-Dimensional Samples by Gaussian Distribution')
subplot(2,1,1)
scatter(X0(:,1),X0(:,2))
hold on
scatter(X1(:,1),X1(:,2))

% Since we know the samples above are Guassian...
% Gaussian class distributions optimal decision boundary can be calculated
% as shown in slide 10 of this deck:
% https://github.com/pwdel/matlab-python/blob/master/99%20Lecture%20Sets/lecture_set08_2018.ppt
% We must derive the equation for the decision boundary that separates these two classes, 
% implement it in code, and draw the boundary.

% https://cse.buffalo.edu/~jcorso/t/CSE555/files/homework_decision_solutions.pdf
% g1 = -0.5*([x1;x2]-mu1?)?*inv(sigma1)*([x1;x2]-mu1?)-log(2*pi)-0.5*log(det(sigma1));

% Bayes Optimal Discriminant Function
% We will base this off of a 1000 sample linspace within our general range.
xspace = linspace(-2,8,100);

% First Factor of Equation
% Inverse Matrix - https://www.mathworks.com/help/matlab/ref/inv.html
% Transpose Matrix - https://www.mathworks.com/help/matlab/ref/transpose.html
% Sum of Series - https://www.mathworks.com/help/symbolic/symsum.html
midpoint = (mu0(:) + mu1(:)).'/2;

% Using variable X below...
A = (1/2)*(X-mu0)*inv(sigma0)*transpose(X-mu0); % We could transpose(xvect-mu0) here if needed
= (1/2)X-(1/2)*mu0

% Second Factor of Equation
% B = 

% Combined A&B Result from Symbolic Math
% (a - 3)^2 - (a/4 - 3/4)*(a - 3) + (b/4 + 1/2)*(b + 2) + (b/4 - 3/2)*(b - 6)

% Expanded Combined A&B Equation
% (3*a^2)/4 - (9*a)/2 + b^2/2 - 2*b + 67/4

% Last piece of equation.
% natural log of determinants of covariance matrix ratio 0/1
C = (1/2)*log(det(sigma0)/det(sigma1))

% Converrt to 


% Creating the Decision Boundary
% Calculate from Covariance Matrix
xspace = linspace(-2,8,1000); % setup the matrix on which the equation will lie
g1 = (power(xspace,2)-6*xspace+18.741)/(-5.333); % solved equation
figure(1)
subplot(2,1,2)
hold on
scatter(X0(:,1),X0(:,2))
hold on
scatter(X1(:,1),X1(:,2))
hold on
plot(xspace,g1)

% Using our derivation
g2 = (


% This is marketdly different than using the Matlab function, "classify" in 
% the Stats and ML Toolbox.

% class = classify(sample,training,group,'type')
% 'type' linear ? Fits a multivariate normal density to each group 


% x1^2-6*x1-5.333*x2+18.741


% Scatter Plot by Group
% https://www.mathworks.com/help/stats/gscatter.html

% Classification
% https://www.mathworks.com/help/stats/examples/classification.html

% Create classification groups
GRP1 = ones(length(X1),1)
GRP2 = zeros(length(X2),1)

% Stack the Data To Fit Into GSCATTER
figure(3)
gscatter(vertcat(X1(:,1),X2(:,1)),vertcat(X1(:,2),X2(:,2)),vertcat(GRP1,GRP2))
hold on
plot(x1,y1)



% Creating a Meshgrid on the space
[X,Y] = meshgrid(linspace(-2,8),linspace(-6,12));
X = X(:); Y = Y(:); % Straighten out the space

% [C,err,P,logp,coeff] = classify([X Y],[X1 X2],...group,'Quadratic');

% This function calculates a decision boundary - how?
j = classify([X,Y],[vertcat(X1(:,1),X2(:,1)),vertcat(X1(:,2),X2(:,2))],vertcat(GRP1,GRP2));
gscatter(X,Y,j,'grb','sod')
                            

%{

% Categorizing Data

...
Block of COMMENTS HERE
...

                                
hold on;
gscatter(X,Y,C,'rb','.',1,'off');
K = coeff(1,2).const;
L = coeff(1,2).linear; 
Q = coeff(1,2).quadratic;
% Function to compute K + L*v + v'*Q*v for multiple vectors
% v=[x;y]. Accepts x and y as scalars or column vectors.
f = @(x,y) K + [x y]*L + sum(([x y]*Q) .* [x y], 2);

h2 = ezplot(f,[4.5 8 2 4]);
set(h2,'Color','m','LineWidth',2)
axis([4.5 8 2 4])
xlabel('Sepal Length')
ylabel('Sepal Width')
title('{\bf Classification with Fisher Training Data}')

...
%}

% Generate another set of samples...classified as 0 and 1
mu3 = [3.0081,5.8363];
sigma3 = [0.3313,-0.6011;-0.6011,2.2407];
X3 = mvnrnd(mu3,sigma3,samplesize); 
p3 = mvnpdf(X3,mu3,sigma3);

mu4 = [2.6701,-2.3410]; 
sigma4 = [0.8797,0.3011;0.3011,1.9954];
X4 = mvnrnd(mu4,sigma4,samplesize); 
p4 = mvnpdf(X4,mu4,sigma4);

figure(2)
hold on
subplot(2,1,2)
scatter(X3(:,1),X3(:,2))
hold on
scatter(X4(:,1),X4(:,2))


