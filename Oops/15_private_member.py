'''Private members are not accessible directly from outside the class. They are intended to be used only within the class.
If you try to access __private_variable directly, you'll get an AttributeError.
Running this file will show that private members need to be accessed through methods.
private member is defined by (__)
'''

# private_member.py
class PrivateExample:
    def __init__(self):
        self.__private_variable = "I am private"  # Private member

    def display_private_variable(self):
        print(f"Private Variable: {self.__private_variable}")

# Test the private member
if __name__ == "__main__":
    example = PrivateExample()
    example.display_private_variable()  # Accessing a private method
    # print(example.__private_variable)  # This will raise an AttributeError because __private_variable is private
