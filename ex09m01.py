
pi = 3.1415926

def my_factoriel(n):
    fakt = 1
    for i in range(1, n + 1):
        fakt *= i
    return fakt

class Person:

    person_instance = 0

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        Person.person_instance += 1
    
    def __del__(self):
        Person.person_instance -= 1
    
    def __str__(self):
        return 'Name: %s\n Last Name: %s\n Age: %s' % (self.name, self.last_name, self.age)
