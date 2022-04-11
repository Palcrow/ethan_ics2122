def encrypt(fileName, shifts):
    f = open(fileName, 'r')
    turns = int(shifts)
    punc = ('`~!@#$%^&*()-_=+[{]}\|;:,<>/?.')
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
            elif letter == 10:
                msg += chr(letter)
            else:
                letter = letter + turns
                if letter > 90:
                    remainder = letter - 90
                    letter = 65 + remainder
                msg += chr(letter)

    print(msg)
