class User:
    pass

user1 = User()
user2 = User()

user1.name = 'John'
user2.name = 'Eric'

class Employee:
    pass

employee1 = Employee()
employee2 = Employee()
employee3 = Employee()

employee1.name = 'Eugene'
employee1.salary = 3000

employee2.name = 'Valeriy'
employee2.salary = 8000

employee3.name = 'Victor'
employee3.salary = 1100

print(employee1.salary + employee2.salary + employee3.salary)

