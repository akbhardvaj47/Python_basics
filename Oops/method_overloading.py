class Overloading_Example:
    def display(self, a=None, b=None):
        if a is None and b is None:
            print("No arguments passed")
        elif b is None:
            print(f"Single argument: {a}")
        else:
            print(f"Sum of {a} and {b} = {a + b}")

obj = Overloading_Example()
obj.display()  # No arguments
obj.display(10)  # Single argument
obj.display(10, 20)  # Two arguments
         