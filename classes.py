'''class Ball:
    def __int__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight


beach_ball = Ball()

print(beach_ball)

print(f'My ball is {beach_ball.color} and weighs {beach_ball.weight} grams.')'''


class Ball:
    def __init__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight


beach_ball = Ball('White', 45, 2.6)
print(beach_ball)
print(f'My ball is {beach_ball.color} and weighs {beach_ball.weight} grams.')
print(f'My ball weighs {beach_ball.weight} grams and {beach_ball.size} cm cube')


class Mammals:
    def __init__(self, sound):
        self.sound = sound


dog = Mammals('bark')
wolf = Mammals('howl')
print(f'Dogs {dog.sound} and wolves {wolf.sound} ')


class Ball:
    def __init__(self, color, size, weight):
        self.color = color
        self.size = size
        self.weight = weight


football = Ball('black and white', 25, 10)
basketball = Ball('orange', 25, 20)

print(f'Basketballs are {basketball.color} and footballs are {football.color}')


class Vehicles:
    def __init__(self, make, brand, model):
        self.brand = brand
        self.model = model
        self.type = make


def color():
    return 'Ash'


class BMW(Vehicles):
    def __init__(self, make, brand, model):
        super().__init__(make, brand, model)

    def drive(self):
        return True


car = Vehicles('Sedan', 'BMW', 'X1')
print(f'The car dealership is selling {car.brand} {car.model}')

new_car = BMW('X1', 'SUV', 'BMW')
car_color = color()
print(f'My new car is {car_color} and it\'s an {new_car.brand}')
