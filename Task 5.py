class User:
    def show(self):
        return '+++'
 
user = User() 
print(user.show())

class Employee:

    def introduce(self):
        print(f"My name is {self.name}")

employee = Employee()
employee.name = 'Eugene'
employee.introduce()
