def encrypt(fileName, shifts):
    f = open(fileName, 'r')
    turns = int(shifts)
    punc = {96,126,33,64,35,36,37,94,38,42,40,41,45,95,61,43,91,123,93,125,59,58,44,60,46,62,47,63,32}
    msg = ''
    code = ''
    for line in f:
        code += line
    code = code.upper()
    for i in code:
        letter = ord(i)
        if letter in punc:
            msg += chr(letter)
        else:
            letter = letter + turns
            if letter > 90:
                remainder = letter - 90
                letter = 65 + remainder
            msg += chr(letter)
    
    print(msg)
