


class Animal:
    alive = True

    def eat(self):
        print('this animal is eating')
        return self

    def sleep(self):
        print('This animal is sleeping')
    
class Rabbit(Animal):
    def run(self):
        print('this fish is runnning')

class Fish(Animal):
    def swim(self):
        print('this fish is swimming')

class Hawk(Animal):
    def fly(self):
        print('this hawk is flying ')

rabbit = Rabbit()
fish=Fish()
hawk=Hawk()

rabbit.eat()
hawk.sleep()
print(fish.alive)

# The None values are being printed because the print() 
# function is used with methods (eat() and sleep()) that do not r
# eturn any value (they just print their messages). Since thes
# e methods do not have a return statement, they return None by default.



rabbit.eat().run()

