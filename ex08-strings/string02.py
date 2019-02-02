class Person:

    def __init__(self, name, last_name, age, average_income):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_income = average_income
    
    def __str__(self):
        return 'Name: %s,\nLast Name: %s,\nAge: %d,\nAverage Income: %.2f\n' % (self.name, self.last_name, self.age, self.average_income)
    
paul = Person('Paul', 'Banks', 36, 128.34)
david = Person('David', 'Kessler', 35, 146.78)

print(paul)
print(david)