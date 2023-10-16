class User:
	def setName(self,name):
		self._name = name 
	
	def getName(self):
		return self._name 

class Student(User):
	def setYear(self, year):
		self._year = year 
	
	def getYear(self):
		return self._year 

class StudentProgrammer(Student):
	def setSkill(self, skill):
		self._skill = skill 
	
	def getSkill(self):
		return self._skill 

class Employee(User):
	def setSalary(self, salary):
		self._salary = salary
	
	def getSalary(self):
		return self._salary

class Programmer(Employee):
    def setCompany(self, company):
        self._company = company
	
    def getCompany(self):
        return self._company

class Designer(Employee):
    def setShift(self, shift):
        self._shift = shift
	
    def getShift(self):
        return self._shift