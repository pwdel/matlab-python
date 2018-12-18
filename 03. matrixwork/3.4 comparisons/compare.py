a = [1, 2, 3, 5, 0]
b = [9, 8, 7, 6, 5]

# fastest performance way to simply find matches, output will be a set
set(a).intersection(b)

# slower way to do it
set(a) & set(b)

# if order is significant, it has to be a for loop (slower)
# output for the following will be nill if comparing a, b above
[i for i, j in zip(a, b) if i == j]

# however comparing a, c we get an output
c = [9, 8, 7, 5, 2]
[i for i, j in zip(a, c) if i == j]

# to get the position of the index of each element
indexlist = []
for i in range(len(a)): # within the range of length of a
    if a[i] == c[i]: # for the point where they are equal
        indexlist.append(i) # append to our indexlist above

output = 'the location of the common values is at index ' + str(indexlist) + ' and the value there is ' + str(a[indexlist[0]])
print(output)

# Pulling those locations out of the original matrix to make a new matrix
temperature0 = [temperature[i] for i in room0]
