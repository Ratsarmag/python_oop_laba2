
class User:
	__age = 0

	def setAge(self,age):
		self.__age = age

	def getAge(self):
		return self.__age

class Student(User):
  def __init__(self):
    self.__age = super().getAge()

  def defincAge(self):
    self.__age = self.__age + 1

student = Student()
student.setAge(10)
print(student.defincAge())
