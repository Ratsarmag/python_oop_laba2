class User:
    name = None

    def show(self):
        print(self.name)

user = User()
user.name = 'John'
user.show()

class Employee:
    name = None
    salary = None
    
    def showName(self):
        print(self.name)

    def showSalary(self):
        print(self.salary)

employee = Employee()
employee.name = 'Eugene'
employee.salary = '2800'

employee.showName()
employee.showSalary()