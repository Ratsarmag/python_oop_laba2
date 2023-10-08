class User:
    __name = None
    __surname = None

    def getName(self):
        return self.__name 
	
    def getSurn(self):
        return self.__surname

    def setName(self, name):
        if (len(name) > 0):
            self.__name = name 
        else:
            raise Exception('name is incorrect') 
	
    def setSurn(self, surname):
        if (len(surname) > 0):
            self.__surname = surname 
        else:
            raise Exception("surname is incorrect!")

user = User()
user.setName('John') 
print(user.getName())

class Employee:
    __name = None
    __salary = None
    __age = None

    def getName(self):
        return self.__name
    
    def getSalry(self):
        return f'{self.__salary}$'
    
    def getAge(self):
        return self.__age
    
    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            raise Exception("age is incorrect!")

employee = Employee()

employee.setName('Eugene')
employee.setSalary(3000)
employee.setAge(18)

print(employee.getName())
print(employee.getSalry())
print(employee.getAge())
