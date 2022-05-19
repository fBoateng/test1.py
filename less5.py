'''a = input('Please enter your name ')
s = str(a)

c = input('Please enter a number ')
v = int(c)

q = input('Please enter a number ')
w = int(q)

print(v + w)

add = v+w
print(add)

ch = input('Enter a char ')
print(ch[3])

sd = input('Enter a char ')[2]
print(sd)

result = eval(input('Enter an expression '))
print(result)'''

'''CI = int(input('Please enter the number of cars imported '))  # CI is cars imported
CS = int(input('Please input the number of cars sold '))  # CS is cars sold

RC = CI - CS

if RC < CS:
    print(str(RC) + 'remaining cars')'''

'''i = 300
j = 400

while i >= 300:
    print('Good ', i)
    while j > 200:
        print('finished')

i= i-1
print()'''

'''songtitle1 = input('Please enter a song title?')
songtitle2 = input('Please enter a song title?')
songtitle3 = input('Please enter a song title?')
songtitle4 = input('Please enter a song title?')


madlib = f'Kanye West said no one man can have all that {songtitle1} \
so he decided to {songtitle2}, just because Eminem said he was {songtitle3}. \
After learning about {songtitle4} from Michael Jackson.'

print(madlib)'''

a = int(input('Enter a number? '))
for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(i, '*', j, '=', i * j)
    print('')

num = int(input('Please enter a number'))
i = 1
while i <= 12:
    print(num, 'x', i, '=', num * 1)
    i += 1
