class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
    
class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        print(self.age)

class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        print(self.gender)

m=GrandChild()
m.get_name('Amit')
m.get_age(20)
m.get_gender('male')

m.show_name()
m.show_age()
m.show_gender()