class User:
      
	def show(self, name, surname):
		return name + ' ' + surname 
	
user = User()

print(user.show('John', 'Smith')) 

class Employee:

    def introduce(self, name, salary):
        print(f"My name is {name}, my salary is {salary}")

employee = Employee()
employee.introduce('Eugene', 2850)
