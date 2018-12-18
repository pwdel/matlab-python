import csv as csv

# write the below list, "A" into a csv file
A = [1,'HelloWorld']

with open('matrix.csv', 'w') as csvfile: # create a new csv file
    fieldnames = ['userId','name'] # create a list of field names
    # for each row of A to extract userId (value1) and pres (value2)
    csvRowdict = {'userId':A[0],'name':A[1]}
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(csvRowdict) # write all instances of the user into a row

# use a for loop to write each n items in a list to a csv file, row by row
