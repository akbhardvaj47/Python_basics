class Vehicle:
    def __init__(self,color,cost):
        self.color=color
        self.cost=cost
    def show_vehicle_details(self):
        print("Vehicle color is",self.color)
        print("Vehicle cost is",self.cost)
        print("I am a Vehicle")

class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")

v1=Vehicle('black',900000)
v1.show_vehicle_details()

c1=Car('white',500000)
c1.show_car_details()
c1.show_vehicle_details()
        