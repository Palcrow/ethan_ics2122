from ast import Import


import os


Loopy = True
AllCharacters = []

while Loopy:
    CharList = []
    name = input('Name: ')
    CharList.append(name)
    prof = input('Class: ')
    CharList.append(prof)
    lvl = input('Level: ')
    CharList.append(lvl)
    AllCharacters.append(CharList)
    os.system('cls')
    print(f'''
Name: {name}
Class: {prof}
Level: {lvl}
''')

    answer = input('Is This All Character You Wish To Add: ')
    if answer == 'yes':
        Loopy = False
    else:
        os.system('cls')
        print('Ok These are Your Characters')

print(AllCharacters)
