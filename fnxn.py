def my_name(name):
    print(f'Hello from {name}')


my_name('Jon')
return_value = my_name('Jon')

print(return_value)


def welcome(name: str, age: int = 15):
    print(f'Welcome {name}, you are {age} years old')


def multiply(num: int, num2: int):
    print(num * num2)


multiply(5, 6)


def max(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z


def main():
    a = int(input('Please enter 1st number? '))
    b = int(input('Please enter 2nd number?'))
    c = int(input('Please enter 3rd number? '))
    largest = max(a, b, c)
    print(f'{largest} is the largest')


main()


def carea(radius):
    area = 3.14 * radius * radius
    print('Area of circle is', area)


l = 5
carea(l)


# factorial
def factorial(num=int) -> int:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


num = 10
f = factorial(num)
print(f'{num} factorial is {f}')


def any_args(*args):
    print(args)


any_args(1, 3, 5)

any_args('ball', 'sell', 123)


def score(name, level, *scores):
    n = input('Please enter a name: ')
    le = input('Please enter a level: ')
    s = input('Please enter your scores: ')
    print(n)
    print(le)
    print(s)


score('Jon', 100, 80, 45, 92, 60)


# n = input('Please enter a name: ').title()
# le = input('Please enter a level: ')
# s = input('Please enter your scores: ')


def score1(name, level, **scores):
    print('Name: ', name)
    print('Level: ', level)
    print('Scores: ', scores)
    for x, y in scores.items():
        print(f'{x} Score: {y}')


score1(name='Ron', level=1, Maths=6, English=5, History=7)
