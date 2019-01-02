def mymax(n1,n2,n3):
    # this function calculates the maximum of three numbers given as input
    max=n1
    if n1>max:
        max=n2
    elif n3>max:
        max=n3
    return max
