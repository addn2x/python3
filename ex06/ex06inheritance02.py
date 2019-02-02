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
    
    def __str__(self):
        return 'Person %d\n name %s\n last name %s\n age %d\n' % (Person.__person_number, self.name, self.last_name, self.age)

class Employee(Person):
    
    __employee_number = 0

    def __init__(self, name, last_name, age, job = None):
        super().__init__(name, last_name, age)
        self.email = name + last_name + '@email.com'
        self.job = job
        Employee.__employee_number += 1
        print(Employee.__name__, Employee.__employee_number, 'is created')
    
    def __del__(self):
        super().__del__()
        Employee.__employee_number -= 1
        print(self.__class__.__name__, self.name, Employee.__employee_number + 1, 'is deleted')
    
    def __str__(self):        
        return  super().__str__() + ' job %s\n' % (self.job)


e = Employee('A', 'B', 22, 'Developer')
print(e)