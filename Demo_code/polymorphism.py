#function with same name but diffrent parameter(overloading)
#function with same name and parameter in diffrent class
class Area:
    def find_area(self, a="none", b="none"):
        if a!='none' and b!='none':
            print('Area of reactangle: ',(a*b))
        elif a!='none':
            print("Area of reactangle: ",(a*a))
        else:
            print('Nothing')
      #Method overloading  
obj=Area()
obj.find_area(10,20)
obj.find_area(30)
obj.find_area()


