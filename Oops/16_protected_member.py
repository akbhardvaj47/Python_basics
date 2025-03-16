'''
Protected members are usually accessed within the class or subclasses (by convention).
In this file, you can directly access the protected variable, but it's not recommended.
Running this file will show how protected variables are supposed to be treated.
protected member is defined by (_)
'''

# protected_member.py
class ProtectedExample:
    def __init__(self):
        self._protected_variable = "I am protected"  # Protected member

    def display_protected_variable(self):
        print(f"Protected Variable: {self._protected_variable}")

# Test the protected member
if __name__ == "__main__":
    example = ProtectedExample()
    example.display_protected_variable()  # Accessing a protected method
    print(example._protected_variable)    # Direct access to a protected variable (not recommended)
