class User:
    def setName(self,name):
        self.name = name 
	
    def getName(self):
	    return self.name 


class Student(User):
    def setName(self,name):
        if (len(name) > 0):
            self.name = name 
        else:
            raise Exception("student name error")

student = Student()
student.setName('john') 


class Employee:
  def setName(self,age):
    if age >= 18 and age <= 65:
        self.name = age
    else:
        raise Exception("employee age error")


  def getName(self):
    return self.age
  