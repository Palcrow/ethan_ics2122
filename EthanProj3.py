#Done
a = int(input('Enter Value For A: '))
if a == 0:
    print('Cant Be 0')
else:
    b = int(input('Enter Value For B: '))
    c = int(input('Enter Value For C: '))

    division = 2*a

    if b**2-4*a*c < 0:
        print('No Roots')
    elif b**2-4*a*c == 0:
        root = -b/division
        print(f'One Root At {root}')
    else:
        sr = (b**2-4*a*c)**0.5
        pSum = -b+sr
        nSum = -b-sr
        print(f'One Root At {pSum/division}\nAnd One Root At {nSum/division}')
