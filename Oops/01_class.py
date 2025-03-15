'''
A class is a blueprint or a template that defines the properties and behavior of an object.
class is defined by class keyword.
'''

class Demo:
    a = 100  # Class variable 'a' is defined and initialized with the value 100

    def display_value(self):  # self parameter is mandatory for each method 
        # Method to print the value of variable 'a' using the instance 'self'
        print(self.a)  # In a class you can access a variable by self keyword

# Creating an object of the class Demo
obj = Demo()

# Accessing and printing the class variable 'a' through the object
print(obj.a)

# Calling the method 'display_value' using the object to print the value of 'a'
obj.display_value()

