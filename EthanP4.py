def encrypt(fileName, shifts):
    global nameFile
    global turns
    nameFile = fileName
    turns = int(shifts)
    wantPunc = input('Remove Punctuation [Yes] [No]: ')
    if wantPunc == 'Yes':
        withPunc()
    else:
        noPunc()

def withPunc():
    f = open(nameFile, 'r')
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

def noPunc():
    f = open(nameFile, 'r')
    punc = ('`~!@#$%^&*()-_=+[{]}\|;:,<.>/?')
    msg = ''
    code = ''
    for line in f:
        code += line
    code = code.upper()
    for i in code:
        if i not in punc:
            letter = ord(i)
            if letter == 32:
                msg += chr(letter)
            else:
                letter = letter + turns
                if letter > 90:
                    remainder = letter - 90
                    letter = 65 + remainder
                msg += chr(letter)
