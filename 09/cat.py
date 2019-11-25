class Cat:
    MAX_LIVES = 9
    def __init__(self):
        self.lives = self.MAX_LIVES

    def name(self):
        self.name = name

    def meow(self):
        print("{}: Meow!".format(self.name))

    def is_alive(self):
        return self.lives > 0
    
    def lose_life(self):
        if self.is_alive(): 
            self.lives -= 1

    def eat(self, food):
        if food =='fish' and self.is_alive() and self.lives < self.MAX_LIVES:
            self.lives += 1

mourek = Cat('Mourek')
mourek.meow()

mourek.is_alive()
mourek.lose_life()

