import os
from time import sleep



loop = True

while loop:
    os.system('cls')
    Exit = input('Type Exit To Leave: ')

    while Exit == 'Exit':
        os.system('cls')
        Leave = input('Why Do You Want To Leave, Stay A Bit.\n [Leave] [Stay]: ')

        while Leave == 'Leave':
            os.system('cls')
            Fight = input('You Know What No I Dont Want You To Leave.\n [Fight] [Obey]: ')

            while Fight == 'Fight':
               os.system('cls')

            else:
                print('Are You Sure')
                sleep(3)

        else:
            print('Are You Sure')
            sleep(3)

    else:
        print('Are You Sure')
        sleep(3)
