class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} ate {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} did not eat {food.name}.')
            self.alive = False


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} ate {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} did not eat {food.name}.')
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Wolf')
a2 = Mammal('Dog')
p1 = Flower('Blue rose')
p2 = Fruit('Orange')

print(f'{a1.name}, {a2.name}')
print(f'{p1.name}, {p2.name} \n')

print(f'Are the wolf and the dog alive? \n {a1.alive}, {a2.alive}')
print(f'Are the wolf and the dog fed? \n {a1.fed}, {a2.fed} \n')
a1.eat(p1)
print(f' Is the wolf alive? - {a1.alive}')
a2.eat(p2)
print(f' Is the dog fed? - {a2.fed}')
