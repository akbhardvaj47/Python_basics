'''Public members can be accessed directly from outside the class.
Running this file will show that you can access both methods and attributes of the class.'''
# public_member.py
class PublicExample:
    def __init__(self):
        self.public_variable = "I am public"

    def display_public_variable(self):
        print(f"Public Variable: {self.public_variable}")

# Test the public member
if __name__ == "__main__":
    example = PublicExample()
    example.display_public_variable()  # Accessing a public method
    print(example.public_variable)     # Direct access to a public variable
