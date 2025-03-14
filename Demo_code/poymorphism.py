class car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('drive')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print('sail')

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print('fly')
    
a=car('desire',2021)
b=Boat('boat1',2023)
c=Plane('lauda',2024)

for i in (a,b,c):
 i.move()