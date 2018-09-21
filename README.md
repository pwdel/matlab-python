# matlab-python
Converting various common Matlab statistical and machine learning tools into Python.

# Motivation and Background

## A Word on Matlab Python Translators

https://github.com/awesomebytes/libermate

# Contents

0. Installation Prerequisites
1.1. Generating Data Sets
1.2. Reading Data From Outside
1.2.1. Reading Data From CSV File
1.2.2. Reading Data From PostGres Database
2. General Encoding & Preprocessing
3. Two Types of Supervised Learning
4. Regression Using Parametric Modeling
5. Classification Using Parametric Modeling
6. K-Nearest Neighbor Regression
7. Piecewise Linear Regression

# Installation Prerequisites

## Python

* Using Python 3.5
pip install numpy
pip install matplotlib
sudo ipython -m pip install mpld3 # install javascript display for matplotlib charts

* Used Jupyter Notebook

## Matlab

Using Matlab 2017

## Displaying Matplotlib

# Data Sets - Generating, Displaying, Reading

## Generating Data Sets

We can generated data sets to play around with using random number functions.
What this allows us to do is quickly and easily generate dummy data for the purposes
of doing statistical analysis or various data science exercises.

# Data Encoding & Preprocessing
It is important to recognize first that the two most common types of input
and output values: numeric (such as speed, mass, volume) or categorical.

Categorical variables are not ordered nor defined by distance.

There is a third type known as an ordered categorical variable, which has
order but not distance.

Preprocessing includes scaling numerical data and ensuring that categorical
variables are uniform.  For numeric inputs and outputs, this may include simple
statistical analysis in order to better understand the data - removing outliers
for example.  It may also involve scaling, for example scaling all data into a
range from 1 to 0.

Some tools in this repo which are used in preprocessing may include:

2. numtype - comparing various data types between the two languages
3. matrixsize - sorting, shifting, and extracting pieces of a matrix


## Reading Data From Outside Source


# Two Types of Supervised Learning Tasks

Supervised learning is when the outputs of a function include direct, ground-truth
values, e.g. the answers to the output are given.  The "supervision," comes from
the fact that those output values, "supervise," the algorithm to make sure
it's performing well, in a sense, hence the name, "supervised learning."

1. Regression - where real valued function estimates are given, and the performance
of a prediction is measured usually by the square of a loss.
2. Classification - such as binary classification, where an indicator seperates
a space into two regions and classified the data points.  Performance of the
prediction in the case of binary classification is usually measured as either,
"right or wrong," for any given point.  Loss is calulated as "actual" vs.
predicted in this case - so it's all very application dependant.

Loss functions should not be blindly adopted for all applications.

# Regression Uing Parametric Modeling

# Regression Using Parametric Modeling
# Classification Using Parametric Modeling
# K-Nearest Neighbor Regression
# Piecewise Linear Regression
