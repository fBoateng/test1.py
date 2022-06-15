class Canis:
    def __init__(self, sound, habitat):
        self.sound = sound
        self.habitat = habitat

    def canivore(self):
        return True


class Dog(Canis):
    def __init__(self, sound, habitat):
        super().__init__(sound, habitat)


class Wolf(Canis):
    def __init__(self, sound, habitat):
        super().__init__(sound, habitat)

    def tame(self):
        return False

    def __repr__(self):
        return f'{self.sound}'

    def __str__(self):
        return f'{self.habitat}'



dog1 = Dog('bark', 'dog pound')
print(f'Dogs {dog1.sound}')

wolf1 = Wolf('howl', 'woods')
print(wolf1.tame(), dog1.habitat, wolf1.sound)


print(f'{wolf1.__repr__()}')
print(f'{wolf1.__str__()}')