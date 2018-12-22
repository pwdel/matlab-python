# Read Data from a CSV File and Create Scatter Plot

import matplotlib
import matplotlib.pyplot as plt
import csv

# https://matplotlib.org/users/annotations_intro.html

filename = 'test.csv'
# Go to first column and extract value into list, skipping first row
with open(filename, mode='r') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    next(readCSV) # skip the first row (header) using next function
    x = []
    y = []
    for row in readCSV: # note, the list[1:] means first through rest of items
        x.append(row[0]) # grab the 0th element in the current row, put into x
        y.append(row[1]) # grab the 1st element in the current row, put into y


# Use List Comprehension To Turn Strings into float64 (double precision)
xflt = [ float(i) for i in x ]
yflt = [ float(i) for i in y ]

# Set up a figure with multiple spaces as subplots (1, 1) spaces
fig, ax = plt.subplots(nrows=1,ncols=1,sharex=True)

# set the overall title
ax.set_title('X vs Y')

# plot out on the top chart ax0
ax.scatter(xflt, yflt, label='X vs Y')

# automatically get handle labels
h1, l1 = ax.get_legend_handles_labels()

# place legends on chart
ax.legend(h1, l1)

# Set common labels with absolute positioning on chart
fig.text(0.5, 0.05, 'X Axis', ha='center', va='center')
fig.text(0.05, 0.5, 'Y Axis', ha='center', va='center', rotation='vertical')

plt.show()
