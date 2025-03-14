class Parent1:
    def assign_string_one(self, str1):
        self.str1=str1
    def show_string_one(self):
        print(self.str1)
    
class parent2:
    def assign_string_two(self, str2):
        self.str2=str2
    def show_string_two(self):
        print(self.str2)

class Child(Parent1, parent2):
    def assign_string_three(self, str3):
        self.str3=str3
    def show_string_three(self):
        print(self.str3)
    
c1=Child()

c1.assign_string_one("I am string of parent 1")
c1.assign_string_two("I am string of parent 2")
c1.assign_string_three("I am string of child")

c1.show_string_one()
c1.show_string_two()
c1.show_string_three()
        
        