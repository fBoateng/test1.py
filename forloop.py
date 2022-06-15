myList = [1, 2, 3, 4, 5]
for item in myList:
    if item % 2 == 0:
        print(f'{item} is even.')
    elif item % 2 != 0:
        print(f'{item} is odd.')

my_str = 'abcdefgh'
for letter in my_str:
    print(letter)

s = {'Fred': 24, 'Will': 21, 'John': 22}
for key in s:
    print(key)
    for key, age in s.items():
        print(f'{key}s age is {age}')

my = [1, 2, 3, 4, 5]
for num in my:
    print(f'{num} * 5 = ', num * 5)

mytuple = [(1, 'car'), (2, 'bicycle'), (3, 'train')]
for item in mytuple:
    print(item)

mytuple = [(1, 'car'), (2, 'bicycle'), (3, 'train')]
for number, item in mytuple:
    print(f'{number} {item}')

for i in 'justice':
    print(i)


