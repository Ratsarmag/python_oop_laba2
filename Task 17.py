class User:
    __name = None
    __surname = None

    def getName(self):
        return self.__name 
	
    def getSurn(self):
        return self.__surname

    def setName(self, name):
        self.__name = name 
	
    def setSurn(self, surname):
        self.__surname = surname 

user = User()
user.setName('John') 
user.setSurn('Smith') 

print(user.getName()) 
print(user.getSurn()) 

class Employee:
    __name = None
    __salary = None
    __age = None

    def getName(self):
        return self.__name
    
    def getSalry(self):
        return self.__salary
    
    def getAge(self):
        return self.__age
    
    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary
        
    def setAge(self, age):
        self.__age = age

employee = Employee()

employee.setName('Eugene')
employee.setSalary(3000)
employee.setAge(18)

print(employee.getName())
print(employee.getSalry())
print(employee.getAge())