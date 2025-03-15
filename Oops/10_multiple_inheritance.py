# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Parent class 2
class Color:
    def __init__(self, color):
        self.color = color
    
    def display_color(self):
        print(f"The color of the animal is {self.color}")

# Child class (inherits from both Animal and Color)
class Dog(Animal, Color):
    def __init__(self, name, color):
        Animal.__init__(self, name)  # Initialize the Animal class
        Color.__init__(self, color)  # Initialize the Color class
    
    def speak(self):
        print(f"{self.name} barks")

# Create an object of Dog class (which inherits from both Animal and Color)
dog = Dog("Tommy", "Golden")

# Call methods from both parent classes
dog.speak()         # Calls speak method from Dog class
dog.display_color() # Calls display_color method from Color class
