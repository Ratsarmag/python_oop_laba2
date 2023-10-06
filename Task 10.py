class User:

    def __init__(self):
        print('+++')

user = User()

class Employee:
    name = 'Eugene'
    surname = 'Nechaev'
    def __init__(self):
        print(self.name + ' ' + self.surname)

employee = Employee()