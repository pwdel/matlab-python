% Learning from Noisy Samples

% Supervised Learning

% Past Data (Training Data) is represented as (xi,yi) i=1,2...n
% In this case, we have a set of animal body and brain weight data.
% Our objective is to estimate a model f(x)

bodyweight = animals{:,2};
brainweight = animals{:,3};

% QUICK REVIEW OF CLEANING TASKS
% One of the first things we need to do is clean the data of outliers in
% order to build a useful model.

figure(1)
scatter(bodyweight,brainweight)

% on that plot above we see that we have outliers which are way beyond the 
% majority of the data.  Here, our data removal is purely data-driven.
% In most real-world cases, data removal is based upon subject matter
% expertise.

animalsfilt = animals(animals.BodyWeight < 1000,:) % filtering out animals over 1klbs

figure(2)
scatter(animalsfilt.BodyWeight,animalsfilt.BrainWeight)

% We can further scale this data to "normalize" it to see if we can gain
% better insights.

figure(3)
scatter(animalsfilt.BodyWeight/max(animalsfilt.BodyWeight),animalsfilt.BrainWeight/max(animalsfilt.BrainWeight))


% Supervised learning - Regression
% The quality of the prediction is measured by tusing the squared loss:
% L(y,f(x))=(y-f(x))^2


% Supervised learning - Classification
% Output y is categorical or class label.  For simplicity, you can consider
% binary classification problems with values 0 and 1
% So error measure classification can be determined by 
% L(y,f(x)) = 0 if y=f(x), or 1 if y!=f(x)

% Another binary classification encoding includes using +1/-1 instead of
% 0/1.  In this case the f(x) is a signed function, hence the corresponding
% 0/1 loss is given as L(y,f(x) = abs(y-f(x))/2

% Of course these above methods should not be used blindly for
% classification problems and are domain-specific.

% Within machine learning there are two tasks - explination of the training
% data, and prediction of the new (test) data.  Using the notation above we
% can measure the quality of the explination through average fitting.
% R(emp) = (1/n)*sum(L(y,f(x) for all n) where n is the number of samples.

% At this point it is important to point out that n should be large to
% avoid the fallacy of small numbers, and that using "test data" to predict
% something that already occured is violating the rule of thumb that
% "hindsight is 20/20."  We are only estimating a model using test data and
% loss function estimation, not predicting.

% Empirical risk minimization is not the same as minimization of prediction
% risk.  Just because you built a model which has zero training error based
% upon the available data does not mean you built the most predictive
% model - you basically built something where hindsight was 20/20.

