class User:
    __name = None

    def __init__(self, name):
        self.__name = name

    def show(self):
        self.__cape(self.__name)


    def __cape(self, str):
        return str

user = User('John')
print(user.show())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.__addSign(self.salary)

    def __addSign(self, num):
        return f'{num}$'
    
employee = Employee('Eugene', 3000)
print(employee.getSalary())


