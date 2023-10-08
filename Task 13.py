class User:
    __name = None

    def __init__(self,name):
        self.__name = name

    def show(self):
        return self.__name
    
user = User('John')
print(user.show())

class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__ (self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def showInfo(self):
        print(f"Info:\n name: {self.__name}\n salary: {self.__salary}\n age: {self.__age}")

employee = Employee('Eugene', 3000, 18)
employee.showInfo()