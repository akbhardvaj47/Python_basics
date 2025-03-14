class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name 
        self.age=age
        self.salary=salary
        self.gender=gender
    
    def show_employee_details(self):
        print("Name of employee is",self.name)
        print("Age of employee is",self.age)
        print("Salary of employee is",self.salary)
        print("gender of employee is",self.gender)

p=Employee('Amit',20,50000,'male')

p.show_employee_details()
        