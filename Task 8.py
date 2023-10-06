class User:
    name = 'oop python'

    def show(self):
        return self.cape(self.name)

    def cape(self, str):
        return str.upper()

class Student:
    name = 'eugene'
    surname = 'nechaev'

    def show(self):
        return self.cape(self.name + ' ' + self.surname)

    def cape(self, str):
        return str.title()
    
    def initials(self):
        return self.name[0].title() + '. ' + self.surname[0].title() + '.'
        
user = User()
print(user.show())

student = Student()
print(student.show())
print(student.initials())
