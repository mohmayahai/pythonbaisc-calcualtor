class Car:
    wheels= 4 #class variable
    def __init__(self,make,model,year,color):
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable
    

    def drive(self):
        print('print the car is driving')

    def stop(self):
        print('this car is stopped')

    



