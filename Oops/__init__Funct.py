# constructor is a special method that is called when an object is created
# All classes have a function called __init__(), which is always executed when the class is being initiated

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "India"



p1 = Person("Suraj", 20)
print(p1.name)
print(p1.age)
print(p1.country) 