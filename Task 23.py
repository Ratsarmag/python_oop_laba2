class City :
  city = None

  def __init__(self,city):
    self.city = city

class User :
  name = None
  surname = None
  city = None

  def __init__(self,name,surname,city):
    self.name = name
    self.surname = surname
    self.city = city

city = City('luis') 
user = User('john', 'smit', city) 

print(user.name) 
print(user.city.city)

class Position:
  position = None

  def __init__(self,position):
    self.position = position

class Department:
  department = None

  def __init__(self,department):
    self.department = department

class User :
  name = None
  position = None
  department = None

  def __init__(self, name, position, department):
    self.name = name
    self.position = position
    self.department = department


position = Position(234)
department = Department('Malcolm')
user = User('John', position, department)

print(user.name)
print(user.position.position)
print(user.department.department)
