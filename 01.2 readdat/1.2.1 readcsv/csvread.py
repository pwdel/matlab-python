# import the CSV module
import csv

# Open the test.csv file in read mode as variable csv_file, printing column names
filename = 'test.csv'
with open(filename, mode='r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    lineCount = 0
    numRows = 0
    for row in csvReader:
        numRows += 1 # iterate the number of rows counter
        if lineCount == 0: # on the first row
            print(f'Column names are {", ".join(row)}')
            lineCount += 1 # exit lineCount


# Go to first column and extract value into list, skipping first row
with open(filename, mode='r') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    next(readCSV) # skip the first row (header) using next function
    x = []
    for row in readCSV: # note, the list[1:] means first through rest of items
        currRow = row[0]
        x.append(str(currRow))
