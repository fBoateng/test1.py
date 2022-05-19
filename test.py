CI = int(input('Please enter the number of cars imported '))  # CI is cars imported
CS = int(input('Please input the number of cars sold '))  # CS is cars sold

RC = CI - CS

if RC < CS:
    print(str(RC) + ' remaining cars')

CI2 = int(input('Please enter the number of cars for year 2'))
CS2 = int(input('Please enter the number of cars sold for year 2 '))
RC2 = CI2 - CS2

if CS2 > RC2:
    print(str(RC2) + ' cars left')

CI3 = int(input('Please enter the number of cars imported for year 3 '))
CS3 = int(input('Please enter the number of cars sold for year 3 '))
RC3 = CI3 - CS3
if CS2 > RC2:
    print(str(RC3) + ' cars left')

CI4 = int(input('Please enter the number of cars imported for year 4 '))
CS4 = int(input('Please enter the number of cars sold for year 4 '))
RC4 = CI4 - CS4
if CS4 > RC4:
    print(str(RC4) + ' ' + 'cars left')


CI5 = int(input('Please enter the number of cars imported for year 5 '))
CS5 = int(input('Please enter the number of cars sold for year 5 '))
RC5 = CI5 - CS5
if CS5 > RC5:
    print(str(RC5) + ' cars left')


TCI = str(CI+CI2+CI3+CI4+CI5) + ' ' + 'total cars imported'
TCS = str(CS+CS2+CS3+CS4+CS5) + ' ' + 'total cars sold'
TRC = str(RC+RC2+RC3+RC4+RC5) + ' ' + 'Total remaining cars'


print(TCI)
print(TCS)
print(TRC)

if TCI > TCS:
    print('imported cars greater than sold cars')
    print(str(TCI) + ' ' + 'were imported')


if TCS < TCI:
    print('total cars sold is less than total cars imported')
    print(str(TCS) + ' ' + ' were sold')


if TCS > TRC:
    print('total cars sold is greater total cars remaining')
    print(str(TRC) + ' ' + 'are left')

