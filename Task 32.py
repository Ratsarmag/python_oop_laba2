'''
class User:
	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

class Student(User):
	def setName(self,name):
		if (len(name) > 0):
			super.setName(name)  # метод родителя
		else:
			raise Exception('student name error')
'''

class User:
	def setAge(self,age):
		if (age >= 0):
			self.age = age
		else:
			raise Exception('need age more 0')
	def getAge(self):
	    return self.age

class Employee(User):
    def setAge(self, age):
        if (age <= 120):	
            super().setAge(age)
        else:
            raise Exception('need age less 120')

employee = Employee()
employee.setAge(-6)