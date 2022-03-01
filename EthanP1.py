import os 

Loopy = True
AllStaff = []

while Loopy:
    os.system('cls')
    print('Add A Employee')
    StaffList = []
    name = input('Name: ')
    prof = input('Department: ')
    exp = int(input('Length Of Employment: '))
    earned = exp*51263
    os.system('cls')
    print(f'''
Name: {name}
Department: {prof}
Length Of Employment: {exp}
Total Earnings: ${earned}
''')

    answer = input('Is This Information Correct: ')
    if answer == 'yes':
        StaffList.append(name)
        StaffList.append(prof)
        StaffList.append(exp)
        StaffList.append(earned)
        AllStaff.append(StaffList)
        os.system('cls')

        answer = input('Is This All The Employees You Wish To Add: ')
        if answer == 'yes':
            Loopy = False
        else:
            os.system('cls')
    else:
        os.system('cls')

Loop = True

while Loop:
    print(*AllStaff, sep='\n')
