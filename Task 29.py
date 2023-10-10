class User:
  def setName(self,name):
    self.name = name 

  def getName(self):
    return self.name 

class Student(User):
  pass

student = Student()
student.setName('john')
name = student.getName() 
print(name) 

class Employee(User):
  pass

employee = Employee()

employee.setName('Eugene')
print(employee.getName())
