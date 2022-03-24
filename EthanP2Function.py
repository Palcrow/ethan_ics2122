fileName = 'numbers.txt'
otherFileName = 'numbers2.txt'

def product():
    f = open(fileName, 'r')
    num1 = int(f.readline())
    num2 = int(f.readline())
    num3 = int(f.readline())
    sum = num1 * num2 * num3
    print(sum)

def unknownProduct():
    f = open(otherFileName, 'r')
    sum = 1
    for x in f:
        sum = sum * int(x)
    print(sum)
