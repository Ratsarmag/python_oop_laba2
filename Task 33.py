class User:
	
	def __init__(self,name, surname):
		self.name = name 
		self.surname = surname 
	
	def getName(self):
		return self.name 
	
	def getSurn(self):
		return self.surname 

class Student(User):
	def __init__(self,name, surname, year):
		super(name, surname) 
		self.year = year 
	
	def getYear(self):
		return self.year 

class Employee(User):
    def __init__(self, name, surname, age, salary):
        super(name, surname) 
        self.age = age
        self.salary = salary
        
    def getAge(self):
        return self.age
        
    def getSalary(self):
        return self.salary