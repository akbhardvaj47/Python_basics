# Define the Rectangle class with width and height
class Rectangle:
    # Initialize the width and height of the rectangle
    def __init__(self, width, height):  # Constructor
        self.width = width    # Instance attribute
        self.height = height  # Instance attribute

    # Method to calculate the area of the rectangle
    def area(self):
        area=self.width * self.height
        print(area)

# Define the Square class which inherits from Rectangle
class Square(Rectangle):
    # Initialize the square by passing the side of the square
    def __init__(self, side):  
        # A square is a special case of a rectangle, where width and height are the same
        super().__init__(side, side)  # Call the parent class constructor

    # Override the area method to calculate the area of the square
    def area(self):
        area=self.width ** 2 
        print(area) # The area of a square is side^2 (width * width)

# Create an object of the Square class with side length 4
obj = Square(4,6)

# Call the area method to calculate the area 
area = obj.area()

# Print the area
print(area)
