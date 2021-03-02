# You can add properties to the child class which might not be present
# in the parent class

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    # Add graduation year to the Student Class
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the Class of", self.graduation_year)

X = Student("Mike", "Tyson", 2021)
X.welcome()

# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.