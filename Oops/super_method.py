# Define the base class Animal
class Animal:
    # Method that describes the speaking behavior of an Animal
    def speak(self):
        print("Animal speaks")

# Define the Dog class, which inherits from Animal
class Dog(Animal):
    # Overriding the speak method for Dog class
    def speak(self):  # This speak method will override the animal speak method
        # Call the speak method of the parent class (Animal)
        super().speak()
        # Additional behavior for Dog class
        print("Dog barks")

# Testing the Dog class and its speak method
dog = Dog()
dog.speak()  # This will call the speak method of the Dog class
