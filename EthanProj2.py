#Done
def product(fileName):
    f = open(fileName, 'r')
    sum = 1
    for x in f:
        sum = sum * int(x)
    f.close
    return sum
