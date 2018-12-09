# matlab-python
Converting various common Matlab statistical and machine learning tools into Python.

# Motivation and Background

This repo is created for those who are familiar with a Matlab background, but have an interest
in being able to do some of the same types of statistical computing and machine learning in Python.

My personal motivation from this project comes from the fact that I studied electrical engineering,
which involved the use of Matlab.  As computing has inevitably become more powerful over the years,
the use of terms such as, "Machine Learning," and "Artificial Intelligence," has become democratized.
Yet fundamentally, all these terms really amount to is the ability to do math at volume.

The, "at volume" side of that statement has to do with the capability to deploy software onto a server.

Matlab was never really geared for being able be re-deployable, it's an academic, highly-maintained
statistical computing software from the 80s, designed with the PC era in mind.  It's designed for the
speed of the individual data scientist to be able to move quickly, without getting in the way.
However, it does not allow for deployment and reproducibility, because you have to buy a license
for each distribution.  This is in contrast to Python and open source data science tools, which while
clunkier in terms of setup and lack of tools, can be infinitely used without the need for licensing.

Some of the best, most interesting mathematical practitioners out there are trained in and fluent in
Matlab, but are not familiar with Python and its various tools.

It is my help that individuals may be able to use this repo as a guide to translate from MATLAB
to Python and assist their careers and work.

## A Word on Matlab Python Translators

Some Matlab-Python translators exist, here are some of those which I have been able to find below.

1. https://github.com/victorlei/smop
    Appears to be continuously updated, high reputation score at 380+ stars.
2. https://github.com/awesomebytes/libermate
3. https://github.com/miaoever/Mat2py
4. https://github.com/buguen/mat2py

Translators are well and good, however my thought is that a fundamental understanding
of the underlying computing and why certain technical decisions are made is superior to simply
plugging things into a translator.  That being said, the above resources are provided
depending upon your use case.

## Assumptions on Machine Used & Tool Prerequisites

I used a Macbook Air 2015 for all of this, running OSX.  There may be some slight
variations in tools and techniques used if you are on a different operating system.

### Quick Note on Python and Containers

This is important if you're going to build an app based upon the code that you're using,
since much of webapps are built based upon linux distributions.  If you're not familiar,
I recommend you check out [containers](https://www.docker.com/resources/what-container)
for deploying and distributing to systems other than personal computers and laptops,
which may be the level of familiarity that many working within the Matlab environment may start off with.

In short, MATLAB is essentially a complete package with a bunch of libraries and ways
of accessing data installed.

Moving to python means you are working, "completely from scratch" and importing a bunch
of tools which give you Matlab functionality.  To ensure that this works across mupltiple
systems, you use containers to ensure consistency.

## Command Line Familiarity

All of the commands and ssh work mentioned were done using the command line (terminal).
You will need a basic familiarity with using a machine command terminal for the following.

If you're not familiar with Python, you should know that there are various
versions of Python, the most common of which are Python 2 and Python 3.
Python 2 is being retired in 2020 permanently and will not be maintained.
So it is recommended to upgrade and use Python 3 and do not use Python 2 at all.

## Installation Requirements

Requirements:
* python3
* pip3 (which is the Python 3 version).
* Homebrew.
* Anaconda & setup of Python environments
* Jupyter notebook and use of proper environments - particularly the python3 environment.

## Installation of libraries

You must install the following from ssh using the following commands:

* Python3 [documentation](https://docs.python.org/3/)
* Numpy [documentation](https://docs.scipy.org/doc/)
pip3 install numpy
* Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/)
pip3 install pandas

# Contents

0. Installation of Prerequisites
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

# Installation of Prerequisites

## Python

* Using Python 3.6
Setup Anaconda Environment for Python3
pip install numpy
pip install matplotlib
sudo ipython -m pip install mpld3 # install javascript display for matplotlib charts

* Use Jupyter Notebook with Python3 Anaconda Environment.

## Matlab

Using Matlab 2017

## Displaying Matplotlib

# Data Sets - Generating, Displaying, Reading

## Generating Data Sets

We can generated data sets to play around with using random number functions.
What this allows us to do is quickly and easily generate dummy data for the purposes
of doing statistical analysis or various data science exercises.

## Reading Data from Local Databases

### Reading Data From a CSV File

Reading from a CSV File is a simple, well-known way of grabbing data for analysis
purposes within the Matlab world.  Examples on how to do this are shown in:

1.2.1 readcsv

This file allows you to read a csv file of arbitrary length

### Reading Data From a PostGres Database

Using a dynamic database server environment is the more established way of
working with data in a "server type" environment.  Here we're showing an example
using PostGres since it is a well-known, easy to use database in web and cloud.

#### Postgresql on Local Machine

To get a PostGres Database set up locally on your machine, you can simply use
the installation from a command line:

(using HomeBrew https://brew.sh/)

$ brew update
$ brew doctor
$ brew install postgres

To maniuplate a postgres database, you can use a simple free program known as Postico.

https://eggerapps.at/postico/

To start a sample database on your machine, you can use the command:

$ brew services start postgresql

The word "start" is the operative word here. You can also use "restart" to start the service.

After you have started a server, you can connect to it via Postico.

1. Create a new Database - matlab-Python
2. Create a new Table - sample
3. Decide columns, names and types.  (datatypes here https://www.w3schools.com/sql/sql_datatypes.asp)
4. Edit content directly within Postico.

Analysis of Speed of Insertation into PostGresql database
https://alliedtesting.github.io/pgmex-blog/2017/06/29/performance-comparison-of-postgresql-connectors-in-matlab-part-I/


##### Matlab Version of "readpostgres"

sqlwrite
https://www.mathworks.com/help/database/ug/database.odbc.connection.sqlwrite.html


##### Python Version of "readpostgres"

We use the most popular PostGresql Python module, psycopg -  http://initd.org/psycopg/download/
Download and install as shown:

$ pip install -U pip # make sure to have an up-to-date pip
$ pip install psycopg2

To install the Python3 version, use:

$ pip3 install psycopg2

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

# Regression Using Parametric Modeling

# Regression Using Parametric Modeling
# Classification Using Parametric Modeling
# K-Nearest Neighbor Regression
# Piecewise Linear Regression
