class User:
    def __init__(self,name,surname):
        self.name = name 
        self.surname = surname
	
    def show(self):
        return self.name + ' ' + self.surname 

user = User('John', 'Smith')
print(user.show())

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    def showName(self):
        return self.name
    
    def showSalary(self):
        return self.salary
    
    def salaryGrowth(self):
        return self.salary * 1.1

employee = Employee('Eugene', 3000)
print(employee.showName())
print(employee.showSalary())
print(employee.salaryGrowth())
