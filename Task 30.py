class User:
  def setName(self,name):
    self.name = name 

  def getName(self):
    return self.name 
  
  def setSurname(self, surname):
    self.surname = surname
  def getSurname(self):
    return self.surname
  
class Student(User):
  def setYear(self, year):
    self.year = year 
	
  def getYear(self):
    return self.year 
  
student = Student()
student.setName('John')
student.setYear(1) 

name = student.getName()
year = student.getYear() 

print(name, year)

class Employee(User):
  def setSalary(self, salary):
    self.salary = salary
	
  def getSalary(self):
    return self.salary
  
employee = Employee()
employee.setName('Euegene')
employee.setSurname('Nechaev')
employee.setSalary(3000)

name = employee.getName()
surname = employee.getSurname()
salary = employee.getSalary()

print(name, surname, salary)