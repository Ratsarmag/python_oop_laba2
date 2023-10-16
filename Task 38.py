'''class User:
	def setAge(self,age):
		self._age = age 
	
	def getAge(self):
		return self._age
	
class Student(User):
	def incAge(self):
		self._age = self._age+1'''
		
class User:
	_name = None
	
	def setName(self,name):
		self._name = name 
	
	def getName(self):
		return self._name 


class Employee(User):
	def setName(self):
		if (len(self._name) > 0):
			self._name = self._name 