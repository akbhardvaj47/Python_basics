# Base class (Parent Class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Intermediate class (Child Class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the Animal class
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks")

# Derived class (Grandchild Class)
class Puppy(Dog):
    def __init__(self, name, breed, age):
        # self.name=name
        # self.breed=breed
        super().__init__(name, breed)  # Call the constructor of the Dog class
        self.age = age
    
    def speak(self):
        print(f"{self.name}, the {self.breed} puppy, barks playfully")
    
    def show_age(self):
        print(f"{self.name} is {self.age} years old")

# Create an object of the Puppy class (grandchild class)
obj_puppy = Puppy("Tommy", "Golden", 4)

# Calling methods from different levels
obj_puppy.speak()      # Calls speak method of Puppy class
obj_puppy.show_age()   # Calls show_age method of Puppy class
