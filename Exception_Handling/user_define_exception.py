'''
You can define your own exceptions by creating custom classes that inherit from Python’s built-in Exception class
'''

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

def calculate_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return x ** 0.5

try:
    num = int(input("Enter a number to calculate the square root: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
except NegativeNumberError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input, please enter a valid integer.")
finally:
    print("Square root calculation complete.")
