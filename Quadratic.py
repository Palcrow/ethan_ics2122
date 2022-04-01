a = int(input('Enter Value For A: '))
b = int(input('Enter Value For B: '))
c = int(input('Enter Value For C: '))

division = 2*a

if b**2-4*a*c > 0:
    print('No Roots')
elif b**2-4*a*c == 0:
    root = -b/division
    print(f'One Root At {root}')
