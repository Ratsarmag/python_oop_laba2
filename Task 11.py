class User:

    def __init__(self,name,surname):
        print(name + ' ' + surname) 

u =  User('John', 'Smith') 

class Employee:
    name = 'Eugene'
    surname = 'Nechaev'
    
    def __init__(self, name, salary):
        print(f"{name}, {salary}")

employee = Employee('Eugene', 3000)

