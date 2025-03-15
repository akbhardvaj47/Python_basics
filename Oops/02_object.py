'''
Objects: An object is an instance of a class, which has its own set of attributes (data) and methods (functions).
'''
# Define a class named 'Demo'
class Demo:
    
    # Method to add two numbers
    def add(self, a, b):
        # Print the sum of 'a' and 'b'
        print(a + b)

    # Method to multiply two numbers
    def mul(self, a, b):
        # Print the product of 'a' and 'b'
        print(a * b)

# Create an object of the 'Demo' class
obj = Demo()
obj1=Demo()   
# You can create multiple objects of a class

# Call the 'add' method with arguments 10 and 20
obj.add(10, 20)

# Call the 'mul' method with arguments 10 and 20
obj.mul(10, 20)
    