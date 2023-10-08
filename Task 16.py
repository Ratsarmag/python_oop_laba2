class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name 
        self.__surname = surname 

    def getName(self):
        return self.__name 
	
    def getSurn(self):
        return self.__surname
  
user = User('John', 'Smith')
print(user.getName()) 
print(user.getSurn()) 

class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__ (self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name
    
    def getSalry(self):
        return self.__salary
    
    def getAge(self):
        return self.__age

employee = Employee('Eugene', 3000, 18)

print(employee.getName())
print(employee.getSalry())
print(employee.getAge())
    