class User:
	pass
user = User()

print(isinstance(user, User)) #True

'''
class Student:
  pass
	
class Employee:
  pass
	
employee = Employee()
print(isinstance(employee, Employee)) #True
print(isinstance(employee, Student)) #False
'''

class Student:
  name = None

  def __init__(self,name):
    self.name = name 

class Employee:
  name = None

  def __init__(self,name):
    self.name = name 


users = [
	 Student('user1'),
	 Employee('user2'),
	 Student('user3'),
	 Employee('user4'),
	 Student('user5'),
	 Employee('user6'),
	 Student('user7'),
] 

i = 0
while i < len(users):
    print(users[i].name)
    i += 1