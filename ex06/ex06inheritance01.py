class Person:

    __person_number = 0

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        Person.__person_number += 1
        print(Person.__name__, Person.__person_number, 'is created')
    
    def __del__(self):
        Person.__person_number -= 1
        print(self.__class__.__name__, self.name, Person.__person_number + 1, 'is deleted')

class Employee(Person):
    
    __employee_number = 0

    def __init__(self, name, last_name, age, job = None):
        super(name, last_name, age)
        self.email = name + last_name + '@email.com'
        self.job = job
        Employee.__employee_number += 1
        print(Employee.__name__, Employee.__employee_number, 'is created')
    
    def __del__(self):
        Employee.__employee_number -= 1
        print(self.__class__.__name__, self.name, Employee.__employee_number + 1, 'is deleted')

