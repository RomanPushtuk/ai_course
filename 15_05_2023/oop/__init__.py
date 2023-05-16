class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def say_sound(self):
        print(f'{self.sound}')


class Dog(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def say_sound(self):
        print(f'{self.sound} + {self.name}')


class Cat(Animal):
    def __init__(self, *args):
        super().__init__(*args)


class Horse(Animal):
    def __init__(self, *args):
        super().__init__(*args)

# d = Dog('Bim', 'Gaf')
# d.say_sound()
