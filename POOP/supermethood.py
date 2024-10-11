class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
       

    def area(self):
        return self.length*self.width

    
class Cubes(Rectangle):

    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
    
    def volume(self):
        return self.length*self.length*self.height
    

square=Square(3,4)
cube = Cubes(3,4,5)

print(cube.volume())
print(square.area())


#abstract class - a form a check and balance

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod #method havinf declaration and not implementation
    def go(self):
        pass

    # @abstractmethod
    # def stop(self):
    #     pass

class Car(Vehicle):
    def go(self):
        print('you drive the car')

# class Motorcyle(Vehicle):
#     pass




### Objects as arguments
class Car1:
    color = None
def change_color(car1,color):
    car1.color=color

car_1=Car1()
car_2=Car1()
car_3=Car1()

change_color(car_1,"red")

print(car_1.color)
print(car_2.color)

#duck typing - the class is less important thatn the method/attirbutes - if it walks and quak like a duck like than it is duck

class Duck:
    def talk(self):
        print('this duck is walking')
    def walk(self):
        print('this duck is walking')

class Chicken:
    def talk(self):
        print('this Chicken is walking')
    def walk(self):
        print('this Chicken is walking')

class Person:
    def cathc(self,duck):
        duck.walk()
        duck.talk()
        print('you caught the crickert')

duck=Duck()
chicken=Chicken()
person=Person()

person.cathc(chicken)

#walrus operator :=
happy = True
print(happy)

print(happy1:=True) 

foods=list()
while food:=input('What food do you like?: ') != 'quit':
    foods.append(food)


def hello():
    print('Hello')

#higher order function = a function that either 
# accepts a function as an argument or retuirn a function in python function are trearted as objects also


def divisor(x):
    def dividen(y):
        return y/x
    return dividen

dev=divisor(2)
print(dev)

print(dev(8))

#lambada = function used instantly for the sometime and then you

def doble(x):
    return x*2

double=lambda x: x*2
double2=doble(2)
print(double(2))
print(double2)







    
