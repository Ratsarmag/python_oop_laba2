'''class User:
	__name  = None
	
	def setName(self,name):
		self.__name = name 
	
	def getName(self):
		return self.__name 

class Student(User):
    pass

student = Student()
student.setName('john') 
name = student.getName() 
print(name) 
'''

class User:
	__name = None
	__surname = None
	
	def setName(self,name):
		self.__name = name 
	
	def getName(self):
		return self.__name 
	
	def setSurn(self, surname):
		self.__surname = surname 
	
	def getSurn(self):
		return self.__surname 

class Employee(User):
	def getFull(self):
	return self.__name + ' ' + self.__surname 

employee = Employee()
employee.setName('eugene')
employee.setSurn('nechaev')
print(employee.getName(), employee.getSurn())