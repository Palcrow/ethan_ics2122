#https://github.com/greendar/ics3_2122
  
import os 

Loopy = True
AllStaff = []

while Loopy:
    os.system('cls')
    print('Add A Employee')
    StaffList = []
    name = input('Name: ')
    prof = input('Profession: ')
    exp = input('Length Of Employment: ')
    os.system('cls')
    print(f'''
Name: {name}
Profession: {prof}
Length Of Employment: {exp}
''')

    answer = input('Is This Information Correct: ')
    if answer == 'yes':
        StaffList.append(name)
        StaffList.append(prof)
        StaffList.append(exp)
        AllStaff.append(StaffList)
        os.system('cls')

        answer = input('Is This All The Employees You Wish To Add: ')
        if answer == 'yes':
            Loopy = False
            os.system('cls')
        else:
            os.system('cls')
    else:
        os.system('cls')

print(AllStaff)

