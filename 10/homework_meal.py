class Meal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} are tasty.".format(food))

class breakfast(Meal):
    def food(self):
        print('{} are healthy.'.format(self.name))

class dinner(Meal):
    def food(self):
        print('{} are from Italian cuisine.'.format(self.name))

Cornflakes = breakfast('Cornflakes')
Pasta = dinner('Pasta')

Cornflakes.eat('Cornflakes')
Pasta.eat('Pasta')

meals = [breakfast('Cornflakes'), dinner('Pasta')]
for meal in meals:
    meal.food()