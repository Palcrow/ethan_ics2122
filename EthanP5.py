def amount(filename):
    f = open(filename, 'r')
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYV1234567890.,:;<>/?[{]}|\=+-_`~!@#$%^&*()\n '
    diction = {}
    msg = ''

    for line in f:
        msg += line

    for i in char:
        diction[i] = 0

    for i in msg:
        diction[i] += 1

    print(diction)
    f.close