# Class Attributes: Attributes that are shared by all objects of a class.
 
class Car:
    wheels = 4  # class attribute

    def __init__(self, make, model, year):
        self.make = make  # instance attribute
        self.model = model  # instance attribute
        self.year = year  # instance attribute
        print(make,model,year)

obj=Car('Toyota','Corolla',2020)        