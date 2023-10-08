class User:
    name = 'John'
    
    def show(self):
        return self.name
    
user = User()
print(user.show())

class Student:
    name = None
    surname = None
    
    def show(self):
        return f"{self.name} {self.surname}"

student = Student()
student.name = 'Eugene'
student.surname = 'Nechaev'
print(student.show())

  