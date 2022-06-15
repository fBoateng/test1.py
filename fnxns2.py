def area(l, b):
    a = l * b
    print(a)


area(5, 7)


def add_2(num1, num2, num3):
    adds = num1 + num2 + num3
    print(adds)


add_2(5, 3, 5)
add_2(-500, 70, 94)


def convert_temperature(c):
    f = c * 9 / 5 + 32
    return f


cel = float(input('Enter temperature in degrees Celsius? '))

farH = convert_temperature(cel)
print(f'{cel} degrees Celsius is equal to {farH} degrees Fahrenheit')


def intro(message):
    line_length = len(message) + 2
    print('*' * line_length)
    print(f'*{message}*')
    print('*' * line_length)


intro('Hello')
intro('ManUnited')


def intro2(message, num_times):
    for i in range(num_times):
        print(message)


intro2('Manchester United', 4)


def vowels(sentence):
    num_vowels = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels


sentence = input('Please write a sentence? ')
print('Number of vowels =', vowels(sentence))


def mystery(s, lst):
    s = s.upper()
    lst = lst + [2]


s = 'a'
lst = [1]
mystery(s, lst)

print(s, lst)



