"""
Objects can also contain methods. 

Methods in objects are functions that belong to the object.

Let us create a method in the Person class

Note: The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, 
but it has to be the first parameter of any function in the class
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hello! My name is " + self.name)

p1 = Person("Ishant", 22)

p1.introduce()