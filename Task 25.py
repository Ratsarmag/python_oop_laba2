class User :
  __name = None

  def __init__(self,name):
    self.__name = name

  def getName(self):
    return self.__name

class UsersCollection:

  def __init__(self):
    self.__users = []

  def add(self,user):
    self.__users.append(user)

  def show(self):
    for user in self.__users:
      print(user.getName())

uc = UsersCollection()
uc.add(User('john')) 
uc.add(User('eric')) 
uc.add(User('kyle')) 
uc.show() 

class Employee :
  __name = None
  __salary = None

  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary
  def getName(self):
    return self.__name
  def getSalary(self):
    return self.__salary
  
class EmployeesCollection:
  __sum = 0
  __avg = 0

  def __init__(self):
    self.__employees= []

  def add(self,employee):
    self.__employees.append(employee)

  def show(self):
    for employee in self.__employees:
      print(employee.getName(), employee.getSalary())
  def showSum(self):
    for employee in self.__employees:
       self.__sum += employee.getSalary()
    return self.__sum
  def showAvg(self):
    self.__avg = self.__sum / len(self.__employees)
    return self.__avg

ec = EmployeesCollection()
ec.add(Employee('Eugene', 3000)) 
ec.add(Employee('Konstantin', 14000)) 
ec.add(Employee('Kirill', 16550)) 
ec.show()
print(ec.showSum())
print(ec.showAvg())
