# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(self.firstname, self.lastname)
    

# Use the person class to create an object
x = Person("John", "Wick")
x.printname()

"""
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class:
"""

# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

# Use the Student class to create an object, and then execute the printname method:

y = Student("Boogie", "Man")
y.printname()