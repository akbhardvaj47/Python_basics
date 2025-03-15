#  Instance Attributes: Attributes that are unique to each object.
class Car:
    wheels=4 # class attribute
    def __init__(self,make,model,year):
        self.make=make   # Instance attribute
        self.model=model # Instance attribute
        self.year=year   # Instance attribute

    def start_engine(self):
        print('Vroom!')    

# Creating an object

obj=Car("Toyota","Corolla",2015)  
obj.start_engine()      