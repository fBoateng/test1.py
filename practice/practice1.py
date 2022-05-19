num = int(input('Enter a number? '))

if num % 2 == 0:
    print('It\'s an even number.')
else:
    print('It\'s an odd number.')

num1 = int(input('Enter a number? '))
num2 = int(input('Enter another number? '))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('Wrong entry.')

num1 = int(input('Enter a number? '))
num2 = int(input('Enter another number? '))
if num1 > num2:
    print(num1, 'is greater than ', num2)
else:
    print(num2, 'is greater than', num1)

nbr = int(input('Enter a number?'))
nbr1 = int(input('Enter a number?'))
nbr2 = int(input('Enter a number?'))

if nbr > nbr1 or nbr > nbr2:
    print(nbr, 'is greater than', nbr1, 'and', nbr2)
elif nbr1 > nbr or nbr > nbr2:
    print(nbr1, 'is greater than', nbr, 'and', nbr2)
elif nbr2 > nbr or nbr2 > nbr1:
    print(nbr2, 'is greater than', nbr, 'and', nbr1)


yr = int(input('Please input a year? '))
if yr % 4 == 0:
    print('It\'s a leap year.')
elif yr % 100 == 0 and yr % 400 == 0:
    print('It\'s a leap year.')
else:
    print('Not a leap year')


day = int(input('Please enter a number from 1-7?'))
if day == 1:
    print('1 is Monday')
elif day == 2:
    print('2 is Tuesday')
elif day == 3:
    print('3 is Wednesday.')
elif day == 4:
    print('4 is Thursday.')
elif day == 5:
    print('5 day is Friday.')
elif day == 6:
    print('6 is Saturday.')
elif day == 7:
    print('7 is Sunday.')
else:
    print('There only 7 days in the calender')






