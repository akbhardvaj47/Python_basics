class Car:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        print(self.color)
    def show_cost(self):
        print(self.cost)
p2=Car()

p2.set_color("blue")
p2.set_cost(5000)
p2.show_color()
p2.show_cost()