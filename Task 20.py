class User:
    __name = None

    def __init__(self,name):
        self.__name = name 

user1 = User('1') 
user2 = User('2') 

print(user1 == user1) # True
print(user1 == user2) # False

class Employee:
    __name = None

    def __init__(self,name):
        self.__name = name 

''' 
emp1 = Employee('John') 
emp2 = Employee('Eric') 

print(emp1 == emp2) - False


emp1 = Employee('John') 
emp2 = Employee('Eric') 

print(emp1 == emp1) - True


emp1 = Employee('John') 
emp2 = Employee('John') 

print(emp1 == emp2) - False


emp1 = Employee('John') 
emp2 = Employee('Eric') 

print(emp1 != emp1) - False


emp1 = Employee('John') 
emp2 = emp1 

print(emp1 == emp2)  - True


emp1 = Employee('John') 
emp2 = Employee('Eric') 

print(emp1 != emp2)  - True


emp1 = Employee('John') 
emp2 = emp1 
emp2.name = 'Eric' 

print(emp1 == emp2) - True
'''

