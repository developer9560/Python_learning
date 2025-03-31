# To map with real world scenarios, we started using objects in code.
# This is called Object Oriented Programming (OOP).
# Objects are used to represent real world entities and their states.

# Class is a blueprint for creating objects
# Object is an instance of a class

class Student:
    name = "suraj kumar"
    age = 20
    marks = 90
    city = "Delhi"


s1 = Student()
print(s1.name)

s2 = Student()
print(s2.age)


class Car:
    color = "red"
    speed = 100
    brand = "BMW"


c1 = Car()
print(c1.color)
print(c1.speed)
print(c1.brand)
