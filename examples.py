n = input('Please enter a name: ')
a = int(input('Please enter the age: '))
t = int(input('Please enter the patient\'s temperature: '))


class Patient:
    def __init__(self, n, a, t):
        self.name = n
        self.age = a
        self.temperature = t

    def display(self):
        print(f'Hello {n}')
        print(f'Your age is {a} years old.')
        print(f'Your body temperature is {t} degrees celsius')


p1 = Patient(n, a, t)
p1.name
p1.age
p1.temperature
p1.display()


class Student:
    def __init__(self, name, age, **scores):
        self.name = name
        self.age = age
        self.scores = scores

    def display(self):
        print('Hello', self.name)
        print('You are', self.age)
        print('You had', self.scores)

    def marks(self):
        for x, y in self.scores.items():
            print(f'{x} Score: {y} marks')

    def averages(self):
        y = self.scores.values()
        y1 = sum(y) / 4
        print(f'Your average score is {y1} ')
        if y1 <= 10:
            print('You have failed.')
        else:
            print('You have passed.')


s_1 = Student(name='Willow', age=12, maths=20, history=18, spelling=15, comprehension=12)
s_1.display()
s_1.marks()
s_1.averages()
print('------------')
print('------------')

s_2 = Student(name='Will', age=13, maths=20, history=18, spelling=19, comprehension=11)
s_2.display()
s_2.marks()
s_2.averages()
print('------------')
print('------------')

s_3 = Student(name='Paul', age=15, maths=9, history=18, spelling=10, comprehension=7)
s_3.display()
s_3.marks()
s_3.averages()

print('------------')
print('------------')

s_4 = Student(name='Wendy', age=15, maths=15, history=10, spelling=10, comprehension=17)
s_4.display()
s_4.marks()
s_4.averages()
