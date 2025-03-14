class Vehicle:
    def __init__(self,color,cost):
        self.color=color
        self.cost=cost
    def show_vechicle_details(self):
        print("vehicle color is",self.color)
        print("vehicle cost is",self.cost)

class Car(Vehicle):
    def __init__(self, color, cost, tyres, hp):
        super().__init__(color, cost)
        self.tyres=tyres
        self.hp=hp

    def show_car_details(self):
        print("Number of tyres is",self.tyres)
        print("horse power of car is ",self.hp)
        print("i am a Car")

a1=Car('blue',200000,6,999)
a1.show_vechicle_details()
a1.show_car_details()
