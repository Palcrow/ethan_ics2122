import os
from time import sleep


def menu():
    
    notDone = True
    while notDone:
        os.system('cls')
        global fileName
        fileName = 'Adminastration.txt'
        gui = '\nWhat Do You Wish To Do?\n'
        gui += ' 1. Add New Teacher.\n'
        gui += ' 2. Display Newest Working Teacher.\n'
        gui += ' 3. Display Oldest Working Teacher.\n'
        gui += ' 4. Display All Teachers\n'
        gui += ' 0. Exit the program.\n'
        print(gui)
        choice = input(': ')
        if choice == '1':
            addStaff()
        elif choice == '2':
            newStaff()
        elif choice == '3':
            oldStaff()
        elif choice == '4':
            allStaff()
        elif choice == '0':
            notDone = False

def addStaff():
    loop = True
    while loop:
        f = open(fileName, 'a')
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
            f.write(f'Name: {name}  Department: {prof}  Length Of Employment: {exp}  Earnings: ${earned}\n')
            allDone = input('Is This All The Employees You Wish To Add\n [Yes] [No]: ')
            if allDone == 'Yes':
                loop = False
                os.system('cls')
            else:
                os.system('cls')
        else:
            os.system('cls')
    f.close()

def newStaff():
    os.system('cls')
    f = open(fileName, 'r')
    for x in f:
        pass
    last_line = x
    print(last_line)
    sleep(30)
    f.close

def oldStaff():
    os.system('cls')
    f = open(fileName, 'r')
    print(f.readline())
    sleep(30)
    f.close

def allStaff():
    os.system('cls')
    f = open(fileName, 'r')
    for x in f:
        print(x, end = '')
    sleep(30)
    f.close
