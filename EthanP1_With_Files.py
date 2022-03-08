import os
import string

Loopy = True
f = open('Staff.txt', 'a')

while Loopy:
    os.system('cls')
    print('Add A Employee')
    name = input('Name: ')
    prof = input('Department: ')
    exp = int(input('Length Of Employment (Number Only): '))
    earned = exp*51263
    os.system('cls')
    print(f'''
Name: {name}
Department: {prof}
Length Of Employment: {exp}
Total Earnings: ${earned}
''')

    answer = input('Is This Information Correct\n [Yes] [No]: ')
    if answer == 'Yes':
        f.write(name)
        f.write('\n')
        f.write(prof)
        f.write('\n')
        f.write(str(exp))
        f.write('\n')
        f.write(str(earned))
        f.write('\n')
        os.system('cls')

        Answer = input('Is This All The Employees You Wish To Add\n [Yes] [No]: ')
        if Answer == 'Yes':
            f.close()
            os.system('cls')
            Loopy = False
        else:
            os.system('cls')
    else:
        os.system('cls')
