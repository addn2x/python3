from Person import Person

class Employee(Person):
    
    __employee_number = 0

    def __init__(self, name, last_name, age, job = None):
        super().__init__(name, last_name, age)
        self.email = name + last_name + '@email.com'
        self.job = job
        Employee.__employee_number += 1
        print(Employee.__name__, Employee.__employee_number, 'is created')
    
    def __del__(self):
        Employee.__employee_number -= 1
        print(self.__class__.__name__, self.name, Employee.__employee_number + 1, 'is deleted')

    def __str__(self):        
        return  super().__str__() + ' email %s\n job %s\n' % (self.email, self.job)

#p = Person('Q', 'W', 32)
#print(p)

#e = Employee('A', 'B', 21, 'Admin')
#print(e)