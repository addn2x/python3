# Destructor

class Person:

    number_of_person = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + '@mail.com'
        Person.number_of_person += 1

    def __del__(self):
        print("Person %d deleted" % (Person.number_of_person))
        Person.number_of_person -= 1

    def info(self):
        return "Name %s last name %s age %d" % (self.first, self.last, self.age)

p01 = Person("John", "Smith", 22)
p02 = Person("Jane", "Doe", 24)

print(p01.info())