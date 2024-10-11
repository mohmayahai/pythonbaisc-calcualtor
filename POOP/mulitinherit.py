class Organism:
    alive=True

class Animal(Organism):
    
    def eat(self):
        print('this thing is can eat')


class Dog(Animal):
    def prey(self):
        print('this is a prey')


dog=Dog()
print(dog.alive)
dog.eat()
dog.prey()