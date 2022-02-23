import os 

Loopy = True
AllCharacters = []

while Loopy:
    os.system('cls')
    print('Add A Employee')
    CharList = []
    name = input('Name: ')
    prof = input('Profession: ')
    exp = input('Experiance: ')
    os.system('cls')
    print(f'''
Name: {name}
Profession: {prof}
Experiance: {exp}
''')

    answer = input('Is This Information Correct: ')
    if answer == 'yes':
        CharList.append(name)
        CharList.append(prof)
        CharList.append(exp)
        AllCharacters.append(CharList)
        os.system('cls')

        answer = input('Is This All The Employees You Wish To Add: ')
        if answer == 'yes':
            Loopy = False
        else:
            os.system('cls')
    else:
        os.system('cls')

print(AllCharacters)
