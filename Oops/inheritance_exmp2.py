""" class Phone:
    def __init__(self, brand, price, camera):
        print("Inside the phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s1 = SmartPhone("Nokia", 10000, "16MP")
print(s1.price)
print(s1.brand)
print(s1.camera)

"""
class Phone:
    def __init__(self, brand, price, camera):
        print("Inside the phone Constructor")
        self.price = price
        self.__brand = brand # this is private variable which cannot accessed by the child
        self.camera = camera

class SmartPhone(Phone):
    pass

s1 = SmartPhone("Nokia", 10000, "16MP")
print(s1.price)
print(s1.camera)