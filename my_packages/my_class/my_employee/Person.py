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