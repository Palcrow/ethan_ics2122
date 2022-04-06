deCode = input('Input Your Message: ')
shift = int(input('Amount Of Shifts: '))
deCode = deCode.upper()
punc = ('`~!@#$%^&*()-_=+[{]}\|;:,<.>/?')
msg = ''

for i in deCode:
    if i not in punc:
        letter = ord(i)
        if letter == 32:
            msg += chr(letter)
        else:
            letter = letter + shift
            if letter > 90:
                remainder = letter - 90
                letter = 65 + remainder
            msg += chr(letter)

print(msg)