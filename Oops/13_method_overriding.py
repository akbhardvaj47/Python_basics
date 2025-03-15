# Parent class
class Animal:
    def info(self):
        print('This is Animal class')
    def sound(self):
        print("Some generic animal sound")

# Child class
class Dog(Animal):
    def info(self):
        print('This is Dog class')
    def sound(self):
        print("Bark")

# Child class
class Cat(Animal):
    def info(self):
        print('This is Cat class')

    def sound(self):
        print("Meow")

# Create instances of the child classes
dog = Dog()
cat = Cat()

# Call the overridden method
dog.info()
dog.sound()  # Output: Bark
cat.info()
cat.sound()  # Output: Meow
