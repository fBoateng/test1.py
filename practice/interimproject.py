# write a simple quiz app code in pycharm for a school

# entering answers for 1st quiz
ans1 = '1957'
ans2 = 'Accra'
ans3 = '4'
ans4 = 'Gold Coast'
ans5 = 'red'

# welcoming user and taking information
user = input(f'Welcome to quiz day. \nPlease enter the correct answer to the questions. \nPlease enter your name? ')
print(f'Welcome {user.title()}!, \nLets go ahead to the questions.')

# points obtained
points = 0

# question 1
q1 = 'What year did Ghana gain independence?'
print(q1)
a1 = input('Please enter your answer? ')
if a1 == ans1:
    print('Correct')
    points += 1
else:
    print('Incorrect')
    points = 0
    print(f'Total points gained is {points}')

# question 2
q2 = print('What is the capital of Ghana? ')
a2 = input('Please enter your answer? ')
if a2.title() == ans2:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 3
q3 = print('How many colors are in the Ghana flag?')

a3 = input('Please enter your answer? ')
if a3 == ans3:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 4
q4 = print('Ghana was formerly called?')
a4 = input('Please enter your answer? ')
if a4.title() == ans4:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 5
q5 = print('What is the first color of the Ghana flag?')

a5 = input('Please enter your answer? ')
if a5 == ans5:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

if points == 5:
    print(f'{user.title()}, you have done excellent!! \nYou scored a total of {points} points.')
elif points == 4:
    print(f'{user.title()}, you have done well!! \nYou scored a total of {points} points.')
elif points == 3 or 2:
    print(f'{user.title()}, try harder!! \nYou scored a total of {points} points.')
elif points == 1:
    print(f'{user.title()}, you have done poor!! \nYou scored a total of {points} points.')
else:
    print(f'{user.title()}, you have failed!! \nYou scored a total of {points} points. ')

# entering answers for 2nd quiz
answ1 = '3'
answ2 = '180'
answ3 = '8'
answ4 = '3'
answ5 = 'True'

# question 1
que1 = 'How many sides have a triangle'
print(que1)
Ans1 = input('Please enter your answer? ')
if Ans1 == answ1:
    print('Correct')
    points += 1
else:
    print('Incorrect')
    points = 0
print(f'Total points gained is {points}')

# question 2
que2 = print('The sum of the interior angles in a triangle is? ')
Ans2 = input('Please enter your answer? ')
if Ans2 == answ2:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 3
que3 = print('How many sides are in an octcagon?')

Ans3 = input('Please enter your answer? ')
if Ans3 == answ3:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 4
que4 = print('If 2 + X = 5 \nFind X')
Ans4 = input('Please enter your answer? ')
if Ans4 == answ4:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

# question 5
que5 = print('The sum of the interior angle of a circle is equal to that of a square? \nA)True \nFalse')

Ans5 = input('Please enter your answer? ')
if Ans5.title() == answ5:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

if points == 10:
    print(f'{user.title()}, you have done excellent!! \nYou scored a total of {points} points.')
elif 5 < points < 9:
    print(f'{user.title()}, you have done well!! \nYou scored a total of {points} points.')
elif 3 < points < 6:
    print(f'{user.title()}, try harder!! \nYou scored a total of {points} points.')
elif points == 1 or 2:
    print(f'{user.title()}, you have done poor!! \nYou scored a total of {points} points.')
else:
    print(f'{user.title()}, you have failed!! \nYou scored a total of {points} points. ')

answers4 = ['ride', 'fly', 'drive', 'sail', 'run']
# fill in the correct answers.
print('Fill in the the blanks with the following words:(Ride, Fly, Drive, Sail,Run) ')
que_1 = print('We _____ a bike everyday.')
ans_1 = input('Please choose your answer? ')

if ans_1 in answers4[0]:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

que_2 = print('I _____ a new sports car ')
ans_2 = input('Please choose your answer')

if ans_2 in answers4[2]:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

print('Fill in the the blanks with the following words:(Ride, Fly, Drive, Sail,Run) ')

que_3 = print('I _____ with Evans twice a week. ')
ans_3 = input('Please choose your answer')

if ans_3 in answers4[4]:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

que_4 = print('Pilots _____ aeroplanes ')
ans_4 = input('Please choose your answer')

if ans_4 in answers4[1]:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')


que_5 = print('Will you _____ with us in our ship? ')
ans_5 = input('Please choose your answer')

if ans_5 in answers4[3]:
    print('Correct')
    points += 1
else:
    print('Incorrect')
print(f'Total points gained is {points}')

if points == 15:
    print(f'{user.title()}, you have done excellent!! \nYou scored a total of {points} points.')
elif 10 < points < 15:
    print(f'{user.title()}, you have done well!! \nYou scored a total of {points} points.')
elif 7 < points < 10:
    print(f'{user.title()}, try harder!! \nYou scored a total of {points} points.')
elif 3 < points < 7:
    print(f'{user.title()}, try extra harder!! \nYou scored a total of {points} points.')
elif points == 1 or 2:
    print(f'{user.title()}, you have done poor!! \nYou scored a total of {points} points.')
else:
    print(f'{user.title()}, you have failed!! \nYou scored a total of {points} points. ')

print('You are done.')

