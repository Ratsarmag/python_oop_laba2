class User :
  __name = None

  def __init__(self,name):
    self.__name = name

  def getName(self):
    return self.__name
users = [
	 User('john'),
	 User('eric'),
	 User('kyle'),
] 

for user in users:
	print(user.getName()) 

class Employee :
  __name = None
  __salary = None

  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary

  def getNameAndSalary(self):
    return self.__name, f"{self.__salary}Р"
  
employees = [
	 Employee('john', 3000),
	 Employee('eric', 14000),
	 Employee('kyle', 28000),
] 

for employee in employees:
	print(employee.getNameAndSalary()) 