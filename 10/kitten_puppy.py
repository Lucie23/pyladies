class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {}!".format(self.name, food))


class Kitten(Animal):    
    def make_sound(self):
        print("{}: Meow!".format(self.name))
    
    def eat(self, food):
        print("({}: looks at {}.)".format(self.name, food))
        super().eat(food)

class Snek(Animal):
    def __init__(self, name):
        name = name.replace('s', 'sss')
        name = name.replace('S', 'SSS')
        super().__init__(name)

class Puppy(Animal):   
    def make_sound(self):
        print("{}: Woof!".format(self.name))

animals = [Kitten('Micka'), Puppy('Azorek')]

for animal in animals:
    animal.eat('meat')
    animal.make_sound()

micka = Kitten('Micka')
azorek = Puppy('Azorek')
micka.eat('granule')
azorek.eat('bone')
standa = Snek('Stanislav')
standa.eat('mouse')
