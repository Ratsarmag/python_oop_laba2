class User:
    def setName(self,name):
        self.name = name 
        
    def getName(self):
        return self.__capeFirst(self.name) 
        
    def __capeFirst(self,stri):
        return stri

class Student(User):
	def setSurn(self,surname):
		self.surname = surname 
	
	def getSurn(self):
		return self.__capeFirst(self.surname)  # будет ошибка

student = Student()
print(student.getSurn)

class Employee(User):
    def setSurn(self,surname):
        self.surname = surname 
	
    def getSurn(self):
        return self.__capeFirst(self.surname)