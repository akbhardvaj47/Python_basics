class A:
    def display_1(self):
        print("This is method of class A")

class B(A):
    def display_2(self):
        print("This is method of class B")

obj=B()
obj.display_1()
obj.display_2()        