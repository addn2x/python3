# Functions
# most basic units of reusable code is the function
# function with and without parameters

def greeting():
    print ("Hi there")
    # return 2 + 3

def print_name(name): #parameter
    print ("Hi there")
    print(name)

def print_person(name, age):
    print ("Hi there")
    print(name)
    print("Your age is", age)

def print_name_default_age(name, age = 30):
    print ("Hi there")
    print(name)
    print("Your age is", age)

###################################

greeting()

name = 'Dave'
print_name(name)

print_name('Jane')

print_person(name, 30)

print_name_default_age('Jane')
print_name_default_age('Ann', 23)