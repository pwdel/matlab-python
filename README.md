# matlab-python
Converting various common Matlab statistical and machine learning tools into Python.

- [Motivation and Background](#motivation-and-background)
  * [Personal Motivation](#personal-motivation)
  * [Origin and History of MATLAB vs. New Paradigm](#origin-and-history-of-matlab-vs-new-paradigm)
    + [Features and Advantages of MATLAB](#features-and-advantages-of-matlab)
    + [Disadvantages of MATLAB](#disadvantages-of-matlab)
  * [A Word on Matlab Python Translators](#a-word-on-matlab-python-translators)
    + [Additional Resources](#additional-resources)
      - [The Matrix Cheatsheet by Sebastian Raschka & Other Translation Guides](#the-matrix-cheatsheet-by-sebastian-raschka-other-translation-guides)
      - [Past Discussions on This Topic](#past-discussions-on-this-topic)
    + [Matlab and "Big Data"](#matlab-and-big-data-)
  * [Assumptions on Machine Used & Tool Prerequisites](#assumptions-on-machine-used-tool-prerequisites)
    + [Quick Note on Python and Containers](#quick-note-on-python-and-containers)
    + [Quote Note on Python and Online Notebooks](#quote-note-on-python-and-online-notebooks)
  * [Command Line Familiarity](#command-line-familiarity)
  * [Versioning (Old Notice)](#versioning-old-notice-)
  * [How I Put This Guide together](#how-i-put-this-guide-together)
  * [Installation Requirements to Run on Local server](#installation-requirements-to-run-on-local-server)
  * [Installation of libraries](#installation-of-libraries)
- [Installation of Prerequisites](#installation-of-prerequisites)
  * [Python](#python)
  * [Matlab](#matlab)
  * [Displaying Matplotlib](#displaying-matplotlib)
- [Data Sets - Generating, Displaying, Reading](#data-sets-generating-displaying-reading)
  * [Generating Data Sets](#generating-data-sets)
  * [Reading Data from Local Databases](#reading-data-from-local-databases)
    + [Reading Data From a CSV File](#reading-data-from-a-csv-file)
    + [Reading Data From a PostGres Database](#reading-data-from-a-postgres-database)
      - [Postgresql on Local Machine](#postgresql-on-local-machine)
        * [Matlab Version of "readpostgres"](#matlab-version-of-readpostgres-)
        * [Python Version of "readpostgres"](#python-version-of-readpostgres-)
- [Data Encoding & Preprocessing](#data-encoding-preprocessing)
  * [Tools Used In Preprocessing](#tools-used-in-preprocessing)
    + [01.1 Generating Data, Declaring variables](#011-generating-data-declaring-variables)
      - [Generating data in the form of random numbers to play around with, putting them into variables.](#generating-data-in-the-form-of-random-numbers-to-play-around-with-putting-them-into-variables)
    + [01.2 Reading Data](#012-reading-data)
      - [Reading data from files such as a CSV file](#reading-data-from-files-such-as-a-csv-file)
    + [02 Numeric Types](#02-numeric-types)
      - [Comparing numeric types whether integers, doubles, etc.  These types are best described in the Numpy documentation.](#comparing-numeric-types-whether-integers-doubles-etc-these-types-are-best-described-in-the-numpy-documentation)
    + [03 Matrix Work](#03-matrix-work)
      - [Python does not really have, "Matricies" as defined in MATLAB (which actually stands for Matrix-Lab). Discussion on some analogs.](#python-does-not-really-have-matricies-as-defined-in-matlab-which-actually-stands-for-matrix-lab-discussion-on-some-analogs)
        * [Using Numpy](#using-numpy)
        * [Using Pandas](#using-pandas)
    + [04 Plotting](#04-plotting)
    + [05 Performance](#05-performance)
    + [06 Functions](#06-functions)
    + [07 Classes](#07-classes)
    + [08 Tables](#08-tables)
    + [09 Cells](#09-cells)
    + [10 Control Statements](#10-control-statements)
      - [10.1 If Else Statements](#101-if-else-statements)
      - [10.2 Loops](#102-loops)
    + [11 Set Operations](#11-set-operations)
    + [12 Casting](#12-casting)
    + [13 Strings](#13-strings)
    + [14 Operators](#14-operators)
    + [15 Functions](#15-functions)
    + [16 Lambda](#16-lambda)
    + [17 Inheritance](#17-inheritance)
    + [18 Scope](#18-scope)
    + [19 Modules](#19-modules)
    + [20 Dates](#20-dates)
    + [30 Containers](#30-containers)
    + [31 Machine Learning Intro](#31-machine-learning-intro)
- [Two Types of Supervised Learning Tasks](#two-types-of-supervised-learning-tasks)
    + [32 Basic Stats](#32-basic-stats)
- [Regression Using Parametric Modeling](#regression-using-parametric-modeling)
- [Classification Using Parametric Modeling](#classification-using-parametric-modeling)
- [K-Nearest Neighbor Regression](#k-nearest-neighbor-regression)
- [Piecewise Linear Regression](#piecewise-linear-regression)

# Motivation and Background

This repo is created for those who are familiar with a Matlab background, but have an interest
in being able to do some of the same types of statistical computing and machine learning in Python.

## Personal Motivation

My personal motivation from this project comes from the fact that I studied electrical engineering,
which involved the use of Matlab.  As computing has inevitably become more powerful over the years,
the use of terms such as, "Machine Learning," and "Artificial Intelligence," has become democratized.
Yet fundamentally, all these terms really amount to is the ability to do math at volume.

The, "at volume" side of that statement has to do with the capability to deploy software onto a server.

## Origin and History of MATLAB vs. New Paradigm

Matlab was never really geared for being able be re-deployable, to work in a, "production" environment.

### Features and Advantages of MATLAB

* Academic, highly-maintained, highly structured.
* Designed with the PC era in mind which means individual contributors, focusing on mathematical models.  
* It's designed for the speed of the individual data scientist to be able to move quickly, without code getting in the way.


### Disadvantages of MATLAB

* Does not allow for cheap deployment and reproducibility, because you have to buy a license for each distribution.  
* This is in contrast to Python and open source data science tools, which while clunkier in terms of setup and lack of tools, can be infinitely used without the need for licensing.
* Some of the best, most interesting mathematical practitioners out there are trained in and fluent in
Matlab, but are not familiar with Python and its various tools.

It is my help that individuals may be able to use this repo as a guide to translate from MATLAB to Python and assist their careers and work.

## A Word on Matlab Python Translators

Some Matlab-Python translators exist, here are some of those which I have been able to find below.

1. https://github.com/victorlei/smop
    Appears to be continuously updated, high reputation score at 380+ stars.
2. https://github.com/awesomebytes/libermate
3. https://github.com/miaoever/Mat2py
4. https://github.com/buguen/mat2py

Translators are well and good, however my thought is that a fundamental understanding of the underlying computing and why certain technical decisions are made is superior to simply plugging things into a translator.  That being said, the above resources are provided depending upon your use case.

### Additional Resources

#### The Matrix Cheatsheet by Sebastian Raschka & Other Translation Guides

https://sebastianraschka.com/blog/2014/matrix_cheatsheet_table.html

http://mathesaurus.sourceforge.net/matlab-numpy.html

#### Past Discussions on This Topic

https://www.reddit.com/r/MachineLearning/comments/5x9tyi/r_which_libraries_to_learn_to_get_started_with_ml/
https://www.reddit.com/r/MachineLearning/comments/6h75h2/d_random_question_why_has_matlaboctave_not_been/


### Matlab and "Big Data"

"Big Data" is a fairly innocuous term, but generally it may be reasonable to define it as meaning
"files that do not fit into available memory."  One potential criticism of Matlab is that it does
not have the capability to expand beyond a single computer, and hence is not suitable for Big Data.
Of course, Matlab is actually an ecosystem and is constantly be developed by the Mathworks company.

* [Matlab Large Files and Big Data Tools](https://www.mathworks.com/help/matlab/large-files-and-big-data.html)

* [Working with Big Data in Matlab](https://www.mathworks.com/solutions/big-data-matlab.html)

In short, there are a wide variety of data types and storage systems that Matlab can handle.  This
guide is not meant to supplant Matlab, but rather to create understanding of the differences between
the two languages and available toolsets/libraries.

Some people may find Matlab useful, some people may find Python useful, for different types of projects.

## Assumptions on Machine Used & Tool Prerequisites

I used a Macbook Air 2015 for all of this, running OSX.  There may be some slight variations in tools and techniques used if you are on a different operating system.

### Quick Note on Python and Containers

This is important if you're going to build an app based upon the code that you're using, since much of webapps are built based upon linux distributions.  If you're not familiar, I recommend you check out [containers](https://www.docker.com/resources/what-container) for deploying and distributing to systems other than personal computers and laptops, which may be the level of familiarity that many working within the Matlab environment may start off with.

In short, MATLAB is essentially a complete package with a bunch of libraries and ways of accessing data installed.

Moving to python means you are working, "completely from scratch" and importing a bunch of tools which give you Matlab functionality.  To ensure that this works across mupltiple systems, you use containers to ensure consistency.

### Quote Note on Python and Online Notebooks

Aside from, "on-machine" methods of deploying Python, there are also Notebooks, such as Jupyter notebooks, which - once a container as the one mentioned above is installed, provide a fast and easy way to write and notate code and psuedocode while playing around.

The next level up from this would be online versions of Notebooks, such as:

* [Microsoft Azure Notebooks - Jupyter Notebooks](https://notebooks.azure.com/help/jupyter-notebooks)
* [Gooogle Colab](https://colab.research.google.com/)
* ...And other alternatives which you could look for yourself!


## Command Line Familiarity

All of the commands and ssh work mentioned were done using the command line (terminal).  You will need a basic familiarity with using a machine command terminal for the following.

## Versioning (Old Notice)

This may be old information for many, but I'm putting this here just in case...

* If you're not familiar with Python or various open source computing languages, you should know that there are various versions of Python, the most common of which are Python 2 and Python 3.
* Python 2 is being retired in 2020 permanently and will not be maintained.  So it is recommended to upgrade and use Python 3 and do not use Python 2 at all.

## How I Put This Guide together

Basically, I have a high familiarity with MATLAB for having worked with it for years, having done a wide variety of data science projects over time including image processing. Typically I would learn about Matlab, and indeed new forms of mathematics that I had not heard about by reading the Matlab documentation and user forums on Mathworks.  Having taken a class during undergraduate back in 2006 taught by Vladimir Cherkassky I compiled some of the thoughts from the book:

Then, I researched various machine learning tools embedded within Python by reading various "top data science toolkits for python" articles such as [this one](https://medium.com/activewizards-machine-learning-company/top-20-python-libraries-for-data-science-in-2018-2ae7d1db8049).

Over time I built in additional fundamentals through some of my own, separate, closed source programming in Python as I went along.

I also got recommendations for toolkits to look into from various friends who work in data science, including [Mike Semeniuk](https://twitter.com/mikhailsemeniuk).

## Installation Requirements to Run on Local server

Requirements:

* python3

* Numpy
  Numpy is a library within Python that allows for the matrix-style manipulation of numbers inherent in Matlab.

* SciPy
  Scipy is a library within Python that allows various types of linear algebra, as well as compiling into C++.

* Scikit-Learn


* Pandas
  Pandas or Python ANalysis of DAta library allows some of the tabular data structure functionality of Matlab.

* Matplotlib
  Matplotlib is basically a plotting library within Python, allows you to do graphs.

* PostGresql
  PostGreSQL is a simple, widely known dynamic database.
  [PostGreSQL Installation Documentation](https://www.postgresql.org/docs/10/tutorial-install.html)

* MySQL
  MySQL is a widely known dynamic database.
  [Guide to Install MySQL with Hombrew](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)
  [Download Community Version](https://dev.mysql.com/downloads/mysql/)


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

# Installation of Prerequisites

## Python

* Using Python 3.6
Setup Anaconda Environment for Python3
pip install numpy
pip install matplotlib
sudo ipython -m pip install mpld3 # install javascript display for matplotlib charts

* Use Jupyter Notebook with Python3 Anaconda Environment.

## Matlab

Using Matlab 2017, Student Version.

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

In order to use this database, you have to buy the Matlab database package.  We're not going to
go through how to use this here.

##### Python Version of "readpostgres"

We use the most popular PostGresql Python module, psycopg -  http://initd.org/psycopg/download/
Download and install as shown:

$ pip install -U pip # make sure to have an up-to-date pip
$ pip install psycopg2

To install the Python3 version, use:

$ pip3 install psycopg2

# Data Encoding & Preprocessing

Within Machine Learning, a lot of the, "basic computational stuff" that one learns in a beginner computer science class - meaning the control statements such as, "if, statements, for loops, while loops, etc." - as well as data types, functions, types of arrays, classes, - the bread and butter which might normally be defined as, "software programming" - might be referred to by a Machine Learning enthusiast as, "Data Encoding and Preprocessing."

To a Machine Learning practitioner, they may define input and output values in a couple different ways:

* Numeric variables which have a value such as speed, mass, volume or...
* Categorical variables which are not ordered nor defined by distance such as A, B, Left, Right, Orange, Blue, Nice, Mean.
* There is a third type known as an ordered categorical variable, which has order but not distance, such as A1, A2, A3 or Fast, Medium, Slow.

Preprocessing includes scaling numerical data and ensuring that categorical variables are uniform.  For numeric inputs and outputs, this may include simple statistical analysis in order to better understand the data - removing outliers for example.  It may also involve scaling, for example scaling all data into a range from 1 to 0.

## Tools Used In Preprocessing

Preprocessing Tools are organized by folders in this Repo.  We are basically just going straight down the line in terms of letting individuals know what types of tools are available and what the analog between Python and MATLAB are.

### 01.1 Generating Data, Declaring variables

#### Generating data in the form of random numbers to play around with, putting them into variables.

### 01.2 Reading Data

#### Reading data from files such as a CSV file

### 02 Numeric Types

#### Comparing numeric types whether integers, doubles, etc.  These types are best described in the Numpy documentation.

### 03 Matrix Work

#### Python does not really have, "Matricies" as defined in MATLAB (which actually stands for Matrix-Lab). Discussion on some analogs.

##### Using Numpy

We wrote some examples using Numpy.  Numpy is good for arrays and creating what are known as, "numbered array."  While Matlab arrays are immediately understood to be numerical arrays, an, "Array" within python is more like a regular "computer programming" array that contains a bunch of values, but it's not necessarily optimized or set up well for doing math.  That's what the plugin, "Numpy" is for.  Numpy includes what are known as, "numbered arrays" or "ndarray" - which have easily accessible values and all sorts of other features much more similar to how Matlab functions.

##### Using Pandas

Pandas is a seperate plugin, which works in conjunction with Numpy, but allows one to much more easily work with the whole, "Matrix" concept.  Conceptually, Pandas is more like a set of Worksbook Spreadsheets, with cells that cannot be merged - so a bit more like Structs in Matlab.

This seems to be, at the time of writing, the crux between the difference between Matlab and Python - while Python or Python/Pandas is not immediately set up with the assumption that you are immediately going to do math, it does give the ability to work with what in Matlab would be known as Structs or Cells.

Within Matlab, a Matrix must be homogenous in terms of the type of data within it - which hypothetically could reduce errors.  In Python, you may need to write tests to ensure that the data you are using across different values is consistent.  Matlab will allow you to immediately test A*B and tell you whether it will work and if not why not from a numerical type standpoint.  Python may have a bunch of other errors that you may have to read through and deal with.

Structs and Cells take a bit more coding and thinking to work with, but not a whole lot - and they give more flexibility with the capability to use dot notation to apply functions to them.  While Matricies in Matlab are super easy to just get going with, leaving, "less in the way" between the user and Math, there are

* Matrix Sizing

### 04 Plotting

### 05 Performance

### 06 Functions

### 07 Classes

### 08 Tables

### 09 Cells

### 10 Control Statements

#### 10.1 If Else Statements

#### 10.2 Loops

### 11 Set Operations

### 12 Casting

### 13 Strings

### 14 Operators

### 15 Functions

### 16 Lambda

### 17 Inheritance

### 18 Scope

### 19 Modules

### 20 Dates

### 30 Containers

### 31 Machine Learning Intro

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

### 32 Basic Stats

# Regression Using Parametric Modeling


# Classification Using Parametric Modeling
# K-Nearest Neighbor Regression
# Piecewise Linear Regression
