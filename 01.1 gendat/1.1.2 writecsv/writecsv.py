import csv as csv

# write the below list, "A" into a csv file
A = [1,'HelloWorld']

with open('matrix.csv', 'w') as csvfile: # create a new csv file
    fieldnames = ['userId','name'] # create a list of field names
    # for each row of A to extract userId (value1) and pres (value2)
    csvRowdict = {'userId':A[0],'name':A[1]}
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(csvRowdict) # write all instances of the user into a row

# use a for loop to write each n items in a list to a csv file, row by row down one column

B = [1,2,3,4,5]

with open('column.csv', "w") as file:
    writer = csv.writer(file)
    """
    Note, if each item in the list is a string, we need [item] to feed csv reader
    an actual list element containing strings to work.  Or in our case [B[row]]

    Otherwise, each row of the csv will contain "s,t,r,i,n,g" as an example
    """
    for row in range(len(B)):
        writer.writerow([B[row]])
