# Class A defines a basic structure with methods and a constructor
class A:
    # Constructor of class A
    def __init__(self):
        print('This is constructor of class A')
    
    # Method to show a message
    def show(self):
        print('This is show method of class A')
    
    # Method to add two numbers
    def add(self, a, b):
        print(a + b)

# Class B inherits from class A
class B(A):
    # Constructor of class B
    def __init__(self):
        print('This is constructor of class B')
        super().__init__()  # Calls the constructor of class A using super()
    
    # Method to display a message specific to class B
    def display(self):
        print('This is display method of class B')
    
    # Method to multiply two numbers (overrides add method in class A)
    def mul(self, a, b):
        print(a * b)  # Multiplies the numbers instead of adding

# Create an instance of class B
obj = B()

# Call the method from class B
obj.display()  # This will call the display method from class B

# Call the add method from class B (which overrides the add method of class A)
obj.add(3, 4)  # This will perform multiplication

# Call the add method from class B (which overrides the add method of class B)
obj.mul(3, 4)  # This will perform multiplication

# Call the show method from class A (since it's inherited by class B)
obj.show()  # This will call the show method from class A
            